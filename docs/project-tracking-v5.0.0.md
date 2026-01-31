# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-01-31, 20:29 PM -03  
**Repository:** carlos-nader/tms-dms-cms-usage-guide

This document tracks how governance rules, WIP files and guide versions evolve during the development of the Falcon BMS TMS/DMS/CMS HOTAS Guide.

---

## 1. GOVERNANCE LAYER

Reference documents that define the project structure:

| Document | Version | Purpose | Scope | Notes |
|---|---|---|---|---|
| VERSION-SYSTEM-v4.2.1 | v4.2.1 | Versioning rules for guide-v | Defines 0.x.x.x vs x.y.z regimes, MAJOR/MINOR/PATCH/SUBPATCH semantics, build date rules. | Updated Session 9; refs v1.4, BRIEFING-v0.2.0.1 alignment documented. |
| BRIEFING-v0.2.0.1 | v0.2.0.1 | Content and layout brief; template specification | Scope, style, layout standard (Geometry Option D, hotastable 15.6 cm, arraystretch 1.25), high-level roadmap. Section 11: EXPANDED (18 Jan 2026) - Complete preamble architecture documentation (11.3.1–11.3.11): document class (report, twoside), encoding/fonts, geometry/spacing, colors/hyperlinks, headers/footers (improved for two-sided layout), chapter formatting (titlesec), tables/columns, graphics/floats (package float), hotastable environment (code corrected for longtable header ordering), reference macros, version control. Preamble code VERIFIED and TESTED per 18 January 2026 (guidetest.tex compilation ✅, PDF generation ✅). | Supersedes v0.1.4.1. Section 11 expanded to ~8,000 words (was ~2,500). All 11 subsections documented with rationale and code examples. New preamble deployed to guide.tex and template-wip-V1.0.tex. |
| WIP-FILE-NAMING-v1.4 | v1.4 | Naming and status for WIP files | Prefixes: section-, table-, visual-, notes-, chapter- with dev/review/final/approved/deprecated status codes. NEW Section 0.5: How to Create WIP File (3-step workflow). | Updated Session 9. All sections reference mandatory template usage. Supersedes v1.3. |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | Canonical WIP template | Per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning (V1.0). **UPDATED 29 Jan 2026:** New hotastable environment (arraystretch 1.25 LOCKED, column widths explicit, enhanced headers). All future WIP files MUST copy from this updated template. | Established Session 9; Updated Session 17 with new preamble infrastructure; Updated Session 24 with hotastable refinements per v0.3.2.1. |
| TRAINING-MISSION-ABBREV-TABLE-v1.0 | v1.0 | Official source for mission abbreviations | Standardized abbreviations for all 33 BMS 4.38.1 training missions, for use when building Tables. | For reference when incorporating mission names. |

**Consequence:** All new WIP files going forward MUST follow BRIEFING-v0.2.0.1 Section 11 template specification (with updated preamble per 18 Jan 2026 and hotastable per 29 Jan 2026) and WIP-FILE-NAMING-v1.4 conventions.

---

## 2. PROJECT SNAPSHOT

Current state as of 2026-01-31, 20:29 PM -03 (Session 24 - v0.3.2.1 SUBPATCH verified):

### 2.1 High-Level Overview

- **Active Regime:** Pre-publication (0.x.x.x)
- **Phase:** Phase 0 -- Chapter Scaffolding
- **Current Guide Version:** guide-v0.3.2.1-20260129 (SUBPATCH refinement: new hotastable environment with arraystretch 1.25, Chapter 4 content corrections, Chapter 5 structure corrections) — stored in wip/guide/, synchronized to guide.tex root
- **Chapters Planned:** 7
- **Chapters with narrative complete in development:** 3/7
  - Chapter 1 -- Introduction (narrative complete)
  - Chapter 5 -- CMS Sections 5.1, 5.2, 5.3 (narrative and tables complete)
  - **Chapter 4 -- DMS Sections 4.1, 4.2, 4.3, and 4.4 (LEFT/RIGHT - WIP IN REVIEW)**
    - Section 4.1 (Concept and SOI) - FINAL & INTEGRATED (with content corrections per v0.3.2.1)
    - Section 4.2 (DMS Up: HUD Designation as SOI) - FINAL & INTEGRATED (with content corrections per v0.3.2.1)
    - Section 4.3 (DMS Down: Toggle SOI Between Displays) - **FINAL & INTEGRATED (v0.3.2.0)**
    - Section 4.4 (DMS Left/Right: Format Selection) - **WIP REVIEW IN PROGRESS** (review status, 2026-01-29)
    - Section 4.5 (Master Mode Summary) - pending per unified Chapter 4 DMS blueprint v1.1
- **Chapters with structure scaffolded:** 4/7
  - Chapters 2 (HOTAS Fundamentals), 3 (TMS), 4 (DMS with 4.1, 4.2, 4.3 direction-based structure locked by blueprint v1.1), plus outlines for 6 (Training References) and 7 (HOTAS Visual Reference)
- **Tables filled:** 1 major HOTAS table (CMS, integrated Sections 5.2–5.3), 3 DMS tables (C4-S1 SOI-by-mode, C4-S2 DMS Up usage, C4-S3 DMS Down usage) all INTEGRATED with enhanced documentation (column explanations); remaining DMS tables (DMS Left/Right, DMS summary) pending per unified Chapter 4 DMS blueprint v1.1.

### 2.2 Layout Standard

Since v0.2.2.0 (geometry and table settings); v0.3.1.0 (preamble upgraded); v0.3.2.0 (semantic refinements); v0.3.2.1 (hotastable arraystretch 1.25 DEPLOYED):
- **Geometry:** Option D (A4, 2.0 cm side margins, 2.5 cm top/bottom)
- **Text width:** 17.0 cm
- **HOTAS table width:** 15.6 cm
- **Table arraystretch:** 1.25 (for readability) — **DEPLOYED in v0.3.2.1**
- **Column definitions:** L{width}, C{width}, R{width} (raggedright, centering, raggedleft with explicit width)
- **Document class:** `report` with `twoside` option (upgraded Session 17)
- **Chapter formatting:** Enhanced via `titlesec` package (upgraded Session 17)
- **Headers/Footers:** Professional two-sided layout with improved page numbers and chapter markers (upgraded Session 17)
- **Additional packages:** `float` for graphics control, `booktabs` + `tabularx` for advanced table formatting (upgraded Session 17)

### 2.3 Tooling & Repository

- **Version Control:** Git/GitHub (repository: tms-dms-cms-usage-guide)
- **Local project root:** projeto-bms (normalized structure)
- **Core folders:**
  - wip/ -- active work-in-progress (LaTeX sections/tables/visuals); contains wip/guide/ subfolder for versioned snapshots
  - archive/ -- approved or deprecated WIP and historical guide snapshots (subfolders: archive/GUIDE/, archive/WIP/)
  - Fig -- images and figures used in guide.tex
  - docs -- governance and tracking documents (Markdown), exported to DOCX via md-to-docx script
- **Editor:** VS Code (default for Markdown and Git-related edits)
- **LaTeX toolchain:** MiKTeX (local compilation)
- **Total Commits:** 255 (GitHub tracked)
- **Releases:** v0.3.2.1 (active, tagged on GitHub 2026-01-29), v0.3.2.0 (archived), v0.3.1.0 (archived), v0.3.0.1 (archived), v0.3.0.0 (archived)

---

## 3. VERSION ROADMAP

### 3.1 Past and Current Versions (0.x.x.x)

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.1.0.0 | Initial scaffold | 0 | **✅ COMPLETED** | Basic structure laid. Chapter/Section skeleton. Integrated Introduction (Chapter 1). Canonical nomenclature: TMS, DMS, CMS (not ICP buttons). |
| v0.1.4.0 | Template adoption | 0 | **✅ COMPLETED** | guide.tex using geometry, columns, and arraystretch per BRIEFING requirements. Layout standard deployed. |
| v0.2.0.1 | Chapter 5 -- CMS (Section 5.1) | 0 | **✅ COMPLETED** | Integrated Section 5.1 (Concept and Interactions -- CMDS/ECM/RWR). Chapter metric 17 → 27. |
| v0.2.1.0 | Chapter 5 -- CMS (Internal structure) | 0 | **✅ COMPLETED** | Refined Chapter 5 internal structure (5.1, 5.2, 5.3 splits). |
| v0.2.2.0 | Chapter 5 -- CMS (Section 5.2) | 0 | **✅ COMPLETED** | Integrated Section 5.2 (Switch Actuation and HOTAS Table). Geometry Option D locked. |
| v0.2.3.0 | Chapter 5 -- CMS (Section 5.2 tables) | 0 | **✅ COMPLETED** | Added tables to Section 5.2 (CMS HOTAS table). |
| v0.2.3.1 | Chapter 5 -- CMS (Table columns documented) | 0 | **✅ COMPLETED** | CMS table (Section 5.2) with documented column explanations (SUBPATCH). |
| v0.2.4.0 | Chapter 5 -- CMS (Section 5.3) | 0 | **✅ COMPLETED** | Integrated Section 5.3 (Block and Variant Notes). Chapter 5 structurally complete (all 3 sections). |
| v0.3.0.0 | Chapter 4 -- DMS (Sections 4.1, 4.2) | 0 | **✅ COMPLETED** | Integrated DMS Sections 4.1 (Concept and SOI) and 4.2 (DMS Up). HOTAS tables: SOI-by-mode (6 rows), DMS Up usage (3 rows). GitHub Release tag 0.3.0.0 created. |
| v0.3.0.1 | Chapter 4 -- DMS (Section 4.2 table docs) | 0 | **✅ COMPLETED** | Section 4.2 (DMS Up) table with documented column explanations. PATCH-level refinement. GitHub Release tag 0.3.0.1 created. |
| v0.3.1.0 | Preamble Infrastructure Upgrade | 0 | **✅ COMPLETED & RELEASED** | **SESSION 17 Update (18 Jan 2026):** Major preamble infrastructure upgrade deployed. Migration: article class → report class with twoside option. New features: titlesec chapter formatting, improved headers/footers for two-sided layout, float package for graphics control, enhanced table packages (booktabs, tabularx). BRIEFING-v0.2.0.1 Section 11 expanded to ~8,000 words with complete preamble documentation (11.3.1–11.3.11). guide.tex migrated and tested ✅. LaTeX compilation verified ✅. PDF output (guidetest.pdf) generated and approved by author ✅. template-wip-V1.0.tex updated with new preamble (all future WIP files compliant). Snapshot guide-v0.3.1.0-20260117.tex created, deployed to wip/guide/, and synchronized to guide.tex root. Previous snapshot (v0.3.0.1) moved to ARCHIVE/GUIDE/. GitHub Release tag 0.3.1.0 created and pushed to repository. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH). Next phase: Continue DMS content (Section 4.3 integration, Sections 4.4, 4.5) and TMS coverage per roadmap. |
| v0.3.2.0 | Chapter 4 -- DMS (Section 4.3 integrated, redaction corrections in 4.1-4.2) | 0 | **✅ COMPLETED & RELEASED** | **SESSION 20 Update (19 Jan 2026):** Section 4.3 (DMS Down) integrated into guide after final semantic refinements and redaction corrections applied to Sections 4.1 and 4.2. Changes: (1) Redaction corrections (grammar, clarity) applied throughout 4.1 and 4.2. (2) Section 4.3 integrated with enhanced semantic clarity: new intro paragraph separating display toggling from format transitions; replaced "valid SOI candidates are HUD, FCR, TGP, WPN..." with "HUD and both MFD" for clarity; HOTAS table Effect/Nuance column optimized (NAV, A-A, A-G refined; "picture evaluation" → "situational awareness"). Validation: Dash-34 alignment confirmed; LaTeX structure verified; cross-references checked. File size: 71935 bytes (guide-v0.3.2.0-20260119.tex in wip/guide/). GitHub Release tag 0.3.2.0 created and pushed. Version bump: v0.3.1.0 → v0.3.2.0 (MINOR bump). Next phase: Sections 4.4 (DMS Left/Right) and 4.5 (Master Mode Summary) WIP development per unified Chapter 4 DMS blueprint v1.1. |
| v0.3.2.1 | HOTAS Table environment upgrade, C4/C5 improvements | 0 | **✅ COMPLETED & RELEASED** | **SESSION 24 Update (29 Jan 2026):** SUBPATCH refinement release. New hotastable environment with arraystretch 1.25 (25% vertical spacing increase), explicit column widths L{width}, enhanced longtable headers (endfirsthead/endhead). Chapter 4: content corrections (redaction improvements in 4.1, 4.2). Chapter 5: structure corrections (section organization refinements). Preamble upgraded: booktabs + tabularx packages added, headheight increased to 25pt, titlesec spacing optimized. template-wip-V1.0.tex synchronized with new preamble. GitHub Release tag v0.3.2.1 created and pushed. Version bump: v0.3.2.0 → v0.3.2.1 (SUBPATCH). Total commits: 255. Next: Section 4.4 (DMS Left/Right) integration → v0.3.3.0 (PATCH) OR new chapter → v0.4.0.0 (MINOR). |
| v0.3.3.0 | Chapter 4 -- DMS Section 4.4 (Left/Right) integration | 0 | **WIP REVIEW** | **PATCH bump** (section integration, not new chapter). DMS Section 4.4 (Left/Right) in review status (2026-01-29). File: section-C4-S4-dms-left-right-review-2026-01-29.tex. PDF generated for visual validation. Next: Author final review cycle and integration decision. |
| v0.4.0.0 | New Chapter (C2 HOTAS Fundamentals OR complete C3 TMS) | 0 | Planned | **MINOR bump** (new chapter entry into guide). Chapter 2 (HOTAS Fundamentals) also in dev status (2026-01-25). Per VERSION-SYSTEM v4.2.1: MINOR increments ONLY when NEW CHAPTER enters guide. |
| v0.5.0.0 | Additional new chapter | 0 | Planned | Full chapter coverage (C2 OR C3). MINOR bump. |
| v0.7.0.0 | All 7 chapters scaffolded | 0 | Target | All chapters with structure and basic narrative. Transition point from Phase 0 to Phase 1. MINOR bump. |

**Post-Phase-0:** v1.0.0 and above will follow VERSION-SYSTEM-v4.2.1 rules for post-publication regimes.
- Phase 1 -- Table population
- Phase 2 -- Community review and release

---

## 4. WIP LAYER

### 4.1 WIP File Naming Quick Reference

Per WIP-FILE-NAMING-v1.4:

| Category | Pattern | Example | Status Codes |
|---|---|---|---|
| Chapters | chapter-CN-TITLE-STATUS-DATE.tex | chapter-C2-hotas-fundamentals-dev-2026-01-25.tex | dev, review, final, approved, deprecated |
| Sections | section-CN-SM-SK-TITLE-STATUS-DATE.tex | section-C5-S1-cms-concept-final-2026-01-07.tex | dev, review, final, approved, deprecated |
| Tables | table-CN-CONTEXT-SWITCH-STATUS-DATE.tex | table-C3-AA-TMS-review-2026-01-17.tex | dev, review, final, approved, deprecated |
| Notes | notes-CN-TOPIC-TYPE-DATE.md | notes-C4-dms-research-questions-2026-01-19.md | no formal status |
| Visuals | visual-CN-DESC-TYPE-STATUS-DATE.ext | visual-C7-hotas-layout-diagram-dev-2026-01-18.svg | dev, review, final, approved, deprecated |

**Key rules:**
- WIP status transitions (dev → review → final → approved) do not directly affect guide version numbers.
- Only integration into guide-v.tex triggers version bumps per VERSION-SYSTEM-v4.2.1.
- Active WIP lives in wip/; integrated or deprecated WIP moves to archive/.
- **UPDATED (Session 24):** All new WIP files MUST copy from TEMPLATES/template-wip-V1.0.tex per BRIEFING-v0.2.0.1 Section 11 (updated preamble with hotastable arraystretch 1.25, deployed v0.3.2.1).

---

### 4.2 Active WIP Snapshot (as of 2026-01-31, 20:29 PM -03)

| WIP File | Status | Last Updated | Target Guide Version | Description |
|---|---|---|---|---|
| **chapter-C2-hotas-fundamentals-dev-2026-01-25.tex** | **dev** | 2026-01-25 | v0.4.0.0 | Chapter 2 (HOTAS Fundamentals). Covers SOI concept, short/long press timing, master modes, HOTAS switch categories (TMS/DMS/CMS). Foundational content for entire guide. WIP file generated from template-wip-V1.0.tex. Status: dev. Preamble: V1.0 (Session 17 compatible). Next: Author review cycle and integration decision (new chapter → MINOR bump v0.4.0.0). |
| **section-C4-S4-dms-left-right-review-2026-01-29.tex** | **review** | 2026-01-29 | v0.3.3.0 | DMS Chapter 4 Section 4.4 (DMS Left/Right: Format Selection). Promoted dev → review (2026-01-21). **SESSION 24 UPDATE:** PDF compiled and validated. Content structure: Overview, Functional Modes (Radar/NAV/Weapons), Button Logic, Integration, Summary. LaTeX structure verified. File size: 21 KB. Status: review. Preamble: V1.0. Next: Author final review → transition to final status → integration into v0.3.3.0 (PATCH bump - section integration, not new chapter). |

**Status codes:**
- dev -- Draft, author working
- review -- Under human review, not yet final or integrated
- final -- Author approved, ready for integration
- approved -- Integrated into guide-v and archived
- deprecated -- Intentionally retired (superseded or abandoned)

---

### 4.3 Integrated Files (Session-by-Session Log)

Complete chronological log of all WIP files that have been integrated into guide-v snapshots.

| Date | WIP Reference File | From Version | To Version | Status | Category | Notes |
|---|---|---|---|---|---|---|
| 2026-01-07 | section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex | v0.1.4.0 | v0.2.0.1 | INTEGRATED | section | CMS 5.1 integrated as new section. Chapters metric 17 → 27. |
| 2026-01-08 | section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex | v0.2.0.1 | v0.2.1.0 | INTEGRATED | section | Human-driven refinement of Chapter 5 internal structure (5.1–5.3 splits, headings). |
| 2026-01-10 | section-C5-S2-cms-actuation-hotas-tables-final-2026-01-09.tex | v0.2.1.0 | v0.2.3.1 | INTEGRATED | section | Integrated CMS 5.2 (CMS Switch Actuation) narrative and main HOTAS table. |
| 2026-01-11 | section-C5-S3-blocks-and-variants-final-2026-01-11.tex | v0.2.3.1 | v0.2.4.0 | INTEGRATED | section | Integrated CMS 5.3 (Block and Variant Notes) narrative and reference tables (External ECM Pod, Internal IDIAS). Chapter 5 now structurally complete (all 3 sections). |
| 2026-01-15 | section-C4-S1-concept-soi-approved-2026-01-15.tex | v0.2.4.0 | v0.3.0.0 | **INTEGRATED** | section | DMS Chapter 4 Section 4.1 (Concept and SOI) with SOI-by-mode table. Promoted to FINAL and **INTEGRATED into guide-v0.3.0.0-20260115**. HOTAS table: Valid SOI Displays by Master Mode (6 rows: NAV, A-A, A-G PRE, A-G VIS, DGFT, MSL OVRD) + clarification of HUD/HMCS SOI constraints in A-A. File moved to ARCHIVE with approved status. |
| 2026-01-15 | section-C4-S2-dms-up-approved-2026-01-15.tex | v0.2.4.0 | v0.3.0.0 | **INTEGRATED** | section | DMS Chapter 4 Section 4.2 (DMS Up: HUD Designation as SOI). Extracted from combined DMS Up/Down WIP, promoted to FINAL, and **INTEGRATED into guide-v0.3.0.0-20260115**. HOTAS table: DMS Up Usage Across NAV, A-A and A-G Master Modes (3 rows) + exception states (Snowplow, MARK/OFLY). File moved to ARCHIVE with approved status. |
| 2026-01-16 | guide-v0.3.0.1-20260116.tex | v0.3.0.0 | v0.3.0.1 | **INTEGRATED (PATCH)** | guide | Section 4.2 (DMS Up) table column explanations added, matching Section 5.2 documentation pattern. No structural changes; PATCH-level refinement only. LaTeX compiled ✅, PDF generated ✅. Snapshot deployed to guide.tex root. Previous snapshot (v0.3.0.0) moved to ARCHIVE/GUIDE/. |
| 2026-01-17 | guide-v0.3.1.0-20260117.tex | v0.3.0.1 | v0.3.1.0 | **INTEGRATED (PATCH - Infrastructure)** | guide | **SESSION 17 - PREAMBLE INFRASTRUCTURE UPGRADE:** Major preamble upgrade deployed. Migration: article class → report class with twoside option. New packages: titlesec (chapter formatting), float (graphics control), booktabs/tabularx (advanced tables). Headers/footers enhanced for two-sided professional layout. BRIEFING-v0.2.0.1 Section 11 expanded to ~8,000 words with complete documentation (11.3.1–11.3.11) covering all preamble components. guide.tex tested via guidetest.tex ✅ (LaTeX compilation verified, PDF generated and approved by author). template-wip-V1.0.tex updated with new preamble (all future WIP files compliant). Snapshot guide-v0.3.1.0-20260117.tex created in wip/guide/ and synchronized to guide.tex root. Previous snapshot (v0.3.0.1) moved to ARCHIVE/GUIDE/. GitHub Release tag 0.3.1.0 created. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH). Infrastructure now production-ready for continued content development. |
| 2026-01-18 | section-C4-S3-dms-down-approved-2026-01-18.tex | v0.3.1.0 | v0.3.2.0 | **FINAL & INTEGRATED** | section | DMS Chapter 4 Section 4.3 (DMS Down: Toggle SOI Between Displays). Promoted review→final on 2026-01-18. **INTEGRATED into guide-v0.3.2.0-20260119** on 2026-01-19. Refined intro separating display toggling from format transitions. Semantic refinement: "HUD and both MFD" replaces format listing for clarity. HOTAS table Effect/Nuance column (col 5) optimized: NAV, A-A, A-G all updated; "picture evaluation" → "situational awareness" (A-A row). Full subsection structure verified: 4.3.1 (DMS Down Effectiveness), 4.3.2 HOTAS table (3 rows + mission refs), 4.3.3 Exception States (Snowplow, MARK/OFLY). File size: 15,094 bytes (archived approved version). Preamble compatibility: V1.0 (updated Session 17). File moved to ARCHIVE with approved status. |
| 2026-01-19 | guide-v0.3.2.0-20260119.tex | v0.3.1.0 | v0.3.2.0 | **INTEGRATED (MINOR)** | guide | **SESSION 20 - DMS SECTION 4.3 INTEGRATION + REDACTION CORRECTIONS:** Section 4.3 (DMS Down) integrated into guide. Additionally, redaction corrections applied to Sections 4.1 and 4.2 (grammar, clarity, semantic refinements). Version bump: v0.3.1.0 → v0.3.2.0 (MINOR bump reflecting integration of Section 4.3). Snapshot guide-v0.3.2.0-20260119.tex created in wip/guide/ (71935 bytes) and synchronized to guide.tex root. Previous snapshot (v0.3.1.0) moved to ARCHIVE/GUIDE/. GitHub Release tag 0.3.2.0 created. Chapter 4 now contains integrated Sections 4.1, 4.2, 4.3 with enhanced semantic clarity and redaction corrections. Next phase: DMS Sections 4.4 (Left/Right) and 4.5 (Master Mode Summary) WIP development per unified Chapter 4 DMS blueprint v1.1. |
| 2026-01-29 | guide-v0.3.2.1-20260129.tex | v0.3.2.0 | v0.3.2.1 | **INTEGRATED (SUBPATCH)** | guide | **SESSION 24 - HOTASTABLE ENVIRONMENT UPGRADE:** New hotastable environment with arraystretch 1.25 (25% vertical spacing), explicit column widths, enhanced headers. Chapter 4 content corrections (4.1, 4.2 redaction improvements). Chapter 5 structure corrections. Preamble upgraded: booktabs + tabularx added, headheight 25pt, titlesec spacing optimized. template-wip-V1.0.tex synchronized. GitHub Release tag v0.3.2.1 created. Version bump: v0.3.2.0 → v0.3.2.1 (SUBPATCH). Total commits: 255. Snapshot deployed to wip/guide/ and guide.tex root. Previous snapshot (v0.3.2.0) moved to ARCHIVE/GUIDE/. |

---

## 5. SESSION LOG

High-level summary of each working session and resulting guide state.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 1 | 2026-01-05 | v0.1.0.0 | v1.0.0 | Initial project setup. Chapter scaffolding (TMS/DMS/CMS nomenclature locked). Introduction chapter integrated. VERSION-SYSTEM-v1.0.0 established. |
| 2 | 2026-01-06 | v0.1.1.0 | v1.1.0 | Placeholder subsections added. MINOR bump rules documented. |
| 3 | 2026-01-07 | v0.1.4.0 | v2.0.0 | Layout standard adopted. BRIEFING created. Geometry locked. |
| 4 | 2026-01-07 | v0.2.0.1 | v2.1.0 | CMS Section 5.1 integrated. Chapter metric 17 → 27. |
| 5 | 2026-01-08 | v0.2.1.0 | v3.0.0 | Chapter 5 structure refined (5.1–5.3). WIP-FILE-NAMING created. |
| 6 | 2026-01-09 | v0.2.2.0 | v3.1.0 | CMS Section 5.2 integrated. Geometry Option D locked. |
| 7 | 2026-01-10 | v0.2.3.0 | v3.2.0 | CMS HOTAS table integrated into Section 5.2. |
| 8 | 2026-01-10 | v0.2.3.1 | v3.3.0 | CMS table column explanations added. SUBPATCH bump. |
| 9 | 2026-01-11 | v0.2.4.0 | v4.0.0 | CMS Section 5.3 integrated. Chapter 5 complete. Template-wip-V1.0.tex established. VERSION-SYSTEM and WIP-FILE-NAMING updated. |
| 10 | 2026-01-13 | v0.2.4.0 (unchanged) | v4.1.0 | DMS blueprint v1.0 created. Project structure analysis. |
| 11 | 2026-01-14 | v0.2.4.0 (unchanged) | v4.1.1 | DMS blueprint v1.1 finalized (direction-based structure). |
| 12 | 2026-01-14 | v0.3.0.0 | v4.2.0 | **v0.3.0.0 RELEASE:** DMS Sections 4.1 and 4.2 integrated. HOTAS tables: SOI-by-mode (6 rows), DMS Up usage (3 rows). MINOR bump. GitHub Release tag 0.3.0.0 created. Total commits: 77. |
| 13 | 2026-01-16 | v0.3.0.1 | v4.2.0 | Section 4.2 (DMS Up) table column explanations added. PATCH bump. LaTeX verified ✅. GitHub Release tag 0.3.0.1 created. |
| 14 | 2026-01-17 | v0.3.0.1 (unchanged) | v4.2.0 | DMS Down WIP promoted to review status. |
| 15 | 2026-01-18 | v0.3.0.1 (unchanged) | v4.2.0 | DMS Down WIP promoted to final status after semantic refinements. Ready for integration. |
| 16 | 2026-01-18 | v0.3.0.1 (unchanged) | v4.2.0 | BRIEFING-v0.2.0.1 Section 11 expanded (~8,000 words). Preamble architecture documented. New preamble prepared (report class, twoside, titlesec, float). guidetest.tex compilation verified ✅. PDF generated ✅. |
| 17 | 2026-01-18 | v0.3.1.0 | v4.2.1 | **v0.3.1.0 RELEASE - PREAMBLE INFRASTRUCTURE UPGRADE:** Major preamble upgrade deployed (article → report class with twoside, titlesec chapter formatting, improved headers/footers, float package). guide.tex migrated and tested ✅. template-wip-V1.0.tex updated. PATCH bump. GitHub Release tag 0.3.1.0 created. Total commits: 107. |
| 18 | 2026-01-18 | v0.3.2.0 (pending) | v4.2.1 | DMS Down Section 4.3 promoted to final status after enhanced semantic refinements (intro paragraph refined, "HUD and both MFD" clarity, HOTAS table Effect/Nuance optimized). Ready for integration into v0.3.2.0. |
| 19 | 2026-01-19 | v0.3.2.0 | v4.2.1 | **v0.3.2.0 INTEGRATION COMPLETE:** Section 4.3 integrated. Redaction corrections in 4.1 and 4.2. MINOR version bump. GitHub Release 0.3.2.0 tagged. Chapter 4 now FINAL & INTEGRATED (Sections 4.1, 4.2, 4.3). Next: DMS 4.4 and 4.5 WIP development. Total commits: 144. |
| 20 | 2026-01-19 | v0.3.2.0 | v5.0.0 | **TRACKING UPDATE:** PROJECT-TRACKING-v5.0.0 released. Complete restructure: new Section 2 (Project Snapshot with 3 subsections), Section 4 (WIP Layer with 3 subsections including chronological integrated files log), Session Log (Section 5), Near-Term Roadmap (Section 6), Key Metrics (Section 7). Enhanced navigation, comprehensive documentation, production-ready tracking. |
| 21 | 2026-01-20 | v0.3.2.0 (unchanged) | v5.0.0 | **DMS LEFT/RIGHT WIP DEVELOPMENT:** Substantive research on DMS Left/Right architecture completed. WIP section-C4-S4-dms-left-right-dev-2026-01-20.tex generated from canonical template. Status: dev. Content sections: Overview, Functional Modes, Button Logic, Integration, Summary. Preamble: V1.0. Awaiting author review and MFD image integration. Next: Integration into v0.3.3.0 (PATCH - section, not new chapter) per Chapter 4 DMS blueprint v1.1. |
| 22 | 2026-01-21 | v0.3.2.0 (unchanged) | v5.0.0 | **DMS LEFT/RIGHT WIP PROMOTED TO REVIEW:** C4-S4 promoted dev → review status. File renamed: section-C4-S4-dms-left-right-dev-2026-01-20.tex → section-C4-S4-dms-left-right-review-2026-01-21.tex. PDF generated for visual validation. Content structure complete: Overview, Functional Modes, Button Logic, Integration, Summary. Status: review. Preamble: V1.0. Next: Author final review cycle and transition to final status prior to integration into v0.3.3.0 (PATCH bump). Total commits: 198. |
| 23 | 2026-01-29 | v0.3.2.0 (unchanged) | v5.0.0 | **PROJECT TRACKING UPDATE:** Section 9 (NEXT TARGET) added. Tracks active development priorities: C2 (HOTAS Fundamentals - dev status), C4:S4 (DMS Left/Right - review status), guide version v0.3.3.0 target (PATCH). Active WIP snapshot updated with both WIP files. Integrated files log updated with C2 and C4-S4 entries. Complete tracking refresh with all mapped changes. |
| 24 | 2026-01-31 | v0.3.2.1 | v5.0.0 | **v0.3.2.1 SUBPATCH VERIFIED:** SUBPATCH refinement release (v0.3.2.0 → v0.3.2.1). New hotastable environment deployed (arraystretch 1.25, explicit column widths, enhanced headers). Chapter 4 content corrections. Chapter 5 structure corrections. Preamble upgraded: booktabs/tabularx added, headheight 25pt, titlesec spacing optimized. template-wip-V1.0.tex synchronized. GitHub Release tag v0.3.2.1 created. Total commits: 255. Version rules confirmed: C4-S4 integration → v0.3.3.0 (PATCH - section); new chapter → v0.4.0.0 (MINOR). |

---

## 6. NEAR-TERM ROADMAP (Next Target Versions)

| Version | Area | Status | Notes |
|---|---|---|---|
| **v0.3.2.1** | HOTAS Table environment upgrade, C4/C5 improvements | **✅ COMPLETED & RELEASED** | SUBPATCH refinement. New hotastable with arraystretch 1.25. Chapter 4 content corrections. Chapter 5 structure corrections. Preamble upgraded. template-wip-V1.0.tex synchronized. GitHub Release tag v0.3.2.1 created. Total commits: 255. |
| **v0.3.3.0** | Chapter 4 -- DMS Section 4.4 (Left/Right) integration | **WIP IN REVIEW** | **PATCH bump** (section integration, not new chapter). Section 4.4 (DMS Left/Right) - review status (2026-01-29), PDF validated ✅. Author final review pending. Next: review → final → integration into v0.3.3.0. |
| **v0.4.0.0** | New Chapter (C2 HOTAS Fundamentals OR complete C3 TMS) | Planned | **MINOR bump** (new chapter entry). Chapter 2 (HOTAS Fundamentals) - dev status (2026-01-25). Per VERSION-SYSTEM v4.2.1: MINOR increments ONLY when NEW CHAPTER enters guide. Author decision: C2 priority vs other chapters. |
| **v0.5.0.0** | Additional new chapter | Planned | Full chapter coverage (C3 TMS OR remaining foundational content). MINOR bump. |
| **v0.6.0.0** | Additional chapter completion | Target | Continue chapter scaffolding per roadmap. |
| **v0.7.0.0** | All 7 chapters scaffolded | Target | Transition to Phase 1 (Table Population). |

---

## 7. KEY METRICS

- **Total Commits:** 255 (GitHub tracked)
- **Latest Version:** v0.3.2.1 (released 2026-01-29)
- **Current Phase:** Phase 0 -- Chapter Scaffolding
- **Active WIP Files:** 2
  - chapter-C2-hotas-fundamentals-dev-2026-01-25.tex (dev)
  - section-C4-S4-dms-left-right-review-2026-01-29.tex (review)
- **Next Integration Targets:**
  - v0.3.3.0: C4-S4 integration (PATCH - section)
  - v0.4.0.0: New chapter (C2 OR C3) (MINOR)
- **Last Updated:** 2026-01-31, 20:29 PM -03

---

## 8. GITHUB ISSUE TRACKING INTEGRATION

### 8.1 Issue-to-WIP Mapping

GitHub Issues are tracked to monitor review and approval workflows for WIP files before integration into guide versions.

| Issue # | Type | Title | Status | Linked WIP File | Target Version | Milestone | Notes |
|---|---|---|---|---|---|---|---|
| **#16** | Documentation | C4:S4 DMS Left/Right - REVIEW | REVIEW | section-C4-S4-dms-left-right-review-2026-01-29.tex | v0.3.3.0 | v0.3.3.0 (Due: ~Feb 2026) | PDF compiled ✅. LaTeX structure verified ✅. Awaiting author final review. 21 KB file. |
| **#17** | Documentation | C4:S4 DMS Left/Right - FINAL | OPEN | (TBD - after #16 closure) | v0.3.3.0 | v0.3.3.0 (Due: ~Feb 2026) | Tracks transition from review → final status. |
| **#18** | Documentation | C4:S4 DMS Left/Right - APPROVED | OPEN | (TBD - after #17 closure) | v0.3.3.0 | v0.3.3.0 (Due: ~Feb 2026) | Tracks final → approved status (post-integration). |
| **#19** | Documentation | C4:S4 DMS Left/Right - INTEGRATION COMPLETE | OPEN | (TBD - after #18 closure) | v0.3.3.0 | v0.3.3.0 (Due: ~Feb 2026) | Confirms Section 4.4 integrated into guide-v0.3.3.0 (PATCH). |
| **#20** | Documentation | C2 HOTAS Fundamentals - REVIEW | REVIEW | chapter-C2-hotas-fundamentals-dev-2026-01-25.tex | v0.4.0.0 | v0.4.0.0 (Due: ~Mar 2026) | Chapter 2 in dev status. Covers SOI, timing, master modes, switch categories. Awaiting promotion to review. |
| **#21** | Documentation | C2 HOTAS Fundamentals - FINAL | OPEN | (TBD - after #20 closure) | v0.4.0.0 | v0.4.0.0 (Due: ~Mar 2026) | Tracks transition from review → final status. |
| **#22** | Documentation | C2 HOTAS Fundamentals - APPROVED | OPEN | (TBD - after #21 closure) | v0.4.0.0 | v0.4.0.0 (Due: ~Mar 2026) | Tracks final → approved status (post-integration). |

### 8.2 Milestone Overview

| Milestone | Due Date | Completion | Open Issues | Closed Issues | Description |
|---|---|---|---|---|---|
| **v0.3.3.0** | ~Feb 2026 | 0/4 (0%) | 4 | 0 | DMS Section 4.4 (Left/Right) integration into guide (PATCH bump - section integration). Issues: #16 (REVIEW - current), #17 (FINAL), #18 (APPROVED), #19 (INTEGRATION). |
| **v0.4.0.0** | ~Mar 2026 | 0/3 (0%) | 3 | 0 | New Chapter (C2 HOTAS Fundamentals) integration (MINOR bump - new chapter). Issues: #20 (REVIEW), #21 (FINAL), #22 (APPROVED). |

### 8.3 Issue Workflow

Standard workflow for WIP progression through GitHub Issues:

1. **REVIEW Issue** (e.g., #16, #20) - WIP file promoted from dev → review status. Author conducts technical review.
2. **FINAL Issue** (e.g., #17, #21) - After REVIEW closure, WIP promoted review → final. Content approved, ready for integration.
3. **APPROVED Issue** (e.g., #18, #22) - After FINAL closure and integration into guide-v, WIP marked approved and archived.
4. **INTEGRATION COMPLETE Issue** (e.g., #19) - Confirms successful integration, version bump, and GitHub Release tag creation.

**Notes:**
- Issues linked to Milestones for version tracking (e.g., v0.3.3.0 PATCH, v0.4.0.0 MINOR).
- REVIEW issues remain OPEN until author confirms transition to FINAL.
- Milestone completion percentage reflects progress toward guide version release.

---

## 9. PRÓXIMAS METAS (NEXT TARGET)

Esta seção rastreia as prioridades ativas de desenvolvimento e os próximos marcos de integração.

### 🎯 **Target 1: Chapter 2 — HOTAS Fundamentals**

**Objetivo:** Integração do conteúdo fundamental sobre HOTAS (SOI, timing, modos mestres, categorias de switches).

**Status:**
- **WIP File:** `chapter-C2-hotas-fundamentals-dev-2026-01-25.tex`
- **Situação Atual:** dev (em desenvolvimento desde 2026-01-25)
- **Issues Relacionadas:**
  - #20: C2 HOTAS Fundamentals - REVIEW (aberta)
  - #21: C2 HOTAS Fundamentals - FINAL (aberta)
  - #22: C2 HOTAS Fundamentals - APPROVED (aberta)
- **Milestone:** v0.4.0.0 (Due: ~Mar 2026, 0/3 complete)

**Conteúdo:**
- SOI concept (Sensor of Interest)
- Short/long press timing mechanics
- Master modes (NAV, A-A, A-G, DGFT, MSL OVRD)
- HOTAS switch categories (TMS/DMS/CMS)
- Foundational material para todo o guide

**Próximos Passos:**
1. dev → review: Promoção após revisão técnica do autor
2. review → final: Aprovação final de conteúdo
3. final → approved: Integração no guide (v0.4.0.0 - **MINOR bump, new chapter**)

---

### 🎯 **Target 2: Chapter 4, Section 4.4 — DMS Right/Left Format Selection**

**Objetivo:** Conclusão da sequência de seções DMS com integração de DMS Left/Right (seleção de formato MFD).

**Status:**
- **WIP File:** `section-C4-S4-dms-left-right-review-2026-01-29.tex`
- **Situação Atual:** review (em revisão desde 2026-01-21, atualizado 2026-01-29)
- **Issues Relacionadas:**
  - #16: C4:S4 DMS Left/Right - REVIEW (aberta) ✅ PDF compilado
  - #17: C4:S4 DMS Left/Right - FINAL (aberta)
  - #18: C4:S4 DMS Left/Right - APPROVED (aberta)
  - #19: C4:S4 DMS Left/Right - INTEGRATION COMPLETE (aberta)
- **Milestone:** v0.3.3.0 (Due: ~Feb 2026, 0/4 complete)

**Conteúdo:**
- Overview da funcionalidade DMS Left/Right
- Functional Modes: Radar, NAV, Weapons
- Button Logic: OSB mapping e context switching
- Integration com SOI system
- Summary e referências de missão

**Validação:**
- ✅ LaTeX structure verified
- ✅ PDF compiled and generated (21 KB file)
- ⏳ Aguardando revisão final do autor

**Próximos Passos:**
1. review → final: Transição após aprovação do autor (#17)
2. final → integration: Merge no guide-v0.3.3.0 (#18) - **PATCH bump (section, not new chapter)**
3. Integration complete: GitHub Release tag 0.3.3.0 (#19)

---

### 🎯 **Target 3: Guide Version Roadmap**

**v0.3.3.0 (próximo PATCH):**
- Complete Chapter 4 Section 4.4 (DMS Left/Right)
- **PATCH bump** (section integration, not new chapter)
- Post-v0.3.2.1 infrastructure ready (hotastable 1.25 deployed)

**v0.4.0.0 (próximo MINOR):**
- New Chapter integration (C2 HOTAS Fundamentals OR C3 TMS complete)
- **MINOR bump** (new chapter entry into guide)
- Per VERSION-SYSTEM v4.2.1: MINOR increments ONLY when NEW CHAPTER enters

**v0.5.0.0 (futuro):**
- Additional new chapter
- Continue scaffolding toward Phase 1

---

**Resumo das Metas:**

| Target | Tipo | Status | Milestone | Próximo Passo Crítico | Version Bump |
|---|---|---|---|---|---|
| **C2 - HOTAS Fundamentals** | Chapter | dev | v0.4.0.0 (~Mar 2026, 0/3) | dev → review (Issue #20) | **MINOR** (new chapter) |
| **C4:S4 - DMS Left/Right** | Section | review | v0.3.3.0 (~Feb 2026, 0/4) | review → final (Issue #17) | **PATCH** (section) |
| **Guide v0.3.3.0** | Version | Planned | C4:S4 integration | Definir prioridade C4:S4 final review | **PATCH** |
| **Guide v0.4.0.0** | Version | Planned | New chapter | Definir prioridade C2 vs C3 | **MINOR** |

---

**END OF PROJECT TRACKING v5.0.0 - UPDATED SESSION 24 (2026-01-31)**