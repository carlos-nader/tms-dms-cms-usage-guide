#!/usr/bin/env python3
"""Forum Topic Views Scraper - Extract from HTML page"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError

def fetch_topic_html(topic_url):
    """Fetch HTML page from forum topic"""
    try:
        print(f"🔄 Fetching topic page...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        req = Request(topic_url, headers=headers)
        with urlopen(req, timeout=15) as response:
            html_content = response.read().decode('utf-8', errors='ignore')
        
        print(f"✓ Topic page fetched successfully")
        return html_content
        
    except Exception as e:
        print(f"✗ Error fetching topic: {e}")
        return None

def extract_views_from_html(html_content):
    """Extract views and posts count from HTML"""
    try:
        print(f"📊 Parsing topic statistics...")
        
        stats = {
            'views': 0,
            'posts': 0,
            'last_update': datetime.now().isoformat()
        }
        
        # Pattern 1: "616 views" or "616 Views"
        views_match = re.search(r'(\d+)\s+views?', html_content, re.IGNORECASE)
        if views_match:
            stats['views'] = int(views_match.group(1))
            print(f"  ✓ Found {stats['views']} views")
        else:
            print(f"  ⚠ Views pattern not found")
        
        # Pattern 2: "14 posts" or "14 Posts"
        posts_match = re.search(r'(\d+)\s+posts?', html_content, re.IGNORECASE)
        if posts_match:
            stats['posts'] = int(posts_match.group(1))
            print(f"  ✓ Found {stats['posts']} posts")
        else:
            print(f"  ⚠ Posts pattern not found")
        
        print(f"✓ Statistics extracted")
        return stats
        
    except Exception as e:
        print(f"✗ Error parsing: {e}")
        return None

def update_readme_badge(stats):
    """Update README with badge"""
    try:
        print(f"📝 Updating README badge...")
        
        readme_path = "README.md"
        if not Path(readme_path).exists():
            print(f"⚠ README.md not found")
            return None, False
        
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        views = stats['views']
        posts = stats['posts']
        
        # Build badge text
        if views > 0:
            badge_text = f"{views} views"
        else:
            badge_text = "0 views"
        
        # Color based on views
        if views >= 500:
            color = "brightgreen"
        elif views >= 250:
            color = "green"
        elif views >= 100:
            color = "yellow"
        elif views >= 10:
            color = "orange"
        else:
            color = "lightgrey"
        
        # Safe badge URL encoding
        safe_badge_text = badge_text.replace(" ", "%20")
        new_badge = f'![Forum Views](https://img.shields.io/badge/Forum%20Views-{safe_badge_text}-{color})'
        
        # Pattern: Safe and simple (matches any Forum badge)
        badge_pattern = r'!\[Forum[^\]]*\]\(https://img\.shields\.io/badge/Forum[^)]*\)'
        
        new_content = re.sub(badge_pattern, new_badge, content, flags=re.IGNORECASE)
        
        # If not found, add at top
        if new_content == content:
            print("⚠ Badge pattern not found, adding new...")
            new_content = new_badge + '\n\n' + content
            print("✓ New badge added")
        else:
            print(f"✓ Badge updated: {badge_text}")
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return new_content, True
        
    except Exception as e:
        print(f"✗ Error updating README: {e}")
        return None, False

def output_to_github_actions(stats):
    """Write to GitHub Actions output"""
    github_output = os.getenv("GITHUB_OUTPUT")
    if not github_output:
        return False

    try:
        with open(github_output, 'a', encoding='utf-8') as f:
            f.write(f"views={stats['views']}\n")
            f.write(f"posts={stats['posts']}\n")
        return True
    except Exception as e:
        print(f"⚠ Could not write outputs: {e}")
        return False

def main():
    print("=" * 60)
    print("📊 Forum Topic Views Scraper v1.0")
    print("=" * 60)

    topic_url = os.getenv("FORUM_TOPIC_URL")
    if not topic_url:
        print("✗ FORUM_TOPIC_URL not set")
        sys.exit(1)
    
    print(f"✓ Topic URL configured")

    html_content = fetch_topic_html(topic_url)
    if html_content is None:
        print("✗ Failed to fetch topic page")
        sys.exit(1)

    stats = extract_views_from_html(html_content)
    if stats is None:
        print("✗ Failed to parse statistics")
        sys.exit(1)

    new_content, was_updated = update_readme_badge(stats)
    output_to_github_actions(stats)

    print("\n" + "=" * 60)
    print("✅ SUCCESS")
    print("=" * 60)
    print(f"👁️  Views: {stats['views']}")
    print(f"💬 Posts: {stats['posts']}")
    print(f"📅 Last Updated: {stats['last_update']}")
    print("=" * 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
