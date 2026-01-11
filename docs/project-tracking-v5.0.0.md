# PROJECT TRACKING --- Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0\
**Regime:** Pre-publication (0.x.x.x)\
**Project Start:** 2026-01-05\
**Last Updated:** 2026-01-10\
**Repository:** `carlos-nader/tms-dms-cms-usage-guide`

This document tracks how governance rules, WIP files and guide versions evolve during the development of the **Falcon BMS TMS/DMS/CMS HOTAS Guide**.

---

## 1. Governance Layer --- Reference Documents

These documents define the rules; PROJECT-TRACKING records how they are applied.

| Document | Version | Purpose | Scope / Notes |
|----------|---------|---------|---------------|
| VERSION-SYSTEM-v4.2.1 | v4.2.1 | Versioning rules for `guide-v*` | Defines 0.x.x.x vs x.y.z regimes; MAJOR/MINOR/PATCH/SUBPATCH semantics; build date rules. Updated Session 9: refs → v1.4; BRIEFING-v0.2.0.1 relation documented. Alignment with FILE-NAMING-v1.4 e BRIEFING-v0.2.0.1 |
| WIP-FILE-NAMING-v1.4 | v1.4 | Naming and status for WIP files | Prefixes `section-*`, `table-*`, `visual-*`, `notes-*`, `chapter-*` with dev/review/final/approved/deprecated. Updated Session 9: Section 0.5 added (How to Create WIP File); Section 9 added (Summary + best practices). |
| BRIEFING-v0.2.0.1 | v0.2.0.1 | Content and layout brief + template | Scope, style, layout standard (Geometry Option D, `hotastable` 15.6 cm, `\\arraystretch=1.25`), high-level roadmap. **NEW Section 11:** Complete template specification per BRIEFING-v0.2.0.1 Section 11. Includes: Geometry Option D, hotastable, arraystretch |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | Canonical WIP template | Per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning (V1.0). Established Session 9. |
| TRAIN. MISSIONS ABBR. TABLE | v1.0 | Official source for use with Tables | Defines abbreviations for all missions from the Training Manual, for use when building Tables |
| PROJECT-TRACKING-v5.0.0 (this) | v5.0.0 | Project tracking and integration log | Records how WIP + VERSION-SYSTEM + layout decisions become concrete guide versions; integrated with Git/GitHub. Content updated Session 9; version unchanged. |

**Integration rules**

- **VERSION-SYSTEM-v4.2.1** governs only `guide-v*.tex` version numbers.
- **WIP-FILE-NAMING-v1.4** governs only files in the WIP/ARCHIVE layer.
- **BRIEFING-v0.2.0.1** defines *what* the guide contains, *how* it looks, and *how* WIP files are structured (Section 11).
- **TEMPLATES/template-wip-V1.0.tex** is the canonical starting point for all new WIP files (per BRIEFING Section 11; mandatory).
- **PROJECT-TRACKING-v5.0.0** records *when and why* those rules are applied and how they map to concrete guide versions.
- **TRAINING MISSION ABBREV TABLE-v1.0** defines abbrevations for all Training Mission from the Training Manual to be used when building tables.

---

## 2. Project Snapshot (Current State)

High-level view of the project **as of 2026-01-10**.

- **Active Regime:** Pre-publication `0.x.x.x` (Phase 0 --- Chapter Scaffolding).
- **Current Guide Version:** `guide-v0.2.3.1-20260110.tex` (section 5.2 integrated).
- **Chapters Planned:** 7.
- **Chapters with narrative complete / in development:** 2 / 7
  - Chapter 1 --- Introduction (narrative complete).
  - Chapter 5 --- CMS Section 5.1 and 5.2 narrative and tables complete; 5.3 in review.
- **Chapters with structure scaffolded:** 4 / 7
  - Chapters 3 (TMS), 4 (DMS), 5 (CMS) plus outlines for 6 (Training References) and 7 (HOTAS Visual Reference).
- **Tables filled:** 1 major CMS HOTAS table integrated (Section 5.2); remaining tables 0 %.
- **Layout Standard (since v0.2.2.0):**
  - Geometry Option D (A4, 2.0 cm side, 2.5 cm top/bottom, 17.0 cm text width).
  - `hotastable` width 15.6 cm, `\\small`, `\\arraystretch=1.25` for table readability.
- **Tooling & Repository:**
  - Git/GitHub repository created: `tms-dms-cms-usage-guide`.
  - Local project root: `projeto-bms` (no space), managed via GitHub Desktop + Git CLI.
  - Core folders aligned with governance:
    - `WIP/` --- active work-in-progress LaTeX sections/tables/visuals.
    - `ARCHIVE/` --- approved or deprecated WIP and historical snapshots.
    - `Fig/`--- images and figures used in `guide.tex`
    - `docs/` --- governance and tracking documents in Markdown (`*.md`), exported to DOCX via `md-to-docx` script.
  - VS Code adopted as the default editor for Markdown and Git-related edits.
- **Governance Update (Session 9):**
  - ✅ **BRIEFING:** v0.1.4.1 → **v0.2.0.1** (NEW Section 11: Template Specification + governance; ~2,500 words covering preamble, metadata block, hotastable environment, section skeleton, integration workflow, versioning & maintenance).
  - ✅ **WIP-FILE-NAMING:** v1.3 → **v1.4** (NEW Section 0.5: How to Create WIP File --- 3-step workflow; NEW Section 9: Summary + best practices; all sections updated to reference mandatory template usage).
  - ✅ **VERSION-SYSTEM:** v4.2 → **v4.2.1** (References updated to WIP-FILE-NAMING-v1.4; BRIEFING-v0.2.0.1 Section 11 relation documented; clarified 3-way integration: BRIEFING + WIP-NAMING + VERSION-SYSTEM).
  - ✅ **TEMPLATES:** **NEW** `TEMPLATES/template-wip-V1.0.tex` (Canonical template per BRIEFING Section 11; preamble/metadata/hotastable locked; independent versioning V1.0; all future WIP MUST copy from this template).
  - 📝 **Consequence:** All new WIP files going forward MUST follow BRIEFING-v0.2.0.1 Section 11 template specification.

---

## 3. Version Roadmap (Guide `guide-v*.tex`)

### 3.1 Past and Current Versions (0.x.x.x)

| Version | Date | Area / Chapter | Status | Short Description |
|---------|------|----------------|--------|-------------------|
| v0.1.0.0 | 2026-01-05 | Chapter 1 --- Introduction | ✅ Complete | Intro structured and integrated. |
| v0.1.1.0 | 2026-01-05 | Chapter 1 --- Introduction | ✅ Complete | Additional intro refinements / structure tweaks. |
| v0.1.3.0 | 2026-01-05 | Chapter 3 --- TMS | ✅ Complete | TMS chapter structure finalised; content pending. |
| v0.1.4.0 | 2026-01-06 | Chapter 4 --- DMS + layout fix | ✅ Complete | DMS restructured to transversal SOI per Dash-34; geometry brace fix. |
| v0.2.0.1 | 2026-01-07 | Chapter 5 --- CMS Section 5.1 | ✅ Complete | CMS 5.1 (Concept & interaction with CMDS/ECM) integrated as new section. |
| v0.2.1.0 | 2026-01-08 | Chapter 5 --- Structure refinement | ✅ Complete | Chapter 5 subsections 5.1--5.3 organised and clarified. |
| v0.2.2.0 | 2026-01-08 | Global layout (all chapters) | ✅ Complete | Geometry Option D + `\\arraystretch=1.25`; **layout-only** changes, no content modifications relative to v0.2.1.0. |
| **v0.2.3.1** | **2026-01-10** | **Chapter 5 --- CMS Section 5.2** | **✅ Active** | **Integrated CMS 5.2 "CMS Switch Actuation" narrative and main HOTAS table into Chapter 5; CMS 5.3 (Block / variant notes) remains in review** |

> Note: All `guide-v0.2.0.1/0.2.1.0` and previous files are preserved under version control (and/or ARCHIVE) for rollback and traceability.

### 3.2 Planned Near-Term Versions

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.2.4.0 | Chapter 5 --- Section 5.3 (CMS) | 0 | 🔄 Planned | Integrate CMS 5.3 "Block and variant notes" once WIP is promoted to final. Successor to partial v0.2.3.1 integration. |
| v0.3.0.0 | Chapter 5 complete + next chapter | 0 | 🎯 Target | Chapter 5 considered complete (concept + actuation + variants). MINOR bump when next major chapter (e.g. TMS or DMS content) is selected. |
| v0.4.0.0 | Chapter 5 CMS tables populated | 0 | 🔄 Planned | Populate CMS HOTAS tables (AUTO/SEMI/MAN, ECM, consent/constraints, operational notes). |
| v0.7.0.0 | All 7 chapters scaffolded | 0 | 📋 Target | All chapters with structure + basic narrative. Transition point from Phase 0 to Phase 1. |

Post-Phase-0:

- `v1.0.0` and above will follow VERSION-SYSTEM-v4.2.1 rules for post-publication regimes (Phase 1 --- table population; Phase 2 --- review & community release).

---

## 4. WIP Layer

### 4.1 WIP File Naming Quick Reference (WIP-FILE-NAMING-v1.4)

General pattern:

```
{prefix}-{location}-{descriptor}-{status}-{date}.{ext}
```

Summary:

| Category | Pattern | Example | Status codes |
|----------|---------|---------|--------------|
| Chapters | `chapter-C{N}-{TITLE}-{STATUS}-{DATE}.tex` | `chapter-C2-hotas-fundamentals-dev-2026-01-20.tex` | dev, review, approved, deprecated |
| Sections | `section-C{N}-S{M}[-S{K}]-{TITLE}-{STATUS}-{DATE}.tex` | `section-C5-S1-cms-concept-final-2026-01-07.tex` | dev, review, final, approved, deprecated |
| Tables | `table-C{N}-{CONTEXT}-{SWITCH}-{STATUS}-{DATE}.tex` | `table-C3-AA-TMS-review-2026-01-17.tex` | dev, review, final, approved, deprecated |
| Notes | `notes-C{N}-{TOPIC}-{TYPE}-{DATE}.md` | `notes-C4-dms-research-questions-2026-01-19.md` | (no formal status) |
| Visuals | `visual-C{N}-{DESC}-{TYPE}-{STATUS}-{DATE}.{ext}` | `visual-C7-hotas-layout-diagram-dev-2026-01-18.svg` | dev, review, final, approved, deprecated |

Key rules:

- WIP status transitions (dev → review → final → approved) **do not** affect guide version numbers directly.
- Only **integration** into `guide-v*.tex` triggers version bumps, according to VERSION-SYSTEM-v4.2.1.
- Active WIP lives in `WIP/`; integrated or deprecated WIP moves to `ARCHIVE/`.
- **NEW (Session 9):** All new WIP files MUST copy from `TEMPLATES/template-wip-V1.0.tex` per BRIEFING-v0.2.0.1 Section 11.

### 4.2 Active WIP Snapshot (as of 2026-01-10)

| File (relative path) | Status | Chapter | **Template Compliance** | Next Action |
|---|---|---|---|---|
| `WIP/section-C5-S3-blocks-and-variants-review-2026-01-09.tex` | review | C5-S3 | ✅ BRIEFING-v0.2.0.1 Section 11 compliant | Apply structural/content adjustments from c5-s3-review.md; then promote to final and integrate into guide-v0.2.4.0. |

### 4.3 WIP Integration Timeline (Historical)

| Date | WIP / Reference File | Version Bump | Category | Notes |
|------|---|---|---|---|
| 2026-01-07 | `section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex` | v0.1.4.0 → v0.2.0.1 (MINOR) | section | CMS 5.1 integrated as new section; chapters metric moved from 1/7 to 2/7. |
| 2026-01-08 | `section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex` | v0.2.0.1 → v0.2.1.0 (PATCH) | section | Human-driven refinement of Chapter 5 internal structure (5.1--5.3 splits and headings). |
| 2026-01-10 | `section-C5-S2-cms-actuation-hotas-tables-final-2026-01-09.tex` | v0.2.1.0 → v0.3.1.0 | section | Integrated CMS 5.2 "CMS Switch Actuation" narrative and main HOTAS table into Chapter 5 (SUBPATCH within 0.2.x.x line) |

Status codes reminder:

- `dev` → draft; `review` → under human review; `final` → approved by human, ready for integration; `approved` → integrated and archived; `deprecated` → intentionally retired.

---

## 5. Session Log (High-Level)

Summary of major decisions and changes per working session. Earlier sessions (1--6) are documented in legacy tracking files; from v5.0.0 onward, sessions are logged here.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---------|------|---|---|---|
| 7 | 2026-01-08 | `v0.2.2.0` | `v4.1.2` | Layout Option D and table `\\arraystretch` adopted; CMS 5.1 fully integrated; Chapter 5 structure (5.1--5.3) refined; WIP files for 5.2 and 5.3 created in `review` status. |
| 8 | 2026-01-09 | `v0.2.2.0` (unchanged) | `v5.0.0` | Project brought under Git/GitHub (`falcon-bms-hotas-tms-dms-cms-guide`); local root normalised to `projeto-bms`; folder structure `WIP/`, `ARCHIVE/`, `docs/` created and aligned with WIP-FILE-NAMING; governance centralised in `.md` files under `docs/` with DOCX exports generated via `md-to-docx`; VS Code and Git CLI configured for Markdown-centric workflow. |
| 9 | 2026-01-09 | `v0.2.2.0` (unchanged) | `v5.0.0` | ✅ **Template establishment:** BRIEFING → v0.2.0.1 (Section 11 --- complete template specification); WIP-NAMING → v1.4 (Section 0.5 --- how to create WIP file); VERSION-SYSTEM → v4.2.1 (references updated; 3-way integration documented). ✅ **TEMPLATES/template-wip-V1.0.tex** created and locked (preamble/metadata/hotastable per BRIEFING Section 11). ✅ **Section-C5-S2 & S3 WIP files** created using new template with corrected LaTeX syntax. 📝 **Going forward:** All new WIP files MUST use template; mandatory governance structure locked. |
| **10** | **2026-01-09** | `V0.2.3.1` | `V5.0.0` | Integrated CMS 5.2 "CMS Switch Actuation" narrative and main HOTAS table into Chapter 5; C5-S2 WIP marked ready for archival; C5-S3 remains under review with dedicated review MD |

> Future sessions should add new rows to this table, keeping summaries concise and always mentioning: (a) resulting guide version, (b) tracking version, and (c) main decisions.

---

## 6. Project Priorities & Phases

### 6.1 Current Priorities (Post-v0.3.1.0)

1. **Finalise and validate Section 5.3 (CMS Block and variant notes); CMS 5.1 and 5.2 already integrated (0.2.0.0 and 0.2.3.1). Integrate 5.3 into a new version v0.2.4.0 while staying in the 0.2.x.x line**
2. **Scaffolding of Remaining Chapters**
   - Consolidate TMS (Chapter 3) and DMS (Chapter 4) structures based on decisions documented in the BRIEFING.

### 6.2 Phases & Timeline (Coarse Plan)

| Phase | Target Versions | Indicative Range | Milestone |
|---|---|---|---|
| 0 | v0.1.0.0 → v0.7.0.0 | 05--22 Jan 2026 | All chapters scaffolded; layout locked at v0.2.2.0; CMS chapter structurally complete. |
| 1 | v1.0.0 → v1.0.x | To be defined | Major HOTAS tables (TMS/DMS/CMS) populated and technically validated. |
| 2 | v2.0.0-RC1/RC2/Stable | To be defined | Final review, community feedback, and public release. |

Phase boundaries and dates are guidelines; actual transitions must be explicitly recorded in this tracking document.

---

## 7. File Status Summary

### 7.1 Guide Files (`guide-v*.tex`)

| File | Version | Type | Status | Short Purpose |
|------|---------|------|--------|---------------|
| `guide-v0.1.4.0-20260106.tex` | 0.1.4.0 | Main guide | ✅ Archive | Intro narrative + Ch.3--4 structure; pre-CMS integration. |
| `guide-v0.2.0.1-20260108.tex` | 0.2.0.1 | Main guide | ✅ Archive | CMS 5.1 integrated (Concept & interaction). |
| `guide-v0.2.1.0-20260108.tex` | 0.2.1.0 | Main guide | ✅ Archive | Chapter 5 structure refined (5.1--5.3). |
| `guide-v0.2.2.0-20260108.tex` | 0.2.2.0 | Main guide | ✅ Archive | Same content as v0.2.1.0; global layout optimisation (Geometry Option D + `\\arraystretch=1.25`). |
| `guide-v0.3.1.0-20260110.tex` | 0.3.1.0 | Main guide | ✅ Active | "CMS Switch Actuation" narrative and main HOTAS table integrated. Use as base snapshot |

### 7.2 WIP Files

| File (relative path) | Status | Type | Next Action |
|---|---|---|---|
| `ARCHIVE/section-C5-S2-cms-actuation-hotas-table-approved-2026-01-10.tex` | approved | section | Integrated into guide v0.2.3.1. |
| `WIP/section-C5-S3-blocks-and-variants-review-2026-01-09.tex` | review | section | Apply c5-s3-review.md adjustments; promote to final; integrate into v0.2.4.0. |

*(Additional WIP and ARCHIVE entries should be appended here as the project evolves.)*

### 7.3 Governance & Tracking Files (`docs/`)

| File | Version | Type | Status | Short Purpose |
|------|---------|------|--------|---------------|
| `docs/BRIEFING-v0.2.0.1.md` | 0.2.0.1 | Reference | ✅ Active | Project brief with **NEW Section 11: Template Specification** (preamble, metadata block, hotastable environment, section skeleton, integration workflow, template versioning & maintenance). Supersedes v0.1.4.1. |
| `docs/WIP-FILE-NAMING-v1.4.md` | 1.4 | Reference | ✅ Active | WIP naming convention. **NEW Section 0.5:** How to Create WIP File (3-step workflow). **NEW Section 9:** Summary + best practices. Supersedes v1.3. |
| `docs/VERSION-SYSTEM-v4.2.1.md` | 4.2.1 | Reference | ✅ Active | Guide versioning rules. References updated to WIP-FILE-NAMING-v1.4; BRIEFING-v0.2.0.1 Section 11 relation documented; 3-way integration clarified. Supersedes v4.2. |
| `TEMPLATES/template-wip-V1.0.tex` | V1.0 | Template | ✅ Active | **Canonical WIP template** per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning (V1.0). Established Session 9. Copy to WIP/ and rename per WIP-FILE-NAMING-v1.4 Section 0.5. |
| `docs/PROJECT-TRACKING-v5.0.0.md` | 5.0.0 | Tracking | ✅ Active | This document --- unified tracking with Git/GitHub integration. Content updated Session 9. |
| `docs/BRIEFING-v0.2.0.1.docx` | 0.2.0.1 | Export | ✅ Derived | DOCX export from Markdown for convenient reading/sharing. |
| `docs/VERSION-SYSTEM-v4.2.1.docx` | 4.2.1 | Export | ✅ Derived | DOCX export from Markdown. |
| `docs/WIP-FILE-NAMING-v1.4.docx` | 1.4 | Export | ✅ Derived | DOCX export from Markdown. |
| `docs/PROJECT-TRACKING-v5.0.0.docx` | 5.0.0 | Export | ✅ Derived | DOCX export from this Markdown via `md-to-docx` script. |
| `docs/TRAINING-MISSION-ABBREV-TABLE-v1.0.docx` | 1.0 | Export | ✅ Derived | DOCX export from this Markdown via `md-to-docx` script. |

---

**Maintenance rule:**

- All structural or governance changes to tracking must be made in `PROJECT-TRACKING-v5.0.0.md`.
- DOCX versions are generated from this file and never edited manually.
- At the end of each working session, this document should be updated (especially sections 2, 4.2, 4.3, 5 and 6) to capture the new state and decisions.
- **Version number of PROJECT-TRACKING-v5.0.0 does NOT change** with content updates (designed for frequent updates; the version marks the baseline structure, not the state).