# LIST OF HOTAS TABLES — Implementation Guide v2.1

**Version:** 2.1  
**Date:** 2026-02-11  
**Status:** Ready for Implementation  
**Project:** Falcon BMS TMS/DMS/CMS HOTAS Guide

---

## 1. Overview

This document provides the complete technical specification and implementation guide for two critical features of the TMS/DMS/CMS HOTAS Guide:

1. **`hotastable` environment v2.1** — Standardized HOTAS table formatting
2. **List of HOTAS Tables** — Automated index system for all HOTAS tables

### 1.1 Purpose

This guide serves as:
- **Technical reference** for LaTeX implementation
- **Integration checklist** for applying changes to the guide
- **Documentation of governance impacts** (BRIEFING, WIP-NAMING)
- **Record of architectural decisions** and rationale

---

## 2. Theme 1: `hotastable` Environment v2.1

### 2.1 Rationale and Design Goals

The `hotastable` environment v2.1 addresses several key requirements:

1. **Eliminate column overflow** — Previous versions experienced text overflow in the Train. column when multiple training missions were referenced
2. **Simplify content** — Train. column now contains only mission numbers (e.g., "18, 28"), not full descriptions
3. **Improve visual spacing** — Increased `\tabcolsep` from 2pt to 3pt for better cell separation
4. **Maintain readability** — Font size reduced to `\footnotesize` (8pt) with compensating row height increase
5. **Ensure multipage continuity** — Proper header repetition on page breaks
6. **Fit within page geometry** — Total table width 15.50 cm (within 17.0 cm text width)

### 2.2 Technical Specification

#### 2.2.1 Environment Parameters

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Font size | `\footnotesize` (8pt) | Greater density, more text per cell |
| `\tabcolsep` | 3pt | Better visual spacing between cells |
| `\arraystretch` | 1.35 | Compensates for smaller font, maintains vertical readability |

#### 2.2.2 Column Widths

| Column | Width | Alignment | Content Type |
|--------|-------|-----------|--------------|
| Mode | 1.00 cm | Left | Master mode, CMDS mode, sensor state |
| Dir. | 0.90 cm | Left | UP, DN, LT, RT (switch direction) |
| Act. | 0.90 cm | Left | S, M, L, LH (actuation type) |
| Function | 3.30 cm | Left | System function or control activated |
| Effect / Nuance | 6.40 cm | Left | Behavior, tactics, constraints (primary narrative column) |
| Dash34 | 1.40 cm | Left | Section references (e.g., 3-60, 2.7.2.2) |
| Train. | 1.60 cm | Left | **Training mission codes only** (e.g., 18, 28) |

**Total width calculation:**
```
Columns: 1.00 + 0.90 + 0.90 + 3.30 + 6.40 + 1.40 + 1.60 = 15.50 cm
Padding (7 cols × 2 sides × 3pt): 7 × 2 × 3pt = 42pt ≈ 1.48 cm
Total: 15.50 + 1.48 = 16.98 cm ✓ (within 17.0 cm text width limit)
```

### 2.3 Complete LaTeX Implementation

**Location in preamble:** Between package declarations and `\begin{document}`

```latex
% ============================================================================
% HOTAS table environment
% Version: 2.1 (2026-02-10)
% ============================================================================

\newenvironment{hotastable}[1]{%
	\footnotesize
	\setlength{\tabcolsep}{3pt}
	\renewcommand{\arraystretch}{1.35}
	\begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{1.60cm}}
		\caption{#1}\label{table.\thetable}\\
		\addtocontents{hotas}{\protect\contentsline{table}{\protect\numberline{\thetable}#1}{\thepage}{table.\thetable}}%
		\rowcolor{headerblue}
		\multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
		\endfirsthead
		\rowcolor{headerblue}
		\multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
		\multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
		\endhead
		\multicolumn{7}{r}{\small\emph{Continued on next page}}\\
		\endfoot
		\endlastfoot
	}{%
	\end{longtable}
}
```

**Required dependencies (must be in preamble before environment definition):**

```latex
\usepackage{array}       % L{width} column type
\usepackage{longtable}   % Multipage tables
\usepackage[table]{xcolor}      % Colors and row coloring

% Color definition
\definecolor{headerblue}{HTML}{003366}

% Custom column type
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
```

### 2.4 Usage Examples

#### 2.4.1 Basic Single-Page Table

```latex
\begin{hotastable}{CMS Switch Actuation with CMDS Manual Mode}
AUTO & Up & Short & Execute Program 1 & Dispenses chaff/flare per program 1 configuration & 2.7.2.1 & 28 \\
AUTO & Down & Short & Execute Program 2 & Dispenses chaff/flare per program 2 configuration & 2.7.2.1 & 28 \\
SEMI & Up & Short & Manual chaff & Single chaff bundle release & 2.7.2.2 & 9, 28 \\
SEMI & Down & Short & Manual flare & Single flare release & 2.7.2.2 & 9, 28 \\
\end{hotastable}
```

#### 2.4.2 Multi-Page Table

For tables exceeding one page, the environment automatically:
- Repeats the header row on continuation pages (`\endhead`)
- Adds "Continued on next page" footer (`\endfoot`)
- Omits footer on final page (`\endlastfoot`)

```latex
\begin{hotastable}{TMS Functions Across All Master Modes}
A-A & Up & Short & Designate FCR target & Locks radar on targeted contact & 3-48 & 18 \\
A-A & Down & Short & Reject current target & Returns FCR to search mode & 3-48 & 18 \\
% ... many rows ...
NAV & Right & Short & Cycle HSD declutter & Toggles map detail levels & 3-52 & 2 \\
\end{hotastable}
```

#### 2.4.3 Train. Column — Mission Number Format

**Correct usage (numbers only):**
```latex
& 2.7.2.1 & 18 \\              % Single mission
& 2.7.2.2 & 9, 28 \\           % Multiple missions
& 2.7.2.2 & 18, 19, 28 \\     % Three missions (max recommended)
```

**Incorrect usage (DO NOT USE):**
```latex
& 2.7.2.1 & \trnref{18 (BARCAP)} \\           % ✗ Old format
& 2.7.2.2 & TRN 18 \\                         % ✗ Includes "TRN" prefix
& 2.7.2.2 & Mission 18 (BARCAP) \\           % ✗ Full description
```

### 2.5 Simplification of Train. Column Content

#### 2.5.1 Rule

The Train. column contains **only mission numbers**, separated by commas.

#### 2.5.2 Migration from Previous Format

**Before (v1.0 with `\trnref` macro):**
```latex
& \dashref{2.7.2.2} & \trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)} \\
```

**After (v2.1 simplified):**
```latex
& 2.7.2.2 & 18, 28 \\
```

#### 2.5.3 Rationale for Simplification

1. **Eliminated overflow** — Mission descriptions required 4.5–5.0 cm; numbers fit in 1.60 cm
2. **Improved readability** — Clean, scannable format
3. **Maintained traceability** — Mission numbers still reference BMS Training Manual 4.38.1
4. **Simplified maintenance** — No need for standardized abbreviation table

#### 2.5.4 Finding Training Mission Descriptions

Mission numbers in the Train. column correspond to missions in **BMS Training Manual 4.38.1**.

Example mapping:
- `18` → Mission 18: RADAR MISSILES — BARCAP
- `28` → Mission 28: SEAD-EW
- `9` → Mission 9: IN-FLIGHT FAILURES

Full mission descriptions and learning objectives are documented in the BMS Training Manual, not in this guide.

---

## 3. Theme 2: List of HOTAS Tables

### 3.1 Rationale and Design Goals

The List of HOTAS Tables provides:

1. **Centralized navigation** — Single index of all HOTAS tables in the guide
2. **Automatic registration** — Each `hotastable` automatically adds itself to the index
3. **Hyperlinked entries** — Click table name to jump directly to that table
4. **Front matter integration** — Appears after Table of Contents, before main content

### 3.2 Technical Specification

#### 3.2.1 Index File System

The List of HOTAS Tables uses a dedicated auxiliary file:
- **File:** `.hotas` (generated during compilation)
- **Format:** Similar to `.toc` (Table of Contents) file
- **Content:** Table numbers, captions, page numbers, hyperlink targets

#### 3.2.2 Macro Definition

**Location in preamble:** After package declarations, before environment definitions

```latex
% --------------------------------------------------------------------------
% HOTAS LOT FILE HANDLE 
% --------------------------------------------------------------------------
\makeatletter
\newcommand{\listofhotastables}{%
	\section*{List of HOTAS Tables}%
	\addcontentsline{toc}{section}{List of HOTAS Tables}%
	\@starttoc{hotas}%
}
\makeatother
```

**Components explained:**
- `\makeatletter` / `\makeatother` — Allow use of `@` in command names (required for `\@starttoc`)
- `\section*{List of HOTAS Tables}` — Creates unnumbered section heading
- `\addcontentsline{toc}{section}{...}` — Adds entry to main Table of Contents
- `\@starttoc{hotas}` — Reads and typesets the `.hotas` file

#### 3.2.3 Automatic Registration (Already Integrated in `hotastable`)

Each `hotastable` environment automatically registers itself via this line:

```latex
\addtocontents{hotas}{\protect\contentsline{table}{\protect\numberline{\thetable}#1}{\thepage}{table.\thetable}}%
```

**This line is already present in the `hotastable` environment code (Section 2.3).** No additional action needed when creating tables.

**Components explained:**
- `\addtocontents{hotas}{...}` — Writes entry to `.hotas` file
- `\protect\contentsline{table}{...}` — Formats entry like standard table list
- `\protect\numberline{\thetable}` — Adds table number (e.g., "Table 5.1")
- `#1` — Table caption (from `\begin{hotastable}{Caption}`)
- `\thepage` — Current page number
- `table.\thetable` — Hyperlink target (from `\label{table.\thetable}`)

### 3.3 Document Integration

**Location in document:** Front matter, after Table of Contents

```latex
\pagenumbering{roman}

\newpage
\tableofcontents
\newpage

% --------------------------------------------------------------------------
% LIST OF HOTAS TABLES
% --------------------------------------------------------------------------
\phantomsection
\listofhotastables
\newpage

\pagenumbering{arabic}
```

**Workflow:**
1. User compiles guide with `pdflatex`
2. Each `hotastable` writes entry to `.hotas` file
3. `\listofhotastables` reads `.hotas` and typesets the index
4. Index appears in PDF between TOC and Chapter 1
5. Index entries are clickable hyperlinks

### 3.4 Example Output

**List of HOTAS Tables (as rendered in PDF):**

```
List of HOTAS Tables

Table 4.1  DMS Down: SOI Toggle Behavior ............................ 42
Table 4.2  DMS Up: HDU Designation ................................... 45
Table 5.1  CMS Actuation with CMDS Manual Mode ....................... 58
Table 5.2  CMS Actuation with CMDS Automatic Mode .................... 60
```

Each entry is a hyperlink — clicking jumps directly to that table in the document.

---

## 4. Content Changes in Existing Tables

### 4.1 Simplification of Train. Column

All existing tables must be updated to use the simplified format.

#### 4.1.1 Search and Replace Patterns

**Option A: Regex (for bulk replacement)**

**Search pattern:**
```regex
\\trnref\{(\d+)\s*\([^)]+\)\}
```

**Replace with:**
```regex
\1
```

**Example transformations:**
- `\trnref{18 (BARCAP)}` → `18`
- `\trnref{28 (SEAD-EW)}` → `28`
- `\trnref{9 (Failures)}` → `9`

**Tools:** VSCode, Sublime Text, or command-line `sed`

**Warning:** Test on a single file first. Always backup before bulk replacement.

**Option B: Manual replacement (safer)**

**Search:** `\trnref{`  
**Action:** Review each occurrence and simplify manually

**Example manual edit:**
```latex
% Before:
& \dashref{2.7.2.2} & \trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)} \\

% After:
& 2.7.2.2 & 18, 28 \\
```

#### 4.1.2 Special Cases

**Multiple missions in same cell:**

```latex
% Before:
\trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)}, \trnref{12 (HARM)}

% After:
18, 28, 12
```

**Empty cells (no applicable training mission):**

```latex
% Before:
& \dashref{3-48} &  \\

% After (no change):
& 3-48 &  \\
```

### 4.2 Table Introduction Text

Each chapter containing `hotastable` tables should include explanatory text before the first table.

#### 4.2.1 Recommended Location

Insert immediately before the first `\begin{hotastable}` in each chapter (e.g., Chapter 4, 5).

#### 4.2.2 Standard Introduction Text

```latex
\subsection*{How to Read the Tables}

The tables in this chapter use the following column structure:

\begin{itemize}[leftmargin=*, nosep]
  \item \textbf{Mode:} The operational context (master mode, CMDS mode, sensor state).
  \item \textbf{Dir.:} The physical direction for pressing the switch (Up, Down, Left, Right).
  \item \textbf{Act.:} The press type (Short, Medium, Long, or Long Hold).
  \item \textbf{Function:} What the switch command activates or controls.
  \item \textbf{Effect / Nuance:} The resulting system behavior, including tactical considerations and constraints.
  \item \textbf{Dash34:} Reference section in the Dash-34 manual (TO 1F-16CMAM-34-1-1 BMS).
  \item \textbf{Train.:} Recommended BMS training mission codes for hands-on practice. 
        \emph{For mission descriptions and learning objectives, refer to the BMS Training Manual 4.38.1.}
\end{itemize}
```

#### 4.2.3 Alternative: Footnote Format

If space is constrained, use a footnote on the first table:

```latex
\begin{hotastable}{CMS Actuation with CMDS Manual Mode\footnotemark}
...
\end{hotastable}

\footnotetext{Training mission codes refer to BMS Training Manual 4.38.1. 
For example, mission 18 is "BARCAP" (Barrier Combat Air Patrol). 
Consult the manual for detailed learning objectives and mission flows.}
```

---

## 5. Impacts on Governance Documents

### 5.1 BRIEFING

**File:** `docs/briefing.md`

**Action:** Update multiple sections to reflect new specifications

**Note:** These changes will be applied **after** the preamble implementation is finalized and approved.

#### 5.1.1 Section 6.3 — Formatação de Tabelas (hotastable)

**Current text (approximate location: lines 255-260):**

```markdown
### 6.3 Formatação de Tabelas (hotastable)

- Font size: `\small` (10pt)
- Row height: `\arraystretch = 1.25`
- Colunas: Mode (1.00cm), Dir. (0.90cm), Act. (0.90cm), Sensor/Mode (3.30cm), Effect/Nuance (6.40cm), Dash-34 (1.40cm), Training (2.10cm)
```

**Replace with:**

```markdown
### 6.3 Formatação de Tabelas (hotastable)

**Environment:** `hotastable`  
**Version:** 2.1 (updated 2026-02-10)

**Formatting parameters:**
- Font size: `\footnotesize` (8pt base)
- Row height: `\arraystretch = 1.35`
- Cell padding: `\tabcolsep = 3pt`

**Column widths:**

| Column | Width | Alignment | Content |
|--------|-------|-----------|---------|
| Mode | 1.00 cm | Left | Master mode, CMDS mode, sensor state |
| Dir. | 0.90 cm | Left | UP, DN, LT, RT |
| Act. | 0.90 cm | Left | S, M, L, LH |
| Function | 3.30 cm | Left | System function or control activated |
| Effect / Nuance | 6.40 cm | Left | Behavior, tactics, constraints (primary narrative column) |
| Dash34 | 1.40 cm | Left | Section references (e.g., 3-60, 2.7.2.2) |
| Train. | 1.60 cm | Left | Training mission codes only (e.g., 18, 28) |

**Total width:**
- Columns: 15.50 cm
- Padding (3pt × 7 cols × 2): 1.48 cm
- **Total: 16.98 cm** (within 17.0 cm text width)

**Training column content:**
The Train. column contains only mission codes (e.g., "18, 28"). 
Mission names and descriptions are referenced in the BMS Training Manual 4.38.1, 
as noted in the table introduction text within each chapter.

**Changelog:**
- v2.1 (2026-02-10): Font reduced to \footnotesize, \tabcolsep increased to 3pt, 
  Train. width reduced to 1.60 cm, arraystretch increased to 1.35
- v2.0 (2026-02-04): Initial v2 specification
- v1.0 (2026-01-XX): Initial implementation with \small, 2pt padding, 2.10 cm Train.
```

#### 5.1.2 New Section — List of HOTAS Tables

**Location:** After existing macros section (approximate location: Section 12.3)

**Add new subsection:**

```markdown
### 12.3.X List of HOTAS Tables Macro

**Macro:** `\listofhotastables`

**Purpose:** Generates an automated index of all HOTAS tables in the guide.

**Location in document:** Front matter, after Table of Contents, before main content.

**Implementation:**

```latex
\makeatletter
\newcommand{\listofhotastables}{%
	\section*{List of HOTAS Tables}%
	\addcontentsline{toc}{section}{List of HOTAS Tables}%
	\@starttoc{hotas}%
}
\makeatother
```

**Usage in document:**

```latex
\tableofcontents
\newpage
\phantomsection
\listofhotastables
\newpage
```

**Automatic registration:** Each `hotastable` environment automatically adds its entry to the `.hotas` index file. No manual registration required.

**Output:** Numbered list of all HOTAS tables with page numbers and hyperlinks.
```

#### 5.1.3 Section on Training Column Content

**Location:** Column descriptions (approximate location: Section 6.7 or similar)

**Add or update:**

```markdown
### 6.7 Column 7: Train. (1.60 cm)

**Content:** Training mission codes only (numbers).

**Format:**
- Single mission: `18`
- Multiple missions: `18, 28` or `18, 19, 28`
- Maximum: 2–3 missions per cell (readability)

**Do NOT use:**
- ✗ `\trnref{18 (BARCAP)}` — Old macro format
- ✗ `TRN 18` — Text prefix
- ✗ `Mission 18 (BARCAP)` — Full description

**Mission reference:** All mission numbers correspond to BMS Training Manual 4.38.1. 
Mission descriptions and learning objectives are documented in that manual, not in this guide.

**Introduction text:** Each chapter with HOTAS tables should include explanatory text 
(see Section 4.2.2 of LIST-OF-TABLES-IMPLEMENTATION-GUIDE-v2_1.md) before the first table.
```

#### 5.1.4 Update to Template Section

**Location:** Section 11 or template documentation

**Update environment code:** Replace `hotastable` environment definition with v2.1 code (from Section 2.3 of this guide).

**Add note:**

```markdown
**Note:** The `hotastable` environment v2.1 includes automatic registration 
with the List of HOTAS Tables. No additional macros are needed when creating new tables.
```

#### 5.1.5 Changelog Entry (Top of BRIEFING)

**Add to changelog section:**

```markdown
**Changelog:**
- v0.2.1.0 (2026-XX-XX): Updated hotastable environment to v2.1, added List of HOTAS Tables, simplified Train. column to numbers-only format, documented deletion of TRAINING-MISSION-ABBREV-TABLE-v1_0.md
- v0.2.0.1 (2026-01-XX): [previous changes]
```

**Note:** Version number (v0.2.1.0) and date to be determined when changes are officially applied.

#### 5.1.6 Document Deleted File

**Location:** Changelog or References section

**Add note:**

```markdown
**Deleted files:**
- `TRAINING-MISSION-ABBREV-TABLE-v1_0.md` — Deleted on 2026-02-XX. This file defined standardized abbreviations for training missions in the Train. column. With the simplification of the Train. column to numbers-only format (v2.1), the abbreviation table became unnecessary. Mission descriptions are now referenced directly in BMS Training Manual 4.38.1.
```

---

### 5.2 WIP-FILE-NAMING-v1.4

**File:** `docs/WIP-FILE-NAMING-v1.4.md`

**Action:** Remove reference to deleted file

#### 5.2.1 Line 78 — Remove Deleted File Reference

**Current text (line 78):**

```markdown
│   ├── project-tracking-v*.md
│   ├── version-system-v*.md
│   ├── wip-naming-v*.md             (This document)
│   ├── briefing-v*.md
│   └── training-mission-abbrev-table-v*.md
```

**Replace with:**

```markdown
│   ├── project-tracking-v*.md
│   ├── version-system-v*.md
│   ├── wip-naming-v*.md             (This document)
│   └── briefing-v*.md
```

**Rationale:** The file `training-mission-abbrev-table-v*.md` has been deleted and should not appear in the file structure documentation.

---

### 5.3 VERSION-SYSTEM-v4.2.1

**File:** `docs/VERSION-SYSTEM-v4.2.1.md`

**Action:** No changes required.

**Rationale:** Version system governs version numbering, not technical specifications. The changes in this guide do not affect versioning rules.

---

### 5.4 PROJECT-TRACKING

**File:** `docs/project-tracking.md`

**Action:** No changes documented in this guide (as requested).

**Note:** Session entries will be added during normal workflow, not specified here.

---

## 6. Implementation Checklist

### 6.1 Pre-Implementation

- [ ] Backup `guide.tex` and all WIP files
- [ ] Create Git branch `feature/hotastable-v2.1` (optional but recommended)
- [ ] List all files containing `hotastable` tables
- [ ] Identify chapters requiring table introduction text

### 6.2 Preamble Updates

- [ ] Verify `hotastable` environment matches Section 2.3 exactly
- [ ] Verify `\listofhotastables` macro matches Section 3.2.2 exactly
- [ ] Verify required dependencies are present (array, longtable, xcolor)
- [ ] Verify custom column type `L{width}` is defined
- [ ] Verify `headerblue` color is defined

### 6.3 Content Updates

- [ ] Simplify Train. column in all existing tables (numbers only)
- [ ] Add table introduction text to Chapter 4 (DMS)
- [ ] Add table introduction text to Chapter 5 (CMS)
- [ ] Add table introduction text to future chapters with tables
- [ ] Verify no `\trnref{XX (NAME)}` patterns remain in table cells

### 6.4 Document Integration

- [ ] Add `\listofhotastables` and `\phantomsection` to front matter (after TOC)
- [ ] Verify `\newpage` separates TOC, List of Tables, and main content
- [ ] Test compilation: `pdflatex guide.tex` (run twice for index generation)
- [ ] Verify no "Overfull \hbox" warnings for tables
- [ ] Visual inspection: tables render correctly, headers repeat on page breaks

### 6.5 Governance Updates (Future)

**Note:** These will be applied when preamble implementation is finalized.

- [ ] Update BRIEFING Section 6.3 (table specifications)
- [ ] Add BRIEFING section on List of HOTAS Tables
- [ ] Update BRIEFING training column documentation
- [ ] Add BRIEFING changelog entry
- [ ] Document deleted file in BRIEFING
- [ ] Remove line 78 from WIP-FILE-NAMING-v1.4

### 6.6 Testing and Validation

- [ ] Compile guide and verify PDF output
- [ ] Click links in List of HOTAS Tables — verify navigation works
- [ ] Print test page — verify font size is readable
- [ ] Check table alignment across all pages
- [ ] Verify caption numbering is sequential
- [ ] Verify all tables appear in List of HOTAS Tables

### 6.7 Finalization

- [ ] Archive old guide snapshot to `archive/GUIDE/`
- [ ] Create new guide snapshot in `wip/guide/`
- [ ] Copy snapshot to `guide.tex` (repository root)
- [ ] Commit changes with descriptive message
- [ ] Create GitHub tag (when appropriate)
- [ ] Create GitHub Release (when appropriate)
- [ ] Update PROJECT-TRACKING with session entry

---

## 7. Troubleshooting

### 7.1 Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| "Undefined control sequence \listofhotastables" | Macro not defined or `\makeatletter` missing | Verify Section 3.2.2 code in preamble |
| "File .hotas not found" | First compilation, file not yet generated | Run `pdflatex` twice |
| List of HOTAS Tables is empty | Tables not using `hotastable` environment | Migrate legacy tables to `hotastable` |
| Table overflow in Train. column | Content not simplified to numbers only | Replace `\trnref{...}` with plain numbers |
| Header not repeating on page breaks | Using `tabular` instead of `longtable` | Use `hotastable` environment (includes longtable) |
| Column widths incorrect | Manual table definition | Use `hotastable` environment exclusively |

### 7.2 Compilation Workflow

For proper index generation, compile **twice**:

```bash
pdflatex guide.tex   # First pass: generates .hotas file
pdflatex guide.tex   # Second pass: reads .hotas and builds index
```

If using latexmk:
```bash
latexmk -pdf guide.tex   # Automatically handles multiple passes
```

---

## 8. Appendix: Diff Summary

### 8.1 hotastable Environment Changes

```diff
\newenvironment{hotastable}[1]{%
-  \small
-  \setlength{\tabcolsep}{2pt}
-  \renewcommand{\arraystretch}{1.25}
-  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{2.10cm}}
+  \footnotesize
+  \setlength{\tabcolsep}{3pt}
+  \renewcommand{\arraystretch}{1.35}
+  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{1.60cm}}
   \caption{#1}\label{table.\thetable}\\
+  \addtocontents{hotas}{\protect\contentsline{table}{\protect\numberline{\thetable}#1}{\thepage}{table.\thetable}}%
```

### 8.2 Train. Column Content Changes

```diff
-& \dashref{2.7.2.2} & \trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)} \\
+& 2.7.2.2 & 18, 28 \\
```

### 8.3 Front Matter Changes

```diff
 \tableofcontents
 \newpage
+\phantomsection
+\listofhotastables
+\newpage
 \pagenumbering{arabic}
```

---

## 9. Version History

| Version | Date | Changes |
|---------|------|---------|
| v2.1 | 2026-02-11 | Complete rewrite based on preamble authority. Added List of HOTAS Tables implementation, detailed BRIEFING and WIP-NAMING impact documentation, comprehensive examples and troubleshooting. |
| v2.0 | 2026-02-05 | Initial specification (superseded) |

---

## 10. References

- **Preamble:** `guide.tex` (repository root) — Authoritative source for all code
- **BRIEFING:** `docs/briefing.md` — Project governance and specifications
- **WIP-NAMING:** `docs/WIP-FILE-NAMING-v1.4.md` — File naming conventions
- **VERSION-SYSTEM:** `docs/VERSION-SYSTEM-v4.2.1.md` — Versioning rules
- **PROJECT-TRACKING:** `docs/project-tracking.md` — Session history

---

**Document Status:** Ready for Implementation  
**Next Action:** Review checklist (Section 6), begin preamble verification  
**Approved By:** Pending

---

**END OF GUIDE**
