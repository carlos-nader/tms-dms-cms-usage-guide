# AI Agent Instructions — Falcon BMS TMS/DMS/CMS Guide Project

## Project Overview

This is a **LaTeX-based technical documentation project** developing a comprehensive usage guide for F-16 HOTAS switches (TMS/DMS/CMS) in Falcon BMS 4.38.1 flight simulator. The project uses a strict governance framework with version control, WIP file lifecycles, and AI-assisted content development.

**Current Status:** Pre-publication phase (v0.3.3.0), 3/7 chapters completed, targeting v1.0 publication

**Primary Languages:** LaTeX (content), Python (automation), PowerShell (validation)

## Critical Governance Documents (Read These First)

All governance documents are in `/docs/` and are **mandatory reading** before making changes:

1. **[briefing.md](../docs/briefing.md)** — Project scope, content outline, LaTeX style guidelines, layout standards
2. **[version-system.md](../docs/version-system.md)** — Guide versioning (0.x.x.x pre-publication vs x.y.z post-publication)
3. **[wip-naming.md](../docs/wip-naming.md)** — WIP file naming conventions and status lifecycle (dev → review → final → approved)
4. **[project-tracking.md](../docs/project-tracking.md)** — Current status, chapter progress, development log

**Rule:** Never modify governance documents without explicit approval. These define the project's operational framework.

## File Structure & Workflows

### The Canonical Guide File

- **`guide.tex`** (root) — Production-ready guide file
- **`wip/guide/guide-v*.tex`** — Active snapshot (must be byte-identical to `guide.tex`)
- **`archive/GUIDE/`** — Historical snapshots

**Integrity Check:** Run `.\check-guide-integrity.ps1` to verify `guide.tex` matches the active snapshot.

### WIP File Lifecycle

All WIP files **MUST** be created from `template/template-wip.tex` (canonical template).

**Naming Pattern:** `{type}-C{N}[-S{M}]-{title}-{status}-{date}.tex`

- **Example:** `section-C4-S2-dms-up-final-2026-01-14.tex`
- **Status codes:** `dev` (draft) → `review` (under review) → `final` (approved) → `approved` (integrated & archived) → `deprecated` (retired)

**Workflow:**
1. Copy `template/template-wip.tex` to `wip/`
2. Rename following the pattern above
3. Edit content (development status: `dev`)
4. Human review (status: `review`)
5. Finalize (status: `final`)
6. **Human integrates** into `guide.tex` (AI assists but does NOT perform integration)
7. Move to `archive/WIP/` with status `approved`

### Version Bumping Rules (0.x.x.x Pre-publication)

**When to bump versions:**
- **MINOR (0.x.0.0)** — New chapter integrated
- **PATCH (0.x.x.0)** — Structural change within existing chapter (e.g., first major table)
- **SUBPATCH (0.x.x.x)** — Small refinements, typo fixes, local polish

**Process:**
1. Update macros in `guide.tex` preamble: `\docversion`, `\docbuild`, `\docenddate`
2. Save snapshot to `wip/guide/guide-v{VERSION}-{YYYYMMDD}.tex`
3. Copy snapshot to `guide.tex` (must be identical)
4. Update `docs/project-tracking.md`
5. Move previous snapshot to `archive/GUIDE/`
6. Create GitHub tag and release

**Never** manually increment versions — follow the decision tables in [version-system.md](../docs/version-system.md).

## LaTeX Conventions & Styling

### Preamble Architecture

The project uses a **consolidated preamble** (documented in `docs/tex-preamble-consolidated.md`):
- Document class: `report` (11pt, a4paper, twoside)
- Geometry: 2cm L/R margins, 2.5cm T/B margins
- Custom environments: `hotastable` (for HOTAS switch tables with 15.6cm width)
- Custom macros: `\docversion`, `\dashlnk{section}`, `\trglnk{mission}`, `\imglink{label}`

### Critical Styling Rules

1. **Table Width:** All HOTAS tables use `\begin{hotastable}` environment (15.6cm fixed width, centered)
2. **Cross-references:** Use `\dashlnk{4.2.1}` for Dash-34 sections, `\trglnk{TEMU-11-SAM}` for training missions
3. **Missions:** Use standard abbreviations from `docs/training-mission-abbrev-table-v1.0.md`
4. **Content Language:** ALL LaTeX content (text, tables, captions) in **English**
5. **Instructions Language:** ALL instructions to AI in **Portuguese** (project convention)

### LaTeX Quality Standards

- Never use placeholder text like "TBD" or "TODO" in integrated content
- All table cells must have substantive content or "N/A"
- Cross-reference every table row to Dash-34 sections and training missions
- Maintain consistent column widths and alignment across similar tables

## Python Automation Scripts

### `generate-integrated-files.py`

Auto-generates tracking reports (`INTEGRATED-FILES.md` and `.json`) showing:
- Tracked files in `wip/`, `archive/`, `docs/`
- Recent commits, tags, releases
- Open issues and milestones

**Triggered by:** GitHub Actions on push (see `.github/workflows/generate-integrated-files.yml`)

### `update-readme-version.py`

Updates README.md version badges when new tags are created.

**Triggered by:** GitHub Actions on tag creation

### PowerShell Validation

`check-guide-integrity.ps1` — Validates byte-identical match between `guide.tex` and active snapshot.

## Development Commands

### Compile LaTeX

```powershell
# In TeXstudio (preferred) or command line
pdflatex guide.tex
```

### Run Integrity Check

```powershell
.\check-guide-integrity.ps1
```

### Generate Tracking Report

```powershell
python scripts/generate-integrated-files.py
```

## Common Tasks for AI Agents

### Creating New WIP Content

1. Copy `template/template-wip.tex` to `wip/`
2. Rename: `section-C{N}-S{M}-{descriptive-title}-dev-{YYYY-MM-DD}.tex`
3. Edit metadata section (file identification, description, status)
4. Develop content following BRIEFING style guidelines
5. **Never** integrate into `guide.tex` without human approval

### Reviewing Existing WIP Files

1. Check naming compliance with `wip-naming.md`
2. Verify content follows BRIEFING style rules
3. Check cross-references (`\dashlnk`, `\trglnk`) are valid
4. Ensure `hotastable` environments are properly formatted
5. Validate training mission abbreviations against `training-mission-abbrev-table-v1.0.md`

### Updating Documentation

1. **Governance docs** (`docs/*.md`) — Consult human before modifying
2. **README.md** — Update only for major changes (usually automated)
3. **INTEGRATED-FILES.md** — Auto-generated, do NOT edit manually

## Project-Specific Patterns

### HOTAS Table Structure (Key Pattern)

The `hotastable` environment uses a 7-column longtable structure (15.6cm total width):

```latex
\begin{hotastable}{Caption Text Here}
\label{tab:switch-action}
% Columns: Mode (1.00cm) | Dir. (0.90cm) | Act. (0.90cm) | Function (3.30cm) | Effect/Nuance (6.40cm) | Dash34 (1.40cm) | Train. (2.10cm)
\midrule
A-A CRM & Up & Short & Bug target & Moves cursor to designate target in FCR. & \dashref{2.1.5} & \trnref{18 (BARCAP)} \\
A-G PRE & Down & Long & Break lock & Releases current designation and returns to search. & \dashref{2.7.1} & \trnref{28 (SEAD-EW)} \\
\bottomrule
\end{hotastable}
```

For complete column specifications, see BRIEFING Section 4.2 and Section 12.3.9.

### Version Metadata Macros

```latex
\newcommand{\docversion}{0.3.3.0}
\newcommand{\docbuild}{20260202}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{02 February 2026}
\newcommand{\chapterscompletedof}{3/7}
```

## What NOT to Do

1. ❌ **Never** integrate WIP content into `guide.tex` without human approval
2. ❌ **Never** modify `template/template-wip.tex` (it's the canonical template)
3. ❌ **Never** create WIP files without using the template
4. ❌ **Never** bump versions without following the decision tables
5. ❌ **Never** modify governance documents (`docs/*.md`) without explicit approval
6. ❌ **Never** write content in Portuguese (content must be English)
7. ❌ **Never** use generic placeholders like "TODO" in LaTeX content
8. ❌ **Never** edit `INTEGRATED-FILES.md` manually (it's auto-generated)

## Quick Reference Links

- **Source Materials:** `misc/fontes/` (Dash-34, Dash-1, training manual PDFs)
- **Figures:** `fig/` (images for the guide)
- **Templates:** `template/` (canonical WIP template, guide structure template)
- **Active Work:** `wip/` (chapter/section files in development)
- **Archive:** `archive/WIP/` (integrated files), `archive/GUIDE/` (old guide versions)

## Questions to Ask Before Making Changes

1. Which governance document defines the rules for this change?
2. Is this a WIP file or the canonical `guide.tex`?
3. Does this require a version bump? Which level (MINOR/PATCH/SUBPATCH)?
4. Have I verified the naming convention against `wip-naming.md`?
5. Is the content in English and instructions in Portuguese?
6. Am I following the BRIEFING style guidelines?

---

**Remember:** This project has a strict governance framework. When in doubt, consult the governance documents in `/docs/` or ask the human author for clarification.
