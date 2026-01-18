#!/usr/bin/env python3

"""
Update README.md with version from Git tag

Triggered on new tag push (e.g., v0.3.1.0)
Extracts version from tag and updates:
  1. Guide Version in Current Project State table
  2. Last Updated date in footer
  3. Status in footer
"""

import os
import re
import subprocess
import sys
from datetime import datetime

def debug_log(msg):
    """Print debug message"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] {msg}", flush=True)

def get_latest_tag():
    """Get latest tag from Git"""
    try:
        tag = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()
        debug_log(f"Latest tag detected: {tag}")
        return tag
    except subprocess.CalledProcessError as e:
        debug_log(f"ERROR: Could not get git tag: {e}")
        sys.exit(1)

def extract_version(tag):
    """Extract version from tag (v0.3.1.0 → 0.3.1.0)"""
    version = tag.lstrip('v')
    debug_log(f"Extracted version: {version}")
    return version

def get_today_date():
    """Get today's date in YYYY-MM-DD format"""
    today = datetime.now().strftime("%Y-%m-%d")
    debug_log(f"Today's date: {today}")
    return today

def update_readme(version, today):
    """Update README.md with new version and date"""
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        debug_log(f"ERROR: {readme_path} not found")
        sys.exit(1)
    
    debug_log(f"Reading {readme_path}...")
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    
    # Update 1: Guide Version in table
    # Pattern: | **Guide Version** | v0.3.1.0 |
    debug_log("Updating Guide Version in table...")
    content = re.sub(
        r"(\| \*\*Guide Version\*\* \| )v[\d.]+",
        rf"\1v{version}",
        content
    )
    
    # Update 2: Last Updated date in footer
    # Pattern: **Last Updated:** 2026-01-18
    debug_log("Updating Last Updated date...")
    content = re.sub(
        r"(\*\*Last Updated:\*\* )\d{4}-\d{2}-\d{2}",
        rf"\1{today}",
        content
    )
    
    # Update 3: Status in footer
    # Pattern: **Status:** Pre-publication v0.3.1.0 ...
    debug_log("Updating Status version...")
    content = re.sub(
        r"(\*\*Status:\*\* Pre-publication )v[\d.]+",
        rf"\1v{version}",
        content
    )
    
    # Check if any changes were made
    if content == original_content:
        debug_log("WARNING: No changes made to README.md")
        return False
    
    debug_log(f"Writing updated {readme_path}...")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    debug_log("✓ README.md updated successfully")
    return True

def main():
    """Main execution"""
    debug_log("=" * 60)
    debug_log("STARTING README UPDATE FROM TAG")
    debug_log("=" * 60)
    
    # Get latest tag
    tag = get_latest_tag()
    
    # Extract version
    version = extract_version(tag)
    
    # Get today's date
    today = get_today_date()
    
    # Update README
    updated = update_readme(version, today)
    
    if updated:
        debug_log(f"✓ Updated README with version v{version} (date: {today})")
    else:
        debug_log("No updates needed or pattern not found")
    
    debug_log("=" * 60)
    debug_log("DONE!")
    debug_log("=" * 60)

if __name__ == "__main__":
    main()
