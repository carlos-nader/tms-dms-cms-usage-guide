#!/usr/bin/env python3
"""
Scrape Falcon BMS Forum RSS feed to extract forum engagement metrics.
Updates README badge with current vote count and engagement stats.

Usage:
    python scrape-forum-votes.py

Environment Variables:
- FORUM_RSS_URL: Full RSS feed URL (with token) from forum
- GITHUB_OUTPUT: Path to GitHub Actions output file (auto-set by Actions)

Returns:
- Exit code 0: Success
- Exit code 1: Error (network issue, parsing error, etc.)
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

def fetch_rss_feed(rss_url):
    """
    Fetch and parse RSS feed from Falcon BMS forum.

    Args:
        rss_url (str): Full RSS URL with authentication token

    Returns:
        ET.Element: Root XML element
        None: If fetch or parse fails
    """
    try:
        print(f"🔄 Fetching RSS feed...")
        with urlopen(rss_url, timeout=10) as response:
            rss_content = response.read()
        
        root = ET.fromstring(rss_content)
        print(f"✓ RSS feed fetched and parsed successfully")
        return root
    except URLError as e:
        print(f"✗ Network error fetching RSS: {e}")
        return None
    except ET.ParseError as e:
        print(f"✗ XML parse error: {e}")
        return None
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None

def extract_votes_and_stats(rss_root):
    """
    Extract vote count, views, and posts from RSS feed.
    
    Falcon BMS forum RSS structure includes:
    - title: Contains vote count info (e.g., "Topic Title [5 votes]" or similar)
    - description: Post content
    - Comments/custom fields may contain engagement stats

    Args:
        rss_root (ET.Element): Parsed RSS root element

    Returns:
        dict: {
            'votes': int,
            'views': int,
            'posts': int,
            'last_update': str (ISO format)
        }
        None: If parsing fails
    """
    try:
        print(f"📊 Parsing forum engagement metrics...")
        
        # Initialize defaults
        stats = {
            'votes': 0,
            'views': 0,
            'posts': 0,
            'last_update': datetime.now().isoformat()
        }
        
        # Find channel/item elements (standard RSS)
        channel = rss_root.find('channel')
        if channel is None:
            print("⚠ No channel element found in RSS")
            return stats
        
        # Count items (posts)
        items = channel.findall('item')
        stats['posts'] = len(items)
        print(f"  ✓ Found {stats['posts']} posts")
        
        # Extract votes from first item title or description
        # Different forums have different formats
        if items:
            first_item = items[0]
            
            # Try to extract from title
            title = first_item.findtext('title', '')
            description = first_item.findtext('description', '')
            
            # Pattern 1: Look for vote count in title/description
            # Formats: "5 votes", "[5]", "Votes: 5", etc.
            vote_patterns = [
                r'(\d+)\s*votes?',
                r'\[\s*(\d+)\s*votes?\s*\]',
                r'votes?:?\s*(\d+)',
            ]
            
            combined_text = title + ' ' + description
            
            for pattern in vote_patterns:
                match = re.search(pattern, combined_text, re.IGNORECASE)
                if match:
                    stats['votes'] = int(match.group(1))
                    print(f"  ✓ Found {stats['votes']} votes")
                    break
            
            # Try to extract views (often in descriptions)
            view_patterns = [
                r'(\d+)\s*views?',
                r'viewed?\s*(\d+)\s*times?',
            ]
            
            for pattern in view_patterns:
                match = re.search(pattern, combined_text, re.IGNORECASE)
                if match:
                    stats['views'] = int(match.group(1))
                    print(f"  ✓ Found {stats['views']} views")
                    break
        
        stats['last_update'] = datetime.now().isoformat()
        print(f"✓ Metrics extracted successfully")
        return stats
        
    except Exception as e:
        print(f"✗ Error parsing metrics: {e}")
        return None

def update_readme_badge(stats):
    """
    Update README.md with new forum engagement badge.
    
    Replaces badge pattern:
    [![Forum Votes](https://img.shields.io/badge/Forum%20Votes-X-brightgreen)](...)
    
    Args:
        stats (dict): Forum engagement statistics
        
    Returns:
        tuple: (updated_content, was_updated)
    """
    try:
        print(f"📝 Updating README badge...")
        
        readme_path = "README.md"
        if not Path(readme_path).exists():
            print(f"⚠ README.md not found, skipping badge update")
            return None, False
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Build new badge text
        votes = stats['votes']
        views = stats['views']
        
        # Badge with votes and views
        if views > 0:
            badge_text = f"{votes} votes • {views} views"
            color = "brightgreen" if votes >= 10 else "green" if votes >= 5 else "yellow"
        else:
            badge_text = f"{votes} votes"
            color = "brightgreen" if votes >= 10 else "green" if votes >= 5 else "yellow"
        
        # Replace badge pattern
        # Pattern: [![Forum Votes](...badge/Forum%20Votes-X-COLOR...](...)]
        badge_pattern = r'(!\[Forum.*?\]\(https://img\.shields\.io/badge/Forum%20(?:Votes|Engagement)-)[^-]+-[^)]+(\)\(.*?\))'
        badge_replacement = rf'\1{badge_text.replace(" ", "%20")}-{color}\2'
        
        new_content = re.sub(badge_pattern, badge_replacement, content)
        
        # If pattern not found, try to add it
        if new_content == content:
            print("⚠ Badge pattern not found in README, adding new one...")
            # Add badge after title or at beginning
            add_badge = f'[![Forum Votes](https://img.shields.io/badge/Forum%20Votes-{badge_text.replace(" ", "%20")}-{color})](https://forum.falcon-bms.com/topic/32541)\n\n'
            new_content = add_badge + content
            print("✓ New badge added to README")
        else:
            print(f"✓ Badge updated: {badge_text}")
        
        # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return new_content, True
        
    except Exception as e:
        print(f"✗ Error updating README: {e}")
        return None, False

def output_to_github_actions(stats):
    """
    Write metrics to GitHub Actions output for use in subsequent steps.

    Args:
        stats (dict): Forum engagement statistics
        
    Returns:
        bool: True if successful
    """
    github_output = os.getenv("GITHUB_OUTPUT")
    if not github_output:
        print("ℹ Not running in GitHub Actions (GITHUB_OUTPUT not set)")
        return False

    try:
        with open(github_output, 'a', encoding='utf-8') as f:
            f.write(f"votes={stats['votes']}\n")
            f.write(f"views={stats['views']}\n")
            f.write(f"posts={stats['posts']}\n")
            f.write(f"timestamp={stats['last_update']}\n")
        print(f"✓ GitHub Actions outputs set")
        return True
    except Exception as e:
        print(f"⚠ Could not write GitHub Actions output: {e}")
        return False

def main():
    """Main execution logic."""
    print("=" * 60)
    print("📊 Forum Engagement Scraper v1.0")
    print("=" * 60)

    # Step 1: Get RSS URL from environment
    print("\n[1/4] Reading configuration...")
    rss_url = os.getenv("FORUM_RSS_URL")
    if not rss_url:
        print("✗ FAILED: FORUM_RSS_URL environment variable not set")
        print("   Set it in GitHub Secrets or pass via workflow")
        sys.exit(1)
    
    print(f"✓ RSS URL configured (token masked)")

    # Step 2: Fetch and parse RSS
    print("\n[2/4] Fetching forum data...")
    rss_root = fetch_rss_feed(rss_url)
    if rss_root is None:
        print("✗ FAILED: Could not fetch RSS feed")
        sys.exit(1)

    # Step 3: Extract metrics
    print("\n[3/4] Extracting metrics...")
    stats = extract_votes_and_stats(rss_root)
    if stats is None:
        print("✗ FAILED: Could not extract metrics")
        sys.exit(1)

    # Step 4: Update README
    print("\n[4/4] Updating README...")
    new_content, was_updated = update_readme_badge(stats)
    if not was_updated and new_content is None:
        print("⚠ WARNING: Could not update README")
    
    # Bonus: Output to GitHub Actions
    print("\n[BONUS] Setting GitHub Actions output variables...")
    output_to_github_actions(stats)

    # Success summary
    print("\n" + "=" * 60)
    print("✅ SUCCESS")
    print("=" * 60)
    print(f"🗳️  Votes: {stats['votes']}")
    print(f"👁️  Views: {stats['views']}")
    print(f"💬 Posts: {stats['posts']}")
    print(f"📅 Last Updated: {stats['last_update']}")
    print("=" * 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
