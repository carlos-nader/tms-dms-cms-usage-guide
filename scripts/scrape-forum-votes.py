#!/usr/bin/env python3
"""
Forum Engagement Scraper - Fixed Version
Scrapes Falcon BMS Forum RSS feed and updates README badge
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
    """Fetch and parse RSS feed"""
    try:
        print(f"🔄 Fetching RSS feed...")
        with urlopen(rss_url, timeout=10) as response:
            rss_content = response.read()
        
        root = ET.fromstring(rss_content)
        print(f"✓ RSS feed fetched successfully")
        return root
    except URLError as e:
        print(f"✗ Network error: {e}")
        return None
    except ET.ParseError as e:
        print(f"✗ XML parse error: {e}")
        return None
    except Exception as e:
        print(f"✗ Error fetching RSS: {e}")
        return None

def extract_votes_and_stats(rss_root):
    """Extract metrics from RSS feed"""
    try:
        print(f"📊 Parsing metrics...")
        
        stats = {
            'votes': 0,
            'views': 0,
            'posts': 0,
            'last_update': datetime.now().isoformat()
        }
        
        channel = rss_root.find('channel')
        if channel is None:
            print("⚠ No channel element found")
            return stats
        
        # Count posts
        items = channel.findall('item')
        stats['posts'] = len(items)
        print(f"  ✓ Found {stats['posts']} posts")
        
        if items:
            first_item = items[0]
            title = first_item.findtext('title', '')
            description = first_item.findtext('description', '')
            combined_text = title + ' ' + description
            
            # Extract votes - FIXED: Simple pattern, no numbered groups
            vote_match = re.search(r'(\d+)\s*votes?', combined_text, re.IGNORECASE)
            if vote_match:
                stats['votes'] = int(vote_match.group(1))
                print(f"  ✓ Found {stats['votes']} votes")
            
            # Extract views
            view_match = re.search(r'(\d+)\s*views?', combined_text, re.IGNORECASE)
            if view_match:
                stats['views'] = int(view_match.group(1))
                print(f"  ✓ Found {stats['views']} views")
        
        print(f"✓ Metrics extracted")
        return stats
        
    except Exception as e:
        print(f"✗ Error parsing: {e}")
        return None

def update_readme_badge(stats):
    """Update README with forum engagement badge - FIXED VERSION"""
    try:
        print(f"📝 Updating README badge...")
        
        readme_path = "README.md"
        if not Path(readme_path).exists():
            print(f"⚠ README.md not found")
            return None, False
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        votes = stats['votes']
        views = stats['views']
        
        # Build badge text
        if views > 0:
            badge_text = f"{votes} votes • {views} views"
        else:
            badge_text = f"{votes} votes"
        
        # Color based on votes
        color = "brightgreen" if votes >= 10 else "green" if votes >= 5 else "yellow"
        
        # FIXED: Safe regex without numbered groups like \10
        safe_badge_text = badge_text.replace(" ", "%20")
        new_badge = f'![Forum Votes](https://img.shields.io/badge/Forum%20Votes-{safe_badge_text}-{color})'
        
        # Pattern: Simple and safe - no problematic group references
        badge_pattern = r'!\[Forum[^\]]*\]\(https://img\.shields\.io/badge/Forum[^)]*\)'
        
        new_content = re.sub(badge_pattern, new_badge, content, flags=re.IGNORECASE)
        
        # If pattern not found, add badge at top
        if new_content == content:
            print("⚠ Badge pattern not found, adding new...")
            new_content = new_badge + '\n\n' + content
            print("✓ New badge added to README")
        else:
            print(f"✓ Badge updated: {badge_text}")
        
        # Write updated README
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return new_content, True
        
    except Exception as e:
        print(f"✗ Error updating README: {e}")
        import traceback
        traceback.print_exc()
        return None, False

def output_to_github_actions(stats):
    """Write metrics to GitHub Actions output"""
    github_output = os.getenv("GITHUB_OUTPUT")
    if not github_output:
        print("ℹ Not running in GitHub Actions")
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
        print(f"⚠ Could not write outputs: {e}")
        return False

def main():
    """Main execution"""
    print("=" * 60)
    print("📊 Forum Engagement Scraper v1.2 (FIXED)")
    print("=" * 60)

    # Get RSS URL
    rss_url = os.getenv("FORUM_RSS_URL")
    if not rss_url:
        print("✗ FORUM_RSS_URL environment variable not set")
        sys.exit(1)
    
    print(f"✓ RSS URL configured (token masked)")

    # Fetch RSS
    print(f"\n[1/4] Fetching forum data...")
    rss_root = fetch_rss_feed(rss_url)
    if rss_root is None:
        print("✗ Failed to fetch RSS")
        sys.exit(1)

    # Extract metrics
    print(f"\n[2/4] Extracting metrics...")
    stats = extract_votes_and_stats(rss_root)
    if stats is None:
        print("✗ Failed to extract metrics")
        sys.exit(1)

    # Update README
    print(f"\n[3/4] Updating README...")
    new_content, was_updated = update_readme_badge(stats)
    
    # Output to GitHub Actions
    print(f"\n[4/4] Setting GitHub Actions outputs...")
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
