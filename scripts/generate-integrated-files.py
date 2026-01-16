#!/usr/bin/env python3
"""
Generate INTEGRATED-FILES Report
Tracks repository state: files, commits, tags, and issues
Outputs: INTEGRATED-FILES.md + INTEGRATED-FILES.json
"""

import os
import json
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import re

# Configuration
REPO_ROOT = Path.cwd()
TIMEZONE = "UTC-3"
OUTPUT_MD = "INTEGRATED-FILES.md"
OUTPUT_JSON = "INTEGRATED-FILES.json"

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
        print(f"Error running git command: {e}")
        return ""

def get_repo_info():
    """Get repository metadata"""
    repo_name = run_git_command("git config --get remote.origin.url").split("/")[-1].replace(".git", "")
    repo_url = run_git_command("git config --get remote.origin.url").replace(".git", "")
    created_date = run_git_command("git log --follow --format=%ai -- . | tail -1").split()[0] if run_git_command("git log --follow --format=%ai -- . | tail -1") else "Unknown"
    last_push = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + f" {TIMEZONE}"
    total_commits = run_git_command("git rev-list --count HEAD")
    releases = run_git_command("git tag -l 'v[0-9]*.[0-9]*.[0-9]*.[0-9]*' --sort=-version:refname | head -5")
    
    # Get languages (simple heuristic)
    tex_files = list(REPO_ROOT.glob("**/*.tex"))
    md_files = list(REPO_ROOT.glob("**/*.md"))
    tex_count = len(tex_files)
    md_count = len(md_files)
    total_files = tex_count + md_count
    tex_pct = int((tex_count / total_files * 100)) if total_files > 0 else 0
    md_pct = int((md_count / total_files * 100)) if total_files > 0 else 0
    
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
        # Check if file is in index
        in_index = run_git_command(f"git ls-files '{file_path}'")
        if not in_index:
            return "untracked"
        
        # Check if modified
        diff = run_git_command(f"git diff --name-only '{file_path}'")
        if diff:
            return "modified"
        
        # Check if staged
        staged = run_git_command(f"git diff --cached --name-only '{file_path}'")
        if staged:
            return "staged"
        
        return "tracked"
    except:
        return "unknown"

def get_tracked_files():
    """Get all tracked files with status and metadata"""
    tracked_files = {}
    section_num = 1
    
    for base_path, config in TRACKED_PATHS.items():
        if config["subfolders"]:
            # Multi-folder tracking (wip, archive)
            for subfolder in config["subfolders"]:
                folder_path = REPO_ROOT / subfolder
                if folder_path.exists() and folder_path.is_dir():
                    files_list = []
                    try:
                        for file in folder_path.rglob(f"*{config['ext']}"):
                            if file.is_file():
                                file_rel = file.relative_to(REPO_ROOT)
                                stat = file.stat()
                                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                                size = stat.st_size
                                status = get_file_status(str(file_rel))
                                
                                files_list.append({
                                    "path": str(file_rel),
                                    "status": status,
                                    "last_modified": mod_time,
                                    "size": f"{size} bytes"
                                })
                    except Exception as e:
                        print(f"Warning: Error scanning {subfolder}: {e}")
                    
                    if files_list:
                        section_key = f"{section_num}. {subfolder}"
                        tracked_files[section_key] = files_list
                        section_num += 1
        else:
            # Single file (guide.tex)
            file_path = REPO_ROOT / base_path
            if file_path.exists():
                stat = file_path.stat()
                mod_time = datetime.fromtimestamp(stat.st_mtime).strftime("%Y-%m-%d %H:%M:%S")
                size = stat.st_size
                status = get_file_status(base_path)
                
                section_key = f"{section_num}. {base_path} (Repository Root)"
                tracked_files[section_key] = [{
                    "path": base_path,
                    "status": status,
                    "last_modified": mod_time,
                    "size": f"{size} bytes"
                }]
                section_num += 1
    
    return tracked_files

def get_recent_commits(limit=10):
    """Get recent commits that modified tracked files"""
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
                
                # Get modified files
                modified = run_git_command(f"git diff-tree --no-commit-id --name-only -r {commit_hash}")
                
                commits.append({
                    "hash": commit_hash[:7],
                    "date": timestamp.split()[0],
                    "time": timestamp.split()[1],
                    "author": author,
                    "modified_files": [f for f in modified.split("\n") if f][:5]
                })
    
    return commits

def get_version_tags():
    """Get version tags matching vX.X.X.X pattern"""
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
    
    return tags[:10]

def get_github_issues():
    """Get GitHub issues using REST API"""
    token = os.environ.get("GITHUB_TOKEN", "")
    repo = os.environ.get("GITHUB_REPOSITORY", "")
    
    if not token or not repo:
        return {"open": [], "closed": []}
    
    import urllib.request
    import json as json_lib
    
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    try:
        # Open issues
        open_url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=10"
        req = urllib.request.Request(open_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            open_issues = json_lib.loads(response.read().decode())
        
        # Recently closed issues (last 30 days)
        thirty_days_ago = (datetime.now() - timedelta(days=30)).isoformat()
        closed_url = f"https://api.github.com/repos/{repo}/issues?state=closed&since={thirty_days_ago}&per_page=10&sort=updated&direction=desc"
        req = urllib.request.Request(closed_url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            closed_issues = json_lib.loads(response.read().decode())
        
        return {"open": open_issues, "closed": closed_issues}
    except Exception as e:
        print(f"Warning: Could not fetch issues: {e}")
        return {"open": [], "closed": []}

def generate_markdown():
    """Generate INTEGRATED-FILES.md"""
    repo_info = get_repo_info()
    tracked_files = get_tracked_files()
    commits = get_recent_commits(10)
    tags = get_version_tags()
    issues = get_github_issues()
    
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
    idx = 1
    for section_name, files in tracked_files.items():
        md += f"### {section_name}\n\n"
        md += "| File Path | Status | Last Modified | Size |\n"
        md += "|-----------|--------|---------------|------|\n"
        for f in files:
            md += f"| {f['path']} | {f['status']} | {f['last_modified']} | {f['size']} |\n"
        md += "\n"
    
    md += "---\n\n## 3. COMMITS\n\n"
    md += "Commits that modified tracked files (last 10 commits):\n\n"
    md += "| Date/Time | Author | Modified Tracked Files |\n"
    md += "|-----------|--------|------------------------|\n"
    for commit in commits:
        modified_str = ", ".join(commit['modified_files'][:3]) if commit['modified_files'] else "-"
        md += f"| {commit['date']} {commit['time']} | {commit['author']} | {modified_str} |\n"
    
    md += "\n---\n\n## 4. VERSION TAGS\n\n"
    md += "Tags matching pattern: `^v[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$`\n\n"
    md += "| Tag | Commit | Date | Message |\n"
    md += "|-----|--------|------|----------|\n"
    for tag in tags:
        md += f"| {tag['tag']} | {tag['commit']} | {tag['date']} | {tag['message']} |\n"
    
    md += "\n---\n\n## 5. GITHUB ISSUES\n\n"
    md += "### 5.1 Open Issues\n\n"
    md += "| # | Title | Created | Labels |\n"
    md += "|---|-------|---------|--------|\n"
    for issue in issues.get("open", [])[:10]:
        labels = ", ".join([l["name"] for l in issue.get("labels", [])]) or "-"
        md += f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {labels} |\n"
    
    md += "\n### 5.2 Recently Closed Issues (Last 30 days)\n\n"
    md += "| # | Title | Created | Closed | Labels |\n"
    md += "|---|-------|---------|--------|--------|\n"
    for issue in issues.get("closed", [])[:10]:
        labels = ", ".join([l["name"] for l in issue.get("labels", [])]) or "-"
        closed_date = issue.get('closed_at', 'Unknown')[:10] if issue.get('closed_at') else 'Unknown'
        md += f"| #{issue['number']} | {issue['title'][:50]} | {issue['created_at'][:10]} | {closed_date} | {labels} |\n"
    
    md += "\n---\n\n**End of Report**\n"
    
    return md

def generate_json_data():
    """Generate JSON structured data"""
    repo_info = get_repo_info()
    tracked_files = get_tracked_files()
    commits = get_recent_commits(10)
    tags = get_version_tags()
    issues = get_github_issues()
    
    return {
        "generated": datetime.now().isoformat(),
        "repository": repo_info,
        "tracked_files": tracked_files,
        "commits": commits,
        "tags": tags,
        "issues": {
            "open": len(issues.get("open", [])),
            "closed": len(issues.get("closed", []))
        }
    }

def main():
    """Main execution"""
    print("Generating INTEGRATED-FILES report...")
    
    # Generate Markdown
    md_content = generate_markdown()
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"✓ {OUTPUT_MD} generated")
    
    # Generate JSON
    json_data = generate_json_data()
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=2, ensure_ascii=False)
    print(f"✓ {OUTPUT_JSON} generated")
    
    print("Done!")

if __name__ == "__main__":
    main()
