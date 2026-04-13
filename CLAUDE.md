# CLAUDE.md — TMS/DMS/CMS Usage Guide for Falcon BMS

## Project Overview

Technical documentation project in LaTeX — a usage guide for the F-16 HOTAS switches
(TMS, DMS, CMS) in Falcon BMS 4.38.1. Pre-publication phase (v0.x.x.x).

- **Repo:** `carlos-nader/tms-dms-cms-usage-guide`
- **Canonical file:** `guide.tex` (repository root)
- **Active snapshot:** `wip/guide/guide-vX.X.X.X-YYYYMMDD.tex`
- **License:** CC BY-NC 4.0
- **Web publication:** [Read the Docs](https://tms-dms-cms-usage-guide.readthedocs.io) · GitBook (synced from `docs-web/`)

## Language Convention

- Instructions and conversation: **Portuguese**
- All LaTeX content (text, tables, captions, macros): **English**

---

## Compilation

**Standard (2 passes required for TOC and List of HOTAS Tables):**

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error guide.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error guide.tex
```

Or using the CI script (full validation):

```bash
bash ci/travis.sh
```

**WIP files follow the same rule** — compile twice when the file contains `hotastable` environments.

---

## Scripts

| Script | What it does |
| -------- | ------------- |
| `scripts/generate-integrated-files.py` | Generates `INTEGRATED-FILES.md` and `.json` (CodeScene: 8.95) |
| `scripts/update-readme-version.py` | Updates version in README and `docs/index.html` (CodeScene: 10) |
| `scripts/validate-tex-preamble.py` | Validates LaTeX preamble consistency |
| `scripts/generate-wip-snapshot.py` | Updates WIP snapshot table in `README.md` |
| `scripts/update-alpha-badge.py` | Updates alpha pre-release badge in `README.md` and `docs/index.html` |
| `scripts/scrape-forum-views-debug.py` | Scrapes forum view count and updates badge in `README.md` |
| `check-guide-integrity.ps1` | Byte-identical check: `guide.tex` ↔ active snapshot |

---

## Reference Sources (local, not committed)

Primary PDF references are stored locally at `misc/fontes/` (gitignored):

| File | Content |
| ------ | --------- |
| `TO 1F-16CMAM-34-1-1 BMS.pdf` | **Dash-34** — primary technical reference |
| `TO 1F-16CMAM-1 BMS.pdf` | BMS Flight Manual (Dash-1) |
| `11-2F-16_Vol5.pdf` | ACC Multi-Command Handbook 11-F16 Vol. 5 |
| `BMS-Training-Manual.pdf` | BMS Training Manual |
| `BMS-User-Manual.pdf` | BMS User Manual |
| `BMS-Threat-Guide.pdf` | BMS Threat Guide |

---

## Governance Documents (sources of truth — read before acting)

1. `docs/briefing.md` — Scope, structure, LaTeX preamble, table standards, workflow
2. `docs/version-system.md` — Version numbering rules
3. `docs/wip-naming.md` — WIP file naming and status lifecycle
4. `docs/project-tracking.md` — Current session log, WIP status, priorities
5. `misc/STYLE-GUIDE.md` — Prose style, voice, forbidden patterns

---

## WIP File Naming

**Pattern:** `{type}-C{N}[-S{M}]-{title}-{status}-{YYYY-MM-DD}.{ext}`

**Examples:**

- `chapter-C4-tms-structure-dev-2026-02-13.tex`
- `section-C5-S2-cms-actuation-review-2026-01-10.tex`

**Status lifecycle:** `dev → review → final → approved` (or `deprecated`)
**Alpha flow (parallel/optional):** `final → alpha → approved`

**Template for new WIP:** `template/template-wip.tex`

---

## Version System (pre-publication)

- **MINOR** bump: new chapter integrated into `guide.tex`
- **PATCH** bump: structural change in existing chapter
- **SUBPATCH** bump: local adjustments, typos
- Version bumps only when content enters `guide.tex` (not on WIP changes)
- Format: `MAJOR.MINOR.PATCH.SUBPATCH` (e.g., `0.4.1.1`)

---

## Commit Conventions

Any commit addressing a GitHub Issue **must** include a `Refs #NN` footer:

```text
Short description of change

Refs #48
```

Multiple issues:

```text
Short description

Refs #44
Refs #48
```

Automated/bot commits are exempt.

---

## Directory Structure

```text
guide.tex                    # Canonical guide (byte-identical to active snapshot)
docs-web/                    # Markdown source for web publication (Read the Docs / GitBook)
  README.md                  # Landing page
  c*-[chapter-title].md      # One file per chapter (pandoc conversion — Alpha.2+)
wip/
  guide/                     # Active snapshot (exactly 1 .tex file)
  chapter-C#-*.tex           # Chapter WIP files
  section-C#-S#-*.tex        # Section WIP files
  guide-v*-alpha.*-*.tex     # Alpha snapshots (only when pre-release active)
archive/
  GUIDE/                     # Historical guide snapshots
  WIP/                       # Integrated/deprecated WIP files
template/
  template-wip.tex           # Canonical WIP template
docs/                        # Governance documents
misc/
  STYLE-GUIDE.md             # Prose and formatting rules
scripts/                     # Automation scripts
ci/
  travis.sh                  # Full CI validation script
fig/                         # Images used in guide
```

---

## hotastable Environment (v2.1)

7-column HOTAS table layout (total width: 15.50 cm):

| Col | Width | Content |
| ----- | ------- | --------- |
| Mode | 1.00 cm | Master mode (NAV, A-A, A-G) |
| Dir. | 0.90 cm | Up / Down / Left / Right |
| Act. | 0.90 cm | S / M / L / LH |
| Function | 3.30 cm | Concise function name |
| Effect / Nuance | 6.40 cm | 1–3 sentences of explanation |
| Dash34 | 1.40 cm | Plain text refs (e.g., "3-48") |
| Train. | 1.60 cm | Mission numbers only (e.g., "18, 28") |

**Key rules:**

- Use plain text in table cells — no macros like `\dashref{}` inside cells
- Train. column: numbers only (deprecated: `\trnref{18 (BARCAP)}`)
- In narrative text: use `\dashref{}`, `\secref{}`, `\tabref{}`, etc.

---

## AI Limits

The AI assistant (Claude Code) may:

- Generate and edit WIP files
- Review prose style and structure
- Run scripts and read files
- Create and manage `MEMORY.md` and related files in the auto memory directory (`.claude/projects/*/memory/`) as needed, without prior approval

The AI must NOT autonomously:

- Decide final status, integration into `guide.tex`, or archival
- Create Git tags or releases
- Make commits or pushes without explicit user approval

---

## Handling Ambiguity and Scope

- If a request has more than one valid interpretation, list them before acting — do not choose silently.
- If assumptions are needed to proceed, state them explicitly.
- If scope is unclear, ask rather than infer.
- Edit only what was explicitly requested. Do not improve, reformat, or restructure adjacent content.
- If an unrelated issue is noticed while working, mention it — do not fix it unless asked.

---

## Critical Rules

- **Never commit or push without explicit user approval**
- All prose must comply with `misc/STYLE-GUIDE.md`
- `INTEGRATED-FILES.md` and `INTEGRATED-FILES.json` are auto-generated — avoid manual edits
- `guide.tex` must always be byte-identical to the active snapshot in `wip/guide/`
