---
layout: default
---
{% raw %}

# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-02-02  
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

**Last updated:** 2026-02-03

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.3.3.0 |
| **Phase** | Phase 0 — Chapter Scaffolding |
| **Chapters Planned** | 7 |
| **Chapters Integrated** | 3/7 (C1, C4, C5) |
| **Chapters In Development** | 1/7 (C2) |
| **Chapters Pending** | 3/7 (C3, C6, C7) |
| **Total Commits** | 340 |
| **Latest Release** | v0.3.3.0 (2026-02-02) |

### Chapter Status

| Ch | Title | Status | Notes |
|----|-------|--------|-------|
| 1 | Introduction | ✅ Integrated | Revised and integrated (v0.3.3.0) |
| 2 | HOTAS Fundamentals | dev | WIP: `chapter-C2-hotas-fundamentals-dev-2026-01-25.tex` |
| 3 | TMS | Scaffolded | Pending development |
| 4 | DMS | ✅ Integrated | Complete chapter integrated (v0.3.3.0) |
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

---

## 4. NEXT TARGETS

### Target 1: Chapter 2 — HOTAS Fundamentals → v0.4.0.0 (MINOR)

| Item | Value |
|------|-------|
| **WIP File** | `chapter-C2-hotas-fundamentals-dev-2026-01-25.tex` |
| **Status** | dev |
| **Milestone** | v0.4.0.0 (Due: 2026-02-15, progress 0/3) |
| **Open Issues** | #20 (REVIEW), #21 (FINAL), #22 (APPROVED) |
| **Version Bump** | MINOR (new chapter entry) |

**Content:** SOI concept, short/long press timing, master modes, HOTAS switch categories.

**Next step:** dev → review (Issue #20)

---

### Target 2: Chapter 3 — TMS → v0.5.0.0 (MINOR)

| Item | Value |
|------|-------|
| **WIP File** | TBD |
| **Status** | Scaffolded |
| **Version Bump** | MINOR (new chapter entry) |

**Next step:** Create WIP file, begin development

---

### Version Roadmap

| Version | Content | Bump Type | Status |
|---------|---------|-----------|--------|
| v0.3.3.0 | C4 complete + C1 revision | PATCH | ✅ **Released** |
| v0.4.0.0 | C2 HOTAS Fundamentals | MINOR | In progress |
| v0.5.0.0 | C3 TMS | MINOR | Planned |

---

## 5. NOTES

### Structural Decisions

**2026-02-02:** C1 revision completed — eliminated redundancy, added Claude to AI acknowledgment, simplified license section, added §1.4.3 (GitHub as canonical source).

**2026-02-02:** v0.3.3.0 released — C4 and C1 integrated in same release (10 issues closed).

---

**END OF PROJECT TRACKING v5.0.0**

{% endraw %}
