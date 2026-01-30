# Falcon BMS 4.38.1 — TMS, DMS and CMS Usage Guide: Project Brief

**Brief Version:** v0.2.0.1-2026-01-29 (Preamble V1.0 Updated: titlesec Full Hierarchy + Optical Fixes)

---

## Repository Identification

- GitHub repository name: `carlos-nader/tms-dms-cms-usage-guide`
- Primary URL: https://github.com/carlos-nader/tms-dms-cms-usage-guide
- Default branch: `main`
- Canonical guide file: `guide.tex` (repository root)
- Versioned snapshots: `wip/guide/guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex`

---

## 0. Context and Working Assumptions

This brief describes how the TMS/DMS/CMS Usage Guide is being built, including:

- Scope, goals and structure of the document.
- Source material and style rules.
- Layout parameters and table standards.
- License and contributor rights.
- High-level overview of the Version System v4.2.1 and how it interacts with GitHub.

All instructions to the assistant are given in **Portuguese**. All content that goes into the **LaTeX document** (text, tables, captions, macros) is in **English**.

The guide is currently in **pre-publication regime (0.x.x.x)** and under active development.

---

## 1. Scope and Goals

- The guide focuses only on three HOTAS switches: **TMS, DMS and CMS**.
- Other HOTAS controls (for example NWS/MSL STEP, MAN RNG/UNCAGE, etc.) may be mentioned only when strictly necessary to understand TMS/DMS/CMS behaviour.
- The document is not a full HOTAS or full avionics manual; it is a usage guide for these three switches, organised by context and supported by tables.
- The language of the document is English; style is clear, concise and manual-like, not chatty.

### 1.1 Main Goals

- Reorganise information that is spread across the BMS Dash-1, Dash-34 and the BMS Training Manual into context-based tables and short explanations.
- Make it easy for a virtual pilot to answer: "In this mode/sensor/weapon, what does each direction of TMS/DMS/CMS do?"
- Cross-reference each table line to:
  - The relevant Dash-34 (and sometimes Dash-1) section.
  - One or more BMS training missions where the behaviour can be practised.

---

## 2. Sources to Align With (But Never Limited To)

When generating or refining content, conceptually align with (but do not copy):

### 2.1 Falcon BMS Dash-34 (TO BMS 1F-16CMAM-34-1-1)

Especially, but never limited to:

- Hands-On Controls (HOTAS) section.
- SOI behaviour.
- Defensive avionics (ALE-47, ECM, CMS).
- Weapon-specific chapters (HARM, Maverick, IAMs, SPICE, Harpoon, etc.).

### 2.2 Falcon BMS Dash-1 (TO BMS 1F-16CMAM-1)

Where relevant (overall aircraft systems, master modes, etc.).

### 2.3 Falcon BMS Training Manual 4.38.1

Especially, but never limited to:

- Mission descriptions and learning objectives.
- Missions involving SEAD/EW, HARM, IAMs, LGBs, BARCAP, IFF, etc.

**Critical rule:** Never reproduce copyrighted text; always paraphrase in original words.

---

## 3. Document Structure (LaTeX Already Prepared)

Assume there is already a LaTeX template with this structure. Do not change the overall structure or helper macros unless explicitly requested, but suggestions may be made when technically justified. Always generate complete LaTeX files when ordered to generate one.

### 3.1 Chapter Breakdown

**1. Introduction**

- 1.1 Scope and purpose.
- 1.2 Version, authorship and AI assistance.
- 1.3 Sources and references.
- 1.4 Document structure and how to read it.

**2. HOTAS Fundamentals**

- 2.1 Sensor of Interest (SOI) and display logic.
- 2.2 Short vs long presses and timing.
- 2.3 Master modes and context-sensitive behaviour.
- 2.4 Overview of TMS, DMS and CMS.

**3. TMS — Target Management Switch**

- 3.1 Concept and general behaviour.
- 3.2 TMS and Situational Awareness displays.
- 3.3 TMS in Air-to-Air.
- 3.4 TMS in Air-to-Ground.
- 3.5 TMS in A-G weapon employment.
- 3.6 TMS — Block / variant notes.

**4. DMS — Display Management Switch**

- 4.1 Concept and Sensor of Interest (SOI).
- 4.2 DMS Up: HDU Designation as SOI.
- 4.3 DMS Down: Toggle SOI Among Displays.
- 4.4 DMS Left/Right.

**5. CMS — Countermeasures Management Switch**

- 5.1 Concept and interaction with CMDS / ECM / RWR.
- 5.2 CMS Switch Actuation.
- 5.3 CMS — Block and variant notes.

**6. Training References and Practical Flows**

- 6.1 How to use this guide with BMS training missions.
- 6.2 Recommended progression.
- 6.3 Example flows for typical missions.

**7. HOTAS Visual Reference**

- 7.1 F-16 HOTAS overview.
- 7.2 TMS, DMS, CMS diagrams with arrows and labels.

### 3.2 Appendices

- Block / variant overview.
- Tables index.

---

## 4. Layout Parameters

### 4.1 Geometry Configuration (Guide Standard)

- Page: A4 paper.
- Left margin: 2.0 cm.
- Right margin: 2.0 cm.
- Top margin: 2.5 cm.
- Bottom margin: 2.5 cm.
- Available text width: 17.0 cm.
- Standard HOTAS table width: 15.6 cm.
- Line spacing: 1.5× (via `\\onehalfspacing`).

### 4.2 Table Formatting Standard (hotastable)

- Font size: `\\small` (10 pt).
- Row height multiplier: `\\arraystretch = 1.25`.
- Column widths (locked per updated preamble): `L{1.00cm}`, `L{0.90cm}`, `L{0.90cm}`, `L{3.30cm}`, `L{6.40cm}`, `L{1.40cm}`, `L{2.10cm}`.

**Column Layout:**
- **Mode** (1.00 cm): Master mode or state abbreviation (NAV, A-A, A-G).
- **Dir.** (0.90 cm): Direction (Up, Down, Left, Right).
- **Act.** (0.90 cm): Actuation type (Short, Long).
- **Function** (3.30 cm): Concise function name (e.g., "Cycle SOI between MFDs").
- **Effect / Nuance** (6.40 cm): Brief explanation (1-3 sentences) of what happens, interactions, exceptions.
- **Dash34** (1.40 cm): Dash-34 section references using `\\dashref{}`.
- **Train.** (2.10 cm): BMS training mission references using `\\trnref{}` with standardized abbreviations.

---

## 5. Style and Content Rules

### 5.1 General Style

- **Language:** English, neutral and technical, similar to a good community manual.
- **Length:** Most sections 2–4 short paragraphs.
- **Tone:** Explanatory, not conversational.
- **Terminology:** Always define acronyms on first use.

### 5.2 Focus

Focus is always TMS, DMS and CMS. Mention other controls only when strictly needed.

### 5.3 Intro and "How to Read" Sections

The Introduction should clearly explain:

- The unofficial and community-made nature.
- Scope (TMS/DMS/CMS only).
- The role of tables and training-mission references.
- That the visual chapter is a quick reference, not the primary source of truth.

---

## 6. Column Filling Guidelines for hotastable

### 6.1 Column 1: Mode (1.00 cm)

Describe the master mode or state where this action applies. Use structured format:
- A-A CRM
- A-G PRE
- NAV

### 6.2 Column 2: Dir. (0.90 cm)

Use physical directions: Up, Down, Left, Right.

### 6.3 Column 3: Act. (0.90 cm)

Describe press type:
- Short — quick tap (≤0.6 s)
- Long — press >0.6 s

### 6.4 Column 4: Function (3.30 cm)

Provide a short name for what the switch does:
- Bug / designate target
- Break track / CZ
- Cycle SOI between MFDs

### 6.5 Column 5: Effect / Nuance (6.40 cm)

Brief explanation (1–3 sentences) of what happens:
- How state changes
- Interactions with other systems
- Exceptions or conditions

### 6.6 Column 6: Dash34 (1.40 cm)

Reference relevant Dash-34 sections using macros:
- `\\dashref{2.1.5}`
- `\\dashref{2.1.5}, \\dashref{2.7.1}`

### 6.7 Column 7: Train. (2.10 cm)

Link behaviour to BMS training missions using standardized abbreviations (see Training Mission Reference Table v1.0):
- `\\trnref{18 (BARCAP)}`
- `\\trnref{18 (BARCAP)}, \\trnref{28 (SEAD-EW)}`

---

## 7. Rules for the HOTAS Visual Reference Chapter

- All figures are illustrative, not official.
- Style should be schematic, similar to technical drawings.
- Only label TMS, DMS and CMS positions; do not label other buttons.
- Keep diagram text extremely short (a few words per arrow).
- Rely on tables for detailed explanations.

---

## 8. Professional Standards for AI-Assisted Content Development

### 8.1 Communication Principles

1. **Professional rigour** — All analysis must be grounded in primary sources and technical accuracy.
2. **No condescension** — Treat the human author as the subject-matter expert and decision-maker.
3. **Error identification** — When corrected, acknowledge the correction explicitly and explain the flawed reasoning.
4. **Primary source grounding** — All TMS/DMS/CMS claims must be traceable to Dash-34, Dash-1, BMS Training Manual, or BMS User Manual.
5. **Structural integrity** — Analyze organizational changes against actual use cases and operational contexts.
6. **Explicit scope boundaries** — Clearly distinguish between what applies to all blocks/variants vs. specific ones, and what is in scope vs. out of scope.

---

## 9. How to Work With This Brief

- The human author will issue instructions in Portuguese.
- The assistant should generate or modify LaTeX snippets that fit cleanly into the existing template.
- Keep sections, labels and references consistent with this brief.
- Use helper macros and the `hotastable` environment as defined.
- Provide rigorous analysis grounded in primary sources.
- Suggest structural improvements only when grounded in technical analysis and with explicit approval.

---

## 10. Version Control System

This section provides a high-level overview of versioning. The authoritative rules are defined in **VERSION-SYSTEM-v4.2.1**. In case of discrepancy between this brief and that document, Version System v4.2.1 is the single source of truth.

### 10.1 Purpose and Scope

- Ensure the guide and its LaTeX sources use a consistent versioning scheme.
- Provide a quick reference so AI-assisted and human edits do not invent ad-hoc version numbers.
- Clarify how version macros in the LaTeX preamble relate to file names, snapshots, and the project tracking document.

### 10.2 Repository Structure for the Guide

- **Canonical file in repository root:** `guide.tex`
  - This is the file Git/GitHub track as the main history.
  - Always contains the latest accepted version.

- **Versioned snapshots in `wip/guide/`:**
  - For each version, there is a snapshot named:
    ```
    wip/guide/guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex
    ```
  - The snapshot for the active version must be byte-identical to `guide.tex`.

### 10.3 LaTeX Version Macros

The LaTeX preamble must contain:

- `\\newcommand{\\docversion}{...}`
- `\\newcommand{\\docbuild}{YYYYMMDD}`
- `\\newcommand{\\fulldocversion}{\\docversion+\\docbuild}`

These must always match:
- The version in the snapshot file name
- The entry in PROJECT-TRACKING document

### 10.4 Two Regimes: Pre-publication (0.x.x.x) and Post-publication (≥ 1.0)

- **Pre-publication (0.x.x.x):**
  - `MAJOR = 0` always
  - `MINOR` tracks order of chapter integration
  - `PATCH` marks structural changes within chapters
  - `SUBPATCH` records small refinements (typos, wording)

- **Post-publication (≥ 1.0):**
  - `MAJOR` = edition number
  - `MINOR` = significant compatible revisions
  - `PATCH` = local corrections and polish

---

## 11. License & Contributor Rights

### 11.1 Project License

This project and all work contributed to it (guide.tex, WIP files, templates, governance documents) is released under:

**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

**Full license:** https://creativecommons.org/licenses/by-nc/4.0/

### 11.2 What This Means for Contributors

#### You Can Do:

- **Use and Share:** Copy, distribute, print, and share this guide freely
- **Translate:** Translate into other languages (translations also CC BY-NC)
- **Adapt & Integrate:** Use sections within your own works (e.g., include TMS explanation in your tactical guide)
- **Improve:** Create enhanced versions with corrections, additional tables, or new sections

#### You Cannot Do:

- **Monetize:** You cannot sell this guide or any derivative work
- **Claim Ownership:** Derivatives cannot claim official status; must indicate source and original author

#### Attribution Required:

All contributions and derivatives must include:
1. Title: "TMS, DMS, CMS Usage Guide for Falcon BMS"
2. Author: "Carlos 'Metal' Nader"
3. Source: https://github.com/carlos-nader/tms-dms-cms-usage-guide
4. License: "CC BY-NC 4.0" with link to creativecommons.org/licenses/by-nc/4.0/

### 11.3 Contributing Work to This Project

When you create WIP files (sections, tables, visuals, notes) that are integrated into this guide:

- Your contribution becomes part of a CC BY-NC 4.0 work
- You retain authorship credit (metadata blocks capture author/AI indication)
- The project author (Carlos "Metal" Nader) retains responsibility for final accuracy and presentation
- Your work will be accessible and free to the Falcon BMS community

### 11.4 Governance & Tracking

License status and contributor rights are documented in:
- **LICENSE file:** Full CC BY-NC 4.0 legal text (repository root)
- **README.md:** License summary and usage details
- **Guide Section 1.3:** License statement in published guide
- **WIP files metadata:** Author/AI indication in all WIP files
- **PROJECT-TRACKING:** Attribution and copyright notes in session logs

### 11.5 Special Case: Official Versions

The project author (Carlos "Metal" Nader) publishes **official versions** (v1.0.0, v2.0.0, etc.) on GitHub. While the CC BY-NC license permits community members to create enhanced versions, the **official repository** remains the canonical source for the community.

---

## 12. WIP File Template and LaTeX Preamble Architecture

### 12.1 Purpose and Location

All work-in-progress files **MUST** be created by copying and adapting:

```text
TEMPLATES/template-wip-V1.0.tex
```

This ensures:
- Standardized, validated preamble identical to main guide
- Consistent metadata blocks
- Content structures aligned with brief expectations
- Automated or semi-automated integration into guide.tex

**Status:** Template V1.0 updated (29 January 2026) with enhanced preamble architecture (titlesec full hierarchy, optical fixes, professional two-sided layout).

### 12.2 What the Template Provides

1. **Standard preamble** (packages, geometry, macros) identical to `guide.tex`
2. **Metadata block** (non-rendered comments for tracking)
3. **Section/subsection skeleton** with proper hierarchy
4. **Configured hotastable environment** with 7-column HOTAS layout

### 12.3 Preamble Architecture (Updated V1.0)

The preamble in `TEMPLATES/template-wip-V1.0.tex` and `guide.tex` is now organized into the following sections:

#### 12.3.1 Document Class

```latex
\documentclass[11pt, a4paper, twoside]{report}
```

- **`report` class:** Professional multi-chapter documents with chapter-level hierarchy
- **`twoside` option:** Optimized for double-sided printing (alternating header/footer layout)
- **Font size:** 11pt base (readable on screen and print)

#### 12.3.2 Basic Encoding and Language

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
```

- **UTF-8 encoding:** Full Unicode support for international characters
- **T1 font encoding:** Proper hyphenation and accented characters
- **English language:** Hyphenation rules and babel localization

#### 12.3.3 Fonts and Microtypography

```latex
\usepackage{lmodern}
\usepackage{microtype}
```

- **Latin Modern fonts:** High-quality, scalable fonts for screen and print
- **Microtype:** Subtle typographic refinements (character protrusion, font expansion)

#### 12.3.4 Page Geometry and Layout

```latex
\usepackage{geometry}
\geometry{a4paper, left=2.0cm, right=2.0cm, top=2.5cm, bottom=2.5cm}
\usepackage{setspace}
\onehalfspacing
```

- **A4 paper:** International standard (210 × 297 mm)
- **Margins:** Symmetric 2.0 cm left/right, 2.5 cm top/bottom
- **Text width:** 17.0 cm (calculated)
- **Line spacing:** 1.5× for readability

#### 12.3.5 Colors and Links

```latex
\usepackage[table]{xcolor}
\definecolor{linkblue}{HTML}{004488}
\definecolor{linkred}{HTML}{882222}
\definecolor{headerblue}{HTML}{003366}
\definecolor{rowgray}{HTML}{F5F5F5}
\definecolor{subheadgray}{HTML}{E0E0E0}

\usepackage{soul}
\usepackage[pdfencoding=auto, psdextra, colorlinks=true, linkcolor=linkblue, 
            citecolor=linkred, urlcolor=linkblue, breaklinks=true]{hyperref}
\usepackage{bookmark}
\usepackage{caption}
\captionsetup{font=small, labelfont=bf, justification=centering, singlelinecheck=true}
```

- **xcolor[table]:** Color support with table row coloring
- **Custom colors:** Professional palette (linkblue, linkred, headerblue, rowgray, subheadgray)
- **soul:** Text highlighting and underlining
- **hyperref:** Clickable PDF links with custom colors, line-breaking support
- **bookmark:** Enhanced PDF bookmarks
- **caption:** Professional figure/table captions (small font, bold labels, centered)

#### 12.3.6 Headers and Footers (Improved for Two-Sided Layout)

```latex
\usepackage{fancyhdr}
\setlength{\headheight}{25pt} % Increased from 15pt for long chapter names
\pagestyle{fancy}
\fancyhf{} % Clear all
\fancyhead[LO,RE]{\small\textit{\leftmark}} % Outer edge: chapter name
\fancyhead[RO,LE]{\small\thepage}           % Inner edge: page number
\fancyfoot{}                                % No footer
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
```

- **fancyhdr:** Custom header/footer control
- **headheight:** Increased to 25pt (accommodates long chapter names without warnings)
- **Two-sided layout:**
  - **Odd pages (recto):** Chapter name left, page number right
  - **Even pages (verso):** Page number left, chapter name right
- **Header rule:** 0.4pt line separating header from content
- **No footer:** All pagination in header

#### 12.3.7 Chapter Formatting and Spacing (via titlesec)

Complete hierarchy with optical refinements:

```latex
\usepackage{titlesec}
```

| Level | Shape | Font | Spacing (Before/After) | Rationale |
|-------|-------|------|------------------------|-----------|
| **chapter** | display | `\Large\bfseries` | 15pt / 28pt | Maximum prominence; standalone on new line; increased spacing after for visual separation |
| **section** | hang | `\large\bfseries` | 15pt / 8pt | Compact; label left, body indented; reduced spacing for density |
| **subsection** | hang | `\normalsize\bfseries` | 12pt / 6pt | Reduced visual weight; still bold for hierarchy clarity |
| **subsubsection** | hang | `\normalsize\bfseries` | 10pt / 4pt | Compressed spacing for maximum compactness |
| **paragraph** | runin | `\small\bfseries` | 8pt / 1em | **Optical fix:** Small font compensates for bold's "optical illusion" (appears larger); inline with text; added vertical separation (8pt before, 1em after) |
| **subparagraph** | runin | `\small` (no bold) | 8pt / 1em | Less prominence than paragraph; prepared for future use |

**Key innovation:** The `\paragraph` level uses `\small\bfseries` to resolve the "optical illusion" where bold text at normal size appears disproportionately large when inline. Reduced font size + bold achieves visual balance.

**Code example (paragraph level):**

```latex
\titleformat{\paragraph}[runin]
  {\normalfont\small\bfseries} % Format: SMALL + bold (optical compensation)
  {}                            % Label: empty (no numbering)
  {0em}                         % Space between label and body (zero, runin)
  {}                            % Body title (inherits format)
\titlespacing{\paragraph}
  {0pt}  % Left margin (no indent)
  {8pt}  % Space BEFORE title (vertical separation added)
  {1em}  % Space AFTER title (horizontal space after ":")
  [0pt]  % Right margin
```

#### 12.3.8 Tables and Macros

```latex
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage{tabularx}

% Custom Columns
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}

% Macro for Visual Reference Links
\newcommand{\imglink}[1]{\hspace{2pt}\hyperref[#1]{\scriptsize\textbf{[Fig]}}}
```

- **booktabs:** Professional table rules (toprule, midrule, bottomrule)
- **array:** Enhanced column definitions
- **longtable:** Multi-page tables with repeating headers
- **tabularx:** Auto-width columns
- **Custom columns:** `L{width}` (left), `C{width}` (center), `R{width}` (right)
- **imglink macro:** Inline figure references in tables

#### 12.3.9 HOTAS Table Environment (hotastable)

```latex
\newenvironment{hotastable}[1]{%
  \small
  \setlength{\tabcolsep}{2pt}
  \renewcommand{\arraystretch}{1.25}
  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{2.10cm}}
  \caption{#1}\\
  \rowcolor{headerblue}
  \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{2.10cm}}{\textbf{\color{white}Train.}} \\
  \endfirsthead
  \rowcolor{headerblue}
  \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{2.10cm}}{\textbf{\color{white}Train.}} \\
  \endhead
  \multicolumn{7}{r}{\small\emph{Continued on next page}}\\
  \endfoot
  \endlastfoot
}{%
  \end{longtable}
}
```

- **Column widths:** Optimized for 15.6 cm total width (Mode 1.00, Dir. 0.90, Act. 0.90, Function 3.30, Effect/Nuance 6.40, Dash34 1.40, Train. 2.10)
- **Header repeat:** Blue header row repeats on every page (`\endfirsthead`, `\endhead`)
- **Footer:** "Continued on next page" on all but last page
- **Compact spacing:** `\tabcolsep{2pt}`, `\arraystretch{1.25}`

#### 12.3.10 Simple Reference Macros for BMS Docs

```latex
\providecommand{\dashref}[1]{Dash-34~\S~#1}
\providecommand{\dashone}[1]{Dash-1~\S~#1}
\providecommand{\trnref}[1]{TRN~#1}
\providecommand{\trnman}{BMS Training Manual 4.38.1}
\providecommand{\bmsver}{Falcon BMS~4.38.1}
\providecommand{\dashrefs}[1]{\textit{TO 1F-16CMAM-34-1-1}, Dash-34, sections \texttt{#1}}
```

- **dashref:** Dash-34 section references (`\dashref{2.1.5}` → "Dash-34 § 2.1.5")
- **dashone:** Dash-1 section references
- **trnref:** Training mission references (`\trnref{18 (BARCAP)}` → "TRN 18 (BARCAP)")
- **trnman:** Full training manual title
- **bmsver:** BMS version string
- **dashrefs:** Extended Dash-34 citation

#### 12.3.11 Version Control Macros

```latex
\newcommand{\docversion}{0.3.2.0}
\newcommand{\docbuild}{20260119}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{19 January 2026}
\newcommand{\chapterscompletedof}{3/7}
\newcommand{\tablesfilledpct}{Chapter 5 and Chapter 4 - 4.1, 4.2 and 4.3}
\newcommand{\fulldocversion}{\docversion+\docbuild}
```

- **docversion:** Semantic version (MAJOR.MINOR.PATCH.SUBPATCH)
- **docbuild:** Build date (YYYYMMDD)
- **fulldocversion:** Combined version string
- **Progress tracking:** Chapters completed, tables filled status

#### 12.3.12 Graphics

```latex
\usepackage{graphicx}
\graphicspath{{fig/}}
\usepackage{float}
```

- **graphicx:** Image inclusion (`\includegraphics`)
- **graphicspath:** Default directory for figures
- **float:** Enhanced float positioning control (`[H]` for "exactly here")

#### 12.3.13 Title and TOC Configuration

```latex
\title{TMS, DMS and CMS Usage Guide for \bmsver}
\author{Carlos ``Metal'' Nader}
\date{Version \fulldocversion{} | Progress: Chapters \chapterscompletedof{} | 
      Tables \tablesfilledpct{} | January 2026}

\begin{document}
\maketitle
\pagenumbering{roman}
\setcounter{tocdepth}{3}    % Show up to \subsubsection in TOC
\setcounter{secnumdepth}{3} % Number up to \subsubsection
\newpage
\tableofcontents
\newpage
\pagenumbering{arabic}
```

- **Title page:** Auto-generated with version and progress info
- **Roman numerals:** Front matter (title, TOC)
- **TOC depth:** Include up to subsubsection level
- **Numbering:** Up to subsubsection level (1.2.3)
- **Arabic numerals:** Main content chapters

### 12.4 Metadata Block Format

```latex
% ============================================================================
% METADATA BLOCK (non-rendered, for tracking)
% ============================================================================
% Target: Chapter C, Section S, Subsection S
% Status: dev
% Date: YYYY-MM-DD
% Author: AI / Human Name
% Notes: TBD: Table population. Known issues: None.
% Cross-ref: Guide v0.2.2.0, related-section-*.tex
% ============================================================================
```

**Mandatory fields:**
- **Target:** Where in guide structure this WIP belongs
- **Status:** dev → review → final → approved → deprecated
- **Date:** Creation or last-edit date (YYYY-MM-DD)
- **Author:** AI (Session #) or Human Name

---

## 13. How to Create and Integrate WIP Files

### Step 1: Create from Template

```bash
cp TEMPLATES/template-wip-V1.0.tex wip/section-C5-S2-cms-new-dev-2026-01-29.tex
```

### Step 2: Update Metadata Block

- Set Target, Status (dev), Date, Author
- Add development notes

### Step 3: Develop Content

- Replace skeleton sections with actual narrative, tables, etc.
- Use `hotastable` environment for HOTAS tables
- Use reference macros: `\dashref{}`, `\trnref{}`, etc.

### Step 4: Test Compilation

```bash
pdflatex section-C5-S2-cms-new-dev-2026-01-29.tex
```

### Step 5: Workflow

- **dev**: Author working
- **review**: Human review
- **final**: Ready for integration
- **approved**: Integrated into guide, moved to ARCHIVE

---

## 14. Quick Reference: File Naming Convention

**Pattern:** `prefix-C#-S#-title-STATUS-YYYYMMDD.ext`

**Examples:**
- `section-C4-S3-dms-down-review-2026-01-17.tex`
- `table-C5-S2-cms-table-final-2026-01-15.tex`
- `visual-C7-hotas-diagram-dev-2026-01-18.svg`
- `notes-C3-research-questions-2026-01-19.md`

**Status codes:**
- `dev` — Draft
- `review` — Under review
- `final` — Ready for integration
- `approved` — Integrated and archived
- `deprecated` — Intentionally retired

---

## 15. Checklist for Contributors

- [ ] Copy template from TEMPLATES/template-wip-V1.0.tex
- [ ] Follow naming convention
- [ ] Complete metadata block
- [ ] Update Status as work progresses
- [ ] Test LaTeX compilation
- [ ] Provide Dash-34 and training mission references
- [ ] Request review when ready (Status: review)
- [ ] Incorporate feedback
- [ ] Mark final when complete (Status: final)
- [ ] Author integrates and archives

---

**Last Updated:** 2026-01-29, 04:30 PM -03  
**Status:** Ready for use and contribution  
**License:** CC BY-NC 4.0  
**Next Update:** After project phase transitions