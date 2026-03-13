#!/usr/bin/env python3
"""Forum Topic Views Scraper - DEBUG VERSION"""

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
        
        print(f"✓ Topic page fetched successfully ({len(html_content)} bytes)")
        return html_content
        
    except Exception as e:
        print(f"✗ Error fetching topic: {e}")
        return None

def _find_views_count(html_content):
    """Try primary then fallback patterns to extract view count."""
    match = re.search(r'(\d+)\s+views?', html_content, re.IGNORECASE)
    if match:
        print(f"  ✓ Found {match.group(1)} views")
        return int(match.group(1))

    print(f"  ⚠ Pattern '\\d+ views' not found")
    alt_patterns = [
        (r'<span class="fw-bold" title="(\d+)">', "Span.fw-bold with title"),
        (r'class="fw-bold" title="(\d+)"', "fw-bold title attribute"),
        (r'\|\s*(\d+)\s+views?', "| views (pipe separator)"),
        (r'views["\']?\s*:\s*(\d+)', "JSON: views: N"),
    ]
    for pattern, desc in alt_patterns:
        alt_match = re.search(pattern, html_content, re.IGNORECASE)
        if alt_match:
            print(f"  ✓ Found via alt pattern '{desc}': {alt_match.group(1)}")
            return int(alt_match.group(1))

    print(f"  ℹ  All alternative patterns failed")
    return 0


def _find_posts_count(html_content):
    """Extract posts count from HTML."""
    match = re.search(r'(\d+)\s+posts?', html_content, re.IGNORECASE)
    if match:
        print(f"  ✓ Found {match.group(1)} posts")
        return int(match.group(1))
    print(f"  ⚠ Posts pattern not found")
    return 0


def extract_views_from_html(html_content):
    """Extract views and posts count from HTML - with DEBUG"""
    try:
        print(f"📊 Parsing topic statistics...")

        print("\n🔍 DEBUG: Searching for 'views' patterns...")
        views_positions = [m.start() for m in re.finditer(r'views?', html_content, re.IGNORECASE)]
        print(f"   Found 'views' keyword at {len(views_positions)} positions")
        if views_positions:
            pos = views_positions[0]
            context = html_content[max(0, pos - 100):min(len(html_content), pos + 100)]
            print(f"   Context around first occurrence:\n      ...{context}...")

        stats = {
            'views': _find_views_count(html_content),
            'posts': _find_posts_count(html_content),
            'last_update': datetime.now().isoformat(),
        }

        print(f"✓ Statistics extracted")
        return stats

    except Exception as e:
        print(f"✗ Error parsing: {e}")
        return None

def _badge_text(views):
    return f"{views} views" if views > 0 else "0 views (check HTML)"


def _badge_color(views):
    if views >= 500:
        return "brightgreen"
    if views >= 250:
        return "green"
    if views >= 100:
        return "yellow"
    if views >= 10:
        return "orange"
    return "lightgrey"


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
        badge_text = _badge_text(views)
        color = _badge_color(views)

        # Safe badge URL encoding
        safe_badge_text = badge_text.replace(" ", "%20")
        new_badge = f'![Forum Views](https://img.shields.io/badge/Forum%20Views-{safe_badge_text}-{color})'

        # Update ONLY the linked Forum Views badge: [![Forum Views](...)](some URL)
        # This avoids touching any other badges and prevents accidental duplication.
        linked_badge_pattern = re.compile(
            r'\[\s*!\[Forum\s*Views\]\(https://img\.shields\.io/badge/Forum%20Views-[^)]*\)\s*\]\((?P<link>[^)]+)\)',
            flags=re.IGNORECASE,
        )

        def _replace_linked(match: re.Match) -> str:
            forum_link = match.group('link')
            return f'[{new_badge}]({forum_link})'

        new_content, subs = linked_badge_pattern.subn(_replace_linked, content)

        if subs == 0:
            print("✗ Linked Forum Views badge not found in README; not modifying file.")
            return None, False

        if subs > 1:
            print(f"⚠ Updated {subs} linked Forum Views badges (expected 1).")
        else:
            print(f"✓ Badge updated: {badge_text}")

        if new_content != content:
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

        return new_content, True
        
    except Exception as e:
        print(f"✗ Error updating README: {e}")
        return None, False

def main():
    print("=" * 60)
    print("📊 Forum Topic Views Scraper v1.0 (DEBUG MODE)")
    print("=" * 60)

    topic_url = os.getenv("FORUM_TOPIC_URL")
    if not topic_url:
        print("✗ FORUM_TOPIC_URL not set")
        sys.exit(1)
    
    print(f"✓ Topic URL configured: {topic_url[:60]}...")

    html_content = fetch_topic_html(topic_url)
    if html_content is None:
        print("✗ Failed to fetch topic page")
        sys.exit(1)

    stats = extract_views_from_html(html_content)
    if stats is None:
        print("✗ Failed to parse statistics")
        sys.exit(1)

    new_content, was_updated = update_readme_badge(stats)
    if not was_updated:
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ RESULT")
    print("=" * 60)
    print(f"👁️  Views: {stats['views']}")
    print(f"💬 Posts: {stats['posts']}")
    print(f"📅 Last Updated: {stats['last_update']}")
    print("=" * 60)

    sys.exit(0)

if __name__ == "__main__":
    main()
