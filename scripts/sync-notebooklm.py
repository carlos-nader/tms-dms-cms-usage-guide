#!/usr/bin/env python3
"""Sync tracked PDFs from the repo to a NotebookLM notebook.

Uses git diff to detect added, modified, and deleted PDFs between two commits,
then syncs those changes to the target notebook. On first run (empty notebook),
uploads all tracked files regardless of git diff.

Usage:
    python scripts/sync-notebooklm.py

Environment variables (required):
    NOTEBOOKLM_AUTH_JSON   -- Playwright storage state JSON (for CI)
    NOTEBOOKLM_NOTEBOOK_ID -- Target notebook ID

Environment variables (optional):
    GIT_BEFORE -- Commit SHA before the push (default: HEAD~1)
    GIT_AFTER  -- Commit SHA after the push  (default: HEAD)
"""

import asyncio
import os
import subprocess
import sys
from pathlib import Path

from notebooklm import NotebookLMClient

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent.resolve()

TRACKED_PATTERNS = [
    "guide.pdf",
    "wip/guide/*.pdf",
    "wip/chapter-C*.pdf",
    "wip/section-C*-S*.pdf",
    "wip/guide-v*-alpha*.pdf",
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_notebook_id() -> str:
    nb_id = os.environ.get("NOTEBOOKLM_NOTEBOOK_ID", "").strip()
    if not nb_id:
        print("ERROR: NOTEBOOKLM_NOTEBOOK_ID is not set.")
        sys.exit(1)
    return nb_id


def collect_repo_pdfs() -> dict[str, Path]:
    """Return {filename: absolute_path} for all tracked PDFs currently in the repo."""
    result = {}
    for pattern in TRACKED_PATTERNS:
        for match in REPO_ROOT.glob(pattern):
            if match.is_file():
                result[match.name] = match
    return result


def git_changed_files(before: str, after: str) -> dict[str, str]:
    """Return {filename: status} for files changed between two commits.

    Status values: 'A' (added), 'M' (modified), 'D' (deleted).
    Only includes files matching TRACKED_PATTERNS.
    """
    try:
        result = subprocess.run(
            ["git", "diff", "--name-status", before, after],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"WARNING: git diff failed ({e}). Falling back to full sync.")
        return {}

    tracked_names = {
        match.name
        for pattern in TRACKED_PATTERNS
        for match in REPO_ROOT.glob(pattern)
    }

    changed = {}
    for line in result.stdout.splitlines():
        parts = line.split("\t", 1)
        if len(parts) != 2:
            continue
        status, filepath = parts[0][0], parts[1]
        filename = Path(filepath).name
        if filename in tracked_names and status in ("A", "M", "D"):
            changed[filename] = status
    return changed


async def get_notebook_sources(client, notebook_id: str) -> dict[str, str]:
    """Return {filename: source_id} for all sources currently in the notebook."""
    sources = await client.sources.list(notebook_id)
    return {s.title: s.id for s in sources if s.title}


def plan_first_run(
    repo_pdfs: dict[str, Path],
    notebook_sources: dict[str, str],
) -> tuple[list[Path], list[str], list[Path]]:
    """Plan a full sync: upload everything missing, delete anything orphaned."""
    to_upload = [path for name, path in repo_pdfs.items() if name not in notebook_sources]
    to_delete = [sid for name, sid in notebook_sources.items() if name not in repo_pdfs]
    to_replace: list[Path] = []
    return to_upload, to_delete, to_replace


def plan_incremental(
    changed: dict[str, str],
    repo_pdfs: dict[str, Path],
    notebook_sources: dict[str, str],
) -> tuple[list[Path], list[str], list[Path]]:
    """Plan an incremental sync based on git diff."""
    to_upload: list[Path] = []
    to_delete: list[str] = []
    to_replace: list[Path] = []

    for filename, status in changed.items():
        if status == "A" and filename in repo_pdfs:
            to_upload.append(repo_pdfs[filename])
        elif status == "D" and filename in notebook_sources:
            to_delete.append(notebook_sources[filename])
        elif status == "M" and filename in repo_pdfs:
            to_replace.append(repo_pdfs[filename])

    return to_upload, to_delete, to_replace


async def delete_sources(client, notebook_id: str, source_ids: list[str]) -> None:
    for source_id in source_ids:
        try:
            await client.sources.delete(notebook_id, source_id)
            print(f"  [deleted]  {source_id}")
        except Exception as e:
            print(f"  [error]    delete {source_id}: {e}")


async def replace_source(
    client,
    notebook_id: str,
    path: Path,
    notebook_sources: dict[str, str],
) -> None:
    """Delete old source by filename and re-upload."""
    old_id = notebook_sources.get(path.name)
    if old_id:
        await delete_sources(client, notebook_id, [old_id])
    await upload_file(client, notebook_id, path)


async def upload_file(client, notebook_id: str, path: Path) -> None:
    try:
        await client.sources.add_file(notebook_id, path, wait=True)
        print(f"  [uploaded] {path.name}")
    except Exception as e:
        print(f"  [error]    upload {path.name}: {e}")


# ---------------------------------------------------------------------------
# Main sync
# ---------------------------------------------------------------------------

async def sync(notebook_id: str) -> None:
    before = os.environ.get("GIT_BEFORE", "HEAD~1")
    after = os.environ.get("GIT_AFTER", "HEAD")

    repo_pdfs = collect_repo_pdfs()
    print(f"Tracked PDFs in repo: {len(repo_pdfs)}")

    async with await NotebookLMClient.from_storage() as client:
        notebook_sources = await get_notebook_sources(client, notebook_id)
        print(f"Sources in notebook:  {len(notebook_sources)}")

        if not notebook_sources:
            print("Notebook is empty — running full sync.")
            to_upload, to_delete, to_replace = plan_first_run(repo_pdfs, notebook_sources)
        else:
            changed = git_changed_files(before, after)
            print(f"Changed PDFs in push: {len(changed)}")
            to_upload, to_delete, to_replace = plan_incremental(changed, repo_pdfs, notebook_sources)

        print(f"To upload:  {len(to_upload)}")
        print(f"To replace: {len(to_replace)}")
        print(f"To delete:  {len(to_delete)}")

        if not to_upload and not to_delete and not to_replace:
            print("\nNothing to sync — notebook is up to date.")
            return

        print()
        await delete_sources(client, notebook_id, to_delete)
        for path in to_replace:
            await replace_source(client, notebook_id, path, notebook_sources)
        for path in to_upload:
            await upload_file(client, notebook_id, path)

    print("\nSync complete.")


def main() -> None:
    notebook_id = get_notebook_id()
    print(f"Notebook:  {notebook_id}")
    print(f"Repo root: {REPO_ROOT}")
    print()
    asyncio.run(sync(notebook_id))


if __name__ == "__main__":
    main()
