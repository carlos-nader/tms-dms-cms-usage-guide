import os
import re
from datetime import datetime

WIP_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'wip')
README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')

DELIM_START = '<!-- WIP-SNAPSHOT-START -->'
DELIM_END = '<!-- WIP-SNAPSHOT-END -->'

STATUS_EMOJI = {
    'dev': '🟠',
    'review': '🟡',
    'final': '⚪'
}


def get_wip_files():
    files = []
    for fname in os.listdir(WIP_DIR):
        fpath = os.path.join(WIP_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith('.tex'):
            files.append(fname)
    return files


def parse_status(fname):
    match = re.search(r'-(dev|review|final)-', fname)
    if match:
        return match.group(1)
    return ''


def get_last_modified(fname):
    fpath = os.path.join(WIP_DIR, fname)
    mod_time = os.path.getmtime(fpath)
    return datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')


def generate_table():
    files = get_wip_files()
    rows = []
    for fname in sorted(files):
        status = parse_status(fname)
        emoji = STATUS_EMOJI.get(status, '')
        last_mod = get_last_modified(fname)
        rows.append(f'| {emoji} {status} | {fname} | {last_mod} |')
    if not rows:
        rows.append('|        |           |              |')
    table = '\n'.join([
        '| Status | File Name | Last Modified |',
        '|:------:|-----------|:-------------|',
        *rows
    ])
    return table


def update_readme():
    with open(README_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    start = content.find(DELIM_START)
    end = content.find(DELIM_END)
    if start == -1 or end == -1:
        print('Delimiters not found in README.md')
        return
    before = content[:start + len(DELIM_START)]
    after = content[end:]
    table = (
        '\n## 🗄️ WIP Snapshot — Active Work-in-Progress Files\n\n'
        + generate_table()
        + '\n\n**Legend:**  ⚪ dev\t🟡 review\t⚪ final\n\n'
        + '> For integrated files, see the `archive/WIP/` folder.'
    )
    new_content = before + '\n' + table + '\n' + after
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('README.md updated with WIP snapshot.')


if __name__ == '__main__':
    update_readme()
