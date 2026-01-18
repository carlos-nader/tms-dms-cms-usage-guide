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
DEBUG = True  # Enable debug logging

def debug_log(msg):
    """Print debug message to stdout"""
    if DEBUG:
        timestamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] DEBUG: {msg}", file=sys.stdout, flush=True)

# Tracked paths (LOWERCASE)
TRACKED_PATHS = {
    "wip/": {"ext": ".tex", "subfolders": ["wip/", "wip/GUIDE/"]},
    "archive/": {"ext": ".tex", "subfolders": ["archive/", "archive/GUIDE/", "archive/WIP/"]},
    "docs/": {"ext": ".md", "subfolders": ["docs/"]},
    "guide.tex": {"ext": ".tex", "subfolders": None},
}

# Helper functions
def run_git_command(cmd):
    """Execute git command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=REPO_ROOT)
        return result.stdout.strip()
    except Exception as e:
        debug_log(f"Error running git command: {e}")
        return ""

def get_repo_info():
    """Get repository metadata"""
    debug_log("=== REPO INFO ===")
    repo_name = run_git_command("git config --get remote.origin.url").split("/")[-1].replace(".git", "")
    debug_log(f"Repo name: {repo_name}")
    repo_url = run_git_command("git config --get remote.origin.url").replace(".git", "")
    debug_log(f"Repo URL: {repo_url}")
    created_date = run_git_command("git log --follow --format=%ai -- . | tail -1").split()[0] if run_git_command("git log --follow --format=%ai -- . | tail -1") else "Unknown"
    last_push = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" {TIMEZONE}"
    total_commits = run_git_command("git rev-list --count HEAD")
    debug_log(f"Total commits: {total_commits}")
    releases = run_git_command("git tag -l 'v[0-9]*.[0-9]*.[0-9]*.[0-9]*' --sort=-version:refname | head -5")

    # Get languages (simple heuristic)
    tex_files = list(REPO_ROOT.glob("**/*.tex"))
    md_files = list(REPO_ROOT.glob("**/*.md"))
    tex_count = len(tex_files)
    md_count = len(md_files)
    total_files = tex_count + md_count
    tex_pct = int((tex_count / total_files * 100)) if total_files > 0 else 0
    md_pct = int((md_count / total_files * 100)) if total_files > 0 else 0
    debug_log(f"Found {tex_count} .tex files, {md_count} .md files (total: {total_files})")

    return {
        "name": repo_name,
        "url": repo_url,
        "created": created_date,
        "last_push": last_push,
        "total_commits": total_commits,
        "releases": releases.split("\n") if releases else [],
        "languages": f"LaTeX: {tex_pct}%, Markdown: {md_pct}%"
    }

def get_file_status(file_path):
    """Determine file status via git"""
    try:
        in_index = run_git_command(f"git ls-files '{file_path}'")
        if not in_index:
            return "untracked"
        diff = run_git_command(f"git diff --name-only '{file_path}'")
        if diff:
            return "modified"
        staged = run_git_command(f"git diff --cached --name-only '{file_path}'")
        if staged:
            return "staged"
        return "tracked"
    except:
        return "unknown"

def get_tracked_files():
    """Get all tracked files with status and metadata"""
    debug_log("=== SCANNING TRACKED FILES ===")
    tracked_files = {}
    section_num = 1
    total_found = 0

    for base_path, config in TRACKED_PATHS.items():
        debug_log(f"Processing base_path: {base_path}")
        if config["subfolders"]:
            # Multi-folder tracking (wip, archive)
            for subfolder in config["subfolders"]:
                folder_path = REPO_ROOT / subfolder
                debug_log(f" Checking subfolder: {folder_path}")
                if folder_path.exists() and folder_path.is_dir():
                    files_list = []
                    try:
                        pattern = f"*{config['ext']}"
                        matching_files = list(folder_path.rglob(pattern))
                        debug_log(f" Found {len(matching_files)} files matching {pattern}")
                        for file in matching_files:
                            if file.is_file():
                                file_rel = file.relative_to(REPO_ROOT)
                                stat = file.stat()
                                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                                size = stat.st_size
                                status = get_file_status(str(file_rel))
                                debug_log(f" - {file_rel} ({size} bytes, {status})")
                                files_list.append({
                                    "path": str(file_rel),
                                    "status": status,
                                    "last_modified": mod_time,
                                    "size": f"{size} bytes"
                                })
                                total_found += 1
                    except Exception as e:
                        debug_log(f" ERROR scanning {subfolder}: {e}")
                    if files_list:
                        section_key = f"{section_num}. {subfolder}"
                        tracked_files[section_key] = files_list
                        section_num += 1
                else:
                    debug_log(f" SKIP: path does not exist or is not a directory")
        else:
            # Single file (guide.tex)
            file_path = REPO_ROOT / base_path
            debug_log(f" Checking single file: {file_path}")
            if file_path.exists():
                stat = file_path.stat()
                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                size = stat.st_size
                status = get_file_status(base_path)
                debug_log(f" Found: {size} bytes, {status}")
                section_key = f"{section_num}. {base_path} (Repository Root)"
                tracked_files[section_key] = [{
                    "path": base_path,
                    "status": status,
                    "last_modified": mod_time,
                    "size": f"{size} bytes"
                }]
                section_num += 1
                total_found += 1
            else:
                debug_log(f" SKIP: file does not exist")

    debug_log(f"TOTAL FILES FOUND: {total_found}")
    return tracked_files

def get_recent_commits(limit=10):
    """Get recent commits that modified tracked files"""
    debug_log("=== RECENT COMMITS ===")
    cmd = f"git log --oneline -n {limit} --format='%H|%ai|%an|%s'"
    output = run_git_command(cmd)
    commits = []
    for line in output.split("\n"):
        if line:
            parts = line.split("|")
            if len(parts) >= 4:
                commit_hash = parts[0]
                timestamp = parts[1]
                author = parts[2]
                modified = run_git_command(f"git diff-tree --no-commit-id --name-only -r {commit_hash}")
                commits.append({
                    "hash": commit_hash[:7],
                    "date": timestamp.split()[0],
                    "time": timestamp.split()[1],
                    "author": author,
                    "modified_files": [f for f in modified.split("\n") if f][:5]
                })
    debug_log(f"Found {len(commits)} recent commits")
    return commits

def get_version_tags():
    """Get version tags matching vX.X.X.X pattern"""
    debug_log("=== VERSION TAGS ===")
    pattern = r"^v\d+\.\d+\.\d+\.\d+$"
    cmd = "git tag -l 'v*.*.*.*' --sort=-version:refname"
    output = run_git_command(cmd)
    tags = []
    for tag in output.split("\n"):
        if tag and re.match(pattern, tag):
            commit_hash = run_git_command(f"git rev-list -n 1 {tag}")
            tag_date = run_git_command(f"git log -1 --format=%ai {tag}").split()[0] if run_git_command(f"git log -1 --format=%ai {tag}") else "Unknown"
            tag_msg = run_git_command(f"git tag -l {tag} -n1").split(" ", 1)[-1] if run_git_command(f"git tag -l {tag} -n1") else ""
            tags.append({
                "tag": tag,
                "commit": commit_hash[:7] if commit_hash else "Unknown",
                "date": tag_date,
                "message": tag_msg[:60] if tag_msg else "-"
            })
    debug_log(f"Found {len(tags)} version tags")
    return tags[:10]

def get_github_issues():
    """Get GitHub issues using REST API with proper token"""
    debug_log("=== GITHUB ISSUES ===")
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")

    if not token or not repo:
        debug_log("SKIP: GITHUB_TOKEN or GITHUB_REPOSITORY not set")
        return {"open": [], "closed": []}

    debug_log(f"Fetching issues from {repo}")
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Open issues
        open_url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=10"
        req = urllib.request.Request(open_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            open_issues = json.loads(response.read().decode())
        debug_log(f"Found {len(open_issues)} open issues")

        # Recently closed issues (last 30 days)
        thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()
        closed_url = f"https://api.github.com/repos/{repo}/issues?state=closed&since={thirty_days_ago}&per_page=10&sort=updated&direction=desc"
        req = urllib.request.Request(closed_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            closed_issues = json.loads(response.read().decode())
        debug_log(f"Found {len(closed_issues)} recently closed issues")

        return {"open": open_issues, "closed": closed_issues}

    except Exception as e:
        debug_log(f"ERROR fetching issues: {e}")
        return {"open": [], "closed": []}

def get_github_milestones():
    """Get GitHub milestones using REST API"""
    debug_log("=== GITHUB MILESTONES ===")
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")

    if not token or not repo:
        debug_log("SKIP: GITHUB_TOKEN or GITHUB_REPOSITORY not set")
        return {"open": [], "closed": []}

    debug_log(f"Fetching milestones from {repo}")
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Open milestones
        open_url = f"https://api.github.com/repos/{repo}/milestones?state=open&per_page=10"
        req = urllib.request.Request(open_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            open_milestones = json.loads(response.read().decode())
        debug_log(f"Found {len(open_milestones)} open milestones")

        # Closed milestones (last 30 days)
        thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()
        closed_url = f"https://api.github.com/repos/{repo}/milestones?state=closed&per_page=10&sort=updated&direction=desc"
        req = urllib.request.Request(closed_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            closed_milestones = json.loads(response.read().decode())
        debug_log(f"Found {len(closed_milestones)} closed milestones")

        return {"open": open_milestones, "closed": closed_milestones}

    except Exception as e:
        debug_log(f"ERROR fetching milestones: {e}")
        return {"open": [], "closed": []}

def generate_markdown():
    """Generate INTEGRATED-FILES.md"""
    repo_info = get_repo_info()
    tracked_files = get_tracked_files()
    commits = get_recent_commits(10)
    tags = get_version_tags()
    issues = get_github_issues()
    milestones = get_github_milestones()

    md = f"""# INTEGRATED FILES REPORT

**Repository:** {repo_info['name']}

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} {TIMEZONE}

**Trigger:** [push | workflow_dispatch]

**Branch:** main

---

## 1. REPOSITORY INFO

| Field | Value |
|-------|-------|
| Name | {repo_info['name']} |
| URL | [{repo_info['url']}]({repo_info['url']}) |
| Created | {repo_info['created']} |
| Last Push | {repo_info['last_push']} |
| Total Commits | {repo_info['total_commits']} |
| Releases | {', '.join(repo_info['releases']) if repo_info['releases'] else 'None'} |
| Languages | {repo_info['languages']} |

---

## 2. TRACKED FILES

"""

    # Add tracked files by section
    if tracked_files:
        for section_name, files in tracked_files.items():
            md += f"### {section_name}\n\n"
            md += "| File Path | Status | Last Modified | Size |\n"
            md += "|-----------|--------|---------------|------|\n"
            for f in files:
                md += f"| {f['path']} | {f['status']} | {f['last_modified']} | {f['size']} |\n"
            md += "\n"
    else:
        md += "**No tracked files found.**\n\n"

    md += "---\n\n## 3. COMMITS\n\n"
    md += "Commits that modified tracked files (last 10 commits):\n\n"

    if commits:
        md += "| Date/Time | Author | Modified Tracked Files |\n"
        md += "|-----------|--------|------------------------|\n"
        for commit in commits:
            modified_str = ", ".join(commit['modified_files'][:3]) if commit['modified_files'] else "-"
            md += f"| {commit['date']} {commit['time']} | {commit['author']} | {modified_str} |\n"
    else:
        md += "**No commits found.**\n"

    md += "\n---\n\n## 4. VERSION TAGS\n\n"
    md += "Tags matching pattern: `^v[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$`\n\n"

    if tags:
        md += "| Tag | Commit | Date | Message |\n"
        md += "|-----|--------|------|----------|\n"
        for tag in tags:
            md += f"| {tag['tag']} | {tag['commit']} | {tag['date']} | {tag['message']} |\n"
    else:
        md += "**No version tags found.**\n"

    md += "\n---\n\n## 5. GITHUB ISSUES\n\n"
    md += "### 5.1 Open Issues\n\n"

    if issues.get("open"):
        md += "| # | Title | Created | Labels |\n"
        md += "|---|-------|---------|--------|\n"
        for issue in issues.get("open", [])[:10]:
            labels = ", ".join([l["name"] for l in issue.get("labels", [])]) or "-"
            md += f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {labels} |\n"
    else:
        md += "**No open issues.**\n"

    md += "\n### 5.2 Recently Closed Issues (Last 30 days)\n\n"

    if issues.get("closed"):
        md += "| # | Title | Created | Closed | Labels |\n"
        md += "|---|-------|---------|--------|--------|\n"
        for issue in issues.get("closed", [])[:10]:
            labels = ", ".join([l["name"] for l in issue.get("labels", [])]) or "-"
            closed_date = issue.get('closed_at', 'Unknown')[:10] if issue.get('closed_at') else 'Unknown'
            md += f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {closed_date} | {labels} |\n"
    else:
        md += "**No recently closed issues.**\n"

    md += "\n---\n\n## 6. GITHUB MILESTONES\n\n"
    md += "### 6.1 Open Milestones\n\n"

    if milestones.get("open"):
        md += "| Title | Progress | Due Date | Description |\n"
        md += "|-------|----------|----------|-------------|\n"
        for ms in milestones.get("open", [])[:10]:
            due_date = ms.get('due_on', 'No due date')[:10] if ms.get('due_on') else "No due date"
            open_issues = ms.get('open_issues', 0)
            closed_issues = ms.get('closed_issues', 0)
            total = open_issues + closed_issues
            progress = f"{closed_issues}/{total}" if total > 0 else "0/0"
            description = ms.get('description', 'N/A')[:40] if ms.get('description') else "N/A"
            md += f"| {ms['title']} | {progress} | {due_date} | {description} |\n"
    else:
        md += "**No open milestones.**\n"

    md += "\n### 6.2 Closed Milestones\n\n"

    if milestones.get("closed"):
        md += "| Title | Progress | Closed Date |\n"
        md += "|-------|----------|-------------|\n"
        for ms in milestones.get("closed", [])[:10]:
            closed_date = ms.get('closed_at', 'Unknown')[:10] if ms.get('closed_at') else 'Unknown'
            open_issues = ms.get('open_issues', 0)
            closed_issues = ms.get('closed_issues', 0)
            total = open_issues + closed_issues
            progress = f"{closed_issues}/{total}" if total > 0 else "0/0"
            md += f"| {ms['title']} | {progress} | {closed_date} |\n"
    else:
        md += "**No closed milestones.**\n"

    md += "\n---\n\n**End of Report**\n"

    return md

def generate_json_data():
    """Generate JSON structured data"""
    repo_info = get_repo_info()
    tracked_files = get_tracked_files()
    commits = get_recent_commits(10)
    tags = get_version_tags()
    issues = get_github_issues()
    milestones = get_github_milestones()

    return {
        "generated": datetime.now().isoformat(),
        "repository": repo_info,
        "tracked_files": tracked_files,
        "commits": commits,
        "tags": tags,
        "issues": {
            "open": len(issues.get("open", [])),
            "closed": len(issues.get("closed", []))
        },
        "milestones": {
            "open": len(milestones.get("open", [])),
            "closed": len(milestones.get("closed", []))
        }
    }

def main():
    """Main execution"""
    debug_log("=" * 60)
    debug_log("STARTING INTEGRATED-FILES REPORT GENERATION (v4)")
    debug_log("=" * 60)
    debug_log(f"Repo root: {REPO_ROOT}")
    debug_log(f"Working directory: {os.getcwd()}")

    # Generate Markdown
    debug_log("\n[STEP 1] Generating Markdown...")
    md_content = generate_markdown()
    md_size = len(md_content.encode('utf-8'))
    debug_log(f"Markdown size: {md_size} bytes")

    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    debug_log(f"✓ {OUTPUT_MD} written to disk")

    # Generate JSON
    debug_log("\n[STEP 2] Generating JSON...")
    json_data = generate_json_data()
    json_str = json.dumps(json_data, indent=2, ensure_ascii=False)
    json_size = len(json_str.encode('utf-8'))
    debug_log(f"JSON size: {json_size} bytes")

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        f.write(json_str)
    debug_log(f"✓ {OUTPUT_JSON} written to disk")

    debug_log("\n" + "=" * 60)
    debug_log("DONE!")
    debug_log("=" * 60)

if __name__ == "__main__":
    main()
