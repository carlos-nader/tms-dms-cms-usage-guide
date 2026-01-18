# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-01-18, 06:39 PM -03  
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

Current state as of 2026-01-18, 06:39 PM -03 (Session 19 - C4-S3 Finalized):

### 2.1 High-Level Overview

- **Active Regime:** Pre-publication (0.x.x.x)
- **Phase:** Phase 0 -- Chapter Scaffolding
- **Current Guide Version:** guide-v0.3.1.0-20260117 (Preamble infrastructure upgrade: report class, twoside, titlesec, improved headers/footers, float support) — stored in wip/guide/, synchronized to guide.tex root
- **Chapters Planned:** 7
- **Chapters with narrative complete in development:** 3/7
  - Chapter 1 -- Introduction (narrative complete)
  - Chapter 5 -- CMS Sections 5.1, 5.2, 5.3 (narrative and tables complete)
  - **Chapter 4 -- DMS Sections 4.1 and 4.2 (narrative and tables COMPLETE and INTEGRATED)**
    - Section 4.1 (Concept and SOI) - FINAL & INTEGRATED
    - Section 4.2 (DMS Up: HUD Designation as SOI) - FINAL & INTEGRATED
    - Section 4.3 (DMS Down: Toggle SOI Between Displays) - **FINAL & READY FOR INTEGRATION** (promoted review→final 2026-01-18)
    - Sections 4.4 (DMS Left/Right) and 4.5 (Master Mode Summary) pending per unified Chapter 4 DMS blueprint v1.1
- **Chapters with structure scaffolded:** 4/7
  - Chapters 2 (HOTAS Fundamentals), 3 (TMS), 4 (DMS with 4.1, 4.2, 4.3 direction-based structure locked by blueprint v1.1), plus outlines for 6 (Training References) and 7 (HOTAS Visual Reference)
- **Tables filled:** 1 major HOTAS table (CMS, integrated Sections 5.2–5.3), 2 DMS tables (C4-S1 SOI-by-mode, C4-S2 DMS Up usage), and 1 DMS Down usage table (C4-S3) all INTEGRATED with enhanced documentation (column explanations); remaining DMS tables (DMS Left/Right, DMS summary) pending per unified Chapter 4 DMS blueprint v1.1.

### 2.2 Layout Standard

Since v0.2.2.0 (geometry and table settings); v0.3.1.0 (preamble upgraded):
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
- **Total Commits:** 121 (GitHub tracked)
- **Releases:** v0.3.1.0 (active, tagged on GitHub 2026-01-18), v0.3.0.1 (archived), v0.3.0.0 (archived)

---

## 3. VERSION ROADMAP

### 3.1 Past and Current Versions (0.x.x.x)

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.3.1.0 | Preamble Infrastructure Upgrade | 0 | **✅ COMPLETED & RELEASED** | **SESSION 17 Update (18 Jan 2026):** Major preamble infrastructure upgrade deployed. Migration: article class → report class with twoside option. New features: titlesec chapter formatting, improved headers/footers for two-sided layout, float package for graphics control, enhanced table packages (booktabs, tabularx). BRIEFING-v0.2.0.1 Section 11 expanded to ~8,000 words with complete preamble documentation (11.3.1–11.3.11). guide.tex migrated and tested ✅. LaTeX compilation verified ✅. PDF output (guidetest.pdf) generated and approved by author ✅. template-wip-V1.0.tex updated with new preamble (all future WIP files compliant). Snapshot guide-v0.3.1.0-20260117.tex created, deployed to wip/guide/, and synchronized to guide.tex root. Previous snapshot (v0.3.0.1) moved to ARCHIVE/GUIDE/. GitHub Release tag 0.3.1.0 created and pushed to repository. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH). Next phase: Continue DMS content (Section 4.3 finalized, Sections 4.4, 4.5) and TMS coverage per roadmap. |
| v0.3.2.0 | Chapter 4 -- DMS (Section 4.3 final→integrate, Sections 4.4, 4.5 WIP) | 0 | Planned | Complete DMS chapter with remaining direction-based sections. Section 4.3 now FINAL; ready for integration. Sections 4.4 (DMS Left/Right) and 4.5 (Master Mode Summary) in WIP creation per unified Chapter 4 DMS blueprint v1.1. PATCH bump. |
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

### 4.2 Active WIP Snapshot (as of 2026-01-18, 06:39 PM -03)

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
| 2026-01-18 | section-C4-S3-dms-down-final-2026-01-18.tex | v0.3.1.0 | v0.3.1.0 (pending integration) | **FINAL** | section | DMS Chapter 4 Section 4.3 (DMS Down: Toggle SOI Between Displays). Refined intro and Effect/Nuance column per semantic clarity (HUD and both MFD vs format lists). 4.3.1 (DMS Down Effectiveness) subsections complete; 4.3.2 HOTAS table finalized; 4.3.3 exception states documented. Status promoted review→final. Ready for integration into v0.3.2.0. |

**CRITICAL UPDATE (18 Jan 2026):** TEMPLATES/template-wip-V1.0.tex has been updated with NEW preamble as of Session 17. All future WIP files MUST copy from this updated template. Previous WIP files created with older preamble (article class) may require manual preamble migration if integration is planned. See BRIEFING-v0.2.0.1 Section 11 for complete preamble specification. Canonical template-wip-V1.0.tex contains:
- Document class: `\documentclass[11pt, a4paper, twoside]{report}`
- NEW packages: titlesec (chapter formatting), float (graphics float placement), booktabs/tabularx (tables)
- Improved headers/footers for twoside layout with chapter markers and page numbers
- Correct hotastable environment with proper longtable header ordering
- Geometry: 2.0 cm margins, 2.5 cm top/bottom, 1.5× line spacing
- All version control macros and reference macros in place
- Preamble tested and verified ✅

**All WIP files created after 18 Jan 2026 are considered "V1.0-compatible" (using updated Session 17 template).**

**Status codes:**
- dev -- Draft, author working
- review -- **Under human review, not yet final or integrated**
- final -- Author approved, ready for integration
- approved -- Integrated into guide-v and archived
- deprecated -- Intentionally retired (superseded or abandoned)
- INTEGRATED -- WIP content already merged into a guide-v snapshot

---

### 4.3 WIP Integration Timeline & Decisions

Summary of major decisions and changes per working session. Earlier sessions 1–6 documented in legacy tracking files; from v5.0.0 onward, sessions logged here.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 7 | 2026-01-08 | v0.2.2.0 | v4.1.2 | Layout Option D and hotastable adopted. CMS 5.1 fully integrated. Chapter 5 structure (5.1–5.3) refined. WIP files for 5.2 and 5.3 created in review status. |
| 8 | 2026-01-09 | v0.2.2.0 (unchanged) | v5.0.0 | Project brought under Git/GitHub. Local root normalized to projeto-bms. Folders WIP, ARCHIVE, docs created and aligned with WIP-FILE-NAMING governance. Centralized in .md files under docs; DOCX exports via md-to-docx. VS Code and Git CLI configured. |
| 9 | 2026-01-09 | v0.2.2.0 (unchanged) | v5.0.0 | **Template establishment:** BRIEFING-v0.2.0.1 Section 11 complete template specification. WIP-NAMING-v1.4 Section 0.5 "How to Create WIP File". VERSION-SYSTEM-v4.2.1 references updated. TEMPLATES/template-wip-V1.0.tex created and locked. Going forward: All new WIP files MUST use template. |
| 10 | 2026-01-10 | v0.2.3.1 | v5.0.0 | **CMS 5.2 Integration:** Integrated CMS Switch Actuation narrative and main HOTAS table into Chapter 5. C5-S2 WIP marked ready for archival. |
| 11 | 2026-01-11 | v0.2.4.0 | v5.0.0 | **CMS 5.3 Integration:** Integrated Block and Variant Notes narrative and 2 reference tables. Validation: LaTeX syntax verified; Dash-34 alignment confirmed. WIP file moved to ARCHIVE. Versioning: v0.2.3.1 → v0.2.4.0 (MINOR bump). |
| 12 | 2026-01-12 | v0.2.4.0 (unchanged) | v5.0.0 | **DMS C4-S1 WIP Created:** Generated section-C4-S1-concept-and-soi-dev-2026-01-12.tex from TEMPLATES/template-wip-V1.0.tex. Full Compliance: 100% verified. Status: dev. Canonical version established; ready for author review cycle. |
| 13 | 2026-01-13 | v0.2.4.0 (unchanged) | v5.0.0 | **C4-S1 Manual Integration + Research Validation:** C4-S1 manually integrated by author with new Table "Valid SOI Displays by Master Mode". Status: dev → **review**. Deep technical research: HUD/HMCS SOI constraints validated against Dash-34. |
| 14 | 2026-01-14 | v0.2.4.0 (unchanged) | v5.0.0 | **C4 Multi-File Development Sprint:** C4-S1-S3 new subsection created. C4-S2 narrative reviewed and approved (95% complete). Comprehensive Dash-34 validation completed. Target: v0.3.0.0 integration after formal review cycles. |
| 15 | 2026-01-15 | **v0.3.0.0** | v5.0.0 | **INTEGRATION COMPLETE:** C4-S1 and C4-S2 (DMS Up) both FINAL and **INTEGRATED into guide-v0.3.0.0-20260115**. Version macros updated. Snapshot saved and validated. Prior snapshot archived. WIP files archived (approved status). Next: DMS Down/Left-Right/Summary per blueprint v1.1. |
| 16 | 2026-01-16 | **v0.3.0.1** | v5.0.0 | **PATCH v0.3.0.1 - Documentation Enhancement:** Section 4.2 (DMS Up) table column explanations added, aligned with Section 5.2 documentation pattern. No structural changes; PATCH-level refinement only. Validation: LaTeX compiled ✅, PDF generated ✅. Snapshot guide-v0.3.0.1-20260116.tex created and deployed. Previous snapshot (v0.3.0.0) moved to ARCHIVE/GUIDE/. Next phase: Infrastructure upgrade or content integration. |
| 17 | 2026-01-18 | **v0.3.1.0** | v5.0.0 | **PATCH v0.3.1.0 - PREAMBLE INFRASTRUCTURE UPGRADE:** Major preamble migration: article → report class with twoside option. New packages: titlesec (chapter formatting), float (graphics control), booktabs/tabularx (advanced tables). Headers/footers enhanced for professional two-sided layout. BRIEFING-v0.2.0.1 Section 11 expanded to ~8,000 words with complete documentation (11.3.1–11.3.11). guide.tex migrated and tested via guidetest.tex ✅. LaTeX compilation verified ✅, PDF approved by author ✅. template-wip-V1.0.tex updated with new preamble (all future WIP compliant). Snapshot guide-v0.3.1.0-20260117.tex created in wip/guide/, synchronized to guide.tex root. GitHub Release tag 0.3.1.0 created and pushed. Version bump: v0.3.0.1 → v0.3.1.0. Infrastructure now production-ready. |
| 18 | 2026-01-18 | v0.3.1.0 (unchanged) | v5.0.0 | **FILE STRUCTURE ALIGNMENT:** GitHub repository audit completed (INTEGRATED-FILES.md). WIP C4-S3 identified as promoted from dev to review status (2026-01-17); file renamed and optimized. Guide snapshot v0.3.1.0-20260117.tex confirmed in wip/guide/ with size 62,878 bytes; synchronized to guide.tex root. PROJECT-TRACKING updated to reflect actual file locations and statuses. All 7 critical file structure updates implemented. Ready for next content development sprint. |
| 19 | 2026-01-18 | v0.3.1.0 (unchanged) | v5.0.0 | **SESSION 19 - DMS DOWN SECTION FINALIZED:** C4-S3 (DMS Down) promoted from review to FINAL. Major refinements: (1) Intro clarification with "It is important to note..." to separate display toggling from format transitions. (2) Semantic refinement throughout: replaced "valid SOI candidates are HUD, FCR, TGP, WPN..." with "HUD and both MFD" to eliminate confusion with format selection (DMS Right/Left) vs display selection (DMS Down). (3) Effect/Nuance column in HOTAS table updated: NAV, A-A, A-G all refined; A-A term "picture evaluation" changed to "situational awareness". (4) Full subsection structure verified: 4.3.1 (DMS Down Effectiveness) with paragraph-based organization; 4.3.2 HOTAS table (3 rows + mission refs); 4.3.3 Exception States (Snowplow, MARK/OFLY). Validation: Dash-34 alignment confirmed; LaTeX structure verified; cross-references checked. File size: 15,171 bytes. Preamble compatibility: V1.0 (updated Session 17). Next action: Integrate into guide-v0.3.2.0 after section 4.4 (DMS Right/Left) completion per unified Chapter 4 DMS blueprint v1.1. |

---

## 5. SESSION LOG

High-level summary of each working session and resulting guide state.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 7 | 2026-01-08 | v0.2.2.0 | v4.1.2 | Layout finalized (Option D, 1.25). CMS 5.1 integrated. Chapter 5 structure refined. WIP 5.2, 5.3 in review. |
| 8 | 2026-01-09 | v0.2.2.0 | v5.0.0 | Git/GitHub setup. Folder structure aligned with governance. VS Code configured. |
| 9 | 2026-01-09 | v0.2.2.0 | v5.0.0 | BRIEFING Section 11 finalized. Template established (mandatory). All new WIP MUST use canonical template. |
| 10 | 2026-01-10 | v0.2.3.1 | v5.0.0 | CMS 5.2 integrated (HOTAS table + narrative). C5-S2 WIP archived. |
| 11 | 2026-01-11 | v0.2.4.0 | v5.0.0 | CMS 5.3 integrated (Block/Variant notes). Chapter 5 structurally complete. DMS Chapter 4 targeted next. |
| 12 | 2026-01-12 | v0.2.4.0 | v5.0.0 | DMS C4-S1 WIP created from canonical template. Author review cycle initiated. |
| 13 | 2026-01-13 | v0.2.4.0 | v5.0.0 | C4-S1 manually integrated with Table. Status: review. Deep technical research completed. |
| 14 | 2026-01-14 | v0.2.4.0 | v5.0.0 | C4-S1-S3 subsection created. C4-S2 approved (95% complete). Comprehensive validation. Target: v0.3.0.0 integration. |
| 15 | 2026-01-15 | **v0.3.0.0** | v5.0.0 | **C4 INTEGRATION COMPLETE.** C4-S1 and C4-S2 both FINAL, audited, and INTEGRATED. MINOR bump. Next: DMS Down/Left-Right/Summary. |
| 16 | 2026-01-16 | **v0.3.0.1** | v5.0.0 | **PATCH version created:** Section 4.2 table explanations added. Documentation enhancement only. Snapshot saved and deployed. |
| 17 | 2026-01-18 | **v0.3.1.0** | v5.0.0 | **INFRASTRUCTURE UPGRADE COMPLETE:** BRIEFING Section 11 expanded. Preamble migrated to report class + twoside. Templates updated. guide.tex tested and verified ✅. GitHub Release 0.3.1.0 tagged. Infrastructure production-ready. |
| 18 | 2026-01-18 | v0.3.1.0 (unchanged) | v5.0.0 | **FILE STRUCTURE ALIGNMENT:** Repository audit completed. WIP C4-S3 status updated (dev → review). Guide file locations and sizes confirmed. Tracking document synchronized with actual GitHub state. |
| 19 | 2026-01-18 | v0.3.1.0 (unchanged) | v5.0.0 | **C4-S3 FINALIZED:** DMS Down section promoted review→final. Intro clarification added. Semantic refinement: HUD/MFD displays vs format selection terminology. HOTAS table column 5 optimized. Exception states documented. Ready for integration into v0.3.2.0. |

---

## 6. PROJECT PRIORITIES & PHASES

### 6.1 Current Priorities (Post-v0.3.1.0)

| Phase | Target Versions | Indicative Range | Milestone |
|---|---|---|---|
| **Phase 0** | v0.1.0.0 – v0.7.0.0 | 05–22 Jan 2026 | All 7 chapters scaffolded; layout locked at v0.2.2.0; CMS chapter structurally complete; DMS Chapter 4 sections 4.1–4.2 integrated with documentation enhancements; Section 4.3 finalized and ready for integration; preamble infrastructure upgraded to production-ready (v0.3.1.0). |
| **Phase 1** | v1.0.0 – v1.0.x | TBD | Major HOTAS tables (TMS/DMS/CMS) populated and technically validated. |
| **Phase 2** | v2.0.0-RC1/RC2/Stable | TBD | Final review, community feedback, public release. |

**Phase boundaries and dates are guidelines.** Actual transitions must be explicitly recorded in this tracking document.

### 6.2 Near-Term Roadmap (Next Target Versions)

| Version | Area | Status | Notes |
|---|---|---|---|
| **v0.3.1.0** | Preamble Infrastructure Upgrade | **✅ COMPLETED & RELEASED** | **SESSION 17 COMPLETE (18 Jan 2026):** BRIEFING-v0.2.0.1 Section 11 expanded with detailed preamble documentation. guide.tex migrated to report class + twoside + titlesec. Templates updated and tested ✅. GitHub Release 0.3.1.0 tagged. Infrastructure now production-ready for continued content development. |
| **v0.3.2.0** | Chapter 4 -- DMS (Section 4.3 final→integrate, Sections 4.4, 4.5 WIP) | Planned | Complete DMS chapter with remaining direction-based sections. Section 4.3 now FINAL; ready for integration. Sections 4.4 (DMS Left/Right) and 4.5 (Master Mode Summary) in WIP creation per unified Chapter 4 DMS blueprint v1.1. PATCH bump. |
| **v0.4.0.0** | Chapter 3 -- TMS (all sections) | Planned | Full TMS coverage after DMS completion. MINOR bump. |
| **v0.5.0.0** | Chapter 2 -- HOTAS Fundamentals | Target | Foundational SOI, short/long press timing, master modes. MINOR bump. |
| **v0.7.0.0** | All 7 chapters scaffolded | Target | Transition to Phase 1. Chapters 2, 3, 4, 5, 6, 7 with basic narrative. MINOR bump. |

---

## 7. FILE STATUS SUMMARY

### 7.1 Guide Files (guide-v.tex)

| File (relative path) | Status | Type | Last Modified | Size | Next Action |
|---|---|---|---|---|---|
| guide-v0.1.4.0-20260106.tex | archive | main guide | 2026-01-06 | — | Reference only; pre-CMS integration. |
| guide-v0.2.0.1-20260108.tex | archive | main guide | 2026-01-08 | — | Reference only; CMS 5.1 integrated. |
| guide-v0.2.1.0-20260108.tex | archive | main guide | 2026-01-08 | — | Reference only; Ch. 5 structure refined. |
| guide-v0.2.2.0-20260108.tex | archive | main guide | 2026-01-08 | — | Reference only; layout Option D applied. |
| guide-v0.2.3.1-20260110.tex | archive | main guide | 2026-01-10 | — | Reference only; CMS 5.2 integrated. |
| guide-v0.2.4.0-20260111.tex | archive | main guide | 2026-01-11 | — | Historical snapshot; moved to ARCHIVE/GUIDE/. |
| guide-v0.3.0.0-20260115.tex | archive | main guide | 2026-01-15 | — | Historical snapshot (v0.3.0.0); moved to ARCHIVE/GUIDE/. C4-S1 and C4-S2 integrated. |
| guide-v0.3.0.1-20260116.tex | archive | main guide | 2026-01-16 | — | Historical snapshot (v0.3.0.1); moved to ARCHIVE/GUIDE/. Section 4.2 table explanations added (PATCH). Previous preamble (article class). |
| wip/guide/guide-v0.3.1.0-20260117.tex | **active** | main guide (WIP) | 2026-01-18 03:56:16 | 62,878 bytes | **CURRENT DEVELOPMENT SNAPSHOT (v0.3.1.0):** Stored in wip/guide/ for version control and iteration. Preamble infrastructure upgrade complete (report class, twoside, titlesec, improved headers/footers, enhanced tables, float support). LaTeX compilation verified ✅. Synchronized to guide.tex (repository root) as working version. Created 2026-01-17, last modified by GitHub workflow 2026-01-18 03:56:16. Use as base for v0.3.2.0 or future content additions. GitHub Release tag 0.3.1.0 references this version. |
| guide.tex | **active** | main guide (root) | 2026-01-18 03:56:16 | 62,878 bytes | **ACTIVE WORKING GUIDE (root copy):** Synchronized with wip/guide/guide-v0.3.1.0-20260117.tex. Deployed to repository root for direct access and compilation. Byte-identical to 20260117 snapshot (62,878 bytes). Use this as the primary guide.tex for development and LaTeX compilation in local workflow. |

---

### 7.2 WIP Files (wip/ folder)

| File (relative path) | Version | Type | Status | Last Modified | Size | Short Purpose |
|---|---|---|---|---|---|---|
| wip/section-C4-S1-concept-soi-final-2026-01-14.tex | -- | section | **final** | 2026-01-14 | — | DMS Chapter 4 Section 4.1 (Concept and SOI). Consolidated FINAL narrative + SOI-by-mode table + HUD/HMCS clarification. **NOW ARCHIVED (approved status).** |
| wip/section-C4-S2-dms-up-final.tex | -- | section | **final** | 2026-01-15 | — | DMS Chapter 4 Section 4.2 (DMS Up: HUD Designation as SOI). FINAL narrative and HOTAS table. **NOW ARCHIVED (approved status).** |
| wip/section-C4-S3-dms-down-final-2026-01-18.tex | -- | section | **FINAL** | 2026-01-18 15:42:49 | 15,171 bytes | DMS Chapter 4 Section 4.3 (DMS Down: Toggle SOI Between Displays). **STATUS PROMOTED: review → FINAL (2026-01-18).** Refined intro with "It is important to note..." clause separating display toggling from format transitions. Semantic refinement: replaced "valid SOI candidates FCR, TGP, WPN..." with "HUD and both MFD" throughout (eliminates confusion with DMS Right/Left format selection). HOTAS table Effect/Nuance column (col 5) optimized: NAV, A-A, A-G all updated; "picture evaluation" → "situational awareness" (A-A row). Full subsection structure verified: 4.3.1 (DMS Down Effectiveness), 4.3.2 HOTAS table, 4.3.3 Exception States. Preamble: V1.0 (updated Session 17, compatible). Next: Integration cycle for v0.3.2.0 after DMS 4.4, 4.5 WIP completion. |
| wip/section-C4-S2-dms-up-down-deprecated-2026-01-14.tex | -- | section | **deprecated** | 2026-01-14 | — | DEPRECATED: Combined C4-S2 (DMS Up/Down) WIP file. Superseded by standalone DMS Up FINAL file and future DMS Down WIP. **Moved to ARCHIVE/ for audit and historical reference.** |
| wip/section-C4-S3-dms-format-cycling-deprecated-2026-01-13.tex | -- | section | **deprecated** | 2026-01-13 | — | DEPRECATED: Early DMS format-cycling attempt. Superseded by planned 4.4 rewrite (DMS Left/Right) per unified Chapter 4 blueprint v1.1. **Moved to ARCHIVE/ for audit.** |

**Status (2026-01-18 18:39 PM):** WIP/ folder synchronized with GitHub state (INTEGRATED-FILES.md). **KEY UPDATE:** C4-S3 dms-down WIP file confirmed promoted to FINAL status (date: 2026-01-18, last modified: 2026-01-18 15:42:49). File size optimized to 15,171 bytes. Ready for next sprint: C4-S3 integration into v0.3.2.0, C4-S4 (DMS Left/Right), C4-S5 (DMS Summary) WIP creation per unified Chapter 4 DMS blueprint v1.1. All new WIP files created after 18 Jan 2026 should copy from updated template-wip-V1.0.tex.

---

### 7.3 Governance & Reference Files (docs/ folder)

| File (relative path) | Version | Type | Status | Short Purpose |
|---|---|---|---|---|
| docs/BRIEFING-v0.2.0.1.md | 0.2.0.1 | reference | active | Project brief with **EXPANDED Section 11 (18 Jan 2026):** Complete preamble architecture documentation (11.3.1–11.3.11) covering document class (report, twoside), encoding/fonts, geometry/spacing, colors/hyperlinks, headers/footers, chapter formatting (titlesec), tables/columns, graphics/floats (float package), hotastable environment, reference macros, version control. Supersedes v0.1.4.1. ~8,000 words. Preamble code VERIFIED and TESTED. |
| docs/WIP-FILE-NAMING-v1.4.md | 1.4 | reference | active | WIP naming convention. Section 0.5: "How to Create WIP File" (3-step workflow). Section 9: Summary + best practices. Supersedes v1.3. |
| docs/VERSION-SYSTEM-v4.2.1.md | 4.2.1 | reference | active | Guide versioning rules. References updated to WIP-FILE-NAMING-v1.4 & BRIEFING-v0.2.0.1 Section 11; 3-way integration clarified. Supersedes v4.2. |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | template | active | **UPDATED 18 Jan 2026 (Session 17):** Canonical WIP template per BRIEFING-v0.2.0.1 Section 11 with NEW preamble. Preamble/metadata/hotastable locked. Independent versioning (V1.0). ALL new WIP files created after 18 Jan 2026 MUST copy from this updated template. Includes: report class, twoside, titlesec, improved headers/footers, float support, booktabs/tabularx. |
| docs/PROJECT-TRACKING-v5.0.0.md | 5.0.0 | tracking | active | Unified tracking document with Git/GitHub integration. **Updated 18 Jan 2026 (Sessions 17–19)** to reflect v0.3.1.0 release, preamble infrastructure upgrade, GitHub Release tagging, file structure alignment per INTEGRATED-FILES audit, WIP C4-S3 status promotion (dev → review → FINAL), and Session 19 finalization of DMS Down section. |
| docs/BRIEFING-v0.2.0.1.docx | 0.2.0.1 | export | derived | DOCX export from Markdown. |
| docs/VERSION-SYSTEM-v4.2.1.docx | 4.2.1 | export | derived | DOCX export from Markdown. |
| docs/WIP-FILE-NAMING-v1.4.docx | 1.4 | export | derived | DOCX export from Markdown. |
| docs/PROJECT-TRACKING-v5.0.0.docx | 5.0.0 | export | derived | DOCX export from this Markdown via md-to-docx script. |
| docs/TRAINING-MISSION-ABBREV-TABLE-v1.0.docx | 1.0 | export | derived | DOCX export from source. |

**Maintenance rule:**
- All structural or governance changes to tracking MUST be made in PROJECT-TRACKING-v5.0.0.md (this file).
- DOCX versions are GENERATED from this file and NEVER edited manually.
- At the end of each working session, this document should be updated (especially Sections 2, 4.2, 4.3, 5, 6, 7) to capture new state and decisions.
- Version number of PROJECT-TRACKING-v5.0.0 does NOT change with content updates. Version marks the baseline structure, not the state. (Designed for frequent updates; version reserved for structural overhauls only.)

---

### 7.4 Update Log

Track high-level edits to this tracking document itself.

| Date | Change | Sections Affected | Reason |
|---|---|---|---|
| 2026-01-11 | Updated guide version to v0.2.4.0; integrated Section 5.3; updated priorities to next DMS target | 2, 3.1, 3.2, 4.2, 4.3, 5, 6, 7 | Section 5.3 (CMS Block/Variant Notes) integration complete. Chapter 5 now structurally complete. |
| 2026-01-12 | Added Session 12; DMS WIP C4-S1 created; updated Active WIP Snapshot; enhanced Current Priorities | 4.2, 4.3, 5, 6.1, 6.2, 7.2 | DMS Section 4.1 WIP file generation complete with 100% compliance. Author review cycle initiated. |
| 2026-01-13 | Added Session 13; C4-S1 manual integration by author; table integrated; status updated to review; updated Active WIP Snapshot and Session Log | 4.2, 4.3, 5, 6.1, 6.2, 7.2, 7.4 | C4-S1 manually integrated by author with official HOTAS table pattern. Status: review. |
| 2026-01-14 | Session 14 completions: C4-S1-S3 subsection created; C4-S2 approved; validation completed. Updated Sections 2, 3, 4, 5, 6, 7. | 2, 3, 4, 5, 6, 7 | C4-S1-S3 subsection addresses HUD/HMCS SOI clarification. C4-S2 approved (95% complete). |
| 2026-01-15 | **Session 15 INTEGRATION COMPLETE:** C4-S1 + C4-S2 INTEGRATED into guide-v0.3.0.0-20260115. Version macros updated. Snapshot deployed. WIP files archived. Roadmap refreshed. | 2.1, 3.1, 4.2, 4.3, 5, 6.2, 7.2, 7.4 | C4 integration complete. MINOR bump v0.2.4.0 → v0.3.0.0. Next: DMS Down/Left-Right/Summary. |
| 2026-01-16 | **Session 16 PATCH UPDATE:** Section 4.2 (DMS Up) table column explanations added. No structural changes; PATCH-level refinement. Snapshot v0.3.0.1 saved and deployed. | 2.1, 3.1, 4.2, 4.3, 5, 6.2, 7.1, 7.4 | PATCH version v0.3.0.1 created. PATCH bump v0.3.0.0 → v0.3.0.1 complete. |
| 2026-01-18 | **SESSION 17: INFRASTRUCTURE UPGRADE TO v0.3.1.0** | 1, 2, 3, 4, 5, 6, 7 | BRIEFING-v0.2.0.1 Section 11 expanded with complete preamble documentation (11.3.1–11.3.11, ~8,000 words). guide.tex migrated to report class, twoside, titlesec, improved headers/footers, enhanced table packages, float support. Tested via guidetest.tex ✅ (LaTeX compilation verified, PDF approved). template-wip-V1.0.tex updated with new preamble (all future WIP compliant). Snapshot guide-v0.3.1.0-20260117.tex created in wip/guide/, synchronized to guide.tex root. GitHub Release tag 0.3.1.0 created and pushed to repository. Preamble infrastructure now production-ready. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH - infrastructure upgrade). Next: Continue content development (DMS Sections 4.3–4.5, TMS coverage). |
| 2026-01-18 | **SESSION 18: FILE STRUCTURE ALIGNMENT & WIP STATUS UPDATE** | 2, 3, 4, 5, 6, 7 | GitHub repository audit completed via INTEGRATED-FILES.md (generated 2026-01-18 03:56:17). **7 Critical File Structure Updates Implemented:** (1) C4-S3 WIP status promoted dev → review (date 2026-01-17); (2) C4-S3 file size optimized to 15,371 bytes; (3) guide-v0.3.1.0 location corrected (wip/guide/, not root); (4) guide-v0.3.1.0 date corrected (20260117, not 20260118); (5) guide-v0.3.1.0 size updated (62,878 bytes, was ~58,500); (6) guide.tex root confirmed synchronized with 20260117 snapshot; (7) Archive subfolders structure clarified (GUIDE/, WIP/). PROJECT-TRACKING now aligned with actual GitHub repository state per INTEGRATED-FILES.md audit. No version bump. Ready for content development. |
| 2026-01-18 | **SESSION 19: C4-S3 DMS DOWN FINALIZED** | 2.1, 3.1, 4.2, 4.3, 5, 6.2, 7.2, 7.4 | DMS Section 4.3 (DMS Down: Toggle SOI Between Displays) promoted from review to FINAL. Major semantic refinement: (1) Intro clarification separating display toggling (DMS Down) from format transitions (DMS Right/Left) with new paragraph: "It is important to note that DMS Down transitions SOI between displays—HUD and the two MFDs—without changing which format is currently displayed on any MFD." (2) Throughout sections 4.3.1: replaced "valid SOI candidates are HUD, FCR, TGP, WPN..." with "HUD and both MFD" for semantic clarity (eliminates confusion with DMS Right/Left, which manipulates formats). (3) HOTAS table column 5 (Effect/Nuance) optimized: all three rows (NAV, A-A, A-G) refined; A-A term "picture evaluation" changed to "situational awareness". (4) Full structure verified: 4.3.1 (subsections for NAV/A-G/A-A), 4.3.2 HOTAS table with 3 rows + mission training refs, 4.3.3 Exception States (Snowplow, MARK/OFLY). Validation complete: Dash-34 alignment, LaTeX syntax, cross-references. File size: 15,171 bytes (optimized). Preamble: V1.0 (Session 17 updated). Next: Integrate into guide-v0.3.2.0 after DMS 4.4 (Left/Right) and 4.5 (Summary) WIP completion per unified Chapter 4 DMS blueprint v1.1. |

---

## END OF PROJECT TRACKING v5.0.0

**For inquiries or updates, contact:** Carlos "Metal" Nader  
**Last updated:** 2026-01-18, 06:39 PM -03  
**Status:** Ready for use / Download
