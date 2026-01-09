# Converter Setup Guide — v3.1.0 with Lua Filters & Variables

**Purpose:** Instructions for installing and using the enhanced MD to DOCX converter with Lua filter support and template variable substitution.

---

## 1. Installation

### 1.1 Files Required

Place these files **in the project root** (same folder as `guide.tex` and `docs/`):

```
project-root/
├── md-to-docx-v3-1-0.bat          ← Main converter script (NEW v3.1.0)
├── docx-enhancements.lua          ← Lua filter for formatting (NEW)
├── template-variables.lua         ← Template variable substitution (NEW)
├── guide.tex
├── docs/
│   ├── BRIEFING-v0-1-4-1.md
│   ├── version-system-v4-2.md
│   ├── WIP-FILE-NAMING-v1-3.md
│   ├── PROJECT-TRACKING-v4-1-2.md
│   └── template.docx              (optional, for custom styling)
└── ...
```

### 1.2 Prerequisites

- **Pandoc 3.0+** installed ([pandoc.org/installing.html](https://pandoc.org/installing.html))
- **Windows Batch Support** (BAT execution enabled)
- **Lua support in Pandoc** (included in Pandoc 3.0+)

---

## 2. Quick Start

### 2.1 For Single Governance File

```bash
# Double-click md-to-docx-v3-1-0.bat
# Choose Option 1: Convert single file
# Paste path to your .md file
# Choose advanced options if desired
# Done!
```

### 2.2 For All Docs/ Files (Recommended)

```bash
# Double-click md-to-docx-v3-1-0.bat
# Choose Option 2: Convert docs/ folder
# Converter auto-detects all .md files in docs/
# Confirms before batch conversion
# Done! All .md → .docx
```

### 2.3 Drag and Drop (Fastest)

```bash
# Drag any .md file directly onto md-to-docx-v3-1-0.bat
# Converter processes it immediately
# Auto-detects template if available
# Opens result in Word (optional)
```

---

## 3. Template Variables

You can now use **template variables** in your Markdown files:

### 3.1 Supported Variables

| Variable | Example | Auto-Detected |
|----------|---------|----------------|
| `${VERSION}` | `0.2.2.0` | From `version-system-v4-2.md` or env |
| `${DATE}` | `2026-01-09` | System date (YYYY-MM-DD) |
| `${DATETIME}` | `2026-01-09 11:35:47` | System date/time |
| `${PROJECT}` | `Falcon BMS TMS/DMS/CMS Guide` | Default or env |
| `${PHASE}` | `Pre-Publication (0.x.x.x)` | From `PROJECT-TRACKING` or env |
| `${AUTHOR}` | `Carlos Nader` | From environment or default |
| `${LOCALE}` | `en_US` | System locale |
| `${TIME}` | `11:35:47` | System time |
| `${YEAR}` | `2026` | System year |
| `${MONTH}` | `January` | System month (full name) |
| `${DAY}` | `09` | System day |
| `${WEEKDAY}` | `Friday` | System weekday (full name) |

### 3.2 Usage Examples

In your Markdown files:

```markdown
# GitHub Desktop Guide — Falcon BMS Guide

**Version:** ${VERSION}  
**Date:** ${DATE}  
**Project:** ${PROJECT}  
**Phase:** ${PHASE}  
**Author:** ${AUTHOR}

---

Last updated: ${DATETIME}
```

Result in DOCX:

```
# GitHub Desktop Guide — Falcon BMS Guide

Version: 0.2.2.0
Date: 2026-01-09
Project: Falcon BMS TMS/DMS/CMS Guide
Phase: Pre-Publication (0.x.x.x)
Author: Carlos Nader

---

Last updated: 2026-01-09 11:35:47
```

### 3.3 Setting Custom Values

Set environment variables before running the converter:

```batch
REM Windows Command Prompt
set FALCON_VERSION=0.3.0.0
set FALCON_PHASE=Phase 1 - CMS
set FALCON_AUTHOR=Your Name

REM Then run the converter
md-to-docx-v3-1-0.bat
```

Or create a `SET-ENVIRONMENT.bat` file in project root:

```batch
@echo off
setlocal

set FALCON_VERSION=0.2.2.0
set FALCON_PHASE=Pre-Publication (0.x.x.x)
set FALCON_AUTHOR=Carlos Nader

REM Launch converter with these variables set
call md-to-docx-v3-1-0.bat

endlocal
```

---

## 4. Lua Filters

### 4.1 What They Do

**`docx-enhancements.lua`:**
- Improves table rendering (consistent widths, alignment)
- Preserves code block styling (monospace, language info)
- Handles links, citations, and footnotes
- Ensures emphasis (italic/bold) is preserved in DOCX
- Manages heading levels properly

**`template-variables.lua`:**
- Replaces `${VARIABLE}` placeholders with actual values
- Auto-reads version from `version-system-v4-2.md`
- Auto-reads phase from `PROJECT-TRACKING` files
- Supports environment variables as fallback

### 4.2 Customizing Filters

You can edit the `.lua` files to customize behavior:

**To add a new variable** in `template-variables.lua`:

```lua
local variables = {
    VERSION = os.getenv('FALCON_VERSION') or '0.2.2.0',
    DATE = os.date('%Y-%m-%d'),
    MYVAR = 'Your Custom Value',  -- Add here
}
```

Then use in Markdown: `${MYVAR}`

**To add table styling** in `docx-enhancements.lua`, modify the `Table` filter function.

### 4.3 Disabling Filters

If you don't want Lua filters applied:

1. **Rename or delete** `docx-enhancements.lua` and/or `template-variables.lua`
2. Converter will detect missing filters and show `[INFO]` message
3. Conversion continues without those filters

---

## 5. Workflow Integration

### 5.1 Standard Session (Governance)

```
1. Pull origin in GitHub Desktop
2. Edit .md files in docs/
3. Run: md-to-docx-v3-1-0.bat
4. Choose Option 2: Convert docs/ folder
5. Verify .docx files in docs/
6. Commit both .md and .docx
7. Push to GitHub
```

### 5.2 WIP Session

```
1. Pull origin
2. Edit WIP/*.md or WIP/*.tex
3. (Optional) Convert WIP .md → .docx
   - Use Option 3: Convert entire folder
   - Choose WIP/ folder
4. Commit WIP changes
5. Push to GitHub
```

### 5.3 Guide Integration Session

```
1. Pull origin
2. Integrate WIP content into guide.tex snapshot
3. (Optional) Convert snapshot to preview DOCX
4. Update guide.tex
5. Commit + Push
```

---

## 6. Menu Options Explained

### Main Menu (When Script Opens)

```
1. Convert single file
   → Choose one .md, specify output
   → Use when converting individual documents

2. Convert docs/ folder ⭐ RECOMMENDED FOR GOVERNANCE
   → Auto-detect all .md in docs/
   → One-click batch conversion
   → Perfect for governance document updates

3. Convert entire folder
   → Choose any folder with .md files
   → Batch process all .md → .docx
   → Use for WIP folders or custom locations

4. View conversion log
   → See history of all conversions
   → Useful for debugging errors

5. Manage settings
   → View environment info (Pandoc version, paths)
   → Select custom template
   → Clear log file

6. Exit
   → Close converter
```

---

## 7. Advanced Options (Per-File)

When converting a file, you can enable:

```
1. --toc
   Adds automatic Table of Contents at top of DOCX

2. --number-sections
   Automatically numbers all headings (1, 2, 3, etc.)

3. --shift-heading-level-by-1
   Changes heading hierarchy (h1 → h2, h2 → h3, etc.)

4. --wrap=none
   Disables line wrapping in output
```

Example: To convert with TOC and numbered sections, choose `1;2` when prompted.

---

## 8. Troubleshooting

### Issue: "Pandoc not found"

**Solution:**
1. Install Pandoc from [pandoc.org/installing.html](https://pandoc.org/installing.html)
2. Add Pandoc to Windows PATH
3. Restart Windows or run: `setx PATH "C:\Program Files\Pandoc;%PATH%"`

### Issue: "Lua filter not found" (Info message only)

**Solution:** This is OK—converter continues without filters. To enable:
1. Place `docx-enhancements.lua` and `template-variables.lua` in project root
2. Re-run converter

### Issue: Template variables not replaced

**Solution:**
1. Verify `template-variables.lua` is in project root
2. Check template variable syntax: `${VARIABLE}` (must have braces)
3. Run with Option 5 (Settings) → View environment info to verify Lua filter is detected

### Issue: "Conversion failed" error

**Solution:**
1. Check error details displayed in console
2. Look at log file: `%USERPROFILE%\Documents\md-to-docx-v3.1.0-log.txt`
3. Ensure Markdown is valid (no unclosed code blocks, etc.)
4. Try converting without advanced options first

### Issue: Backup .docx.backup files accumulating

**Solution:** These are safe to delete. They're automatic backups before re-converting.

```bash
# Delete all .backup files (optional)
cd docs/
del *.docx.backup
```

---

## 9. Best Practices

1. **Always use Option 2 for docs/** — Fastest and safest for governance documents
2. **Keep Lua filters in project root** — Converter auto-detects them
3. **Review DOCX before committing** — Template styling may vary
4. **Never edit .docx manually** — Always regenerate from .md
5. **Use template variables for metadata** — Auto-updates on each conversion
6. **Set environment variables once** — Create `SET-ENVIRONMENT.bat` for consistency

---

## 10. Version History

### v3.1.0 (Current)
- ✅ Lua filter support (docx-enhancements.lua, template-variables.lua)
- ✅ Template variable substitution (${VERSION}, ${DATE}, etc.)
- ✅ Auto-detection of Lua filters
- ✅ Environment variable support

### v3.0.0
- ✅ Auto-detect docs/ folder
- ✅ Smart template selection
- ✅ Auto-open DOCX
- ✅ Backup of previous versions
- ✅ Color-coded output

### v2.9.6
- Basic MD to DOCX conversion
- Manual file selection
- Simple template support

---

## 11. Quick Reference

| Task | Steps |
|------|-------|
| **Convert all governance docs** | Run script → Option 2 → Confirm |
| **Convert single file** | Run script → Option 1 → Enter path |
| **Drag & drop conversion** | Drag .md onto .bat → Choose options |
| **Add template variable** | Add `${VAR}` in Markdown, set in .lua filter |
| **View errors** | Option 4 (View log) or check `Documents/md-to-docx-v3.1.0-log.txt` |
| **Disable Lua filters** | Rename `.lua` files (optional) |
| **Set custom version** | Create `SET-ENVIRONMENT.bat` with `set FALCON_VERSION=...` |

---

## 12. Support & Feedback

For issues or improvements:

1. Check this guide first
2. Review error log (Option 4)
3. Check GitHub issues in repository
4. Contact project maintainer

---

**Updated:** 2026-01-09  
**Version:** v3.1.0  
**Status:** Production Ready
