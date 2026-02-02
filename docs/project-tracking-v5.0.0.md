---
layout: default
---
{% raw %}

# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING-v6.0.0  
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

**Last updated:** 2026-02-02

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.3.2.1 |
| **Phase** | Phase 0 — Chapter Scaffolding |
| **Chapters Planned** | 7 |
| **Chapters with Narrative** | 3/7 (C1, C4, C5) |
| **Chapters Scaffolded** | 4/7 (C2, C3, C6, C7) |
| **Total Commits** | 313 |
| **Latest Release** | v0.3.2.1 (2026-01-29) |

### Chapter Status

| Ch | Title | Status | Notes |
|----|-------|--------|-------|
| 1 | Introduction | Revision in progress | WIP: `chapter-C1-introduction-dev-2026-02-02.tex` |
| 2 | HOTAS Fundamentals | dev | WIP: `chapter-C2-hotas-fundamentals-dev-2026-01-25.tex` |
| 3 | TMS | Scaffolded | Pending development |
| 4 | DMS | final | WIP: `chapter-C4-dms-final-2026-02-01.tex` — ready for integration |
| 5 | CMS | Integrated | Complete (§5.1, §5.2, §5.3) |
| 6 | Training References | Scaffolded | Pending development |
| 7 | Visual Reference | Scaffolded | Structure TBD |

---

## 3. DEVELOPMENT LOG

Chronological record of significant changes. For detailed commit history, see INTEGRATED-FILES.md.

| Date | Guide Version | Key Changes |
|------|---------------|-------------|
| 2026-01-05 | v0.1.0.0 | Initial project setup. Chapter scaffolding. Introduction integrated. VERSION-SYSTEM-v1.0.0 established. |
| 2026-01-06 | v0.1.1.0 | Placeholder subsections added. |
| 2026-01-07 | v0.1.4.0 | Layout standard adopted. BRIEFING created. Geometry locked. |
| 2026-01-07 | v0.2.0.1 | CMS Section 5.1 integrated. |
| 2026-01-08 | v0.2.1.0 | Chapter 5 structure refined (5.1–5.3). WIP-FILE-NAMING created. |
| 2026-01-09 | v0.2.2.0 | CMS Section 5.2 integrated. Geometry Option D locked. |
| 2026-01-10 | v0.2.3.0 | CMS HOTAS table integrated into Section 5.2. |
| 2026-01-10 | v0.2.3.1 | CMS table column explanations added. SUBPATCH. |
| 2026-01-11 | v0.2.4.0 | CMS Section 5.3 integrated. Chapter 5 complete. Template-wip-V1.0.tex established. |
| 2026-01-13 | — | DMS blueprint v1.0 created. |
| 2026-01-14 | — | DMS blueprint v1.1 finalized (direction-based structure). |
| 2026-01-14 | v0.3.0.0 | **RELEASE:** DMS Sections 4.1 and 4.2 integrated. GitHub Release tag created. |
| 2026-01-16 | v0.3.0.1 | Section 4.2 table column explanations added. PATCH. |
| 2026-01-17 | — | DMS Down WIP promoted to review. |
| 2026-01-18 | — | DMS Down WIP promoted to final. BRIEFING Section 11 expanded (~8,000 words). |
| 2026-01-18 | v0.3.1.0 | **RELEASE:** Preamble infrastructure upgrade (article → report class, titlesec, twoside). |
| 2026-01-19 | v0.3.2.0 | **RELEASE:** Section 4.3 integrated. Redaction corrections in 4.1/4.2. |
| 2026-01-19 | — | PROJECT-TRACKING-v5.0.0 released. |
| 2026-01-20 | — | DMS Left/Right WIP development started. |
| 2026-01-21 | — | DMS Left/Right promoted to review. |
| 2026-01-25 | — | C2 HOTAS Fundamentals WIP created. |
| 2026-01-29 | v0.3.2.1 | **RELEASE:** Hotastable environment upgrade (arraystretch 1.25). Chapter 4/5 corrections. |
| 2026-01-30 | — | C4:S4 issues closed (#16, #17, #18). C4 consolidated into full chapter WIP. |
| 2026-02-01 | — | C4 chapter promoted to final (`chapter-C4-dms-final-2026-02-01.tex`). |
| 2026-02-02 | — | C1 revision: structural analysis, new WIP created (`chapter-C1-introduction-dev-2026-02-02.tex`). |

---

## 4. NEXT TARGETS

### Target 1: Chapter 4 Integration → v0.3.3.0 (PATCH)

| Item | Value |
|------|-------|
| **WIP File** | `chapter-C4-dms-final-2026-02-01.tex` |
| **Status** | final — ready for integration |
| **Milestone** | v0.3.3.0 (Due: 2026-02-06, progress 5/7) |
| **Open Issues** | #27 (FINAL), #28 (APPROVED) |
| **Version Bump** | PATCH (section/content integration, not new chapter) |

**Next step:** Author approval → integration into guide.tex → v0.3.3.0 release

---

### Target 2: Chapter 1 Revision → v0.3.3.x (SUBPATCH)

| Item | Value |
|------|-------|
| **WIP File** | `chapter-C1-introduction-dev-2026-02-02.tex` |
| **Status** | dev |
| **Issue** | #26 (Rewrite C1) |
| **Version Bump** | SUBPATCH (refinement of existing chapter) |

**Changes:**
- Eliminated intro/§1.1 redundancy
- Added Claude to AI acknowledgment (alongside Perplexity)
- Simplified license section (summary + link)
- New §1.4.3 (GitHub as canonical source)
- Clear C7 explanation as visual quick reference

**Next step:** dev → review → final → integration

---

### Target 3: Chapter 2 — HOTAS Fundamentals → v0.4.0.0 (MINOR)

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

### Version Roadmap

| Version | Content | Bump Type | Status |
|---------|---------|-----------|--------|
| v0.3.3.0 | C4 complete integration + C4:S1-S3 rewrite | PATCH | In progress |
| v0.3.3.x | C1 revision | SUBPATCH | Planned |
| v0.4.0.0 | C2 HOTAS Fundamentals | MINOR | Planned |
| v0.5.0.0 | C3 TMS (or additional chapter) | MINOR | Future |

---

## 5. NOTES

### Structural Decisions

**2026-01-14:** Chapter 4 (DMS) follows direction-based structure per blueprint v1.1:
- §4.1 Concept and SOI
- §4.2 DMS Up
- §4.3 DMS Down
- §4.4 DMS Left/Right
- §4.5 Master Mode Summary (pending)

**2026-01-30:** C4 sections consolidated into single chapter WIP file for final review and integration.

**2026-02-02:** C1 revision addresses redundancy, incomplete AI credit, and confusing structure. New organization moves version/authorship to end (§1.4) and streamlines document structure explanation (§1.3).

---

**END OF PROJECT TRACKING v6.0.0**

{% endraw %}
