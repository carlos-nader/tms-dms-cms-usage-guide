# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-01-14, 21:37 PM -03  
**Repository:** carlos-nader/tms-dms-cms-usage-guide

This document tracks how governance rules, WIP files and guide versions evolve during the development of the Falcon BMS TMS/DMS/CMS HOTAS Guide.

---

## 1. GOVERNANCE LAYER

Reference documents that define the project structure:

| Document | Version | Purpose | Scope | Notes |
|---|---|---|---|---|
| VERSION-SYSTEM-v4.2.1 | v4.2.1 | Versioning rules for guide-v | Defines 0.x.x.x vs x.y.z regimes, MAJOR/MINOR/PATCH/SUBPATCH semantics, build date rules. | Updated Session 9; refs v1.4, BRIEFING-v0.2.0.1 alignment documented. |
| BRIEFING-v0.2.0.1 | v0.2.0.1 | Content and layout brief; template specification | Scope, style, layout standard (Geometry Option D, hotastable 15.6 cm, arraystretch 1.25), high-level roadmap. NEW Section 11: Complete template specification per BRIEFING Section 11, preamble/metadata/hotastable locked. | Supersedes v0.1.4.1. Section 11 governance ~2,500 words. |
| WIP-FILE-NAMING-v1.4 | v1.4 | Naming and status for WIP files | Prefixes: section-, table-, visual-, notes-, chapter- with dev/review/final/approved/deprecated status codes. NEW Section 0.5: How to Create WIP File (3-step workflow). | Updated Session 9. All sections reference mandatory template usage. Supersedes v1.3. |
| TEMPLATEStemplate-wip-V1.0.tex | V1.0 | Canonical WIP template | Per BRIEFING-v0.2.0.1 Section 11. Preamble/metadata/hotastable locked. Independent versioning (V1.0). | Established Session 9. All future WIP files MUST copy from this template. |
| TRAINING-MISSION-ABBREV-TABLE-v1.0 | v1.0 | Official source for mission abbreviations | Standardized abbreviations for all 33 BMS 4.38.1 training missions, for use when building Tables. | For reference when incorporating mission names. |

**Consequence:** All new WIP files going forward MUST follow BRIEFING-v0.2.0.1 Section 11 template specification and WIP-FILE-NAMING-v1.4 conventions.

---

## 2. PROJECT SNAPSHOT

Current state as of 2026-01-14, 21:37 PM -03:

### 2.1 High-Level Overview

- **Active Regime:** Pre-publication (0.x.x.x)
- **Phase:** Phase 0 -- Chapter Scaffolding
- **Current Guide Version:** guide-v0.2.4.0-20260111 (Section 5.3 integrated)
- **Chapters Planned:** 7
- **Chapters with narrative complete in development:** 2/7
  - Chapter 1 -- Introduction (narrative complete)
  - Chapter 5 -- CMS Sections 5.1, 5.2, 5.3 (narrative and tables complete)
  - (Chapter 4 -- DMS Sections 4.1, 4.1.3 narratives 100% complete; 4.2 narrative 95% complete; tables under development for 4.1, 4.2, 4.3)
- **Chapters with structure scaffolded:** 4/7
  - Chapters 2 (HOTAS Fundamentals), 3 (TMS), 4 (DMS with sections 4.1, 4.1.3, 4.2 under review; 4.3 in dev), plus outlines for 6 (Training References) and 7 (HOTAS Visual Reference)
- **Tables filled:** 1 major HOTAS table (CMS, integrated Sections 5.2--5.3); remaining tables: 3 in development (C4-S1, C4-S2, C4-S3 tables under construction)

### 2.2 Layout Standard

Since v0.2.2.0:
- **Geometry:** Option D (A4, 2.0 cm side margins, 2.5 cm top/bottom)
- **Text width:** 17.0 cm
- **HOTAS table width:** 15.6 cm
- **Table arraystretch:** 1.25 (for readability)
- **Column definitions:** L{width}, C{width}, R{width} (raggedright, centering, raggedleft with explicit width)

### 2.3 Tooling & Repository

- **Version Control:** Git/GitHub (repository: tms-dms-cms-usage-guide)
- **Local project root:** projeto-bms (normalized structure)
- **Core folders:**
  - WIP -- active work-in-progress (LaTeX sections/tables/visuals)
  - ARCHIVE -- approved or deprecated WIP and historical snapshots
  - Fig -- images and figures used in guide.tex
  - docs -- governance and tracking documents (Markdown), exported to DOCX via md-to-docx script
- **Editor:** VS Code (default for Markdown and Git-related edits)
- **LaTeX toolchain:** MiKTeX (local compilation)

---

## 3. VERSION ROADMAP

### 3.1 Past and Current Versions (0.x.x.x)

| Target Version | Expected Area | Phase | Status | Notes |
|---|---|---|---|---|
| v0.3.0.0 | Chapter 4 -- DMS (Sections 4.1--4.3) | 0 | IN PROGRESS | **Session 14 update:** C4-S1 (Concept & SOI) WIP REVIEW status (section-C4-S1-concept-soi-review-2026-01-13.tex), includes Table "Valid SOI Displays by Master Mode" (6 rows: NAV, A-A, A-G PRE, A-G VIS, DGFT, MSL OVRD). C4-S1-S3 (HUD as SOI in A-A and HMCS Capabilities) NEW subsection, status DEV (section-C4-S1-S3-hud-soi-hmcs-capabilities-dev-2026-01-14.tex), ~220 words conceptual clarification, single Dash-34 ref. C4-S2 (DMS Up/Down: SOI Management) WIP REVIEW status (section-C4-S2-dms-up-down-review-2026-01-13.tex), 95% narrative complete (S2.1 and S2.2 complete, S2.3 placeholder for consolidated table), includes 3 practical scenarios + hotastable tables. C4-S2-DEPRECATED version exists (section-C4-S2-dms-up-down-deprecated-2026-01-13.tex) for audit trail. C4-S3 (DMS Left/Right: Format Cycling) WIP DEV status (section-C4-S3-dms-format-cycling-dev-2026-01-13.tex), not reviewed in Session 14. MINOR bump upon integration of all sections. |
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
- Active WIP lives in WIP/; integrated or deprecated WIP moves to ARCHIVE/.
- **NEW (Session 9):** All new WIP files MUST copy from TEMPLATES/template-wip-V1.0.tex per BRIEFING-v0.2.0.1 Section 11 (mandatory).

---

### 4.2 Active WIP Snapshot (as of 2026-01-14, 21:37 PM -03)

| Date | WIP Reference File | From Version | To Version | Status | Category | Notes |
|---|---|---|---|---|---|---|
| 2026-01-07 | section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex | v0.1.4.0 | v0.2.0.1 | INTEGRATED | section | CMS 5.1 integrated as new section. Chapters metric 17 → 27. |
| 2026-01-08 | section-C5-S1-concept-and-interactions-cmds-ecm-rwr-final-2026-01-07.tex | v0.2.0.1 | v0.2.1.0 | INTEGRATED | section | Human-driven refinement of Chapter 5 internal structure (5.1--5.3 splits, headings). |
| 2026-01-10 | section-C5-S2-cms-actuation-hotas-tables-final-2026-01-09.tex | v0.2.1.0 | v0.2.3.1 | INTEGRATED | section | Integrated CMS 5.2 (CMS Switch Actuation) narrative and main HOTAS table. |
| 2026-01-11 | section-C5-S3-blocks-and-variants-final-2026-01-11.tex | v0.2.3.1 | v0.2.4.0 | INTEGRATED | section | Integrated CMS 5.3 (Block and Variant Notes) narrative and reference tables (External ECM Pod, Internal IDIAS). Chapter 5 now structurally complete (all 3 sections). |
| 2026-01-12 | section-C4-S1-concept-and-soi-dev-2026-01-12.tex | -- | -- | dev | section | DMS Chapter 4 Section 1 (Concept and SOI). WIP file created from template-wip-V1.0.tex with author-approved narrative. Narrative 100% complete; tables: 0 (intentional, Section 4.3). Compliance 100% verified (wip-naming-v1.4, template-wip-V1.0.tex, briefing-v0.2.0.1). Status: dev → ready for review. |
| 2026-01-13 | section-C4-S1-concept-soi-review-2026-01-13.tex | v0.2.4.0 | -- | **review** | section | DMS Chapter 4 Section 1 (Concept and SOI). Manually integrated by author with Table "Valid SOI Displays by Master Mode" (6 rows: NAV, A-A, A-G PRE, A-G VIS, DGFT, MSL OVRD). Heading uses official HOTAS pattern (rowcolor headerblue + textcolor white). Compliance 100% verified. Status: **dev → review** (NOT yet final; pending formal approval before guide-v0.3.0.0 integration). File remains in WIP/. |
| 2026-01-14 | section-C4-S1-S3-hud-soi-hmcs-capabilities-dev-2026-01-14.tex | -- | -- | **dev** | section (subsection) | NEW Subsection 4.1.3: "HUD as SOI in A-A and HMCS Capabilities". Resolves reader confusion regarding HUD/HMCS targeting capability when HUD cannot be SOI. Clarifies: SOI routing mechanism ≠ Display functional capability. ~220 words, conceptual level, single Dash-34 Section 2.5 reference. Validates against Dash-34 2.1.1.2.3 (SOI definition), 2.5.5.1 (AIM-9 BORE), 2.5.5.5 (AATLL), 2.5.5.2-3 (FCR ACM BORE slaving). Full compliance verified (wip-naming-v1.4, template-wip-V1.0.tex, briefing-v0.2.0.1). Status: dev (ready for formal review and subsection-level integration into C4-S1 parent). |
| 2026-01-14 | section-C4-S2-dms-up-down-review-2026-01-13.tex | v0.2.4.0 | -- | **review** | section | DMS Chapter 4 Section 2 (DMS Up/Down: SOI Management). Sections 4.2.1 (DMS Up) and 4.2.2 (DMS Down) 100% narrative complete with 3 practical scenarios (NAV toggle, A-A toggle, A-G VIS). Hotastable tables: Table 4.2.1 (DMS Up Usage Across A-A and A-G), Table 4.2 (DMS Down Toggle Logic by Current SOI), Table 4.3 (DMS Down Behavior and Available SOI Displays by Master Mode). Section 4.2.3 (Master Mode Behavior Consolidated) marked as placeholder for Phase 2 (future integrated table). Compliance 100% verified. Status: review (narrative 95% complete; ready for author formal approval cycle before guide-v0.3.0.0 integration). File: WIP/section-C4-S2-dms-up-down-review-2026-01-13.tex. |
| 2026-01-14 | section-C4-S2-dms-up-down-deprecated-2026-01-13.tex | -- | -- | **deprecated** | section | DEPRECATED: Earlier iteration of C4-S2 (DMS Up/Down) WIP file retained for audit trail. Superseded by active C4-S2 review version. Kept in WIP/ with deprecated status for version control history. No further action; archive upon guide integration completion. |
| 2026-01-13 | section-C4-S3-dms-format-cycling-dev-2026-01-13.tex | -- | -- | **dev** | section | DMS Chapter 4 Section 3 (DMS Left/Right: Format Cycling). Status: dev (not reviewed in Session 14). Placeholder for future detailed narrative on MFDS format page cycling, horizontal axis DMS behavior across all master modes. Tables and cross-references to follow. Next: Formal author review planned for subsequent session. |

**Status codes:**
- dev -- Draft, author working
- review -- **Under human review, not yet final or integrated**
- final -- Author approved, ready for integration
- approved -- Integrated into guide-v and archived
- deprecated -- Intentionally retired (superseded or abandoned)

---

### 4.3 WIP Integration Timeline & Decisions

Summary of major decisions and changes per working session. Earlier sessions 1--6 documented in legacy tracking files; from v5.0.0 onward, sessions logged here.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 7 | 2026-01-08 | v0.2.2.0 | v4.1.2 | Layout Option D and hotastable adopted. CMS 5.1 fully integrated. Chapter 5 structure (5.1--5.3) refined. WIP files for 5.2 and 5.3 created in review status. |
| 8 | 2026-01-09 | v0.2.2.0 (unchanged) | v5.0.0 | Project brought under Git/GitHub (falcon-bms-hotas-tms-dms-cms-guide). Local root normalized to projeto-bms. Folders WIP, ARCHIVE, docs created and aligned with WIP-FILE-NAMING governance. Centralized in .md files under docs; DOCX exports via md-to-docx. VS Code and Git CLI configured for Markdown-centric workflow. |
| 9 | 2026-01-09 | v0.2.2.0 (unchanged) | v5.0.0 | **Template establishment:** BRIEFING-v0.2.0.1 Section 11 complete template specification. WIP-NAMING-v1.4 Section 0.5 "How to Create WIP File". VERSION-SYSTEM-v4.2.1 references updated; 3-way integration documented. TEMPLATES/template-wip-V1.0.tex created and locked (preamble/metadata/hotastable per BRIEFING Section 11). Section C5-S2, S3 WIP files created using new template. Going forward: All new WIP files MUST use template (mandatory governance structure locked). |
| 10 | 2026-01-10 | v0.2.3.1 | v5.0.0 | **CMS 5.2 Integration:** Integrated CMS Switch Actuation narrative and main HOTAS table into Chapter 5. C5-S2 WIP marked ready for archival. C5-S3 remains under review with dedicated review MD. |
| 11 | 2026-01-11 | v0.2.4.0 | v5.0.0 | **CMS 5.3 Integration:** Integrated Block and Variant Notes narrative and 2 reference tables (External ECM Pod [BlockVariants 3 operators], Internal ECM/IDIAS [BlockVariants 2 operators]). Validation: LaTeX syntax verified; Dash-34 Sections 2.7.4.1.12, 2.7.4.2.56 alignment confirmed. BMS 4.38.1 block/variant compliance checked. WIP file moved to ARCHIVE with approved status. Versioning: v0.2.3.1 → v0.2.4.0 (MINOR version bump; new complete section). Next Phase: DMS Chapter 4 integration planned for v0.3.0.0. |
| 12 | 2026-01-12 | v0.2.4.0 (unchanged) | v5.0.0 | **DMS C4-S1 WIP Created:** Generated section-C4-S1-concept-and-soi-dev-2026-01-12.tex from TEMPLATES/template-wip-V1.0.tex. Integrated author-approved DMS introduction narrative (Sections 4.1.1 SOI Definition, 4.1.2 DMS Role, 4.1.3 SOI Flow Example). Applied author corrections (slug concept-soi → concept-and-soi). Full Compliance: 100% verified against wip-naming-v1.4, template-wip-V1.0.tex, briefing-v0.2.0.1. Status: dev (never formally reviewed). Canonical version established; ready for author review cycle. Next: Author formal review; dev → review → final; upon final approval, AI integrates into guide-v0.3.0.0. |
| 13 | 2026-01-13 | v0.2.4.0 (unchanged) | v5.0.0 | **C4-S1 Manual Integration + Research Validation:** (1) C4-S1 manually integrated by author with new Table "Valid SOI Displays by Master Mode" (6 rows: NAV, A-A, A-G PRE, A-G VIS, DGFT, MSL OVRD). Heading uses official HOTAS pattern (rowcolor headerblue + textcolor white). File renamed to section-C4-S1-concept-soi-review-2026-01-13.tex (corrected date in filename); status: dev → **review** (NOT yet final; awaiting formal approval before guide integration). File location: WIP/section-C4-S1-concept-soi-review-2026-01-13.tex. (2) Deep technical research: HUD/HMCS SOI constraints in A-A/DGFT/MSL OVRD validated against Dash-34 Sections 2.1.1.2.3, 2.5.5.1, 2.5.5.5, 2.5.5.2-3. HMCS cueing independence from SOI status confirmed with evidence: AIM-9 BORE (2.5.5.1), AATLL (2.5.5.5), FCR ACM BORE slaving (2.5.5.2-3). (3) LaTeX formatting guidance: hotastable, tabularx, booktabs, array packages verified against guide.tex preamble. (4) Support documentation: Comprehensive validation document and analysis file generated. Next: Begin C4-S2 (DMS Up/Down operations). |
| 14 | 2026-01-14 | v0.2.4.0 (unchanged, awaiting C4 integration) | v5.0.0 | **C4 Multi-File Development Sprint:** (1) **C4-S1-S3 NEW subsection created:** section-C4-S1-S3-hud-soi-hmcs-capabilities-dev-2026-01-14.tex. "HUD as SOI in A-A and HMCS Capabilities" resolves core ambiguity: SOI architectural restriction ≠ Display functional capability. ~220 words, conceptual level, single Dash-34 Section 2.5 reference. Comprehensive Dash-34 validation performed (sections 2.1.1.2.3, 2.5.5.1, 2.5.5.5, 2.5.5.2-3). Full compliance with wip-naming-v1.4, template-wip-V1.0.tex, briefing-v0.2.0.1. Status: dev (ready for formal review and subsection-level integration into C4-S1 parent). (2) **C4-S2 WIP Status Advanced:** section-C4-S2-dms-up-down-review-2026-01-13.tex reviewed and approved by author. Narrative sections 4.2.1 (DMS Up) and 4.2.2 (DMS Down) 100% complete with hotastable tables and 3 practical scenarios. Section 4.2.3 (Master Mode Behavior) marked as placeholder (consolidated table for future phase). Hotastable syntax verified (column type definitions corrected 2026-01-13). Status: review (narrative 95% complete; ready for formal approval cycle before guide-v0.3.0.0 integration). (3) **C4-S2-DEPRECATED version documented:** section-C4-S2-dms-up-down-deprecated-2026-01-13.tex retained for audit trail (superseded by active review version). (4) **C4-S3 WIP Status Noted:** section-C4-S3-dms-format-cycling-dev-2026-01-13.tex (DMS Left/Right: Format Cycling) remains in dev status. Not reviewed in Session 14; scheduled for formal author review in next session. (5) **Comprehensive analysis completed:** Deep Dash-34 validation of HUD/HMCS SOI constraints; identification of AIM-9 BORE, AATLL, FCR ACM BORE as proof that HMCS maintains off-boresight targeting independently of SOI status. Analysis saved in workspace documentation. (6) **Next scheduled milestones:** Await formal author review cycle completion for C4-S1 (may transition review → final); await author approval of C4-S1-S3 (likely final by next session); C4-S2 formal approval cycle initiated. Upon all 4 components (C4-S1, C4-S1-S3, C4-S2, C4-S3) reaching final status: AI integrates all into guide-v0.3.0.0 with MINOR version bump. **Session Output:** 4 .tex files tracked (C4-S1 existing but with updated filename date, C4-S1-S3 new, C4-S2 existing, C4-S2-deprecated existing for audit), comprehensive analysis document, integration recommendations documented. PROJECT-TRACKING-v5.0.0 updated with 15 alterations across 6 sections. |

---

## 5. SESSION LOG

High-level summary of each working session and resulting guide state.

| Session | Date | Guide Version after | Tracking Version | Key Changes |
|---|---|---|---|---|
| 7 | 2026-01-08 | v0.2.2.0 | v4.1.2 | Layout finalized (Option D, 1.25). CMS 5.1 integrated. Chapter 5 structure refined. WIP 5.2, 5.3 in review. |
| 8 | 2026-01-09 | v0.2.2.0 | v5.0.0 | Git/GitHub setup. Folder structure (WIP/ARCHIVE/docs) aligned with governance. VS Code configured. |
| 9 | 2026-01-09 | v0.2.2.0 | v5.0.0 | BRIEFING-v0.2.0.1 Section 11 (template spec) finalized. TEMPLATES/template-wip-V1.0.tex established (mandatory). WIP-NAMING-v1.4 Section 0.5 added. All new WIP MUST use canonical template. |
| 10 | 2026-01-10 | v0.2.3.1 | v5.0.0 | CMS 5.2 integrated (HOTAS table + narrative). C5-S2 WIP archived. |
| 11 | 2026-01-11 | v0.2.4.0 | v5.0.0 | CMS 5.3 integrated (Block/Variant notes, reference tables). Chapter 5 structurally complete. DMS Chapter 4 (v0.3.0.0) targeted next. |
| 12 | 2026-01-12 | v0.2.4.0 | v5.0.0 | DMS C4-S1 WIP created from canonical template. 100% compliance verified. Author review cycle initiated. Canonical version documented. |
| 13 | 2026-01-13 | v0.2.4.0 | v5.0.0 | C4-S1 manually integrated by author with Table "Valid SOI Displays by Master Mode". Status: dev → **review** (NOT final yet). File: WIP/section-C4-S1-concept-soi-review-2026-01-13.tex. Deep technical research on HUD/HMCS SOI constraints completed (Dash-34 validation). LaTeX guidance aligned with project standards. Next: Begin C4-S2 MFDS Format Cycling. |
| 14 | 2026-01-14 | v0.2.4.0 | v5.0.0 | C4-S1-S3 new subsection created (HUD/HMCS SOI clarification). C4-S2 narrative reviewed and approved (95% complete; placeholder S2.3). Comprehensive Dash-34 validation completed. 4 .tex files in WIP (C4-S1 review, C4-S1-S3 dev, C4-S2 review, C4-S2-deprecated deprecated, C4-S3 dev) tracked with clear status. Analysis documentation generated. Target: v0.3.0.0 integration after formal review cycles complete. PROJECT-TRACKING-v5.0.0 updated (15 alterations across 6 sections). |

**Future sessions:** Add new rows to this table, keeping summaries concise and always mentioning: (a) resulting guide version, (b) tracking version, (c) main decisions.

---

## 6. PROJECT PRIORITIES & PHASES

### 6.1 Current Priorities (Post-v0.2.4.0)

| Phase | Target Versions | Indicative Range | Milestone |
|---|---|---|---|
| **Phase 0** | v0.1.0.0 – v0.7.0.0 | 05–22 Jan 2026 | All 7 chapters scaffolded; layout locked at v0.2.2.0; CMS chapter structurally complete. |
| **Phase 1** | v1.0.0 – v1.0.x | TBD | Major HOTAS tables (TMS/DMS/CMS) populated and technically validated. |
| **Phase 2** | v2.0.0-RC1/RC2/Stable | TBD | Final review, community feedback, public release. |

**Phase boundaries and dates are guidelines.** Actual transitions must be explicitly recorded in this tracking document.

### 6.2 Near-Term Roadmap (Next Target Versions)

| Version | Area | Status | Notes |
|---|---|---|---|
| **v0.3.0.0** | Chapter 4 -- DMS (Sections 4.1, 4.1.3 narratives finalized; 4.2 approved-pending; 4.3 DEV) | IN PROGRESS | **Session 14 Update:** C4-S1 (Concept & SOI) WIP REVIEW status, includes Table "Valid SOI Displays by Master Mode" (6 rows). C4-S1-S3 (HUD as SOI in A-A and HMCS Capabilities) NEW subsection, status DEV. C4-S2 (DMS Up/Down: SOI Management) WIP REVIEW status, 95% narrative complete (S2.3 consolidated table is placeholder), includes 3 practical scenarios + hotastable tables. C4-S2-deprecated version retained for audit trail. C4-S3 (DMS Left/Right: Format Cycling) status DEV (not reviewed in Session 14). **Integration Plan:** Upon formal author approval of C4-S1, C4-S1-S3, and C4-S2 (expected next session), AI integrates all into guide-v0.3.0.0 with MINOR version bump. Full integration of Chapter 4 structure targeted for v0.3.x.x (subsequent minor bumps as C4-S3 and additional subsections complete). |
| **v0.4.0.0** | Chapter 3 -- TMS (all sections) | Planned | Full TMS coverage after DMS completion. MINOR bump. |
| **v0.5.0.0** | Chapter 2 -- HOTAS Fundamentals | Target | Foundational SOI, short/long press timing, master modes. MINOR bump. |
| **v0.7.0.0** | All 7 chapters scaffolded | Target | Transition to Phase 1. Chapters 2, 3, 4, 5, 6, 7 with basic narrative. MINOR bump. |

---

## 7. FILE STATUS SUMMARY

### 7.1 Guide Files (guide-v.tex)

| File (relative path) | Status | Type | Next Action |
|---|---|---|---|
| guide-v0.1.4.0-20260106.tex | archive | main guide | Reference only; pre-CMS integration. |
| guide-v0.2.0.1-20260108.tex | archive | main guide | Reference only; CMS 5.1 integrated. |
| guide-v0.2.1.0-20260108.tex | archive | main guide | Reference only; Ch. 5 structure refined. |
| guide-v0.2.2.0-20260108.tex | archive | main guide | Reference only; layout Option D applied. |
| guide-v0.2.3.1-20260110.tex | archive | main guide | Reference only; CMS 5.2 integrated. |
| guide-v0.2.4.0-20260111.tex | **active** | main guide | Current baseline snapshot. Use as base for v0.3.0.0 prep (C4 sections pending formal approval before integration). |

---

### 7.2 WIP Files (WIP/ folder)

| File (relative path) | Version | Type | Status | Short Purpose |
|---|---|---|---|---|
| WIP/section-C4-S1-concept-soi-review-2026-01-13.tex | -- | section | **review** | DMS Chapter 4 Section 1 (Concept and SOI). Manually integrated by author with Table "Valid SOI Displays by Master Mode" (6 rows: NAV, A-A, A-G PRE, A-G VIS, DGFT, MSL OVRD). Status: dev → **review** (NOT yet final; pending formal approval before guide-v0.3.0.0 integration). File remains in WIP/ pending author's formal review cycle completion. |
| WIP/section-C4-S1-S3-hud-soi-hmcs-capabilities-dev-2026-01-14.tex | -- | section (subsection) | **dev** | NEW Subsection 4.1.3: "HUD as SOI in A-A and HMCS Capabilities". Resolves reader confusion regarding HUD/HMCS targeting capability when HUD cannot be SOI. Clarifies: SOI routing mechanism ≠ Display functional capability. ~220 words, conceptual level, single Dash-34 Section 2.5 reference. Comprehensive Dash-34 validation performed. Full compliance verified (wip-naming-v1.4, template-wip-V1.0.tex, briefing-v0.2.0.1). Status: dev (ready for formal review and subsection-level integration into C4-S1 parent). |
| WIP/section-C4-S2-dms-up-down-review-2026-01-13.tex | -- | section | **review** | DMS Chapter 4 Section 2 (DMS Up/Down: SOI Management). Sections 4.2.1 (DMS Up) and 4.2.2 (DMS Down) 100% narrative complete with 3 practical scenarios. Hotastable tables: Table 4.2.1 (DMS Up Usage), Table 4.2 (Toggle Logic), Table 4.3 (DMS Down by Master Mode). Section 4.2.3 (Master Mode Behavior) is placeholder for consolidated table. Compliance 100% verified. Status: review (narrative ready; awaiting formal author approval cycle before guide-v0.3.0.0 integration). |
| WIP/section-C4-S2-dms-up-down-deprecated-2026-01-13.tex | -- | section | **deprecated** | DEPRECATED: Earlier iteration of C4-S2 (DMS Up/Down) WIP file. Superseded by active C4-S2 review version. Retained for audit trail and version control history. No further action required; archive upon guide integration completion. |
| WIP/section-C4-S3-dms-format-cycling-dev-2026-01-13.tex | -- | section | **dev** | DMS Chapter 4 Section 3 (DMS Left/Right: Format Cycling). Status: dev (not reviewed in Session 14). Placeholder for detailed narrative on MFDS format page cycling, horizontal axis DMS behavior. Tables and cross-references pending. Next: Formal author review planned for subsequent session. |

**Session 14 Status (2026-01-14):** PROJECT-TRACKING-v5.0.0 successfully updated with 15 alterations across 6 sections to reflect:
- C4-S1 existing WIP file (REVIEW status, filename updated to reflect corrected 2026-01-13 date)
- C4-S1-S3 NEW subsection WIP file (created 2026-01-14, DEV status)
- C4-S2 existing WIP file (REVIEW status, narrative approved by author)
- C4-S2-deprecated existing WIP file (DEPRECATED status, retained for audit trail)
- C4-S3 existing WIP file (DEV status, not reviewed in Session 14)
- Updated timeline and roadmap for v0.3.0.0 integration planning
- Enhanced session log entry for Session 14
- Expanded Project Snapshot to clarify multiple WIP files in development

All updates preserve versioning scheme (PROJECT-TRACKING-v5.0.0 remains baseline structure) and integrate new state changes without structural overhaul.

---

### 7.3 Governance & Reference Files (docs/ folder)

| File (relative path) | Version | Type | Status | Short Purpose |
|---|---|---|---|---|
| docs/BRIEFING-v0.2.0.1.md | 0.2.0.1 | reference | active | Project brief with NEW Section 11: Template Specification (preamble, metadata block, hotastable environment, section skeleton, integration workflow, template versioning, maintenance). Supersedes v0.1.4.1. |
| docs/WIP-FILE-NAMING-v1.4.md | 1.4 | reference | active | WIP naming convention. NEW Section 0.5: "How to Create WIP File" (3-step workflow). NEW Section 9: Summary + best practices. Supersedes v1.3. |
| docs/VERSION-SYSTEM-v4.2.1.md | 4.2.1 | reference | active | Guide versioning rules. References updated to WIP-FILE-NAMING-v1.4 & BRIEFING-v0.2.0.1 Section 11; 3-way integration clarified. Supersedes v4.2. |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | template | active | **Canonical WIP template per BRIEFING-v0.2.0.1 Section 11.** Preamble/metadata/hotastable locked. Independent versioning (V1.0). Established Session 9. ALL new WIP files MUST copy from this template. |
| docs/PROJECT-TRACKING-v5.0.0.md | 5.0.0 | tracking | active | This document -- unified tracking with Git/GitHub integration. Updated Session 14 with 15 alterations. |
| docs/BRIEFING-v0.2.0.1.docx | 0.2.0.1 | export | derived | DOCX export from Markdown. |
| docs/VERSION-SYSTEM-v4.2.1.docx | 4.2.1 | export | derived | DOCX export from Markdown. |
| docs/WIP-FILE-NAMING-v1.4.docx | 1.4 | export | derived | DOCX export from Markdown. |
| docs/PROJECT-TRACKING-v5.0.0.docx | 5.0.0 | export | derived | DOCX export from this Markdown via md-to-docx script. |
| docs/TRAINING-MISSION-ABBREV-TABLE-v1.0.docx | 1.0 | export | derived | DOCX export from source. |

**Maintenance rule:**
- All structural or governance changes to tracking MUST be made in PROJECT-TRACKING-v5.0.0.md (this file).
- DOCX versions are GENERATED from this file and NEVER edited manually.
- At the end of each working session, this document should be updated (especially Sections 2, 4.2, 4.3, 5, 6) to capture new state and decisions.
- Version number of PROJECT-TRACKING-v5.0.0 does NOT change with content updates. Version marks the baseline structure, not the state. (Designed for frequent updates; version reserved for structural overhauls only.)

---

### 7.4 Update Log

| Date | Change | Sections Affected | Reason |
|---|---|---|---|
| 2026-01-11 | Updated guide version to v0.2.4.0; integrated Section 5.3; updated priorities to next DMS target | 2, 3.1, 3.2, 4.2, 4.3, 5, 6, 7 | Section 5.3 (CMS Block/Variant Notes) integration complete. Chapter 5 now structurally complete. |
| 2026-01-12 | Added Session 12; DMS WIP C4-S1 created; updated Active WIP Snapshot; enhanced Current Priorities | 4.2, 4.3, 5, 6.1, 6.2, 7.2 | DMS Section 4.1 WIP file generation complete with 100% compliance. Author review cycle initiated. Canonical version documented. |
| 2026-01-13 | Added Session 13; C4-S1 manual integration by author; table "Valid SOI Displays by Master Mode" integrated; status updated to review (NOT final); updated Active WIP Snapshot and Session Log | 4.2, 4.3, 5, 6.1, 6.2, 7.2, 7.4 | C4-S1 manually integrated by author with official HOTAS table pattern. Status: dev → review (pending formal approval cycle). File remains in WIP/. Deep technical validation and research documentation completed. Next: Begin C4-S2 MFDS Format Cycling. |
| 2026-01-14 | Session 14 completions: C4-S1-S3 new subsection created; C4-S2 narrative approved; comprehensive Dash-34 validation completed; integration plan for v0.3.0.0 finalized. Updated Sections 2, 3, 4, 5, 6, 7 for WIP file tracking, roadmap clarity, session log entry. | 2, 3, 4, 5, 6, 7 | C4-S1-S3 subsection addresses HUD/HMCS SOI ambiguity with ~220 words conceptual explanation + comprehensive Dash-34 validation (sections 2.1.1.2.3, 2.5.5.1, 2.5.5.5, 2.5.5.2-3). C4-S2 advanced to review status with author approval (narrative 95% complete, tables complete, placeholder S2.3 for future consolidated table). C4-S2-deprecated version documented for audit trail. Multiple WIP files in different states (C4-S1 review, C4-S1-S3 dev, C4-S2 review, C4-S3 dev) require enhanced tracking. Next: Await formal author review cycle completion for C4-S1 and C4-S2; proceed to C4-S3 review or guide integration. PROJECT-TRACKING-v5.0.0 updated (15 alterations applied, version number remains v5.0.0). |

---

## END OF PROJECT TRACKING v5.0.0

**For inquiries or updates, contact:** Carlos "Metal" Nader  
**Last updated:** 2026-01-14, 21:37 PM -03  
**Status:** Ready for use / Download
