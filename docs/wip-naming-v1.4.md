---
layout: default
title: "WIP File Naming Convention"
sitemap:
  priority: 0.2
  changefreq: monthly
---
{% raw %}

# Falcon BMS TMS/DMS/CMS Guide — WIP File Naming Convention v1.4

## Work-in-Progress File Organization and Nomenclature

**Status:** Official Rule Set (v1.4)  
**Effective Date:** 03 February 2026  
**Applies to:** All isolated chapter, section, table, note, and visual files under development  
**Relationship to VERSION-SYSTEM:** Complementary; does NOT affect main document versioning  
**Relationship to BRIEFING:** Operational rules for files described structurally in BRIEFING Section 11

---

## 0. Introduction and Scope

### 0.1 Purpose

During the development of the TMS/DMS/CMS Guide, content is created and revised in **isolated files** before integration into the main document (`guide.tex`). This specification establishes a **clear, unambiguous naming convention** for all work-in-progress (WIP) files to enable:

- **Quick identification** of file type, target location, and development stage
- **Automatic sorting** by chapter, section, and creation date
- **Audit trail** of structure and progress
- **Efficient workflow** without version-control overhead
- **Predictable automation** of file status transitions and organization

### 0.2 Key Principles

**WIP files do NOT affect the version number of the main document (`guide.tex`).**

Only content integrated into the main file triggers a version bump. WIP filenames are organizational tools, not version markers.

**All WIP files MUST be created from the canonical template:**

```text
template/template-wip-V1.0.tex
```

This ensures preamble consistency, metadata structure, and integration hygiene. The template is versioned independently (currently V1.0) and governed by BRIEFING Section 11. Never modify the template directly; always copy, rename following Section 2 patterns, and then edit the copy.

**Human controls integration.** The human author is responsible for integrating WIP content into the guide snapshot. AI assists with content creation and review, but does not perform the actual integration.

### 0.3 Scope

This convention applies to:

- Isolated chapter files (`chapter-*.tex`) — including consolidated chapters
- Isolated section files (`section-*.tex`)
- Table files under development (`table-*.tex`)
- Research notes and snippets (`notes-*.md`)
- Visual assets (diagrams, flowcharts, schematics) (`visual-*.*`)

This convention does **NOT** apply to:

- The main guide file (`guide.tex`) — covered by VERSION-SYSTEM
- Guide snapshots (`wip/guide/guide-v*.tex`) — covered by VERSION-SYSTEM
- Compiled PDFs or other binary outputs
- Git commit messages or version control metadata
- External reference materials or archived publications
- **The canonical template file** (`template/template-wip-V1.0.tex`) — this is the **structural foundation** that WIP files derive from, not a WIP file itself

### 0.4 File Organization Structure

All WIP files are organized in a dedicated project structure:

```text
project-root/
├── guide.tex                        (CANONICAL — subject to VERSION-SYSTEM)
│
├── docs/                            (Project governance documents)
│   ├── project-tracking-v*.md
│   ├── version-system-v*.md
│   ├── wip-naming-v*.md             (This document)
│   └── briefing-v*.md
│
├── template/                       (Canonical templates)
│   └── template-wip-V1.0.tex        (Mandatory starting point for all WIP files)
│
├── wip/                             (Active work-in-progress)
│   ├── chapter-*.tex                (Chapter WIP files)
│   ├── section-*.tex                (Section WIP files)
│   ├── table-*.tex                  (Table WIP files)
│   ├── notes-*.md                   (Research notes)
│   ├── visual-*.*                   (Visual assets)
│   │
│   └── guide/                       (Guide snapshots — VERSION-SYSTEM)
│       └── guide-v*.tex             (Current active snapshot)
│
└── archive/                         (Completed, deprecated, or historical)
    ├── GUIDE/                       (Previous guide snapshots)
    │   └── guide-v*.tex
    │
    └── WIP/                         (Integrated or deprecated WIP files)
        ├── section-*-approved-*.tex
        └── chapter-*-deprecated-*.tex
```

**Key points:**
- Lowercase for first-level folders (`wip/`, `archive/`, `docs/`, `template/`)
- Uppercase for archive subfolders (`GUIDE/`, `WIP/`)
- Only one active snapshot in `wip/guide/` at a time
- All previous snapshots archived in `archive/GUIDE/`

### 0.5 How to Create a New WIP File (Step-by-Step)

All WIP files MUST start from the canonical template. Follow this workflow:

#### Step 1: Copy the Template

Copy the template file from the templates folder to the wip folder:

```text
Copy: template/template-wip-V1.0.tex
To:   wip/[temporary-name].tex
```

The template is a complete, compilable LaTeX document. This ensures all WIP files inherit:
- Standardized preamble (geometry, packages, macros)
- Metadata block structure (for tracking)
- Pre-configured `hotastable` environment (ready for tables)

#### Step 2: Rename Following Section 2 Patterns

After copying, immediately rename the file using the exact naming pattern for your WIP type:

| Type | Pattern | Example |
|------|---------|---------|
| Chapter | `chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex` | `chapter-C3-tms-dev-2026-01-09.tex` |
| Section | `section-C{N}-S{M}-{TITLE}-{STATUS}-{DATE}.tex` | `section-C5-S2-cms-actuation-dev-2026-01-09.tex` |
| Table | `table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex` | `table-C3-AA-TMS-dev-2026-01-09.tex` |
| Notes | `notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md` | `notes-C5-cms-structure-outline-2026-01-09.md` |
| Visual | `visual-C{N}-{DESC}-{TYPE}-{STATUS}-{DATE}.{ext}` | `visual-C7-tms-hat-diagram-dev-2026-01-09.svg` |

Always start with status `dev` (never reviewed by human).

#### Step 3: Fill Content and Update Status as You Progress

1. **Edit the metadata block** to document target chapter, section, and status.

2. **Fill the content:** Write narrative, populate tables, add visuals.

3. **Update status in filename as you progress:**
   - `dev` → when first created from template
   - `review` → when human begins iteration
   - `final` → when human decides "this is solid, ready to integrate"
   - `approved` → after human integrates into guide (move to `archive/WIP/`)

**Critical rule:** NEVER modify the template file itself. Always copy first, then rename and edit the copy.

---

## 1. Global Naming Rules

### 1.1 Character Set

- **Allowed:** `a-z`, `0-9`, hyphens (`-`)
- **Prohibited:** spaces, dots (except extension), special characters (`@`, `#`, `$`, `_` in body)
- **Case:** lowercase only
- **Encoding:** UTF-8

### 1.2 Separators

- **Hyphens (`-`):** Primary separator for all components
- **Dots (`.`):** Reserved for file extension only

```text
✅ section-C3-S2-fcr-crm-modes-review-2026-01-18.tex
❌ section_C3.S2_fcr_crm_modes_review_20260118.tex
```

### 1.3 Date Format

All dates use **ISO 8601 extended format:** `YYYY-MM-DD`

```text
✅ 2026-01-18
❌ 20260118, 01/18/2026, 18 Jan 2026
```

### 1.4 Filename Length

- **Maximum:** 100 characters (recommended for readability)
- If exceeding, abbreviate the title or split into multiple files

---

## 2. File Categories and Naming Patterns

### 2.1 Chapter Files

**Purpose:** Complete chapters under development, including consolidated chapters that combine multiple sections.

**Pattern:**
```text
chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex
```

**Examples:**
```text
chapter-C1-introduction-dev-2026-01-05.tex
chapter-C4-dms-final-2026-02-01.tex
chapter-C5-cms-countermeasures-approved-2026-01-21.tex
```

**Consolidated Chapter Pattern:**

When developing a chapter, you may either:
1. **Work section-by-section:** Create individual `section-C{N}-S{M}-*.tex` files, then integrate each into the guide
2. **Work as consolidated chapter:** Create a single `chapter-C{N}-*.tex` file containing all sections

The consolidated approach is preferred when:
- Multiple sections are ready for review together
- Sections have strong interdependencies
- You want to review chapter flow as a whole

**Example workflow (C4 DMS):**
```text
# Individual sections developed first:
section-C4-S1-concept-soi-final-2026-01-14.tex
section-C4-S2-dms-up-final-2026-01-14.tex
section-C4-S3-dms-down-final-2026-01-18.tex
section-C4-S4-dms-left-right-final-2026-01-21.tex

# Then consolidated for final review:
chapter-C4-dms-review-2026-01-30.tex  (contains all sections)
chapter-C4-dms-final-2026-02-01.tex   (ready for integration)
```

### 2.2 Section Files

**Purpose:** Individual sections developed in isolation, to be merged into a chapter or guide.

**Pattern:**
```text
section-C{N}-S{M}-{TITLE}-{STATUS}-{DATE}.tex
section-C{N}-S{M}-S{K}-{TITLE}-{STATUS}-{DATE}.tex  (subsection)
```

**Examples:**
```text
section-C3-S1-concept-general-behaviour-dev-2026-01-15.tex
section-C3-S2-fcr-crm-modes-review-2026-01-18.tex
section-C4-S2-S1-mfds-format-selection-final-2026-01-19.tex
```

**Hierarchy preference:** Keep filenames shallow (max 2 levels: `C{N}-S{M}-S{K}`). Use document structure inside the file for deeper nesting.

### 2.3 Table Files

**Purpose:** HOTAS tables (TMS, DMS, CMS) developed in isolation.

**Pattern:**
```text
table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex
```

**Context codes:** `AA` (Air-to-Air), `AG` (Air-to-Ground), `DGFT` (Dogfight), `NAV` (Navigation), `MFDS` (MFD/SOI), `ALLM` (All Modes)

**Examples:**
```text
table-C3-AA-TMS-dev-2026-01-15.tex
table-C4-MFDS-DMS-review-2026-01-20.tex
table-C5-ALLM-CMS-final-2026-01-22.tex
```

### 2.4 Notes Files

**Purpose:** Research notes, outlines, reference compilations. Never published; support materials only.

**Pattern:**
```text
notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md
```

**Types:** `research`, `snippet`, `outline`, `questions`, `reference`, `example`

**Examples:**
```text
notes-C3-fcr-radar-modes-research-2026-01-12.md
notes-C5-cms-structure-outline-2026-01-15.md
notes-GEN-missing-content-questions-2026-01-16.md
```

**Note:** Notes do NOT have status codes — they're either in `wip/` (active) or `archive/WIP/` (historical).

### 2.5 Visual Files

**Purpose:** Diagrams, flowcharts, schematics, reference cards.

**Pattern:**
```text
visual-C{N}-{DESCRIPTION}-{TYPE}-{STATUS}-{DATE}.{ext}
```

**Types:** `diagram`, `flowchart`, `schematic`, `reference`, `illustration`

**Extensions:** `.svg` (preferred), `.pdf`, `.png`, `.tex` (TikZ only)

**Examples:**
```text
visual-C7-tms-hat-layout-diagram-dev-2026-01-28.svg
visual-C3-radar-mode-flowchart-final-2026-01-20.tex
visual-C6-quick-reference-card-review-2026-01-25.pdf
```

### 2.6 Title Slugification Rules

When creating filenames, convert descriptive titles to slugs:

| Rule | Example |
|------|---------|
| Use established acronyms | "Frequency-Cued Radar" → `fcr` |
| Keep 2-4 key concepts | "FCR and CRM operational integration" → `fcr-crm-integration` |
| Max ~30 characters for title | Abbreviate or split if longer |
| Lowercase, hyphens only | `fcr-crm-modes` ✅, `FCR_CRM_Modes` ❌ |

**Established acronyms:** FCR, CRM, SAM, DMS, TMS, CMS, SOI, MFD, HUD, RWR, CMDS, ECM

---

## 3. Status Codes and Lifecycle

### 3.1 Status Definitions

| Status | Location | Meaning | Next Status |
|--------|----------|---------|-------------|
| `dev` | `wip/` | Never reviewed by human | `review` or `deprecated` |
| `review` | `wip/` | Under human iteration | `final` or `deprecated` |
| `final` | `wip/` | Approved, ready to integrate | `approved` or `deprecated` |
| `approved` | `archive/WIP/` | Integrated into guide | (terminal) |
| `deprecated` | `archive/WIP/` | Abandoned | (terminal) |

### 3.2 Lifecycle Diagram

```text
                    ┌─────────┐
                    │   dev   │
                    │ (wip/)  │
                    └────┬────┘
                         │
              ┌──────────┼──────────┐
              │                     │
       (human review)          (abandon)
              │                     │
         ┌────▼────┐          ┌─────▼──────┐
         │ review  │          │ deprecated │
         │ (wip/)  │          │(archive/WIP)│
         └────┬────┘          └────────────┘
              │
    ┌─────────┼─────────┐
    │                   │
(approve)          (discard)
    │                   │
┌───▼───┐         ┌─────▼──────┐
│ final │         │ deprecated │
│(wip/) │         │(archive/WIP)│
└───┬───┘         └────────────┘
    │
    ├───────────────┐
    │               │
(integrate)    (change mind)
    │               │
┌───▼─────┐   ┌─────▼──────┐
│approved │   │ deprecated │
│(archive/│   │(archive/WIP)│
│  WIP/)  │   └────────────┘
└─────────┘
```

### 3.3 Transition Rules

**Allowed:**
- `dev → review` (human begins work)
- `dev → deprecated` (abandon before review)
- `review → review` (continue iteration — update date)
- `review → final` (human approves)
- `review → deprecated` (discard during iteration)
- `final → approved` (after integration)
- `final → deprecated` (change mind before integration)

**Forbidden:**
- `review → dev` (cannot un-review)
- `final → review` (cannot un-approve)
- `approved → any` (terminal, immutable)
- `deprecated → any` (terminal, immutable)

### 3.4 Success Path Example

```text
2026-01-15: section-C3-S2-fcr-crm-modes-dev-2026-01-15.tex
            (AI generates from template)

2026-01-18: section-C3-S2-fcr-crm-modes-review-2026-01-18.tex
            (Human begins editing)

2026-01-20: section-C3-S2-fcr-crm-modes-final-2026-01-20.tex
            (Human: "Ready to integrate")

2026-01-25: Human integrates content into guide snapshot
            Human moves file to archive/WIP/ and renames:
            archive/WIP/section-C3-S2-fcr-crm-modes-approved-2026-01-25.tex
```

---

## 4. Integration Workflow

### 4.1 When to Mark FINAL

A WIP file transitions to `final` when:

1. Content is structurally complete
2. Content is narratively complete
3. Cross-references verified
4. Terminology consistent with rest of guide
5. Technical accuracy confirmed against sources
6. Human is satisfied — no more iterations needed

### 4.2 Integration into Main Document

**Human is responsible for integration.** AI assists with content creation and review but does not perform integration.

**Workflow:**

1. **Human decides:** "Ready to integrate [filename]"
2. **Human copies content** from `final` WIP file into the guide snapshot (`wip/guide/guide-v*.tex`)
3. **Human handles LaTeX:** cross-references, labels, formatting
4. **Human compiles** and verifies no errors
5. **Human updates version** per VERSION-SYSTEM:
   - Update `\docversion` and `\docbuild` macros
   - Save new snapshot in `wip/guide/`
   - Copy snapshot to `guide.tex` (repository root)
   - Move previous snapshot to `archive/GUIDE/`
6. **Human updates PROJECT-TRACKING** with integration event
7. **Human creates GitHub tag and release** (see Section 5)
8. **Human archives WIP file:**
   - Move from `wip/` to `archive/WIP/`
   - Rename `final` → `approved`

### 4.3 Archival

**`archive/WIP/` contains:**
- `*-approved-*.tex` — successfully integrated files
- `*-deprecated-*.tex` — abandoned files (kept for audit trail)

**`archive/GUIDE/` contains:**
- Previous guide snapshots (`guide-v*.tex`)

---

## 5. GitHub Integration

WIP files integrate with GitHub's project management features:

### 5.1 Issues

- Each significant WIP file can have a corresponding GitHub Issue
- Issue tracks development progress, review feedback, blockers
- Issue title matches WIP purpose: "C4:S4 — DMS Left/Right"
- Issue is closed when WIP content is integrated

### 5.2 Milestones

- Milestones group issues toward a release target
- Milestone name matches version: "v0.3.3.0", "v0.4.0.0"
- When all milestone issues are closed → release is ready

### 5.3 Workflow

```text
Issue created → WIP file created (dev)
      ↓
Issue updated → WIP iterated (review)
      ↓
Issue ready → WIP approved (final)
      ↓
Integration → Tag + Release → Close Issue → Close Milestone (if complete)
```

---

## 6. Responsibility Matrix

| Task | AI | Human |
|------|-----|-------|
| Generate new WIP file from template | ✅ Can do | — |
| Rename `dev → review` | ⚠️ Only when instructed | ✅ When editing offline |
| Content creation and revision | ✅ Can do | ✅ Can do |
| Decide `review → final` | ❌ Cannot | ✅ Must decide |
| Decide `→ deprecated` | ❌ Cannot | ✅ Must decide |
| Integrate into guide snapshot | ❌ Cannot | ✅ Must do |
| Update guide version | ❌ Cannot | ✅ Must do |
| Move files to `archive/` | ❌ Cannot | ✅ Must do |
| Rename to `approved` | ❌ Cannot | ✅ Must do |
| Create GitHub tag/release | ❌ Cannot | ✅ Must do |
| Update PROJECT-TRACKING | ✅ Can propose | ✅ Must verify/commit |

---

## 7. Quick Reference

### 7.1 Naming Patterns

| Type | Pattern |
|------|---------|
| Chapter | `chapter-C{N}-{title}-{status}-{date}.tex` |
| Section | `section-C{N}-S{M}-{title}-{status}-{date}.tex` |
| Table | `table-C{N}-{context}-{switch}-{status}-{date}.tex` |
| Notes | `notes-C{N}-{topic}-{type}-{date}.md` |
| Visual | `visual-C{N}-{desc}-{type}-{status}-{date}.{ext}` |

### 7.2 Status Codes

| Status | Location | Meaning |
|--------|----------|---------|
| `dev` | `wip/` | Never reviewed |
| `review` | `wip/` | Under iteration |
| `final` | `wip/` | Ready to integrate |
| `approved` | `archive/WIP/` | Integrated |
| `deprecated` | `archive/WIP/` | Abandoned |

### 7.3 Folder Structure

| Path | Contents |
|------|----------|
| `wip/` | Active WIP files |
| `wip/guide/` | Current guide snapshot |
| `archive/WIP/` | Integrated/deprecated WIP files |
| `archive/GUIDE/` | Previous guide snapshots |
| `template/` | Canonical WIP template |

### 7.4 Checklist for AI

When generating filenames, verify:
- ✅ All lowercase
- ✅ Hyphens separate components
- ✅ Date is YYYY-MM-DD
- ✅ Status is valid (`dev`, `review`, `final`, `approved`, `deprecated`)
- ✅ Title is 2-4 key concepts (slugified)
- ✅ Total filename ≤ 100 characters
- ✅ File created from `template/template-wip-V1.0.tex`

---

## 8. Relationship to Other Documents

| Document | Responsibility |
|----------|----------------|
| **VERSION-SYSTEM** | Version numbering for `guide.tex` and snapshots |
| **BRIEFING** | Template structure, preamble architecture, layout standards |
| **WIP-FILE-NAMING-v1.4** | WIP file naming, status tracking, integration workflow |
| **PROJECT-TRACKING** | Session log, project state, development history |

**Integration points:**
1. All WIP files start from template (per BRIEFING Section 11)
2. WIP files don't bump versions — only integration does (per VERSION-SYSTEM)
3. Integration triggers version bump, tag, and release (per VERSION-SYSTEM Section 6.5)
4. All changes logged in PROJECT-TRACKING

---

**Document Status:** Production-Ready  
**Effective Date:** 03 February 2026  
**Last Updated:** 25 February 2026  
**Version:** v1.4

{% endraw %}
