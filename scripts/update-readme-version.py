#!/usr/bin/env python3
"""
Update README with guide version from Git tags or manual input.

Supports both:
  - Automatic: Triggered by tag push (extracts version from latest tag)
  - Manual: Triggered via workflow_dispatch (uses OVERRIDE_VERSION env var)

Usage:
  python update-readme-version.py

Environment Variables:
  - OVERRIDE_VERSION: Manual version input (takes precedence over git tag)
  - GITHUB_OUTPUT: Path to GitHub Actions output file (auto-set by Actions)

Returns:
  - Exit code 0: Success
  - Exit code 1: Error (missing version, file not found, etc.)
"""

import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def get_version_from_git():
    """
    Extract version from latest Git tag.
    
    Expected format: v0.3.2.0 -> returns 0.3.2.0
    
    Returns:
        str: Version string (e.g., "0.3.2.0")
        None: If no tags found or git command fails
    """
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            check=True
        )
        tag = result.stdout.strip()
        # Remove leading 'v' if present
        version = tag.lstrip('v')
        print(f"✓ Extracted version from git tag: {version}")
        return version
    except subprocess.CalledProcessError:
        print("⚠ No git tags found in repository")
        return None
    except FileNotFoundError:
        print("⚠ Git command not found (make sure Git is installed)")
        return None


def get_version_from_env():
    """
    Get version from OVERRIDE_VERSION environment variable.
    
    Set by workflow_dispatch (manual trigger).
    
    Returns:
        str: Version string (e.g., "0.3.2.0")
        None: If not set
    """
    version = os.getenv("OVERRIDE_VERSION")
    if version:
        print(f"✓ Using manual version from environment: {version}")
    return version


def validate_version(version):
    """
    Validate version format (e.g., 0.3.2.0).
    
    Args:
        version (str): Version string to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not version:
        return False
    
    # Accept formats: 0.3.2.0 or 0.3.2
    pattern = r'^[0-9]+\.[0-9]+\.[0-9]+(\.[0-9]+)?$'
    if re.match(pattern, version):
        return True
    
    print(f"✗ Invalid version format: {version}")
    print("  Expected format: X.Y.Z or X.Y.Z.W (e.g., 0.3.2.0)")
    return False


def read_readme(filepath):
    """
    Read README file.
    
    Args:
        filepath (str): Path to README file
        
    Returns:
        str: File contents
        None: If file not found
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"✗ README file not found: {filepath}")
        return None
    except Exception as e:
        print(f"✗ Error reading README: {e}")
        return None


def update_readme_content(content, new_version):
    """
    Update version in README content.
    
    Replaces patterns like:
      **Status:** Pre-publication v0.3.1.0 (Preamble Infrastructure Upgrade)
      with:
      **Status:** Pre-publication v{new_version} (...)
    
    Also updates:
      **Last Updated:** YYYY-MM-DD
    
    Args:
        content (str): Original README content
        new_version (str): New version to insert
        
    Returns:
        tuple: (updated_content, num_replacements)
    """
    updated = content
    replacements = 0
    
    # Pattern 1: Update version in "Pre-publication v..." line
    # Matches: **Status:** Pre-publication v0.3.1.0 (optional description)
    version_pattern = r'(Pre-publication\s+v)[\d.]+'
    replacement = rf'\g<1>{new_version}'
    new_content, count = re.subn(version_pattern, replacement, updated)
    
    if count > 0:
        print(f"✓ Updated Guide Version references: {count} occurrence(s)")
        replacements += count
        updated = new_content
    else:
        print("⚠ No 'Pre-publication v...' pattern found in README")
    
    # Pattern 2: Update "Last Updated" timestamp (simple date format)
    now = datetime.now()
    # Format: 2026-01-19 (simple date)
    timestamp = now.strftime("%Y-%m-%d")
    
    # Match: **Last Updated:** YYYY-MM-DD
    timestamp_pattern = r'(\*\*Last Updated:\*\*\s+)\d{4}-\d{2}-\d{2}'
    timestamp_replacement = rf'\g<1>{timestamp}'
    new_content, count = re.subn(timestamp_pattern, timestamp_replacement, updated)
    
    if count > 0:
        print(f"✓ Updated timestamp: {timestamp}")
        replacements += count
        updated = new_content
    else:
        print("⚠ No 'Last Updated' line found in README (timestamp not updated)")
    
    return updated, replacements


def write_readme(filepath, content):
    """
    Write updated content back to README.
    
    Args:
        filepath (str): Path to README file
        content (str): Updated content
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ README file saved: {filepath}")
        return True
    except Exception as e:
        print(f"✗ Error writing README: {e}")
        return False


def output_to_github_actions(version, source):
    """
    Write output variables for GitHub Actions.
    
    Sets variables in GITHUB_OUTPUT for use in subsequent steps.
    
    Args:
        version (str): Version that was updated
        source (str): Source of version ("tag" or "manual")
        
    Returns:
        bool: True if successful, False if not in GitHub Actions
    """
    github_output = os.getenv("GITHUB_OUTPUT")
    
    if not github_output:
        print("ℹ Not running in GitHub Actions (GITHUB_OUTPUT not set)")
        return False
    
    try:
        with open(github_output, 'a', encoding='utf-8') as f:
            f.write(f"version={version}\n")
            f.write(f"source={source}\n")
            f.write(f"timestamp={datetime.now().isoformat()}\n")
        print(f"✓ GitHub Actions output variables set")
        return True
    except Exception as e:
        print(f"⚠ Could not write GitHub Actions output: {e}")
        return False


def main():
    """Main execution logic."""
    
    print("=" * 60)
    print("📝 README Version Updater v2.0")
    print("=" * 60)
    
    # Step 1: Determine version source
    print("\n[1/5] Determining version source...")
    
    version = get_version_from_env()  # Manual input (takes precedence)
    source = "manual"
    
    if not version:
        version = get_version_from_git()  # Automatic from tag
        source = "tag"
    
    if not version:
        print("\n✗ FAILED: No version found (neither git tag nor OVERRIDE_VERSION)")
        sys.exit(1)
    
    print(f"ℹ Version source: {source.upper()}")
    
    # Step 2: Validate version
    print("\n[2/5] Validating version format...")
    
    if not validate_version(version):
        print("✗ FAILED: Invalid version format")
        sys.exit(1)
    
    print(f"✓ Version is valid: {version}")
    
    # Step 3: Read README
    print("\n[3/5] Reading README file...")
    
    readme_path = "README.md"
    if not Path(readme_path).exists():
        # Fallback to docs/ if exists
        readme_path = "docs/PROJECT-TRACKING-v5.0.0.md"
    
    content = read_readme(readme_path)
    if content is None:
        print("✗ FAILED: Could not read README")
        sys.exit(1)
    
    print(f"✓ README loaded ({len(content)} bytes)")
    
    # Step 4: Update README content
    print("\n[4/5] Updating version in README...")
    
    updated_content, num_changes = update_readme_content(content, version)
    
    if num_changes == 0:
        print("⚠ WARNING: No version updates were made")
        print("  Check that README contains proper version markers")
    else:
        print(f"✓ Made {num_changes} update(s)")
    
    # Step 5: Write updated README
    print("\n[5/5] Saving updated README...")
    
    if not write_readme(readme_path, updated_content):
        print("✗ FAILED: Could not write README")
        sys.exit(1)
    
    # Bonus: Output to GitHub Actions
    print("\n[BONUS] Setting GitHub Actions output variables...")
    output_to_github_actions(version, source)
    
    # Success summary
    print("\n" + "=" * 60)
    print("✅ SUCCESS")
    print("=" * 60)
    print(f"📝 Updated: {readme_path}")
    print(f"🔢 Version: {version}")
    print(f"📌 Source: {source.upper()}")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S -03')}")
    print("=" * 60)
    
    sys.exit(0)


if __name__ == "__main__":
    main()
