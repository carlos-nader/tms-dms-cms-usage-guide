# Falcon BMS TMS/DMS/CMS Guide — WIP File Naming Convention v1.4

## Work-in-Progress File Organization and Nomenclature

**Status:** Official Rule Set (v1.4)  
**Effective Date:** 09 January 2026  
**Applies to:** All isolated chapter, section, table, note, and visual files under development  
**Supersedes:** v1.3  
**Relationship to VERSION-SYSTEM-v4.2.1:** Complementary; does NOT affect main document versioning  
**Relationship to BRIEFING-v0.2.0.0:** Operational rules for files described structurally in BRIEFING Section 11

---

## 0. Introduction and Scope

### 0.1 Purpose

During the development of the TMS/DMS/CMS Guide, content is created and revised in **isolated files** before integration into the main document (`guide-v*.tex`). This specification establishes a **clear, unambiguous naming convention** for all work-in-progress (WIP) files to enable:

- **Quick identification** of file type, target location, and development stage
- **Automatic sorting** by chapter, section, and creation date
- **Audit trail** of structure and progress
- **Efficient workflow** without version-control overhead
- **Predictable automation** of file status transitions and organization

### 0.2 Key Principle

**WIP files do NOT affect the version number of the main document (`guide-v*.tex`).**

Only content integrated into the main file triggers a version bump. WIP filenames are organizational tools, not version markers.

**All WIP files MUST be created from the canonical template:**

```text
TEMPLATES/template-wip-V1.0.tex
```

This ensures preamble consistency, metadata structure, and integration hygiene. The template is versioned independently (currently V1.0) and governed by BRIEFING-v0.2.0.0 Section 11. Never modify the template directly; always copy, rename following Section 2 patterns, and then edit the copy.

### 0.3 Scope

This convention applies to:

- Isolated chapter files (`chapter-*.tex`)
- Isolated section files (`section-*.tex`)
- Table files under development (`table-*.tex`)
- Research notes and snippets (`notes-*.md`)
- Visual assets (diagrams, flowcharts, schematics) (`visual-*.*`)

This convention does **NOT** apply to:

- The main guide file (`guide-v*.tex`) — covered by VERSION-SYSTEM-v4.2.1
- Compiled PDFs or other binary outputs
- Git commit messages or version control metadata
- External reference materials or archived publications
- **The canonical template file** (`TEMPLATES/template-wip-V1.0.tex`) — this is the **structural foundation** that WIP files derive from, not a WIP file itself

### 0.4 File Organization Structure

All WIP files are organized in a dedicated project root structure with a canonical template folder:

```text
project-root/
├── guide-v0.2.2.0-20260108.tex              (MAIN — subject to VERSION-SYSTEM-v4.2.1)
├── PROJECT-TRACKING.md
├── VERSION-SYSTEM-v4.2.1.md
├── WIP-FILE-NAMING-v1.4.md                  (This document)
│
├── TEMPLATES/                               (Canonical templates)
│   └── template-wip-V1.0.tex               (Mandatory starting point for all WIP files)
│
├── WIP/                                     (Active work-in-progress)
│   ├── chapter-*.tex
│   ├── section-*.tex
│   ├── table-*.tex
│   ├── notes-*.md
│   └── visual-*.*
│
└── ARCHIVE/                                 (Completed, deprecated, or integrated)
    ├── section-*-approved-*.tex             (Successfully integrated)
    ├── chapter-*-deprecated-*.tex           (Abandoned or rejected)
    └── guide-v0.*.*..*-*.tex                (Previous main versions)
```

### 0.5 How to Create a New WIP File (Step-by-Step)

All WIP files MUST start from the canonical template. Follow this workflow:

#### Step 1: Copy the Template

Copy the template file from the TEMPLATES folder to the WIP folder with a **temporary name**:

```text
Copy: TEMPLATES/template-wip-V1.0.tex
To: WIP/temporary-wip-file.tex
```

The template is a complete, compilable LaTeX document. This ensures all WIP files inherit:
- Standardized preamble (geometry, packages, macros)
- Metadata block structure (for tracking)
- Pre-configured `hotastable` environment (ready for tables)

#### Step 2: Rename Following Section 2 Patterns

After copying, immediately rename the file using the exact naming pattern for your WIP type:

**For chapters:**
```text
chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex
Example: chapter-C3-tms-target-management-dev-2026-01-09.tex
```

**For sections:**
```text
section-C{N}-S{M}[-S{K}]-{TITLE}-{STATUS}-{DATE}.tex
Example: section-C5-S2-cms-actuation-dev-2026-01-09.tex
```

**For tables:**
```text
table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex
Example: table-C3-AA-TMS-dev-2026-01-09.tex
```

**For notes:**
```text
notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md
Example: notes-C5-cms-structure-outline-2026-01-09.md
```

**For visuals:**
```text
visual-C{N}-{DESCRIPTION}-{TYPE}-{STATUS}-{DATE}.{ext}
Example: visual-C7-tms-hat-layout-diagram-dev-2026-01-09.svg
```

Always start with status `dev` (never started human review).

#### Step 3: Fill Content and Update Status as You Progress

1. **Edit the metadata block** (lines 52–75 in template) to document:
   - Target chapter, section, subsection
   - Current status (`dev` initially)
   - Your notes about what needs to be done

2. **Fill the content:**
   - Write narrative in sections/subsections
   - Populate `hotastable` rows for tables
   - Add visual descriptions or references

3. **Update status in filename as you progress:**
   - `dev` → when first created from template
   - `dev` → `review` when you start human iteration
   - `review` → `final` when you decide "this is solid, no more changes"
   - `final` → `approved` (AI does this after integration into main document)

**Critical rule:** NEVER modify the template file itself. Always copy first, then rename and edit the copy.

---

## 1. Global Naming Rules

### 1.1 Character Set and Encoding

- **Allowed characters:** `a-z`, `0-9`, hyphens (`-`), underscores (for file extension in visuals)
- **Prohibited:** spaces, dots (except file extension), special characters (`@`, `#`, `$`, etc.)
- **Case:** lowercase only
- **Encoding:** UTF-8

### 1.2 Separator Conventions

- **Hyphens (`-`):** Primary separator for all components within filename
- **Dots (`.`):** Reserved for file extension only (e.g., `.tex`, `.md`, `.svg`)
- **No underscores** within the filename body (exception: visual file extensions like `.svg`)

**Example (correct):**

```text
section-C3-S2-S1-fcr-crm-modes-review-2026-01-18.tex
         ↑   ↑   ↑                    ↑       ↑
     hyphens for all separations; dots only for extension
```

**Example (incorrect):**

```text
section_C3.S2.S1_fcr_crm_modes_review_20260118.tex  ❌ (wrong separators)
section-C3.S2.S1-fcr-crm-modes-review-2026-01-18.tex  ❌ (dots in hierarchy confuse file extension)
```

### 1.3 Date Format

All dates in WIP filenames use **ISO 8601 extended format:**

```text
YYYY-MM-DD

Examples:
2026-01-06
2026-01-18
2026-02-05
```

**Not acceptable:**
- `20260106` (compact, not human-readable)
- `01/06/2026` (ambiguous locale)
- `6 Jan 2026` (inconsistent parsing)

### 1.4 Filename Length

- **Maximum filename length:** 255 characters (filesystem limit)
- **Recommended maximum:** 100 characters (for readability and terminal compatibility)
- **Example current max:** `section-C3-S2-S1-fcr-radar-frequency-cuing-in-sam-dt-and-fcr-modes-review-2026-01-18.tex` (~95 chars) ✅

If a filename exceeds 100 characters, **abbreviate the title component** or split into multiple files.

---

## 2. File Categories and Naming Patterns

### 2.1 Category 1: Full Chapter Files

**Purpose:** Complete chapters or major chapter sections under development, scaffolding, or revision before integration into main document.

**Naming Pattern:**

```text
chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex
```

**Components:**

| Component | Format | Description | Example |
|-----------|--------|-------------|---------| 
| `chapter` | fixed prefix | Type identifier (always "chapter") | `chapter` |
| `C{N}` | C + digit 1-7 | Target chapter number | `C1`, `C3`, `C7` |
| `{TITLE}` | slugified string | Descriptive title (lowercase, hyphens for spaces) | `introduction`, `tms-target-management` |
| `{STATUS}` | one of: `dev`, `review`, `final`, `approved`, `deprecated` | Development stage (defined Section 3.1) | `dev`, `review`, `final`, `approved`, `deprecated` |
| `{DATE}` | YYYY-MM-DD | Creation or last-edit date | `2026-01-15`, `2026-01-20` |
| Extension | `.tex` | LaTeX source file | `.tex` |

**Examples:**

```text
chapter-C1-introduction-dev-2026-01-05.tex
chapter-C3-tms-target-management-review-2026-01-20.tex
chapter-C5-cms-countermeasures-final-2026-01-21.tex
chapter-C7-hotas-visual-reference-approved-2026-01-30.tex
```

**Rules:**

1. Chapter number `C{N}` must be 1-7 (matches planned scope).
2. Title must be descriptive (avoid generic names like "draft" or "work").
3. Status is mandatory; no omissions.
4. Date is mandatory; helps track file age.
5. Template must be used as starting point (Section 0.5).

---

### 2.2 Category 2: Section and Subsection Files

**Purpose:** Individual sections or subsections developed in isolation, to be merged into a chapter later.

**Naming Pattern (Section):**

```text
section-C{N}-S{M}-{TITLE}-{STATUS}-{DATE}.tex
```

**Naming Pattern (Subsection):**

```text
section-C{N}-S{M}-S{K}-{TITLE}-{STATUS}-{DATE}.tex
```

**Components:**

| Component | Format | Description | Example |
|-----------|--------|-------------|---------| 
| `section` | fixed prefix | Type identifier | `section` |
| `C{N}` | C + digit 1-7 | Target chapter | `C3`, `C4` |
| `S{M}` | S + digit ≥ 1 | Section number within chapter | `S1`, `S2`, `S3` |
| `[S{K}]` | S + digit ≥ 1 | Optional: subsection number | `S1`, `S2`, `S3` (appears if subsection exists) |
| `{TITLE}` | slugified string | Descriptive title | `fcr-crm-modes`, `soi-definition` |
| `{STATUS}` | one of: `dev`, `review`, `final`, `approved`, `deprecated` | Development stage | `dev`, `review`, `final`, `approved`, `deprecated` |
| `{DATE}` | YYYY-MM-DD | Creation or last-edit date | `2026-01-15` |
| Extension | `.tex` | LaTeX source file | `.tex` |

**Examples:**

```text
section-C3-S1-concept-general-behaviour-dev-2026-01-15.tex
section-C3-S2-fcr-crm-modes-review-2026-01-18.tex
section-C3-S2-S1-fcr-detail-final-2026-01-19.tex
section-C3-S2-S2-sam-approved-2026-01-20.tex
section-C4-S1-soi-definition-dev-2026-01-16.tex
section-C4-S2-S1-mfds-format-selection-review-2026-01-19.tex
```

**Rules:**

1. Chapter number `C{N}` must be 1-7.
2. Section number `S{M}` starts at 1 and increments within chapter.
3. Subsection `S{K}` is **optional**:
   - Omit if file represents a full section.
   - Include if file represents a subsection within a section (e.g., `S2-S1`).
4. Subsection hierarchy can extend further if needed (`S{M}-S{K}-S{L}`), but keep filenames under 100 chars.
5. Status and date mandatory.
6. Template must be used as starting point (Section 0.5).

---

### 2.3 Category 3: Table Files

**Purpose:** HOTAS tables (TMS, DMS, CMS) developed in isolation before embedding in section files.

**Naming Pattern:**

```text
table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex
```

**Components:**

| Component | Format | Description | Example |
|-----------|--------|-------------|---------| 
| `table` | fixed prefix | Type identifier | `table` |
| `C{N}` | C + digit 1-7 | Target chapter | `C3`, `C4`, `C5` |
| `{CONTEXT}` | operational context code | Operational context (A-A, A-G, DGFT, NAV, etc.) | `AA`, `AG`, `DGFT`, `NAV`, `MFDS` |
| `{SWITCH}` | TMS, DMS, or CMS | HOTAS switch/system type | `TMS`, `DMS`, `CMS` |
| `{STATUS}` | one of: `dev`, `review`, `final`, `approved`, `deprecated` | Development stage | `dev`, `review`, `final`, `approved`, `deprecated` |
| `{DATE}` | YYYY-MM-DD | Creation or last-edit date | `2026-01-15` |
| Extension | `.tex` | LaTeX source file | `.tex` |

**Table-Specific Status Codes:**

For tables, status codes indicate fill level and review state:

| Status | Meaning | Typical Use Case |
|--------|---------|------------------| 
| `dev` | Structure defined, rows being populated, never reviewed (0-70% filled) | Ongoing table construction, never seen by human |
| `review` | Table has been reviewed by human, rows being refined (70-99% filled) | In iteration after human feedback |
| `final` | All rows complete, human approval given, ready to integrate (99-100% filled) | Awaiting integration into main document |
| `approved` | Integrated into main document, archived | Historical record |
| `deprecated` | Abandoned, no longer valid (at any fill level) | Alternative approach chosen; kept for audit trail |

**Examples:**

```text
table-C3-AA-TMS-dev-2026-01-15.tex
table-C3-AA-TMS-review-2026-01-19.tex
table-C3-AA-TMS-final-2026-01-20.tex
table-C3-AA-TMS-approved-2026-01-21.tex
table-C3-AG-TMS-dev-2026-01-18.tex
table-C4-MFDS-DMS-review-2026-01-20.tex
table-C5-ALLM-CMS-final-2026-01-22.tex
```

**Rules:**

1. Chapter number `C{N}` identifies target chapter.
2. Context must be recognized operational mode (AA, AG, DGFT, NAV, etc.).
3. Switch must be one of: `TMS`, `DMS`, `CMS`.
4. Multiple tables per chapter-context-switch combination are possible; differentiate by dates and status.
5. Status mandatory; reflects current development stage.
6. Date mandatory; tracks table development timeline.
7. Template must be used as starting point (Section 0.5).

---

### 2.4 Category 4: Notes and Research Files

**Purpose:** Research notes, snippets, outlines, reference compilations, and example collections under development. These are **never part of the main guide**; they support writing and review.

**Naming Pattern:**

```text
notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md
```

**Components:**

| Component | Format | Description | Example |
|-----------|--------|-------------|---------| 
| `notes` | fixed prefix | Type identifier | `notes` |
| `C{N}` | C + digit 1-7, or `GEN` | Target chapter, or `GEN` for cross-chapter | `C3`, `C4`, `GEN` |
| `{TOPIC}` | slugified string | Research or note topic | `fcr-radar-modes`, `dms-soi-logic` |
| `{TYPE}` | one of: `research`, `snippet`, `outline`, `questions`, `reference`, `example` | Type of note (defined below) | `research`, `snippet`, `outline` |
| `{DATE}` | YYYY-MM-DD | Creation date | `2026-01-12` |
| Extension | `.md` | Markdown file (human-readable text) | `.md` |

**Note Types:**

| Type | Purpose | Example |
|------|---------|---------| 
| `research` | Raw research, citations, external references, source material | `notes-C3-fcr-radar-modes-research-2026-01-12.md` |
| `snippet` | Partial paragraphs, draft explanations, early-stage writing | `notes-C4-dms-soi-logic-snippet-2026-01-14.md` |
| `outline` | Detailed outline, structure planning, section breakdown | `notes-C5-cms-structure-outline-2026-01-15.md` |
| `questions` | Open questions, gaps to fill, clarifications needed | `notes-GEN-missing-content-questions-2026-01-16.md` |
| `reference` | Citation compilations, source collections, bibliography | `notes-C3-dash34-references-reference-2026-01-13.md` |
| `example` | Practical examples, test cases, scenario descriptions | `notes-C3-tms-example-scenarios-example-2026-01-17.md` |

**Examples:**

```text
notes-C3-fcr-radar-modes-research-2026-01-12.md
notes-C4-dms-soi-logic-snippet-2026-01-14.md
notes-C5-cms-structure-outline-2026-01-15.md
notes-GEN-missing-content-questions-2026-01-16.md
notes-C3-dash34-references-reference-2026-01-13.md
notes-C3-tms-example-scenarios-example-2026-01-17.md
```

**Rules:**

1. Chapter identifier: use `C1` through `C7` for chapter-specific notes, or `GEN` for general/cross-chapter notes.
2. Topic must be specific (avoid generic names).
3. Type must be one of the six defined types above; no omissions or variations.
4. Date mandatory; helps track note age and relevance.
5. **Status field not used for notes** — notes are always "in progress" until moved to archive.
6. Notes are **never published** as part of the guide; they are **support materials only**.

---

### 2.5 Category 5: Visual and Diagram Files

**Purpose:** Diagrams, flowcharts, schematics, reference cards, illustrations, and other visual assets under development.

**Naming Pattern:**

```text
visual-C{N}-{DESCRIPTION}-{TYPE}-{STATUS}-{DATE}.{ext}
```

**Components:**

| Component | Format | Description | Example |
|-----------|--------|-------------|---------| 
| `visual` | fixed prefix | Type identifier | `visual` |
| `C{N}` | C + digit 1-7 | Target chapter | `C3`, `C7` |
| `{DESCRIPTION}` | slugified string | What the visual shows | `tms-hat-layout`, `radar-mode-flowchart` |
| `{TYPE}` | one of: `diagram`, `flowchart`, `schematic`, `reference`, `illustration` | Visual type (defined below) | `diagram`, `flowchart`, `schematic` |
| `{STATUS}` | one of: `dev`, `review`, `final`, `approved`, `deprecated` | Development stage (visuals use same codes as text) | `dev`, `review`, `final`, `approved`, `deprecated` |
| `{DATE}` | YYYY-MM-DD | Creation or last-edit date | `2026-01-20` |
| `{ext}` | file extension | `.svg`, `.pdf`, `.png`, or `.tex` (for TikZ) | `.svg`, `.pdf`, `.png`, `.tex` |

**Visual Types:**

| Type | Purpose | Typical Format |
|------|---------|----------------| 
| `diagram` | HOTAS switch layout, system architecture, block diagrams | `.svg`, `.pdf` |
| `flowchart` | Decision trees, mode progression, operational flow | `.tex` (TikZ), `.svg`, `.pdf` |
| `schematic` | Detailed system block diagrams, functional architecture | `.svg`, `.pdf` |
| `reference` | Quick-ref cards, checklists, summary sheets | `.pdf`, `.png` |
| `illustration` | Annotated screenshots, example walkthrough, labeled images | `.png`, `.pdf` |

**Visual Status Codes:**

| Status | Meaning | Typical Use |
|--------|---------|-------------| 
| `dev` | Initial sketch, draft layout, structure being defined, never reviewed | In progress, not ready for review |
| `review` | Complete or nearly complete, has been reviewed, undergoing refinement | Design review feedback cycle |
| `final` | Approved by human, no further changes expected | Approved for inclusion in main document |
| `approved` | Integrated into main document, archived | Historical record |
| `deprecated` | Abandoned, no longer valid | Alternative visual chosen; kept for audit trail |

**Examples:**

```text
visual-C7-tms-hat-layout-diagram-dev-2026-01-28.svg
visual-C7-tms-hat-layout-diagram-review-2026-01-29.svg
visual-C7-tms-hat-layout-diagram-final-2026-01-30.svg
visual-C7-tms-hat-layout-diagram-approved-2026-02-02.svg
visual-C3-radar-mode-flowchart-dev-2026-01-20.tex
visual-C4-mfds-organization-schematic-review-2026-01-19.svg
visual-C6-tms-dms-cms-quick-reference-final-2026-01-25.pdf
```

**Rules:**

1. Chapter number identifies the primary chapter where visual will appear.
2. Description should be concise but descriptive.
3. Type must be one of the five defined types.
4. Status must be `dev`, `review`, `final`, `approved`, or `deprecated` (unified with text files).
5. File extension must match the file format (`.svg` for Scalable Vector Graphics, `.pdf` for PDF, `.png` for raster, `.tex` for TikZ diagrams).
   - **Clarification:** `.tex` files in this context are **TikZ diagrams only**, not main document files (those follow VERSION-SYSTEM-v4.2.1).
6. For `.svg` and `.tex` files, maintain source files in WIP folder (preferred for editability).
7. Multiple versions of same visual may exist at different stages; distinguish by date and status.

---

## 2.6 Automation Rules

### 2.6.1 Purpose

Automation rules enable **predictable, algorithmic naming** and **status transitions** without subjective judgment. These rules apply when:

- **AI generates** new files
- **AI modifies** existing files based on feedback
- **Human edits** files and changes status
- **AI integrates** files into main document

### 2.6.2 Decision Tree: Title Slugification

**When AI generates a filename, the `{TITLE}` component must be slugified according to these rules:**

#### Step 1: Input Analysis

```text
Raw input: "Frequency-Cued Radar (FCR) and Cockpit Resource Management (CRM) modes"
Chapter context: C3 (TMS/DMS/CMS Overview)
File type: section
```

#### Step 2: Title Reduction Logic

**Rule: Prefer short, canonical names over exhaustive descriptive lists.**

```text
Decision Tree:

Is there a recognized acronym or short form?
├─ YES: Use it
│  Example: "FCR and CRM modes" → fcr-crm-modes ✅
│
└─ NO: Proceed to Step 3
```

#### Step 3: Multi-Component Reduction

**Rule: Reduce multi-part titles to 2-4 key concepts; prioritize nouns over adjectives.**

```text
Decision Tree:

Count components: {article} {adj} {noun} {prep} {adj} {noun}
├─ ≤ 4 components: Keep all (slugify) → fcr-and-crm-modes
├─ 5-7 components: Keep noun phrases only → fcr-crm-modes ✅ (2 nouns: FCR, CRM + object: modes)
└─ > 7 components: Extract key terms, use abbreviations

Example transformations:
"The comprehensive Frequency-Cued Radar integration in the Tactical Mode Switch"
→ fcr-tactical-mode-switch (3 key terms: FCR, Tactical, ModeSwitch)

"Aircraft defensive systems countermeasure employment for all modes"
→ countermeasure-employment (2 key terms: less redundant)
```

#### Step 4: Acronym and Abbreviation Priority

**Rule: Prefer established acronyms and abbreviations already used in the guide.**

```text
Established acronyms (use these):
- FCR → Frequency-Cued Radar
- CRM → Cockpit Resource Management
- SAM → Surface-to-Air Missile
- DMS → Defensive Management System
- TMS → Tactical Mode Switch
- DCS → Digital Combat Simulation

Do not expand: Use fcr-crm-modes, not frequency-cued-radar-cockpit-resource-modes
```

#### Step 5: Length Check & Abbreviation

**Rule: If slugified title > 30 characters, abbreviate further or split into sub-files.**

```text
Decision Tree:

Length of {TITLE} component:
├─ ≤ 30 chars: ACCEPT
│  Example: fcr-crm-modes (14 chars) ✅
│
├─ 31-50 chars: Abbreviate non-key terms
│  Example: frequency-cued-radar-cockpit-resource-modes (51 chars)
│  → reduce to: fcr-crm-modes (14 chars) ✅
│
└─ > 50 chars: SPLIT into multiple files OR use abbreviations
   Example: "radar-frequency-cuing-in-sam-defensive-terrain-following-modes" (70 chars)
   → Split: 
      section-C3-S2-S1-fcr-sam-integration-dev-2026-01-15.tex (defensive: SAM)
      section-C3-S2-S2-radar-terrain-following-dev-2026-01-15.tex (terrain-following)
```

#### Step 6: Hyphenation & Word Separation

**Rule: Separate distinct concepts with hyphens; keep compound terms together.**

```text
Examples:
✅ fcr-crm-modes (3 concepts: FCR, CRM, modes)
✅ tms-hat-layout (3 concepts: TMS, HAT, layout)
✅ dms-soi-logic (3 concepts: DMS, SOI, logic)
❌ frequency-cued-radar-modes (too granular; use fcr-modes)
❌ fcr_crm_modes (underscores prohibited in body)
```

### 2.6.3 Hierarchy Level Preference (Shallow > Deep)

**Rule: Prefer shallow subsection hierarchies in filenames; use document structure for deeper nesting.**

#### Rationale

```text
Flat filenames:
section-C3-S2-fcr-crm-modes-dev-2026-01-15.tex (66 chars) ✅
section-C3-S2-S1-fcr-detail-dev-2026-01-15.tex (59 chars) ✅
section-C3-S2-S1-S1-mode-behavior-dev-2026-01-15.tex (67 chars) ✅

Deep hierarchies:
section-C3-S2-S1-S1-S1-very-detailed-topic-dev-2026-01-15.tex (75 chars) ❌ (excessive depth)
```

#### Decision Tree: When to Add Subsection Level

```text
Decision Tree:

Does the content fit logically in parent section?
├─ YES: Omit subsection level
│  File: section-C3-S2-fcr-crm-modes-dev-2026-01-15.tex ✅
│
└─ NO: Content is standalone, needs own file
   Does it deserve its own file?
   ├─ YES: Add ONE subsection level
   │  File: section-C3-S2-S1-fcr-detail-dev-2026-01-15.tex ✅
   │
   └─ NO: Keep in parent, mark with subsection in document structure (not filename)
      File: section-C3-S2-fcr-crm-modes-dev-2026-01-15.tex ✅
      (Document structure inside the file shows subsections)
```

#### Preference Rules

```text
1. PREFER ONE LEVEL: section-C3-S2-{TITLE}
   When: Section content is coherent unit

2. ACCEPT TWO LEVELS: section-C3-S2-S1-{TITLE}
   When: Subsection is distinct enough to warrant separate file

3. AVOID THREE+ LEVELS: section-C3-S2-S1-S1-{TITLE}
   When: Document structure shows deeper nesting; filename stays shallow
   Rationale: Keep filename readable; LaTeX \subsubsection handles the rest
```

### 2.6.4 Status Transition Rules

**Status transitions are AUTOMATIC based on file events, not subjective judgment.**

#### Rule Set 1: Status Transition Triggers

```text
┌─────────────────────────────────────────────────────────────┐
│ FILE GENERATION (AI)                                        │
│ → Status: dev                                               │
│ → Reason: Never reviewed by human; untouched                │
│ → Location: WIP/                                            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ FILE MODIFICATION (Human offline work OR AI with feedback)  │
│ → Status: review                                            │
│ → Reason: Human has touched/will touch; in iteration cycle  │
│ → Location: WIP/                                            │
│ → AI Action: If AI modifies, rename file to review          │
│ → Human Action: If human edits, rename locally to review    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ HUMAN APPROVAL (You decide: "This is solid, done iterating")│
│ → Status: final                                             │
│ → Reason: Human confident; ready to integrate when able     │
│ → Location: WIP/                                            │
│ → Human Action: Only human decides; rename to final         │
│ → AI Action: Awaiting integration signal                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ POST-INTEGRATION ARCHIVAL (After AI integrates into guide)  │
│ → Status: approved                                          │
│ → Reason: Successfully integrated; now historical record    │
│ → Location: ARCHIVE/                                        │
│ → Human Action: Move file from WIP/ to ARCHIVE/; rename     │
│ → AI Action: Cannot move folders; document integration done │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DISCARD DURING ITERATION (Human decides not to proceed)     │
│ → Status: deprecated                                        │
│ → Reason: File no longer needed during development cycle    │
│ → Location: ARCHIVE/                                        │
│ → Trigger: review → deprecated                              │
│ → Human Action: Move file from WIP/ to ARCHIVE/; rename     │
│ → AI Action: Document in PROJECT-TRACKING why deprecated    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ DISCARD AFTER FINAL APPROVAL (Human changes mind)           │
│ → Status: deprecated                                        │
│ → Reason: File was ready but human decides not to use       │
│ → Location: ARCHIVE/                                        │
│ → Trigger: final → deprecated                               │
│ → Human Action: Move file from WIP/ to ARCHIVE/; rename     │
│ → AI Action: Document in PROJECT-TRACKING why deprecated    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ EARLY ABANDONMENT (Human rejects before review)             │
│ → Status: deprecated                                        │
│ → Reason: File never reviewed; alternative approach chosen  │
│ → Location: ARCHIVE/                                        │
│ → Trigger: dev → deprecated                                 │
│ → Human Action: Move file from WIP/ to ARCHIVE/; rename     │
│ → AI Action: Document in PROJECT-TRACKING why deprecated    │
└─────────────────────────────────────────────────────────────┘
```

#### Rule Set 2: No Backwards Transitions and Allowed Transitions

**FORBIDDEN transitions (non-regressive):**

```text
FORBIDDEN transitions:
review ↛ dev      (File cannot un-reviewed; stays review through iterations)
final ↛ review    (Final files do not go back; only move forward to approved or deprecated)
approved ↛ any    (Archived files are immutable; create new file if changes needed)
deprecated ↛ any  (Archived files are immutable; create new file if reapproval needed)
```

**ALLOWED transitions:**

```text
ALLOWED transitions:
dev → review          (First touch by human/AI)
review ↔ review       (Multiple iteration cycles stay in review)
review → final        (Human approval for integration into main document)
review → deprecated   (Human decides file is useless during iteration)
final → approved      (After integration & move to ARCHIVE/)
final → deprecated    (If, after being ready to integrate, human decides it's useless & move to ARCHIVE/)
dev → deprecated      (If abandoned before any review & move to ARCHIVE/)
```

#### Rule Set 3: Status Transitions by Actor

**For clarity, each transition is documented with trigger, decision maker, action, and automation level:**

| Transition | Trigger | Decision | Action | Auto? |
|-----------|---------|----------|--------|-------| 
| **dev → review** | File touched by human OR AI modifies it | AI (implicit) | AI renames if modifying; human renames if editing offline | Semi |
| **review → review** | More iterations needed | Human (implicit) | File stays in review; continue editing | Auto |
| **review → final** | Human satisfied, no more iterations | Human (explicit) | Human manually renames to final | Manual |
| **review → deprecated** | Human decides file is useless during iteration | Human (explicit) | Human moves to ARCHIVE/ and renames to deprecated | Manual |
| **final → approved** | File integrated into guide and moved to ARCHIVE/ | Human (explicit) | Human moves file and renames to approved | Manual |
| **final → deprecated** | Human changes mind after final approval | Human (explicit) | Human moves to ARCHIVE/ and renames to deprecated | Manual |
| **dev → deprecated** | File abandoned before any review | Human (explicit) | Human moves to ARCHIVE/ and renames to deprecated | Manual |

### 2.6.5 Automation Responsibility Matrix (v1.4)

**AI and Human responsibilities for WIP file operations:**

| Task | AI Capability | Human Role | Rules & Notes |
|------|-------------|-----------|-----| 
| **Generate new file** | ✅ Can do | N/A | Always `dev` status; use TEMPLATES/template-wip-V1.0.tex as base |
| **Rename to review** | ⚠️ Semi-auto (only when explicitly asked) | ✅ Manual (when you edit) | AI renames ONLY on explicit instructions: "Improve this", "Fix this", "Review and enhance". Human renames locally after offline edits. |
| **Decide final status** | ❌ Cannot do | ✅ Must decide | Only human judges quality; always manual |
| **Decide deprecated status** | ❌ Cannot do | ✅ Must decide | Only human decides to discard (any stage); always manual |
| **Integrate into guide-v*.tex** | ✅ Can do (LaTeX) | ⚠️ Verifies | AI integrates; human verifies correctness |
| **Move to ARCHIVE/** | ❌ Cannot do | ✅ Must do | Human has filesystem access; only human can move folders |
| **Rename to approved** | ❌ Cannot do | ✅ Must do | Human renames after moving to ARCHIVE/ |
| **Mark deprecated** | ❌ Cannot do | ✅ Must do | Human explicitly marks abandoned files at any stage |

### 2.6.6 Title Slugification Examples

| Use Case | Raw Content | Decision | Result |
|----------|------------|----------|-----------| 
| **Simple** | "Frequency-Cued Radar modes" | Use acronym (FCR) | `fcr-modes` ✅ |
| **Multi-acronym** | "FCR and CRM operational integration" | Keep both acronyms + object | `fcr-crm-integration` ✅ |
| **Verbose** | "The tactical employment of defensive systems in terrain-following mode" | Extract nouns (tactical, defensive, terrain-following) | `defensive-terrain-following` ✅ |
| **Compound** | "HOTAS Target Management System (TMS) button layout reference" | Use acronym + key concept | `tms-button-layout` ✅ |
| **Too Long** | "Frequency-Cued Radar Cockpit Resource Management mode selection decision logic flow" | Split into files | `fcr-crm-mode-selection` + `decision-logic-flow` ✅ |
| **Abbreviate** | "Surface-to-Air Missile target prioritization algorithm" | Use acronym + verb + object | `sam-target-prioritization` ✅ |

### 2.6.7 Automation Checklist for AI

**When generating or modifying filenames, verify:**

- ✅ All lowercase  
- ✅ Hyphens separate components; no underscores in body  
- ✅ Date is YYYY-MM-DD format  
- ✅ Status is one of: `dev`, `review`, `final`, `approved`, `deprecated`  
- ✅ Title is 2-4 key concepts maximum (slugified)  
- ✅ Total filename ≤ 100 characters  
- ✅ File type prefix matches content (chapter, section, table, notes, visual)  
- ✅ Chapter/section numbers match document structure  
- ✅ Subsection hierarchy is shallow (prefer C-S over C-S-S-S)  
- ✅ File location matches status:
  - `dev`, `review`, `final` → WIP/
  - `approved`, `deprecated` → ARCHIVE/
- ✅ WIP file created from TEMPLATES/template-wip-V1.0.tex (Section 0.5)

---

## 3. Status Codes and Lifecycle

### 3.1 Status Code Definitions

**Four primary status codes:**

| Status | Location | Meaning | Human Involvement | Next Status |
|--------|----------|---------|-------------------|------------| 
| **`dev`** | WIP/ | Raw, never reviewed | None yet | review |
| **`review`** | WIP/ | Under iteration cycle | Active (multiple cycles possible) | final OR deprecated |
| **`final`** | WIP/ | Approved, ready to integrate | Human decision made | approved (after integration) OR deprecated (if no integration) |
| **`approved`** | ARCHIVE/ | Integrated & archived | Integration complete | (immutable) |

**Auxiliary status code:**

| Status | Location | Meaning | Usage |
|--------|----------|---------|-------| 
| **`deprecated`** | ARCHIVE/ | Abandoned, no longer valid | Alternative approach chosen; kept for audit trail |

### 3.2 Lifecycle Transitions

#### Standard Lifecycle with All Deprecated Paths

```text
                    ┌─────────────┐
                    │   dev       │
                    │  (WIP/)     │
                    └────┬────────┘
                         │
                ┌────────┴────────┐
                │                 │
         (first edit)        (abandon early)
                │                 │
           ┌────▼─────┐    ┌──────▼──────────┐
           │  review  │    │  deprecated     │
           │ (WIP/)   │    │  (ARCHIVE/)     │
           └────┬─────┘    └─────────────────┘
                │          (dev→deprecated)
       ┌────────┼────────┐
       │                 │
  (approve)         (discard during iter)
       │                 │
  ┌────▼──────┐          │
  │   final   │──────────┤
  │  (WIP/)   │          │
  └────┬──────┘          │
       │                 │
 ┌─────┴──────┐    ┌─────▼────────────┐
 │             │    │  deprecated      │
(integrate)  (change mind) │  (ARCHIVE/)      │
 │             │    └──────────────────┘
 │             └────(final→deprecated)
 │
┌▼────────────┐
│   approved  │
│  (ARCHIVE/) │
└─────────────┘
```

#### Scenario 1: Success Path (dev → review → final → approved)

```text
2026-01-15: section-C3-S2-fcr-crm-modes-dev-2026-01-15.tex
            (AI generated from template; never touched by human)

2026-01-18: section-C3-S2-fcr-crm-modes-review-2026-01-18.tex
            (You start working on it; or AI modifies + renames)
            (In WIP/ folder; you make edits)

2026-01-19: (Still in review; multiple edit cycles)
            section-C3-S2-fcr-crm-modes-review-2026-01-19.tex

2026-01-20: section-C3-S2-fcr-crm-modes-final-2026-01-20.tex
            (You: "This is solid. Done iterating.")
            (Still in WIP/)

2026-01-25: You tell AI: "Integrate C3.S2 now"
            AI integrates into guide-v0.2.1.0-2026-01-25.tex

2026-01-26: You verify integration, then:
            Move from WIP/ to ARCHIVE/
            Rename: ARCHIVE/section-C3-S2-fcr-crm-modes-approved-2026-01-26.tex
```

**Key Points:**
- Iteration cycles occur within `review` status
- Only human decides when to advance to `final`
- Only human moves to `ARCHIVE/` and renames to `approved` after integration

#### Scenario 2: Discard During Iteration (review → deprecated)

```text
2026-01-15: section-C3-S2-fcr-alternative-design-dev-2026-01-15.tex
            (AI generated from template)

2026-01-18: section-C3-S2-fcr-alternative-design-review-2026-01-18.tex
            (You start iterating on it)

2026-01-19: section-C3-S2-fcr-alternative-design-review-2026-01-19.tex
            (Multiple edit cycles)

2026-01-21: (After 3 days of work, you realize main approach is better)
            You decide to discard this alternative
            You move to ARCHIVE/ and rename:
            ARCHIVE/section-C3-S2-fcr-alternative-design-deprecated-2026-01-21.tex
            (Document in PROJECT-TRACKING: "Alternative approach abandoned; main version used")
```

**Key Points:**
- File was in iteration but deemed unnecessary
- Discarded DURING development, not after approval
- Transition: `review → deprecated` (human decision)
- Archived for historical reference, clearly marked as not for use

#### Scenario 3: Last-Minute Regret (final → deprecated)

```text
2026-01-20: section-C3-S2-new-radar-modes-final-2026-01-20.tex
            (You approved it: "Ready to integrate")

2026-01-24: (You were planning to integrate, but chapter scope changed)
            You realize this section is no longer needed
            You move to ARCHIVE/ and rename:
            ARCHIVE/section-C3-S2-new-radar-modes-deprecated-2026-01-24.tex
            (Document in PROJECT-TRACKING: "Scope change; section no longer applies")
```

**Key Points:**
- File was `final` (ready for integration)
- But BEFORE integration, human changes mind
- Transition: `final → deprecated` (human decision)
- Prevents unnecessary integration into main document
- Archived with full context for future reference

#### Scenario 4: Early Abandonment (dev → deprecated)

```text
2026-01-15: section-C3-S2-experimental-feature-dev-2026-01-15.tex
            (AI generated from template)

2026-01-15: (Immediately after generation, you review and decide not to pursue)
            You realize this feature is no longer in scope
            You move to ARCHIVE/ and rename:
            ARCHIVE/section-C3-S2-experimental-feature-deprecated-2026-01-15.tex
            (Document in PROJECT-TRACKING: "Experimental feature out of scope; abandoned")
```

**Key Points:**
- File was generated but NEVER edited by human
- Discarded before entering review cycle
- Transition: `dev → deprecated` (rare, but allowed)
- Prevents accumulation of dead files in WIP/
- Archived immediately, never caused iteration overhead

#### Notes Lifecycle (Simplified)

```text
┌──────────┐         ┌──────────┐
│   WIP/   │────────▶│ ARCHIVE/ │
│ (active) │         │  (done)  │
└──────────┘         └──────────┘
(no status change; either in WIP or ARCHIVE)
```

Notes do NOT have status codes in filename. Status is implicit:
- In WIP/ = still useful, might reference later
- In ARCHIVE/ = historical, no longer active

---

## 4. Integration Workflow

### 4.1 When to Move a File to FINAL Status

A WIP file transitions to `final` status when:

1. **Content is structurally complete** — All planned sections/subsections/rows are present.
2. **Content is narratively complete** — Explanations are clear and sufficient; no major gaps remain.
3. **Cross-references verified** — Internal links to other sections, tables, and appendices are checked.
4. **Terminology consistent** — Names of modes, commands, screens, references align with rest of guide.
5. **Technical accuracy confirmed** — References to Dash-1, Dash-34, BMS manuals are verified where applicable.
6. **Human approval given** — You have reviewed and are satisfied; no more iterations needed.

### 4.2 Integration into Main Document

When a WIP file marked `final` is ready to integrate:

1. **You tell AI:** "Ready to integrate [filename]"
2. **AI copies content** from `final` file into appropriate location in `guide-v*.tex`
3. **AI handles LaTeX code:**
   - Cross-references, citations, labels
   - Formatting consistency
   - Package dependencies
4. **AI verifies compilation** — Ensures no new LaTeX errors or warnings
5. **AI updates main document version** — Increment MAJOR, MINOR, or PATCH per VERSION-SYSTEM-v4.2.1
6. **AI updates PROJECT-TRACKING** — Log integration event, date, affected chapter(s)
7. **You verify integration** — Check main document; confirm content looks correct
8. **You move file to ARCHIVE:**
   - Move from `WIP/` to `ARCHIVE/` (you have filesystem access)
   - Rename `final` to `approved`: `ARCHIVE/section-C3-S2-fcr-crm-modes-approved-2026-01-26.tex`

### 4.3 Archival Strategy

**ARCHIVE/ folder contains three types of files:**

1. **Successfully integrated files** (`approved` status)
   - Original WIP file moved here after integration confirmed
   - Kept for audit trail and structure reference
   - Shows what was merged and when

2. **Deprecated or abandoned files** (`deprecated` status)
   - Explicitly marked as rejected or no longer valid
   - Example: alternative approaches not selected
   - Kept for historical reference; clearly marked as not for use

3. **Previous main document versions** — Older `guide-v*.tex` files (per VERSION-SYSTEM-v4.2.1)
   - Frozen snapshots of main document at each version

---

## 5. Quick Reference Table

| File Type | Pattern | Example | Status Codes |
|-----------|---------|---------|--------------| 
| **Chapter** | `chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex` | `chapter-C3-tms-target-management-final-2026-01-20.tex` | dev, review, final, approved, deprecated |
| **Section** | `section-C{N}-S{M}-{TITLE}-{STATUS}-{DATE}.tex` | `section-C3-S2-fcr-crm-modes-review-2026-01-18.tex` | dev, review, final, approved, deprecated |
| **Subsection** | `section-C{N}-S{M}-S{K}-{TITLE}-{STATUS}-{DATE}.tex` | `section-C3-S2-S1-fcr-detail-final-2026-01-19.tex` | dev, review, final, approved, deprecated |
| **Table** | `table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex` | `table-C3-AA-TMS-final-2026-01-21.tex` | dev, review, final, approved, deprecated |
| **Notes** | `notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md` | `notes-C3-fcr-radar-modes-research-2026-01-12.md` | (none; implicit) |
| **Visual** | `visual-C{N}-{DESCRIPTION}-{TYPE}-{STATUS}-{DATE}.{ext}` | `visual-C7-tms-hat-layout-diagram-final-2026-01-30.svg` | dev, review, final, approved, deprecated |

---

## 6. Special Cases and Edge Cases

### 6.1 Multiple Files for Same Content

**Scenario:** Multiple versions of a section exist (e.g., alternative layouts, experimental content).

**Solution:** Create separate files with different titles or dates; do NOT reuse same filename:

```text
section-C3-S2-fcr-crm-modes-final-2026-01-18.tex  (primary version)
section-C3-S2-fcr-crm-modes-alt-layout-review-2026-01-18.tex  (alternative)
```

Mark non-primary versions clearly to avoid confusion. When one version is approved and integrated, the other can be archived with `deprecated` status.

### 6.2 Subsection Hierarchy Exceeding Three Levels

**Scenario:** Content requires sub-sub-subsections (rare).

**Solution:** Extend the pattern as needed, but keep total filename under 100 characters:

```text
section-C3-S2-S1-S1-very-detailed-topic-review-2026-01-20.tex  (~83 chars) ✅
```

Rationale: Document structure (inside the file) shows additional nesting; filename shows top-level hierarchy.

### 6.3 Table with Very Long Context or Descriptors

**Scenario:** Context code or table name is long (e.g., "WEAPON-EMPLOYMENT-AND-SPECIAL-MODES").

**Solution:** Use abbreviations or acronyms:

```text
❌ table-C3-WEAPON-EMPLOYMENT-AND-SPECIAL-MODES-TMS-dev-2026-01-15.tex  (too long)
✅ table-C3-WASM-TMS-dev-2026-01-15.tex  (abbreviate)
```

Or split into multiple focused tables:

```text
table-C3-weapon-employment-TMS-dev-2026-01-15.tex
table-C3-special-modes-TMS-dev-2026-01-15.tex
```

### 6.4 Cross-Chapter Content

**Scenario:** A section or note spans multiple chapters (e.g., "HOTAS Principles" applies to TMS, DMS, and CMS).

**Solution:** File primary location and reference others:

```text
section-C2-S1-hotas-principles-general-dev-2026-01-12.tex  (primary)
notes-GEN-hotas-cross-chapter-reference-2026-01-12.md      (reference note)
```

Or create chapter-specific versions:

```text
section-C2-S1-hotas-principles-general-dev-2026-01-12.tex
section-C3-S1-hotas-principles-tms-context-dev-2026-01-12.tex
section-C4-S1-hotas-principles-dms-context-dev-2026-01-12.tex
section-C5-S1-hotas-principles-cms-context-dev-2026-01-12.tex
```

### 6.5 When to Split a Long File into Multiple Files

**Scenario:** A section file grows very large (> 3000 lines or > 2000 words).

**Solution:** Split logically into subsections:

```text
OLD (too large):
section-C3-S2-fcr-crm-comprehensive-guide-dev-2026-01-15.tex  (3500 lines)

NEW (split):
section-C3-S2-S1-fcr-concept-dev-2026-01-15.tex
section-C3-S2-S2-fcr-modes-detail-dev-2026-01-15.tex
section-C3-S2-S3-crm-integration-dev-2026-01-15.tex
```

Rationale: Smaller files are easier to iterate, review, and integrate independently.

---

## 7. Compliance Checklist

### 7.1 General Checklist (All File Types)

Before considering a WIP file valid under this convention:

- Filename follows correct pattern (correct prefixes, separators, date format)
- Status is one of the allowed codes (`dev`, `review`, `final`, `approved`, `deprecated`)
- Date is ISO 8601 format (`YYYY-MM-DD`)
- No spaces or prohibited characters in filename
- All lowercase
- File saved in `WIP/` folder (or `ARCHIVE/` if `approved`/`deprecated`)
- File extension matches file type (`.tex` for LaTeX, `.md` for Markdown, `.svg` for vectors, etc.)
- Title is slugified (hyphens between words, 2–4 key concepts max)
- File created from TEMPLATES/template-wip-V1.0.tex (Section 0.5)

### 7.2 Integration Checklist (Before Moving to APPROVED)

Only move a file to `approved` (and ARCHIVE/) when:

- AI has integrated content into main document
- LaTeX compiles without errors
- Cross-references updated in main document
- Main document version bumped per VERSION-SYSTEM-v4.2.1
- PROJECT-TRACKING updated with integration event
- You have verified integration looks correct
- Original file moved from `WIP/` to `ARCHIVE/`
- File renamed from `final` to `approved` in `ARCHIVE/`

---

## 8. Relationship to VERSION-SYSTEM-v4.2.1 and BRIEFING-v0.2.0.0

This WIP File Naming Convention is **complementary** to both VERSION-SYSTEM-v4.2 and BRIEFING-v0.2.0.0, not a replacement.

| Document | Responsibility |
|----------|----------------| 
| `VERSION-SYSTEM-v4.2.1` | Defines version numbering for main document `guide-v*.tex` |
| `BRIEFING-v0.2.0.0` (Section 11) | Specifies structure, preamble, and configuration of `TEMPLATES/template-wip-V1.0.tex` |
| `WIP File Naming v1.4` | Defines **operational** organization and **status tracking** for isolated WIP files; explains how to **use** the template |

**Key integration points:**

1. **Template as mandatory foundation** — All WIP files created from TEMPLATES/template-wip-V1.0.tex per BRIEFING Section 11 and WIP-NAMING Section 0.5.
2. **No version bumps from WIP files** — Only content merged into main document triggers version increments per VERSION-SYSTEM-v4.2.1.
3. **Integration workflow** — When WIP file marked `final` is integrated by AI, main document version increments per VERSION-SYSTEM-v4.2.1 rules.
4. **PROJECT-TRACKING** — All three systems feed into `PROJECT-TRACKING.md` for unified project history.
5. **AI Responsibility** — AI handles LaTeX integration, version bumping, and file naming per this convention; human verifies and makes approval decisions.

---

## 9. Summary and Best Practices

### 9.1 Summary of Key Rules

1. Use **canonical template** — All WIP files start from TEMPLATES/template-wip-V1.0.tex (Section 0.5).
2. Use **flat WIP folder** — No subfolders; type-prefixed filenames provide structure.
3. **Mandatory fields** — All filenames must include type prefix, chapter/topic identifier, descriptive title, status, and date.
4. **Status is explicit** — Always include one of the defined status codes; no ambiguity.
5. **Dates are ISO 8601** — Ensures sortability and eliminates ambiguity.
6. **Hyphens only** — No dots except file extension, no spaces, no special characters.
7. **Hierarchy in filename** — Sections show `C3-S2-S1` notation; subsection numbers explicit in filename.
8. **Shallow hierarchies preferred** — Use document structure for deeper nesting; filenames stay readable.
9. **Automation is algorithmic** — Status transitions based on events, not subjective judgment.
10. **Human controls approval** — Only humans decide final status; only humans move files to `approved`.

### 9.2 Best Practices for Workflow

1. Use descriptive, concise titles — Avoid generic names; make filenames self-documenting. Slugify aggressively (2–4 key concepts).
2. Update status regularly — As file evolves (`dev` → `review` → `final`), rename to reflect current state.
3. Archive on integration — Move successfully merged files to `ARCHIVE/` to keep `WIP/` tidy and uncluttered.
4. Use `PROJECT-TRACKING` — Log integration events, abandonment reasons, major milestones.
5. Date represents last edit — Keep date current; update when making significant changes to a file.
6. Respect status immutability — Files cannot go backwards (`review` never goes back to `dev`; `final` never back to `review`).
7. **Start from template** — Always copy TEMPLATES/template-wip-V1.0.tex before creating new WIP files; never edit template directly.

---

## 10. Version History

| Version | Date & Time (UTC-3) | Type | Changes |
|---------|----------------------|------|---------| 
| **v1.0** | 07 Jan 2026, 00:00 | Initial release | Defines five file categories, four status codes, integration workflow. |
| **v1.1** | 07 Jan 2026, 01:30 | MAJOR UPDATE | Added Section 2.6 Automation Rules; clarified status transitions (`dev`→`review`→`final`→`approved`/`deprecated`); added decision trees for title slugification; clarified hierarchy preference; added automation responsibility matrix; unified status codes across all file types. |
| **v1.2** | 07 Jan 2026, 01:50 | MINOR UPDATE | Expanded status transitions; added three independent deprecated paths (`review`→`deprecated`, `final`→`deprecated`, `dev`→`deprecated`); updated Section 2.6.4 Status Transitions by Actor with 7 explicit transitions; updated Section 3.2 Lifecycle Transitions with expanded ASCII diagram and four complete scenario timelines (Success, Discard During Iteration, Last-Minute Regret, Early Abandonment); clarified human decision points and automation boundaries for deprecation at all file lifecycle stages. |
| **v1.3** | 07 Jan 2026, 03:04 | PATCH UPDATE | Fixed separator rule typo in Section 1.2; clarified in Section 2.5 that `.tex` files in visuals are TikZ diagrams only; corrected Section 2.6.5 Automation Responsibility Matrix so that AI renames `dev→review` only when explicitly instructed by human; reformatted tables for improved clarity and legibility. |
| **v1.4** | 09 Jan 2026, 05:52 | MINOR UPDATE | **NEW Section 0.5: "How to Create a New WIP File (Step-by-Step)"** — Mandatory workflow explaining template use (copy, rename, fill content); **UPDATED Section 0.2** — Added key principle about canonical template requirement; **UPDATED Section 0.3** — Clarified template is not a WIP file (it's the foundation); **UPDATED Section 0.4** — Added `TEMPLATES/` folder with template location; **UPDATED all references** BRIEFING-v0.1.4.1 → BRIEFING-v0.2.0.0; **UPDATED Section 2.6.5** — Added mandatory template requirement to automation checklist; **UPDATED Relationship section** — Added explicit link to BRIEFING-v0.2.0.0 Section 11; **ADDED to all file categories** — Template requirement in rules; **Version bump rationale:** Template establishment is a governance expansion (MINOR, not PATCH). |

---

**Document Status:** Production-Ready (v1.4)  
**Effective Date:** 09 January 2026  
**Last Updated:** 09 January 2026, 05:52 -03  
**Version:** v1.4