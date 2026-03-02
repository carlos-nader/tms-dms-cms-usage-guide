#!/usr/bin/env python3
"""
Update alpha pre-release badge in README.md and docs/index.html.

Scans wip/ root for an alpha snapshot file (guide*alpha*.tex).
- If found: fills ALPHA-BADGE-START/END and ALPHA-FOOTER-START/END delimiters
- If not found: clears delimiter blocks (badge absent)

Usage:
  python scripts/update-alpha-badge.py

Returns:
  - Exit code 0: Success (with or without alpha snapshot)
  - Exit code 1: I/O error
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
WIP_DIR = REPO_ROOT / "wip"
README_PATH = REPO_ROOT / "README.md"
INDEX_PATH = REPO_ROOT / "docs" / "index.html"

GITHUB_REPO = "https://github.com/carlos-nader/tms-dms-cms-usage-guide"

# Matches: guide-v0.4.2.0-alpha.1-20260301.tex
#          guide-v0.4.2.0-alpha.1.1-20260301.tex
TEX_PATTERN = re.compile(r'^guide-(v[\d.]+-alpha\.[\d.]+)-(\d{8})\.tex$')
PDF_PATTERN = re.compile(r'^guide-(v[\d.]+-alpha\.[\d.]+)-(\d{8})\.pdf$')


def alpha_sort_key(version, yyyymmdd):
    """Sort key for alpha versions (core version, alpha counters, date)."""
    core_part, alpha_part = version[1:].split("-alpha.")
    core_nums = tuple(int(n) for n in core_part.split("."))
    alpha_nums = tuple(int(n) for n in alpha_part.split("."))
    date_num = int(yyyymmdd)
    return core_nums, alpha_nums, date_num


def find_alpha_snapshot():
    """Return latest alpha snapshot in wip/ root as (version, filename) or (None, None)."""
    candidates = []
    for f in WIP_DIR.iterdir():
        if not f.is_file():
            continue
        m = TEX_PATTERN.match(f.name)
        if m:
            version = m.group(1)
            yyyymmdd = m.group(2)
            candidates.append((alpha_sort_key(version, yyyymmdd), version, f.name))

    if candidates:
        candidates.sort()
        _, version, fname = candidates[-1]
        return version, fname
    return None, None


def find_alpha_pdf(target_tex_filename=None):
    """Return matching latest alpha PDF in wip/ root, preferring exact stem match to target tex."""
    if target_tex_filename:
        expected_pdf = Path(target_tex_filename).with_suffix('.pdf').name
        expected_path = WIP_DIR / expected_pdf
        if expected_path.exists() and expected_path.is_file():
            return expected_pdf

    candidates = []
    for f in WIP_DIR.iterdir():
        if not f.is_file():
            continue
        m = PDF_PATTERN.match(f.name)
        if m:
            version = m.group(1)
            yyyymmdd = m.group(2)
            candidates.append((alpha_sort_key(version, yyyymmdd), f.name))

    if candidates:
        candidates.sort()
        return candidates[-1][1]
    return None


def replace_block(content, start_tag, end_tag, inner):
    """
    Replace everything between start_tag and end_tag (inclusive).
    If inner is non-empty, inserts it between the tags.
    If inner is empty, leaves tags on consecutive lines (block cleared).
    Returns (new_content, replacement_count).
    """
    pattern = re.compile(
        re.escape(start_tag) + r'.*?' + re.escape(end_tag),
        re.DOTALL
    )
    if inner:
        replacement = f"{start_tag}\n{inner}\n{end_tag}"
    else:
        replacement = f"{start_tag}\n{end_tag}"
    return pattern.subn(replacement, content)


def build_readme_badge(version):
    # shields.io uses -- to represent a literal - in badge labels
    version_encoded = version.replace('-', '--')
    badge_url = (
        f"https://img.shields.io/badge/alpha-{version_encoded}-orange"
        f"?style=for-the-badge&logo=flask&logoColor=white"
    )
    releases_url = f"{GITHUB_REPO}/releases"
    return f"[![Alpha]({badge_url})]({releases_url})"


def build_readme_footer(version):
    return f"Alpha pre-release available: {version}"


def build_index_badge(version, pdf_filename):
    pdf_url = f"{GITHUB_REPO}/blob/main/wip/{pdf_filename}"
    return (
        f'<a href="{pdf_url}"\n'
        f'   target="_blank" rel="noopener noreferrer" style="text-decoration: none;">\n'
        f'  <span style="background: linear-gradient(135deg, #ff8c00, #e65c00);\n'
        f'               color: white; padding: 0.4em 0.8em; border-radius: 20px;\n'
        f'               font-weight: bold; font-size: 0.85rem;\n'
        f'               box-shadow: 0 2px 4px rgba(255,140,0,0.3);\n'
        f'               display: inline-block; margin-top: 0.4em;">\n'
        f'    Alpha {version} \u2014 Pre-release PDF\n'
        f'  </span>\n'
        f'</a>'
    )


def update_file(path, updates):
    """
    Apply a list of (start_tag, end_tag, inner) updates to a file.
    Returns True if the file was modified.
    """
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"✗ Cannot read {path}: {e}")
        sys.exit(1)

    updated = content
    for start_tag, end_tag, inner in updates:
        updated, count = replace_block(updated, start_tag, end_tag, inner)
        if count == 0:
            print(f"  ⚠ Delimiter not found in {path.name}: {start_tag}")

    if updated == content:
        print(f"  No changes in {path.name}")
        return False

    try:
        path.write_text(updated, encoding='utf-8')
        print(f"✓ Updated {path.name}")
        return True
    except Exception as e:
        print(f"✗ Cannot write {path}: {e}")
        sys.exit(1)


def main():
    print("=" * 60)
    print("Alpha Badge Updater")
    print("=" * 60)

    version, tex_filename = find_alpha_snapshot()

    if version:
        pdf_filename = find_alpha_pdf(tex_filename)
        print(f"✓ Alpha snapshot: {tex_filename}")
        print(f"  Version: {version}")
        if pdf_filename:
            print(f"  PDF: {pdf_filename}")
        else:
            print("  ⚠ No alpha PDF found in wip/ — index.html badge will be skipped")

        readme_badge = build_readme_badge(version)
        readme_footer = build_readme_footer(version)

        print("\n[README.md]")
        update_file(README_PATH, [
            ("<!-- ALPHA-BADGE-START -->", "<!-- ALPHA-BADGE-END -->", readme_badge),
            ("<!-- ALPHA-FOOTER-START -->", "<!-- ALPHA-FOOTER-END -->", readme_footer),
        ])

        print("\n[docs/index.html]")
        index_badge = build_index_badge(version, pdf_filename) if pdf_filename else ""
        update_file(INDEX_PATH, [
            ("<!-- ALPHA-BADGE-START -->", "<!-- ALPHA-BADGE-END -->", index_badge),
        ])

    else:
        print("  No alpha snapshot in wip/ — clearing badge blocks")

        print("\n[README.md]")
        update_file(README_PATH, [
            ("<!-- ALPHA-BADGE-START -->", "<!-- ALPHA-BADGE-END -->", ""),
            ("<!-- ALPHA-FOOTER-START -->", "<!-- ALPHA-FOOTER-END -->", ""),
        ])

        print("\n[docs/index.html]")
        update_file(INDEX_PATH, [
            ("<!-- ALPHA-BADGE-START -->", "<!-- ALPHA-BADGE-END -->", ""),
        ])

    print("\n" + "=" * 60)
    print("✅ Done")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
