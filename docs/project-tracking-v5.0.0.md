# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-01-21, 22:00 PM -03  
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
| TEMPLATEStemplate-wip-V1.0.tex | V1.0 | Canonical WIP template | Per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning (V1.0). **UPDATED 18 Jan 2026:** New preamble deployed (report class, twoside, titlesec, improved headers/footers, float support). All future WIP files MUST copy from this updated template. | Established Session 9; Updated Session 17 with new preamble infrastructure. |
| TRAINING-MISSION-ABBREV-TABLE-v1.0 | v1.0 | Official source for mission abbreviations | Standardized abbreviations for all 33 BMS 4.38.1 training missions, for use when building Tables. | For reference when incorporating mission names. |

**Consequence:** All new WIP files going forward MUST follow BRIEFING-v0.2.0.1 Section 11 template specification (with updated preamble per 18 Jan 2026) and WIP-FILE-NAMING-v1.4 conventions.

---

## 2. PROJECT SNAPSHOT

Current state as of 2026-01-21, 22:00 PM -03 (Session 22 - DMS Left/Right WIP Promoted to Review):

### 2.1 High-Level Overview

- **Active Regime:** Pre-publication (0.x.x.x)
- **Phase:** Phase 0 -- Chapter Scaffolding
- **Current Guide Version:** guide-v0.3.2.0-20260119 (Section 4.3 DMS Down integrated, redaction corrections in 4.1 and 4.2, enhanced semantic clarity) — stored in wip/guide/, synchronized to guide.tex root
- **Chapters Planned:** 7
- **Chapters with narrative complete in development:** 3/7
  - Chapter 1 -- Introduction (narrative complete)
  - Chapter 5 -- CMS Sections 5.1, 5.2, 5.3 (narrative and tables complete)
  - **Chapter 4 -- DMS Sections 4.1, 4.2, 4.3, and 4.4 (LEFT/RIGHT - WIP IN REVIEW)**
    - Section 4.1 (Concept and SOI) - FINAL & INTEGRATED (with redaction corrections)
    - Section 4.2 (DMS Up: HUD Designation as SOI) - FINAL & INTEGRATED (with redaction corrections)
    - Section 4.3 (DMS Down: Toggle SOI Between Displays) - **FINAL & INTEGRATED (v0.3.2.0)** (promoted review→final 2026-01-18, integrated 2026-01-19)
    - Section 4.4 (DMS Left/Right: Format Selection) - **WIP REVIEW IN PROGRESS** (review status, 2026-01-21)
    - Section 4.5 (Master Mode Summary) - pending per unified Chapter 4 DMS blueprint v1.1
- **Chapters with structure scaffolded:** 4/7
  - Chapters 2 (HOTAS Fundamentals), 3 (TMS), 4 (DMS with 4.1, 4.2, 4.3 direction-based structure locked by blueprint v1.1), plus outlines for 6 (Training References) and 7 (HOTAS Visual Reference)
- **Tables filled:** 1 major HOTAS table (CMS, integrated Sections 5.2–5.3), 3 DMS tables (C4-S1 SOI-by-mode, C4-S2 DMS Up usage, C4-S3 DMS Down usage) all INTEGRATED with enhanced documentation (column explanations); remaining DMS tables (DMS Left/Right, DMS summary) pending per unified Chapter 4 DMS blueprint v1.1.

### 2.2 Layout Standard

Since v0.2.2.0 (geometry and table settings); v0.3.1.0 (preamble upgraded); v0.3.2.0 (semantic refinements):
- **Geometry:** Option D (A4, 2.0 cm side margins, 2.5 cm top/bottom)
- **Text width:** 17.0 cm
- **HOTAS table width:** 15.6 cm
- **Table arraystretch:** 1.25 (for readability)
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
- **Total Commits:** 198 (GitHub tracked)
- **Releases:** v0.3.2.0 (active, tagged on GitHub 2026-01-19), v0.3.1.0 (released 2026-01-18), v0.3.0.1 (archived), v0.3.0.0 (archived)

---

## 3. VERSION ROADMAP

### 3.1 Past and Current Versions (0.x.x.x)

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.3.1.0 | Preamble Infrastructure Upgrade | 0 | **✅ COMPLETED & RELEASED** | **SESSION 17 Update (18 Jan 2026):** Major preamble infrastructure upgrade deployed. Migration: article class → report class with twoside option. New features: titlesec chapter formatting, improved headers/footers for two-sided layout, float package for graphics control, enhanced table packages (booktabs, tabularx). BRIEFING-v0.2.0.1 Section 11 expanded to ~8,000 words with complete preamble documentation (11.3.1–11.3.11). guide.tex migrated and tested ✅. LaTeX compilation verified ✅. PDF output (guidetest.pdf) generated and approved by author ✅. template-wip-V1.0.tex updated with new preamble (all future WIP files compliant). Snapshot guide-v0.3.1.0-20260117.tex created, deployed to wip/guide/, and synchronized to guide.tex root. Previous snapshot (v0.3.0.1) moved to ARCHIVE/GUIDE/. GitHub Release tag 0.3.1.0 created and pushed to repository. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH). Next phase: Continue DMS content (Section 4.3 integration, Sections 4.4, 4.5) and TMS coverage per roadmap. |
| v0.3.2.0 | Chapter 4 -- DMS (Section 4.3 integrated, redaction corrections in 4.1-4.2) | 0 | **✅ COMPLETED & RELEASED** | **SESSION 20 Update (19 Jan 2026):** Section 4.3 (DMS Down) integrated into guide after final semantic refinements and redaction corrections applied to Sections 4.1 and 4.2. Changes: (1) Redaction corrections (grammar, clarity) applied throughout 4.1 and 4.2. (2) Section 4.3 integrated with enhanced semantic clarity: new intro paragraph separating display toggling from format transitions; replaced "valid SOI candidates are HUD, FCR, TGP, WPN..." with "HUD and both MFD" for clarity; HOTAS table Effect/Nuance column optimized (NAV, A-A, A-G refined; "picture evaluation" → "situational awareness"). Validation: Dash-34 alignment confirmed; LaTeX structure verified; cross-references checked. File size: 71935 bytes (guide-v0.3.2.0-20260119.tex in wip/guide/). GitHub Release tag 0.3.2.0 created and pushed. Version bump: v0.3.1.0 → v0.3.2.0 (MINOR bump). Next phase: Sections 4.4 (DMS Left/Right) and 4.5 (Master Mode Summary) WIP development per unified Chapter 4 DMS blueprint v1.1. |
| v0.4.0.0 | Chapter 3 -- TMS (Sections 3.1--3.5) | 0 | Planned | Integrate full TMS coverage after DMS completion. MINOR bump. |
| v0.5.0.0 | Chapter 2 -- HOTAS Fundamentals | 0 | Target | Integrate foundational SOI, short/long press timing, master modes. MINOR bump. |
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
| Chapters | chapter-CN-TITLE-STATUS-DATE.tex | chapter-C2-hotas-fundamentals-dev-2026-01-20.tex | dev, review, final, approved, deprecated |
| Sections | section-CN-SM-SK-TITLE-STATUS-DATE.tex | section-C5-S1-cms-concept-final-2026-01-07.tex | dev, review, final, approved, deprecated |
| Tables | table-CN-CONTEXT-SWITCH-STATUS-DATE.tex | table-C3-AA-TMS-review-2026-01-17.tex | dev, review, final, approved, deprecated |
| Notes | notes-CN-TOPIC-TYPE-DATE.md | notes-C4-dms-research-questions-2026-01-19.md | no formal status |
| Visuals | visual-CN-DESC-TYPE-STATUS-DATE.ext | visual-C7-hotas-layout-diagram-dev-2026-01-18.svg | dev, review, final, approved, deprecated |

**Key rules:**
- WIP status transitions (dev → review → final → approved) do not directly affect guide version numbers.
- Only integration into guide-v.tex triggers version bumps per VERSION-SYSTEM-v4.2.1.
- Active WIP lives in wip/; integrated or deprecated WIP moves to archive/.
- **UPDATED (Session 17):** All new WIP files MUST copy from TEMPLATES/template-wip-V1.0.tex per BRIEFING-v0.2.0.1 Section 11 (updated preamble, now with report class, twoside, titlesec, float support).

---

### 4.2 Active WIP Snapshot (as of 2026-01-21, 22:00 PM -03)

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
| 2026-01-20 | section-C4-S4-dms-left-right-dev-2026-01-20.tex | v0.3.2.0 | (pending) | WIP - IN DEVELOPMENT | section | DMS Chapter 4 Section 4.4 (DMS Left/Right: Format Selection). **SESSION 21 WIP GENERATION (20 Jan 2026):** Substantive research completed on DMS Left/Right architecture, OSB mapping, functional modes (radar, nav, weapons). WIP file generated from updated template-wip-V1.0.tex per BRIEFING-v0.2.0.1. Content structure: Overview, Functional Modes, Button Logic, Integration, Summary. Status: dev. Preamble: V1.0 (Session 17 compatible). Next: Author review cycle and integration into v0.4.0.0 per unified Chapter 4 DMS blueprint v1.1. |
| 2026-01-21 | section-C4-S4-dms-left-right-review-2026-01-21.tex | v0.3.2.0 | (pending) | WIP - REVIEW | section | DMS Chapter 4 Section 4.4 (DMS Left/Right: Format Selection). **SESSION 22 UPDATE (21 Jan 2026):** C4-S4 promoted dev → review. File renamed to reflect status change (dev-2026-01-20.tex → review-2026-01-21.tex). Content complete and ready for technical review cycle. PDF generated for visual validation. Status: review. Preamble: V1.0 (Session 17 compatible). Next: Author final review and transition to final status prior to integration into v0.4.0.0 per unified Chapter 4 DMS blueprint v1.1. |

**Status codes:**
- dev -- Draft, author working
- review -- Under human review, not yet final or integrated
- final -- Author approved, ready for integration
- approved -- Integrated into guide-v and archived
- deprecated -- Intentionally retired (superseded or abandoned)
- INTEGRATED -- WIP content already merged into a guide-v snapshot

---

## 5. SESSION LOG

High-level summary of each working session and resulting guide state.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 20 | 2026-01-19 | **v0.3.2.0** | v5.0.0 | **v0.3.2.0 INTEGRATION COMPLETE:** Section 4.3 integrated. Redaction corrections in 4.1 and 4.2. MINOR version bump. GitHub Release 0.3.2.0 tagged. Chapter 4 now FINAL & INTEGRATED (Sections 4.1, 4.2, 4.3). Next: DMS 4.4 and 4.5 WIP development. Total commits: 144. |
| 21 | 2026-01-20 | v0.3.2.0 (unchanged) | v5.0.0 | **DMS LEFT/RIGHT WIP DEVELOPMENT:** Substantive research on DMS Left/Right architecture completed. WIP section-C4-S4-dms-left-right-dev-2026-01-20.tex generated from canonical template. Status: dev. Content sections: Overview, Functional Modes, Button Logic, Integration, Summary. Preamble: V1.0. Awaiting author review and MFD image integration. Next: Integration into v0.4.0.0 per Chapter 4 DMS blueprint v1.1. |
| SESSION | 2026-01-21 | v0.3.2.0 (unchanged) | v5.0.0 | **DMS LEFT/RIGHT WIP PROMOTED TO REVIEW:** C4-S4 promoted dev → review status. File renamed: section-C4-S4-dms-left-right-dev-2026-01-20.tex → section-C4-S4-dms-left-right-review-2026-01-21.tex. PDF generated for visual validation. Content structure complete: Overview, Functional Modes, Button Logic, Integration, Summary. Status: review. Preamble: V1.0. Next: Author final review cycle and transition to final status prior to integration into v0.4.0.0. Total commits: 198. |

---

## 6. NEAR-TERM ROADMAP (Next Target Versions)

| Version | Area | Status | Notes |
|---|---|---|---|
| **v0.3.2.0** | Chapter 4 -- DMS (Sections 4.1–4.3 final→integrated, Sections 4.4–4.5 pending) | **✅ COMPLETED & RELEASED** | Section 4.3 integrated. Redaction corrections in 4.1 and 4.2. Total commits: 198. Next: DMS Sections 4.4 (Left/Right) and 4.5 (Master Mode Summary) WIP development. |
| **v0.4.0.0** | Chapter 4 -- DMS (Section 4.4 Left/Right + Section 4.5 Summary) | **WIP IN REVIEW** | Section 4.4 promoted to review status (2026-01-21). File: section-C4-S4-dms-left-right-review-2026-01-21.tex. PDF generated for visual validation. Next: Author final review cycle and integration into v0.4.0.0 after Section 4.5 completion. |
| **v0.5.0.0** | Chapter 3 -- TMS (all sections) | Planned | Full TMS coverage after DMS completion. |
| **v0.6.0.0** | Chapter 2 -- HOTAS Fundamentals | Target | Foundational SOI, short/long press timing, master modes. |
| **v0.7.0.0** | All 7 chapters scaffolded | Target | Transition to Phase 1. |

---

## 7. KEY METRICS

- **Total Commits:** 198 (GitHub tracked)
- **Latest Version:** v0.3.2.0 (released 2026-01-19)
- **Current Phase:** Phase 0 -- Chapter Scaffolding
- **C4-S4 Status:** WIP - REVIEW (as of 2026-01-21)
- **Last Updated:** 2026-01-21, 22:00 PM -03

---

**END OF PROJECT TRACKING v5.0.0 - UPDATED SESSION 22**
