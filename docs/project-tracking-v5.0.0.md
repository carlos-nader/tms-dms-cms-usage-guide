%============================================================================
% PROJECT TRACKING - Falcon BMS TMS/DMS/CMS HOTAS Guide
% Version: v5.1.0
% Last Updated: 2026-01-26, 0014 AM -03
% Status: Updated with Chapter 2 WIP progress (Session 23)
%============================================================================

# PROJECT TRACKING v5.1.0
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version**: v5.1.0  
**Regime**: Pre-publication 0.x.x.x  
**Project Start**: 2026-01-05  
**Last Updated**: 2026-01-26, 0014 AM -03  
**Repository**: carlos-nader/tms-dms-cms-usage-guide

---

## 1. GOVERNANCE LAYER

Reference documents that define project structure:

| Document | Version | Purpose | Scope | Notes |
|----------|---------|---------|-------|-------|
| VERSION-SYSTEM-v4.2.1 | v4.2.1 | Versioning rules for guide-v | Defines 0.x.x.x vs x.y.z regimes, MAJOR/MINOR/PATCH/SUBPATCH semantics, build date rules | Updated Session 9 refs v1.4, BRIEFING-v0.2.0.1 alignment documented |
| BRIEFING-v0.2.0.1 | v0.2.0.1 | Content and layout brief, template specification | Scope, style, layout standard. Geometry Option D, hotastable 15.6 cm, arraystretch 1.25, high-level roadmap | Section 11 EXPANDED 18 Jan 2026 — Complete preamble architecture documentation 11.3.1–11.3.11 (document class report, twoside, encoding/fonts, geometry/spacing, colors/hyperlinks, headers/footers, chapter formatting titlesec, tables/columns, graphics/floats package float, hotastable environment, reference macros, version control). Preamble code VERIFIED and TESTED per 18 January 2026 (guidetest.tex compilation ✓, PDF generation ✓). Supersedes v0.1.4.1. Section 11 expanded to 8,000 words (was 2,500). All 11 subsections documented with rationale and code examples. New preamble deployed to guide.tex and template-wip-V1.0.tex |
| WIP-FILE-NAMING-v1.4 | v1.4 | Naming and status for WIP files | Prefixes section-, table-, visual-, notes-, chapter- with dev/review/final/approved/deprecated status codes | NEW Section 0.5 How to Create WIP File (3-step workflow). Updated Session 9. All sections reference mandatory template usage. Supersedes v1.3 |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | Canonical WIP template | Per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning V1.0 | UPDATED 18 Jan 2026: New preamble deployed (report class, twoside, titlesec, improved headers/footers, float support). All future WIP files MUST copy from this updated template. Established Session 9. Updated Session 17 with new preamble infrastructure |
| TRAINING-MISSION-ABBREV-TABLE-v1.0 | v1.0 | Official source for mission abbreviations | Standardized abbreviations for all 33 BMS 4.38.1 training missions, for use when building Tables | For reference when incorporating mission names |

**Consequence**: All new WIP files going forward MUST follow BRIEFING-v0.2.0.1 Section 11 template specification with updated preamble per 18 Jan 2026 and WIP-FILE-NAMING-v1.4 conventions.

---

## 2. PROJECT SNAPSHOT (Updated Session 23)

- **Active Regime**: Pre-publication 0.x.x.x
- **Phase**: Phase 0 – Chapter Scaffolding
- **Current Guide Version**: guide-v0.3.2.0-20260119 (Chapter 4.3 DMS Down integrated, redaction corrections in 4.1/4.2, enhanced semantic clarity)
- **Chapters Planned**: 7
- **Chapters with narrative in development**: 4/7
  - **Chapter 1** — Introduction: narrative complete
  - **Chapter 2** — HOTAS Fundamentals: **WIP review, narrative progress Session 2** (2 sections 2.1 Overview/2.2 Master Modes) [NEW]
  - **Chapter 4** — DMS: Sections 4.1, 4.2, 4.3 FINAL INTEGRATED, Sections 4.4 LEFTRIGHT (review).
  - **Chapter 5** — CMS: Sections 5.1, 5.2, 5.3 narrative and tables complete
- **Chapters with structure scaffolded**: 5/7
  - Chapters 2 HOTAS Fundamentals, 3 TMS, 4 DMS with 4.1, 4.2, 4.3 direction-based structure locked by blueprint v1.1, plus outlines for 6 Training References and 7 HOTAS Visual Reference
- **Tables filled**: 4 major HOTAS tables
  - CMS (integrated Sections 5.2–5.3)
  - 3 DMS tables (C4-S1 SOI-by-mode, C4-S2 DMS Up usage, C4-S3 DMS Down usage) all INTEGRATED with enhanced documentation
  - Remaining DMS tables (DMS LeftRight, DMS summary) pending per unified Chapter 4 DMS blueprint v1.1

---

### 2.1 High-Level Overview (Updated)

Since v0.2.2.0:
- **Geometry Option D**: A4, 2.0 cm side margins, 2.5 cm top/bottom; text width 17.0 cm; HOTAS table width 15.6 cm; arraystretch 1.25
- **Document class**: report with twoside option (upgraded Session 17)
- **Chapter formatting**: Enhanced via titlesec package (upgraded Session 17)
- **Headers/Footers**: Professional two-sided layout with improved page numbers and chapter markers (upgraded Session 17)
- **Additional packages**: float (graphics control), booktabs/tabularx (advanced table formatting) (upgraded Session 17)

---

### 2.2 Layout Standard

- **Version Control**: GitHub repository tms-dms-cms-usage-guide
- **Local project root**: projeto-bms (normalized structure)
- **Core folders**:
  - `wip/` — active work-in-progress LaTeX sections/tables/visuals (contains wipguide/ subfolder for versioned snapshots)
  - `archive/` — approved/deprecated WIP and historical guide snapshots (subfolders: archiveGUIDE, archiveWIP)
  - `fig/` — images and figures used in guide.tex
  - `docs/` — governance and tracking documents (Markdown, exported to DOCX via md-to-docx script)
- **Editor**: VS Code (default for Markdown and Git-related edits)
- **LaTeX toolchain**: MiKTeX (local compilation)
- **Total Commits**: 198 (GitHub tracked)
- **Latest Release**: v0.3.2.0 (tagged 2026-01-19)

---

## 3. VERSION ROADMAP (Updated Session 23)

### 3.1 Past and Current Versions (0.x.x.x)

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.3.1.0 | Preamble Infrastructure Upgrade | 0 | COMPLETED RELEASED | SESSION 17 Update 18 Jan 2026. Major preamble infrastructure upgrade deployed. Migration: article → report class with twoside option. New features: titlesec chapter formatting, improved headers/footers for two-sided layout, float package for graphics control, enhanced table packages (booktabs, tabularx). BRIEFING-v0.2.0.1 Section 11 expanded to 8,000 words with complete preamble documentation (11.3.1–11.3.11). guide.tex migrated and tested ✓. LaTeX compilation verified ✓. PDF output guidetest.pdf generated and approved by author ✓. template-wip-V1.0.tex updated with new preamble — all future WIP files compliant. Snapshot guide-v0.3.1.0-20260117.tex created, deployed to wipguide, and synchronized to guide.tex root. Previous snapshot v0.3.0.1 moved to ARCHIVE/GUIDE. GitHub Release tag 0.3.1.0 created and pushed to repository. Version bump: v0.3.0.1 → v0.3.1.0 (PATCH). Next phase: Continue DMS content Section 4.3 integration, Sections 4.4, 4.5 and TMS coverage per roadmap |
| v0.3.2.0 | Chapter 4 – DMS Section 4.3 integration + redaction corrections | 0 | COMPLETED RELEASED | SESSION 20 Update 19 Jan 2026. Section 4.3 DMS Down integrated into guide after final semantic refinements and redaction corrections applied to Sections 4.1 and 4.2. Changes: (1) Redaction corrections (grammar, clarity) applied throughout 4.1 and 4.2; (2) Section 4.3 integrated with enhanced semantic clarity (new intro paragraph separating display toggling from format transitions; replaced "valid SOI candidates are HUD, FCR, TGP, WPN..." with "HUD and both MFD" for clarity); HOTAS table Effect/Nuance column optimized (NAV, A-A, A-G refined; picture evaluation situational awareness A-A row). Validation: Dash-34 alignment confirmed ✓. LaTeX structure verified ✓. Cross-references checked ✓. File size: 71935 bytes (guide-v0.3.2.0-20260119.tex in wipguide). GitHub Release tag 0.3.2.0 created and pushed. Version bump: v0.3.1.0 → v0.3.2.0 (MINOR bump). Next phase: Sections 4.4 DMS LeftRight and 4.5 Master Mode Summary WIP development per unified Chapter 4 DMS blueprint v1.1 |
| **v0.x.0.0** | **Chapter 2 – HOTAS Fundamentals** | **0** | **WIP dev (AI Session 23)** | **NEW SESSION 23 Progress 2026-01-26, 0014 AM**. Chapter 2 narrative developed: 2 sections (2.1 Overview of TMS/DMS/CMS + 2.2 Master Modes and Context Principles). Text-puro (no figures/tables/SOI-detail/press-timing). Dash-34-aligned (refs 2.1, 2.1.5, 2.1.1.2.1, 2.1.1.2.3, 2.1.1.11, 2.1.1.13, 2.1.6.3). Fwd to Chapters 3 (TMS), 4 (DMS), 5 (CMS) detailed tables. File: chapter-C2-hotas-fundamentals-dev-20260125.tex (status dev). WIP metadata complete. Template-wip-V1.0.tex used (preamble V1.0 intact per governance). Next: Author review + optional refinement, promote to final, integrate into v0.5.0.0. PATCH or MINOR bump TBD |
| v0.x.0.0 | Chapter 3 – TMS all sections (3.1–3.6) | 0 | Planned | Full TMS coverage after DMS completion. MINOR bump |
| v0.7.0.0 | All 7 chapters scaffolded | 0 | Target | Transition to Phase 1. All chapters with structure and basic narrative. MINOR bump. Phase 1 – Table population; Phase 2 – Community review and release |

**Post-Phase-0**: v1.0.0 and above will follow VERSION-SYSTEM-v4.2.1 rules for post-publication regimes.

---

## 4. WIP LAYER

### 4.1 WIP File Naming Quick Reference (Per WIP-FILE-NAMING-v1.4)

| Category | Pattern | Example | Status Codes |
|---|---|---|---|
| Chapters | chapter-CN-TITLE-STATUS-DATE.tex | chapter-C2-hotas-fundamentals-dev-2026-01-25.tex | dev, review, final, approved, deprecated |
| Sections | section-CN-SM-SK-TITLE-STATUS-DATE.tex | section-C5-S1-cms-concept-final-2026-01-07.tex | dev, review, final, approved, deprecated |
| Tables | table-CN-CONTEXT-SWITCH-STATUS-DATE.tex | table-C3-AA-TMS-review-2026-01-17.tex | dev, review, final, approved, deprecated |
| Notes | notes-CN-TOPIC-TYPE-DATE.md | notes-C4-dms-research-questions-2026-01-19.md | no formal status |
| Visuals | visual-CN-DESC-TYPE-STATUS-DATE.ext | visual-C7-hotas-layout-diagram-dev-2026-01-18.svg | dev, review, final, approved, deprecated |

**Key rules**:
- WIP status transitions (dev → review → final → approved) do not directly affect guide version numbers
- Only integration into guide-v.tex triggers version bumps per VERSION-SYSTEM-v4.2.1
- Active WIP lives in `wip/`; integrated or deprecated WIP moves to `archive/`
- **UPDATED Session 17**: All new WIP files MUST copy from `TEMPLATES/template-wip-V1.0.tex` per BRIEFING-v0.2.0.1 Section 11 (updated preamble with report class, twoside, titlesec, float support)

---

### 4.2 Active WIP Snapshot (Updated Session 23)

| Date | WIP Reference File | From Version | To Version | Status | Category | Notes |
|---|---|---|---|---|---|---|
| 2026-01-07 | section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex | v0.1.4.0 | v0.2.0.1 | INTEGRATED | section | CMS 5.1 integrated as new section. Chapters metric: 1/7 → 2/7 |
| 2026-01-08 | (guide-v0.2.1.0-20260108) | v0.2.0.1 | v0.2.1.0 | INTEGRATED | guide | Human-driven refinement of Chapter 5 internal structure (5.1–5.3 splits, headings) |
| 2026-01-10 | section-C5-S2-cms-actuation-hotas-tables-final-2026-01-09.tex | v0.2.1.0 | v0.2.3.1 | INTEGRATED | section | CMS 5.2 narrative and main HOTAS table integrated |
| 2026-01-11 | section-C5-S3-blocks-and-variants-final-2026-01-11.tex | v0.2.3.1 | v0.2.4.0 | INTEGRATED | section | CMS 5.3 narrative and reference tables. Chapter 5 now structurally complete (all 3 sections) |
| 2026-01-15 | section-C4-S1-concept-soi-approved-2026-01-15.tex | v0.2.4.0 | v0.3.0.0 | INTEGRATED | section | DMS Chapter 4 Section 4.1. SOI-by-mode table. File moved to ARCHIVE (approved) |
| 2026-01-15 | section-C4-S2-dms-up-approved-2026-01-15.tex | v0.2.4.0 | v0.3.0.0 | INTEGRATED | section | DMS Chapter 4 Section 4.2. File moved to ARCHIVE (approved) |
| 2026-01-16 | (guide-v0.3.0.1-20260116.tex) | v0.3.0.0 | v0.3.0.1 | INTEGRATED | guide | Section 4.2 column explanations added (PATCH refinement) |
| 2026-01-17 | (guide-v0.3.1.0-20260117.tex) | v0.3.0.1 | v0.3.1.0 | INTEGRATED | guide-infrastructure | SESSION 17 – PREAMBLE INFRASTRUCTURE UPGRADE (PATCH). Migration article → report with twoside, titlesec, float, booktabs/tabularx. Headers/footers enhanced. BRIEFING-v0.2.0.1 Section 11 expanded (8,000 words). template-wip-V1.0.tex updated. LaTeX compilation ✓, PDF ✓. GitHub Release tag 0.3.1.0 |
| 2026-01-18 | section-C4-S3-dms-down-approved-2026-01-18.tex | v0.3.1.0 | v0.3.2.0 | FINAL INTEGRATED | section | DMS Chapter 4 Section 4.3. Promoted review → final on 2026-01-18. Integrated into guide-v0.3.2.0 on 2026-01-19. Refined intro. Semantic refinement "HUD and both MFD". File moved to ARCHIVE (approved) |
| 2026-01-19 | (guide-v0.3.2.0-20260119.tex) | v0.3.1.0 | v0.3.2.0 | INTEGRATED | guide | SESSION 20 – DMS SECTION 4.3 INTEGRATION + REDACTION CORRECTIONS. Sections 4.1, 4.2 grammar/clarity refined. Section 4.3 integrated. Version bump MINOR. Chapter 4 now contains integrated Sections 4.1, 4.2, 4.3 with enhanced semantic clarity. Next: DMS Sections 4.4 LeftRight and 4.5 Master Mode Summary WIP development |
| 2026-01-20 | section-C4-S4-dms-left-right-dev-2026-01-20.tex | v0.3.2.0 | pending | WIP – IN DEVELOPMENT | section | DMS Chapter 4 Section 4.4. SESSION 21 WIP GENERATION. Substantive research completed on DMS LeftRight architecture, OSB mapping, functional modes. Content structure: Overview, Functional Modes, Button Logic, Integration, Summary. Status dev. Preamble V1.0. Next: Author review + integration into v0.4.0.0 |
| 2026-01-21 | section-C4-S4-dms-left-right-review-2026-01-21.tex | v0.3.2.0 | pending | WIP – REVIEW | section | DMS Chapter 4 Section 4.4. SESSION 22 UPDATE. Promoted dev → review. PDF generated. Content complete. Status review. Preamble V1.0. Next: Author final review + final status + integration into v0.4.0.0 |
| **2026-01-26** | **chapter-C2-hotas-fundamentals-review-2026-01-25.tex** | **v0.3.2.0 unchanged** | **pending** | **WIP – IN DEVELOPMENT** | **chapter** | **SESSION 23 – CHAPTER 2 NARRATIVE PROGRESS (NEW)**. 2 sections developed: 2.1 Overview of TMS/DMS/CMS (3 subsections, full TMS/DMS/CMS intro, fwd Chapters 3–5) + 2.2 Master Modes and Context Principles (2 subsections, mode fundamentals, SOI coupling, timing defer to Chapters 3–5). Text-puro (no figures/tables/detailed SOI/press-timing). Dash-34-aligned (2.1, 2.1.5, 2.1.1.2.1, 2.1.1.2.3, 2.1.1.11, 2.1.1.13, 2.1.6.3). Template-wip-V1.0.tex used (preamble V1.0 intact). Metadata: Target=C2, Status=dev, Date=2026-01-25, Author=AI Session 23. Notes: "Text-puro overview for Cap.2; fwd 3-5; Dash-34-aligned; no SOI-detail/presses; fwd tabled to chapters 3-5". Next: Author review + optional refinement, promote to final, integrate into v0.5.0.0 |

---

## 5. SESSION LOG (Updated Session 23)

| Session | Date | Guide Version | Tracking Version | Key Changes |
|---|---|---|---|---|
| Session 20 | 2026-01-19 | v0.3.2.0 | v5.0.0 | v0.3.2.0 INTEGRATION COMPLETE. Section 4.3 integrated. Redaction corrections in 4.1 and 4.2. MINOR version bump. GitHub Release 0.3.2.0 tagged. Chapter 4 now FINAL INTEGRATED (Sections 4.1, 4.2, 4.3). Next: DMS 4.4 and 4.5 WIP development. Total commits: 144 |
| Session 21 | 2026-01-20 | v0.3.2.0 unchanged | v5.0.0 | DMS LEFTRIGHT WIP DEVELOPMENT. Substantive research on DMS LeftRight architecture completed. WIP section-C4-S4-dms-left-right-dev-2026-01-20.tex generated from canonical template. Status dev. Content sections: Overview, Functional Modes, Button Logic, Integration, Summary. Preamble V1.0. Awaiting author review and MFD image integration. Next: Integration into v0.4.0.0 per Chapter 4 DMS blueprint v1.1 |
| Session 22 | 2026-01-21 | v0.3.2.0 unchanged | v5.0.0 | DMS LEFTRIGHT WIP PROMOTED TO REVIEW. C4-S4 promoted dev → review status. File renamed (dev → review). PDF generated for visual validation. Content structure complete (Overview, Functional Modes, Button Logic, Integration, Summary). Status review. Preamble V1.0. Next: Author final review cycle + transition to final status prior to integration into v0.4.0.0. Total commits: 198 |
| **Session 23** | **2026-01-26** | **v0.3.2.0 unchanged** | **vx.x.x** | **CHAPTER 2 NARRATIVE PROGRESS (NEW).** Text-puro narrative developed for Chapter 2 HOTAS Fundamentals: 2 sections (2.1 Overview + 2.2 Master Modes). Dash-34-aligned, no figures/tables/SOI-detail/press-timing. Fwd Chapters 3–5. WIP file: chapter-C2-hotas-fundamentals-dev-20260125.tex (status dev). Template-wip-V1.0.tex used (preamble V1.0 intact per governance). Metadata complete. Next: Author review + optional refinement, promote to final, integrate into v0.5.0.0. PROJECT-TRACKING updated to v5.1.0 reflecting new Chapter 2 status and pending v0.5.0.0 integration |

---

## 6. NEAR-TERM ROADMAP (Updated Session 23)

**Next Target Versions**:
- **v0.4.0.0**: DMS Sections 4.4 LeftRight + 4.5 Master Mode Summary (WIP 4.4 in review; 4.5 pending)
- **v0.5.0.0**: Chapter 2 HOTAS Fundamentals (WIP dev, Session 23, ready for author review + integration)
- **v0.6.0.0**: Chapter 3 TMS (all sections 3.1–3.6, planned after DMS completion)
- **v0.7.0.0**: All 7 chapters scaffolded (transition to Phase 1)

---

## 7. KEY METRICS

- **Total Commits**: 200 (GitHub tracked)
- **Latest Version**: v0.3.2.0 (released 2026-01-19)
- **Current Phase**: Phase 0 – Chapter Scaffolding
- **C4-S4 Status**: WIP – REVIEW (as of 2026-01-21)
- **C2 Status**: WIP – IN DEVELOPMENT (Session 23, 2026-01-26, ready for review)
- **Last Updated**: 2026-01-26, 0014 AM -03

---

**END OF PROJECT TRACKING v5.1.0 – UPDATED SESSION 23**
