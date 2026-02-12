---
layout: default
---
{% raw %}

# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-02-11  
**Repository:** carlos-nader/tms-dms-cms-usage-guide

This document tracks governance rules, project state, and development history. For detailed file tracking, issue status, and commit history, see [INTEGRATED-FILES.md](../INTEGRATED-FILES.md) (auto-generated).

---

## 1. GOVERNANCE LAYER

| Document | Version | Purpose |
|----------|---------|---------|
| VERSION-SYSTEM | v4.2.1 | Versioning rules (0.x.x.x vs x.y.z regimes, MAJOR/MINOR/PATCH/SUBPATCH) |
| BRIEFING | v0.2.0.1 | Content brief, layout standard (Geometry D, hotastable 15.6 cm), preamble architecture |
| WIP-FILE-NAMING | v1.4 | File naming conventions, status codes (dev/review/final/approved/deprecated) |
| TEMPLATES/template-wip-V1.0.tex | V1.0 | Canonical WIP template (preamble, metadata, hotastable) |
| TRAINING-MISSION-ABBREV-TABLE | v1.0 | Standardized abbreviations for 33 BMS training missions |

**Rule:** All WIP files must be created from `TEMPLATES/template-wip-V1.0.tex`.

---

## 2. PROJECT SNAPSHOT

**Last updated:** 2026-02-11

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.4.1.0 |
| **Phase** | Phase 0 — Chapter Scaffolding |
| **Chapters Planned** | 7 |
| **Chapters Integrated** | 4/7 (C1, C2, C3, C5) |
| **Chapters In Development** | 1/7 (C4) |
| **Chapters Pending** | 2/7 (C6, C7) |
| **Total Commits** | 479 |
| **Latest Release** | v0.4.1.0 (2026-02-11) |

### Chapter Status

| Ch | Title | Status | Notes |
|----|-------|--------|-------|
| 1 | Introduction | ✅ Integrated | Revised and integrated (v0.3.3.0) |
| 2 | HOTAS Fundamentals | ✅ Integrated | Complete (v0.4.0.0) |
| 3 | DMS | ✅ Integrated | Complete (v0.4.0.0, renumbered from Ch 4) |
| 4 | TMS | dev | WIP: `chapter-C4-tms-structure-dev-2026-02-11.tex` |
| 5 | CMS | ✅ Integrated | Complete (§5.1, §5.2, §5.3) |
| 6 | Training References | Scaffolded | Pending development |
| 7 | Visual Reference | Scaffolded | Structure TBD |

---

## 3. DEVELOPMENT LOG

Chronological record of significant changes. For detailed commit history, see INTEGRATED-FILES.md.

| Date | Guide Version | Key Changes |
|------|---------------|-------------|
| 2026-01-05 | v0.1.0.0 | Initial project setup. Chapter scaffolding. Introduction integrated. |
| 2026-01-07 | v0.1.4.0 | Layout standard adopted. BRIEFING created. Geometry locked. |
| 2026-01-11 | v0.2.4.0 | Chapter 5 (CMS) complete. Template-wip-V1.0.tex established. |
| 2026-01-14 | v0.3.0.0 | **RELEASE:** DMS Sections 4.1 and 4.2 integrated. |
| 2026-01-18 | v0.3.1.0 | **RELEASE:** Preamble infrastructure upgrade (article → report class). |
| 2026-01-19 | v0.3.2.0 | **RELEASE:** Section 4.3 (DMS Down) integrated. |
| 2026-01-29 | v0.3.2.1 | **RELEASE:** Hotastable environment upgrade (arraystretch 1.25). |
| 2026-02-02 | v0.3.3.0 | **RELEASE:** C4 (DMS) complete chapter integrated. C1 (Introduction) revised and integrated. Milestone v0.3.3.0 completed (10/10 issues). |
| 2026-02-04 | — | C3 TMS WIP created. Copilot instructions added. Preamble improvements and hotastable v2.0 / List of HOTAS Tables implementation guides drafted (Issues #34 and #33). |
| 2026-02-06 | — | C2 WIP restarted (deprecated v2026-01-25, v2026-02-06). Issues #33 (hotastable v2 + List of Tables), #34 (preamble improvements), #36 (structural change: DMS↔TMS chapter swap) created. |
| 2026-02-09 | — | **C2 Review Session:** Comprehensive review of HOTAS Fundamentals chapter completed. All content validated against Dash-34 (SOI definition, visual indicators, master modes, switch physical locations). Corrected critical errors (TMS/CMS both on flight stick, not throttle). Removed operational details to maintain conceptual focus appropriate for C2. Eliminated redundant paragraphs and grammatical errors. Status progression: dev → review → final (Issue #20 closed). Ready for integration (Issue #22). Updated `chapter-restructure-and-c2-plan.md` to v1.1 reflecting actual implementation decisions vs original spec. Total commits: 431. |
| 2026-02-10 | v0.4.0.0 | **RELEASE:** C2 (HOTAS Fundamentals) integrated. Chapter reorganization: DMS (C4→C3), TMS (C3→C4). SOI content refactored (C2 conceptual, C3 operational). All labels and cross-references updated. Issues #22 (C2 APPROVED) and #36 (Structural Change) closed. Milestone "Integrate C2 and Main Chapter Reorganization" completed (4/4). Total commits: 439. |
| 2026-02-11 | v0.4.1.0 | **RELEASE:** Preamble v2.1 infrastructure improvements. hotastable environment optimized (v2.1: footnotesize font, adjusted spacing, simplified Training column). List of HOTAS Tables automated indexing feature added. Cross-reference macros implemented (`\secref`, `\chapref`, `\tabref`, `\figref`). PDF metadata configuration added. Issues #33 and #34 closed. Milestone "Infrastructure Improvements" completed (2/2). Total commits: 479. |

---

## 4. NEXT TARGETS

### Target 1: Chapter 4 — TMS → v0.5.0.0 (MINOR)

| Item | Value |
|------|-------|
| **WIP File** | `chapter-C4-tms-structure-dev-2026-02-11.tex` |
| **Status** | dev |
| **Milestone** | Integrate C4 (TMS — Target Management Switch) — Guide Version v0.5.0.0 (Due: 2026-03-10, progress 0/3) |
| **Open Issues** | #38 (REVIEW), #39 (FINAL), #40 (APPROVED) |
| **Version Bump** | MINOR (new chapter entry) |

**Content:** TMS concept, situational awareness, A-A employment, A-G employment, weapon-specific behavior, block/variant notes. Most complex HOTAS switch (13+ specialized tables).

**Dependencies:** ✅ v0.4.1.0 completed (infrastructure ready)

**Next step:** Continue development → review → final → approved

---

### Version Roadmap

| Version | Content | Bump Type | Status |
|---------|---------|-----------|--------|
| v0.4.0.0 | C2 HOTAS Fundamentals + C3↔C4 reorganization | MINOR | ✅ Released |
| v0.4.1.0 | Infrastructure improvements (hotastable v2.1, List of HOTAS Tables, cross-refs, PDF metadata) | PATCH | ✅ **Released** |
| v0.5.0.0 | C4 TMS integration | MINOR | Planned |

---

## 5. NOTES

### Structural Decisions

**2026-02-10:** v0.4.0.0 released — Major milestone: C2 (HOTAS Fundamentals) integrated, establishing conceptual foundation for SOI, master modes, and HOTAS switch behavior. Structural reorganization completed: DMS (C4→C3), TMS (C3→C4). SOI content distribution finalized: C2 provides conceptual foundation, C3 provides operational details with tables. All labels systematically renumbered, all cross-references verified. Issues #22 and #36 closed. Milestone "Integrate C2 and Main Chapter Reorganization" completed (4/4). Infrastructure improvement milestones created: v0.4.1.0 (PATCH — hotastable v2.0, preamble, List of Tables) and v0.5.0.0 (MINOR — C4 TMS integration). Issues #38, #39, #40 created for C4 development workflow.

**2026-02-11:** v0.4.1.0 released — PATCH for LaTeX infrastructure improvements (Issues #33, #34). hotastable environment updated to v2.1 with optimized parameters (footnotesize font, adjusted spacing, Training column simplified to numbers only). List of HOTAS Tables automated indexing feature implemented with `\listofhotastables` macro (requires `\phantomsection` for correct PDF bookmark navigation). Cross-reference macros added (`\secref`, `\chapref`, `\tabref`, `\figref`) for full-phrase clickability. PDF metadata configuration via `\hypersetup` added. enumitem package integrated. BRIEFING-v0.2.0.1 updated with complete preamble v2.1 specification. Obsolete `training-mission-abbrev-table-v1.0.md` removed. Milestone "Infrastructure Improvements" completed (2/2). Total commits: 479.

---

**END OF PROJECT TRACKING v5.0.0**

{% endraw %}
