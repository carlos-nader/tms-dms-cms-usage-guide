#!/usr/bin/env python3

"""
Generate INTEGRATED-FILES Report (v4 - ISSUES + MILESTONES)
Tracks repository state: files, commits, tags, issues, and milestones
Outputs: INTEGRATED-FILES.md + INTEGRATED-FILES.json
"""

import os
import json
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path
import re
import urllib.request
import urllib.error

# Configuration
REPO_ROOT = Path.cwd()
TIMEZONE = "UTC-3"
OUTPUT_MD = "INTEGRATED-FILES.md"
OUTPUT_JSON = "INTEGRATED-FILES.json"
DEBUG = os.environ.get("INTEGRATED_FILES_DEBUG", "0") == "1"

def debug_log(msg):
    """Print debug message to stdout"""
    if DEBUG:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] DEBUG: {msg}", file=sys.stdout, flush=True)

# Tracked paths (LOWERCASE)
TRACKED_PATHS = {
    "wip/": {"ext": ".tex", "subfolders": ["wip/"], "exclude_pattern": r"^guide-v\d+\.\d+\.\d+\.\d+-alpha\.\d+(\.\d+)?-\d{8}\.tex$"},
    "wip/ (alpha snapshots)": {"ext": ".tex", "subfolders": ["wip/"], "include_pattern": r"^guide-v\d+\.\d+\.\d+\.\d+-alpha\.\d+(\.\d+)?-\d{8}\.tex$", "label": "Alpha Snapshots"},
    "archive/": {"ext": ".tex", "subfolders": ["archive/GUIDE/", "archive/WIP/"]},
    "docs/": {"ext": ".md", "subfolders": ["docs/"]},
    "wip/guide/": {"ext": ".tex", "subfolders": ["wip/guide/"]},
    "guide.tex": {"ext": ".tex", "subfolders": None, "label": "Repository Root"},
    "misc/STYLE-GUIDE.md": {"ext": ".md", "subfolders": None, "label": "misc/"},
}

# ---------------------------------------------------------------------------
# Git helpers
# ---------------------------------------------------------------------------

def run_git_command(cmd):
    """Execute git command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=REPO_ROOT)
        return result.stdout.strip()
    except Exception as e:
        debug_log(f"Error running git command: {e}")
        return ""

def normalize_repo_path(path):
    """Normalize paths to Git-friendly repo-relative POSIX format."""
    return str(path).replace("\\", "/").lstrip("./")

# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------

def _github_env():
    """Return (token, repo) tuple, or (None, None) if not configured."""
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    if not token or not repo:
        return None, None
    return token, repo

def _github_headers(token):
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }

def _fetch_github_api(url, token):
    """Fetch a GitHub API URL and return parsed JSON, or None on error."""
    try:
        req = urllib.request.Request(url, headers=_github_headers(token))
        with urllib.request.urlopen(req, timeout=10) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        debug_log(f"ERROR fetching {url}: {e}")
        return None

# ---------------------------------------------------------------------------
# Data collection
# ---------------------------------------------------------------------------

def get_repo_info():
    """Get repository metadata"""
    debug_log("=== REPO INFO ===")
    repo_name = run_git_command("git config --get remote.origin.url").split("/")[-1].replace(".git", "")
    repo_url = run_git_command("git config --get remote.origin.url").replace(".git", "")
    debug_log(f"Repo name: {repo_name}, URL: {repo_url}")

    # Repository creation date (root commit). This avoids expensive `git log` output capture
    # and is cross-platform (no reliance on `tail`).
    root_commits = run_git_command("git rev-list --max-parents=0 HEAD")
    if root_commits:
        root_commit = root_commits.splitlines()[-1].strip()
        created_line = run_git_command(f"git show -s --format=%ai {root_commit}")
        created_date = created_line.split()[0] if created_line else "Unknown"
    else:
        created_date = "Unknown"

    last_push = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" {TIMEZONE}"
    total_commits = run_git_command("git rev-list --count HEAD")
    debug_log(f"Total commits: {total_commits}")

    releases = run_git_command("git tag -l 'v[0-9]*.[0-9]*.[0-9]*.[0-9]*' --sort=-version:refname | head -5")

    # Get languages (simple heuristic)
    tex_files = list(REPO_ROOT.glob("**/*.tex"))
    md_files = list(REPO_ROOT.glob("**/*.md"))
    tex_count, md_count = len(tex_files), len(md_files)
    total_files = tex_count + md_count
    tex_pct = int(tex_count / total_files * 100) if total_files > 0 else 0
    md_pct = int(md_count / total_files * 100) if total_files > 0 else 0
    debug_log(f"Found {tex_count} .tex files, {md_count} .md files (total: {total_files})")

    return {
        "name": repo_name,
        "url": repo_url,
        "created": created_date,
        "last_push": last_push,
        "total_commits": total_commits,
        "releases": releases.split("\n") if releases else [],
        "languages": f"LaTeX: {tex_pct}%, Markdown: {md_pct}%",
    }

def get_file_status(file_path):
    """Determine file status via git"""
    try:
        repo_path = normalize_repo_path(file_path)
        in_index = subprocess.run(
            ["git", "ls-files", "--error-unmatch", "--", repo_path],
            cwd=REPO_ROOT, capture_output=True, text=True,
        )
        if in_index.returncode != 0:
            return "untracked"
        if run_git_command(f'git diff --name-only -- "{repo_path}"'):
            return "modified"
        if run_git_command(f'git diff --cached --name-only -- "{repo_path}"'):
            return "staged"
        return "tracked"
    except Exception:
        return "unknown"

def _scan_folder(folder_path, config):
    """Scan a single folder and return list of file dicts matching config."""
    files_list = []
    exclude_pat = config.get("exclude_pattern")
    include_pat = config.get("include_pattern")
    try:
        matching_files = list(folder_path.glob(f"*{config['ext']}"))
        debug_log(f"  Found {len(matching_files)} files matching *{config['ext']}")
        for file in matching_files:
            if not file.is_file():
                continue
            fname = file.name
            if exclude_pat and re.match(exclude_pat, fname):
                debug_log(f"  SKIP (excluded): {fname}")
                continue
            if include_pat and not re.match(include_pat, fname):
                continue
            file_rel = file.relative_to(REPO_ROOT).as_posix()
            stat = file.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            size = stat.st_size
            status = get_file_status(file_rel)
            debug_log(f"  - {file_rel} ({size} bytes, {status})")
            files_list.append({
                "path": file_rel,
                "status": status,
                "last_modified": mod_time,
                "size": f"{size} bytes",
            })
    except Exception as e:
        debug_log(f"  ERROR scanning {folder_path}: {e}")
    return files_list

def get_tracked_files():
    """Get all tracked files with status and metadata"""
    debug_log("=== SCANNING TRACKED FILES ===")
    tracked_files = {}
    section_num = 1
    total_found = 0

    for base_path, config in TRACKED_PATHS.items():
        debug_log(f"Processing base_path: {base_path}")

        if config["subfolders"]:
            for subfolder in config["subfolders"]:
                folder_path = REPO_ROOT / subfolder
                debug_log(f"  Checking subfolder: {folder_path}")
                if not (folder_path.exists() and folder_path.is_dir()):
                    debug_log("  SKIP: path does not exist or is not a directory")
                    continue
                files_list = _scan_folder(folder_path, config)
                if files_list:
                    section_label = config.get("label", subfolder)
                    tracked_files[f"{section_num}. {section_label}"] = files_list
                    section_num += 1
                    total_found += len(files_list)
        else:
            file_path = REPO_ROOT / base_path
            debug_log(f"  Checking single file: {file_path}")
            if not file_path.exists():
                debug_log("  SKIP: file does not exist")
                continue
            stat = file_path.stat()
            mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            size = stat.st_size
            status = get_file_status(base_path)
            debug_log(f"  Found: {size} bytes, {status}")
            label = config.get("label", "Repository Root")
            tracked_files[f"{section_num}. {base_path} ({label})"] = [{
                "path": base_path,
                "status": status,
                "last_modified": mod_time,
                "size": f"{size} bytes",
            }]
            section_num += 1
            total_found += 1

    debug_log(f"TOTAL FILES FOUND: {total_found}")
    return tracked_files

def get_recent_commits(limit=10):
    """Get recent commits that modified tracked files"""
    debug_log("=== RECENT COMMITS ===")
    cmd = f"git log --oneline -n {limit} --format='%H|%ai|%an|%s'"
    output = run_git_command(cmd)
    commits = []

    for line in output.split("\n"):
        if not line:
            continue
        parts = line.split("|")
        if len(parts) < 4:
            continue
        commit_hash = parts[0]
        timestamp = parts[1]
        author = parts[2]
        modified = run_git_command(f"git diff-tree --no-commit-id --name-only -r {commit_hash}")
        commits.append({
            "hash": commit_hash[:7],
            "date": timestamp.split()[0],
            "time": timestamp.split()[1],
            "author": author,
            "modified_files": [f for f in modified.split("\n") if f][:5],
        })

    debug_log(f"Found {len(commits)} recent commits")
    return commits

def _collect_git_tags(glob_pattern, regex_pattern, label):
    """Shared implementation for version and pre-release tag collection."""
    debug_log(f"=== {label.upper()} ===")
    output = run_git_command(f"git tag -l '{glob_pattern}' --sort=-version:refname")
    tags = []

    for tag in output.split("\n"):
        if not tag or not re.match(regex_pattern, tag):
            continue
        commit_hash = run_git_command(f"git rev-list -n 1 {tag}")
        date_raw = run_git_command(f"git log -1 --format=%ai {tag}")
        tag_date = date_raw.split()[0] if date_raw else "Unknown"
        tag_msg_raw = run_git_command(f"git tag -l {tag} -n1")
        tag_msg = tag_msg_raw.split(" ", 1)[-1] if tag_msg_raw else ""
        tags.append({
            "tag": tag,
            "commit": commit_hash[:7] if commit_hash else "Unknown",
            "date": tag_date,
            "message": tag_msg[:60] if tag_msg else "-",
        })

    debug_log(f"Found {len(tags)} {label}")
    return tags[:10]

def get_version_tags():
    """Get version tags matching vX.X.X.X pattern"""
    return _collect_git_tags("v*.*.*.*", r"^v\d+\.\d+\.\d+\.\d+$", "version tags")

def get_prerelease_tags():
    """Get pre-release tags matching vX.X.X.X-alpha.N[.M] pattern"""
    return _collect_git_tags("v*-alpha.*", r"^v\d+\.\d+\.\d+\.\d+-alpha\.\d+(\.\d+)?$", "pre-release tags")

def get_github_issues():
    """Get GitHub issues using REST API with proper token"""
    debug_log("=== GITHUB ISSUES ===")
    token, repo = _github_env()
    if token is None:
        debug_log("SKIP: GITHUB_TOKEN or GITHUB_REPOSITORY not set")
        return {"open": [], "closed": []}

    debug_log(f"Fetching issues from {repo}")
    base = f"https://api.github.com/repos/{repo}/issues"
    thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()

    open_issues = _fetch_github_api(f"{base}?state=open&per_page=10", token) or []
    open_issues = [i for i in open_issues if "pull_request" not in i]
    debug_log(f"Found {len(open_issues)} open issues")

    closed_issues = _fetch_github_api(
        f"{base}?state=closed&since={thirty_days_ago}&per_page=10&sort=updated&direction=desc", token
    ) or []
    closed_issues = [i for i in closed_issues if "pull_request" not in i]
    debug_log(f"Found {len(closed_issues)} recently closed issues")

    return {"open": open_issues, "closed": closed_issues}

def get_github_milestones():
    """Get GitHub milestones using REST API"""
    debug_log("=== GITHUB MILESTONES ===")
    token, repo = _github_env()
    if token is None:
        debug_log("SKIP: GITHUB_TOKEN or GITHUB_REPOSITORY not set")
        return {"open": [], "closed": []}

    debug_log(f"Fetching milestones from {repo}")
    base = f"https://api.github.com/repos/{repo}/milestones"

    open_ms = _fetch_github_api(f"{base}?state=open&per_page=10", token) or []
    debug_log(f"Found {len(open_ms)} open milestones")

    closed_ms = _fetch_github_api(
        f"{base}?state=closed&per_page=10&sort=updated&direction=desc", token
    ) or []
    debug_log(f"Found {len(closed_ms)} closed milestones")

    return {"open": open_ms, "closed": closed_ms}

def collect_all_data():
    """Collect all report data once and return as a dict."""
    return {
        "repo_info": get_repo_info(),
        "tracked_files": get_tracked_files(),
        "commits": get_recent_commits(10),
        "tags": get_version_tags(),
        "prerelease_tags": get_prerelease_tags(),
        "issues": get_github_issues(),
        "milestones": get_github_milestones(),
    }

# ---------------------------------------------------------------------------
# Markdown section helpers
# ---------------------------------------------------------------------------

def _md_repo_info(repo_info):
    return (
        "## 1. REPOSITORY INFO\n\n"
        "| Field | Value |\n|-------|-------|\n"
        f"| Name | {repo_info['name']} |\n"
        f"| URL | [{repo_info['url']}]({repo_info['url']}) |\n"
        f"| Created | {repo_info['created']} |\n"
        f"| Last Push | {repo_info['last_push']} |\n"
        f"| Total Commits | {repo_info['total_commits']} |\n"
        f"| Releases | {', '.join(repo_info['releases']) if repo_info['releases'] else 'None'} |\n"
        f"| Languages | {repo_info['languages']} |\n"
    )

def _md_tracked_files(tracked_files):
    lines = ["## 2. TRACKED FILES\n"]
    if not tracked_files:
        lines.append("**No tracked files found.**\n")
        return "\n".join(lines)
    for section_name, files in tracked_files.items():
        lines.append(f"### {section_name}\n")
        lines.append("| File Path | Status | Last Modified | Size |")
        lines.append("|-----------|--------|---------------|------|")
        for f in files:
            lines.append(f"| {f['path']} | {f['status']} | {f['last_modified']} | {f['size']} |")
        lines.append("")
    return "\n".join(lines)

def _md_commits(commits):
    lines = [
        "## 3. COMMITS\n",
        "Commits that modified tracked files (last 10 commits):\n",
    ]
    if commits:
        lines += [
            "| Date/Time | Author | Modified Tracked Files |",
            "|-----------|--------|------------------------|",
        ]
        for c in commits:
            modified_str = ", ".join(c["modified_files"][:3]) if c["modified_files"] else "-"
            lines.append(f"| {c['date']} {c['time']} | {c['author']} | {modified_str} |")
    else:
        lines.append("**No commits found.**")
    return "\n".join(lines)

def _md_tag_table(tag_list):
    rows = [
        "| Tag | Commit | Date | Message |",
        "|-----|--------|------|---------|",
    ]
    for t in tag_list:
        rows.append(f"| {t['tag']} | {t['commit']} | {t['date']} | {t['message']} |")
    return "\n".join(rows)

def _md_tags(tags, prerelease_tags):
    lines = [
        "## 4. VERSION TAGS\n",
        "Tags matching pattern: `^v[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$`\n",
        _md_tag_table(tags) if tags else "**No version tags found.**",
        "\n---\n",
        "## 5. PRE-RELEASE TAGS\n",
        "Tags matching pattern: `^v[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+-alpha\\.[0-9]+(\\.[0-9]+)?$`\n",
        _md_tag_table(prerelease_tags) if prerelease_tags else "**No pre-release tags found.**",
    ]
    return "\n".join(lines)

def _md_section_table(items, empty_msg, headers, row_fn):
    """Build a markdown table section; returns list of lines."""
    if not items:
        return [empty_msg]
    return [*headers, *(row_fn(item) for item in items[:10])]

def _issue_labels(issue):
    return ", ".join(l["name"] for l in issue.get("labels", [])) or "-"

def _open_issue_row(issue):
    return f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {_issue_labels(issue)} |"

def _closed_issue_row(issue):
    closed_date = (issue.get("closed_at") or "Unknown")[:10]
    return f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {closed_date} | {_issue_labels(issue)} |"

def _md_open_issues_section(issues_list):
    return _md_section_table(
        issues_list, "**No open issues.**",
        ["| # | Title | Created | Labels |", "|---|-------|---------|--------|"],
        _open_issue_row,
    )

def _md_closed_issues_section(issues_list):
    return _md_section_table(
        issues_list, "**No recently closed issues.**",
        ["| # | Title | Created | Closed | Labels |", "|---|-------|---------|--------|--------|"],
        _closed_issue_row,
    )

def _md_issues(issues):
    return "\n".join([
        "## 6. GITHUB ISSUES\n",
        "### 6.1 Open Issues\n",
        *_md_open_issues_section(issues.get("open", [])),
        "\n### 6.2 Recently Closed Issues (Last 30 days)\n",
        *_md_closed_issues_section(issues.get("closed", [])),
    ])

def _ms_progress(ms):
    o, c = ms.get("open_issues", 0), ms.get("closed_issues", 0)
    return f"{c}/{o + c}" if (o + c) > 0 else "0/0"

def _open_ms_row(ms):
    due = (ms.get("due_on") or "No due date")[:10]
    desc = (ms.get("description") or "N/A")[:40]
    return f"| {ms['title']} | {_ms_progress(ms)} | {due} | {desc} |"

def _closed_ms_row(ms):
    return f"| {ms['title']} | {_ms_progress(ms)} | {(ms.get('closed_at') or 'Unknown')[:10]} |"

def _md_open_milestones_section(ms_list):
    return _md_section_table(
        ms_list, "**No open milestones.**",
        ["| Title | Progress | Due Date | Description |", "|-------|----------|----------|-------------|"],
        _open_ms_row,
    )

def _md_closed_milestones_section(ms_list):
    return _md_section_table(
        ms_list, "**No closed milestones.**",
        ["| Title | Progress | Closed Date |", "|-------|----------|-------------|"],
        _closed_ms_row,
    )

def _md_milestones(milestones):
    return "\n".join([
        "## 7. GITHUB MILESTONES\n",
        "### 7.1 Open Milestones\n",
        *_md_open_milestones_section(milestones.get("open", [])),
        "\n### 7.2 Closed Milestones\n",
        *_md_closed_milestones_section(milestones.get("closed", [])),
    ])

# ---------------------------------------------------------------------------
# Output generators
# ---------------------------------------------------------------------------

def generate_markdown(data):
    """Generate INTEGRATED-FILES.md from pre-collected data."""
    repo_info = data["repo_info"]
    header = (
        "# INTEGRATED FILES REPORT\n\n"
        f"**Repository:** {repo_info['name']}\n\n"
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {TIMEZONE}\n\n"
        "**Trigger:** [push | workflow_dispatch]\n\n"
        "**Branch:** main\n\n---\n\n"
    )
    sections = [
        _md_repo_info(repo_info),
        "---\n",
        _md_tracked_files(data["tracked_files"]),
        "---\n",
        _md_commits(data["commits"]),
        "\n---\n",
        _md_tags(data["tags"], data["prerelease_tags"]),
        "\n---\n",
        _md_issues(data["issues"]),
        "\n---\n",
        _md_milestones(data["milestones"]),
        "\n---\n\n**End of Report**\n",
    ]
    return header + "\n".join(sections)

def generate_json_data(data):
    """Generate JSON structured data from pre-collected data."""
    issues = data["issues"]
    milestones = data["milestones"]
    return {
        "generated": datetime.now().isoformat(),
        "repository": data["repo_info"],
        "tracked_files": data["tracked_files"],
        "commits": data["commits"],
        "tags": data["tags"],
        "prerelease_tags": data["prerelease_tags"],
        "issues": {
            "open": len(issues.get("open", [])),
            "closed": len(issues.get("closed", [])),
        },
        "milestones": {
            "open": len(milestones.get("open", [])),
            "closed": len(milestones.get("closed", [])),
        },
    }

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    """Main execution"""
    debug_log("=" * 60)
    debug_log("STARTING INTEGRATED-FILES REPORT GENERATION (v4)")
    debug_log("=" * 60)
    debug_log(f"Repo root: {REPO_ROOT}")
    debug_log(f"Working directory: {os.getcwd()}")

    debug_log("\n[STEP 0] Collecting all data...")
    data = collect_all_data()

    debug_log("\n[STEP 1] Generating Markdown...")
    md_content = generate_markdown(data)
    md_size = len(md_content.encode("utf-8"))
    debug_log(f"Markdown size: {md_size} bytes")
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    debug_log(f"✓ {OUTPUT_MD} written to disk")

    debug_log("\n[STEP 2] Generating JSON...")
    json_data = generate_json_data(data)
    json_str = json.dumps(json_data, indent=2, ensure_ascii=False)
    json_size = len(json_str.encode("utf-8"))
    debug_log(f"JSON size: {json_size} bytes")
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        f.write(json_str)
    debug_log(f"✓ {OUTPUT_JSON} written to disk")

    debug_log("\n" + "=" * 60)
    debug_log("DONE!")
    debug_log("=" * 60)

if __name__ == "__main__":
    main()
