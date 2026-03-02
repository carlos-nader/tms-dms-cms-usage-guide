---
layout: default
title: "Project Tracking"
sitemap:
  priority: 0.3
  changefreq: monthly
---
{% raw %}

# PROJECT TRACKING
## Falcon BMS TMS/DMS/CMS HOTAS Guide

**Document Version:** PROJECT-TRACKING (2026-03-02)
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-03-02  
**Repository:** carlos-nader/tms-dms-cms-usage-guide

This document tracks governance rules, project state, and development history. For detailed file tracking, issue status, and commit history, see [INTEGRATED-FILES.md](../INTEGRATED-FILES.md) (auto-generated).

---

## 1. GOVERNANCE LAYER

| Document | Last Updated | Purpose |
|----------|-------------|---------|
| VERSION-SYSTEM | 2026-02-25 | Versioning rules (`docs/version-system.md`) |
| BRIEFING | 2026-02-25 | Content scope, layout standard, preamble architecture (`docs/briefing.md`) |
| WIP-FILE-NAMING | 2026-02-25 | File naming conventions and status lifecycle (`docs/wip-naming.md`) |
| TEMPLATES | 2026-02-10 | Canonical WIP template (`template/template-wip.tex`) |
| CHANGELOG | 2026-02-18 | Release history and integration milestones (`CHANGELOG.md`) |
| STYLE-GUIDE | 2026-02-21 | Prose style, voice, formatting, and prohibited patterns (`misc/STYLE-GUIDE.md`) |

**Rule:** All WIP files must be created from `TEMPLATES/template-wip.tex`.

---

## 2. PROJECT SNAPSHOT

**Last updated:** 2026-03-02

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.4.1.1 |
| **Phase** | Phase 0 — Chapter Scaffolding |
| **Chapters Planned** | 7 |
| **Chapters Integrated** | 4/7 (C1, C2, C3, C5) |
| **Chapters In Development** | 1/7 (C4) |
| **Chapters Pending** | 2/7 (C6, C7) |
| **Total Commits** | 768 |
| **Latest Release** | v0.4.1.1 (2026-02-18) |

### Chapter Status

| Ch | Title | Status | Notes |
|----|-------|--------|-------|
| 1 | Introduction | ✅ Integrated | Revised and integrated (v0.3.3.0) |
| 2 | HOTAS Fundamentals | ✅ Integrated | Complete (v0.4.0.0) |
| 3 | DMS | ✅ Integrated | Complete (v0.4.0.0, renumbered from Ch 4) |
| 4 | TMS | 🔄 **review** | WIP: Main chapter file `chapter-C4-tms-structure-dev-2026-02-13.tex`. Section file: `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,729 bytes, §4.3 A-A intro + §4.3.5 IFF intro + §4.3.5.1 SCAN Mode + §4.3.5.2 LOS Mode: **~28.57% complete**) + dependency `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (20,687 bytes, TGP intro for C2, status **final**). Subsections §4.3.1–§4.3.4, §4.3.5.3–§4.3.5.5, §4.3.6 remain in draft. **C4 WIP resumed** after v0.4.1.1 completion. |
| 5 | CMS | ✅ Integrated | Style revision complete (`wip/chapter-C5-style-rev-review-2026-02-26.tex`, 37,709 bytes). WIP status: **review** — author review in progress (§5.1–§5.2.4 approved, §5.3 pending). Pending #48 resolution and author final check → final. |
| 6 | Training References | Scaffolded | Pending development |
| 7 | Visual Reference | Scaffolded | Structure TBD |

### 2.1 Style Revision Snapshot — v0.4.2.0

Style revision pass currently underway to remove AI-generated prose patterns across all integrated chapters. See issue #44 and §4 Target 1 for full details.

| Metric | Value |
|--------|-------|
| **Target Version** | v0.4.2.0 |
| **Milestone** | Style Revision |
| **Chapters in Scope** | 5 (C1, C2, C3, C4, C5) |
| **Chapters Revised** | 1/5 (C5 — pending final approval) |
| **Chapters In Progress** | 1/5 (C5) |
| **Chapters Pending** | 4/5 (C1, C2, C3, C4) |
| **Open Issues** | #44 (style revision), #46 (C1), #47 (C2), #48 (C5 — BYP/STBY modes) |

### Chapter Style Revision Status

| Ch | Title | Style Rev. | Notes |
|----|-------|-----------|-------|
| 1 | Introduction | 🟡 Pending | — |
| 2 | HOTAS Fundamentals | 🟡 Pending | — |
| 3 | DMS | 🟡 Pending | — |
| 4 | TMS | 🟡 Pending | WIP: `section-C4-S3-tms-aa-review-2026-02-17.tex` — style review required before development resumes |
| 5 | CMS | 🔄 In progress | Style revision complete. Author final review in progress. Issue #48 open. |

---

## 3. DEVELOPMENT LOG

Chronological record of significant changes. For detailed commit history, see INTEGRATED-FILES.md.

| Date | Guide Version | Key Changes |
|------|---------------|-------------|
| 2026-01-05 | v0.1.0.0 | Initial project setup. Chapter scaffolding. Introduction integrated. |
| 2026-01-07 | v0.1.4.0 | Layout standard adopted. BRIEFING created. Geometry locked. |
| 2026-01-11 | v0.2.4.0 | Chapter 5 (CMS) complete. Template-wip.tex established. |
| 2026-01-14 | v0.3.0.0 | **RELEASE:** DMS Sections 4.1 and 4.2 integrated. |
| 2026-01-18 | v0.3.1.0 | **RELEASE:** Preamble infrastructure upgrade (article → report class). |
| 2026-01-19 | v0.3.2.0 | **RELEASE:** Section 4.3 (DMS Down) integrated. |
| 2026-01-29 | v0.3.2.1 | **RELEASE:** Hotastable environment upgrade (arraystretch 1.25). |
| 2026-02-02 | v0.3.3.0 | **RELEASE:** C4 (DMS) complete chapter integrated. C1 (Introduction) revised and integrated. Milestone v0.3.3.0 completed (10/10 issues). |
| 2026-02-09 | v0.4.0.0 | **RELEASE:** C2 (HOTAS Fundamentals) integrated. C3↔C4 chapter renumbering (DMS → C3, TMS → C4). |
| 2026-02-11 | v0.4.1.0 | **RELEASE:** Infrastructure improvements (hotastable v2.1, List of HOTAS Tables, cross-ref macros, PDF metadata). |
| 2026-02-18 | v0.4.1.1 | **RELEASE:** Repetition cleanup (9 corrections across C1–C5) + hotastable `\label` fixes. Forum contribution by user Daddyk (post #450980). |
| 2026-02-19 → 2026-02-23 | — | **Style revision (C5) — complete.** Decision to conduct v0.4.2.0 style revision pass following community feedback (BMS Forum, users Van and mirv). Issue #44 opened. Milestone "v0.4.2.0 — Style Revision" created (due 2026-03-20). TMS milestone due date updated from 2026-03-10 to 2026-04-20. STYLE-GUIDE created and promoted to public (`misc/STYLE-GUIDE.md`). BRIEFING §5.3 updated with mandatory STYLE-GUIDE reference. WIP file: `wip/chapter-C5-style-rev-review-2026-02-22.tex` (36,771 bytes). C5 style revision completed (§5.1–§5.3): full prose rewrite, hotastable cells revised, Dash-34 validation pass executed (imprecisions corrected, Program 5 mention added, RF Switch Override rewritten). Sub-issue #48 opened: BYP and STBY modes not covered in §5.2.1 — cascade impacts mapped across C5. WIP status: **review** (pending #48 + author final check → final). Total commits: 603 → **649** (+46 commits). |
| 2026-02-24 | — | **Author review pass (C5) — in progress.** WIP file updated to `wip/chapter-C5-style-rev-review-2026-02-24.tex` (36,343 bytes). Author review started: §5.1 approved (session 2026-02-23). Session 2026-02-24: §5.2 opening, §5.2.1 opening, §5.2.1.1–§5.2.1.3 prose and tables approved. Session 2026-02-24 (2): §5.2.1 Program 5 sentence, §5.2.1.2 prose, §5.2.1.3 prose approved. §5.2.2–§5.3 pending. See issue #44 for full change log. Total commits: 649 → **669** (+20 commits). |
| 2026-03-02 | — | **MERGED:** Alpha release infrastructure integrated into `main` (PR #50, issue #49 closed). Integrated files report regenerated. |

---

## 4. NEXT TARGETS

### Target 1: Style Revision → v0.4.2.0 (PATCH)

| Item | Value |
|------|-------|
| **Status** | **In Progress** — C5 author review in progress (§5.1–§5.2.4 approved, §5.3 pending). Next: complete C5 author review (§5.3), then C1, C2, C3. |
| **Milestone** | "v0.4.2.0 — Style Revision" (due 2026-03-20, progress 1/5) |
| **Open Issues** | #44 (Style revision: remove AI-speak across all integrated chapters), #46 (C1), #47 (C2), #48 (C5 — Add BYP and STBY modes to §5.2.1) |
| **Version Bump** | PATCH: style revision affects multiple chapters simultaneously; not a simple correction |
| **Scope** | All integrated chapters: C1, C2, C3 (DMS), C5 (CMS) |
| **Criteria** | Remove abstract/eloquent phrasing that no human technical writer would produce; prioritize clarity and directness over elegance. Adhere to `misc/STYLE-GUIDE.md`. |
| **Next step** | Complete C5 author review (§5.3). Resolve #48 within C5 WIP before → final. Then open WIP files for C1, C2, C3 style revision passes. |
| **WIP Files** | `wip/chapter-C5-style-rev-review-2026-02-26.tex` (C5: **review**, 100% style-revised — author review in progress, §5.3 pending) |
| **Forum** | Next forum post planned for v0.4.2.0 release; forum thread left to cool down after Feb 19 exchange |

---

### Target 2: Chapter 4 — TMS → v0.5.0.0 (MINOR)

| Item | Value |
|------|-------|
| **WIP Files** | `chapter-C4-tms-structure-dev-2026-02-13.tex` (main), `section-C4-S3-tms-aa-review-2026-02-17.tex` (§4.3: **review**), `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (dependency: **final**) |
| **Status** | **Resumed** after v0.4.1.1 completion. Active status: `review` (C4:§4.3 intro, C4:§4.3.5 intro, C4:§4.3.5.1, C4:§4.3.5.2), `dev` (remaining subsections) |
| **Milestone** | "Integrate C4:S3 (TMS — AA) — Guide Version v0.5.0.0" (due 2026-04-20, progress 0/3) |
| **Open Issues** | #38 (REVIEW — resumed), #39 (FINAL), #40 (APPROVED) |
| **Version Bump** | MINOR (new chapter entry) |
| **Content** | TMS concept, situational awareness, A-A employment, A-G employment, weapon-specific behavior, block/variant notes. Most complex HOTAS switch (13+ specialized tables). |
| **Dependencies** | ✅ v0.4.1.1 completed; ⚠️ v0.4.2.0 (style revision) should precede or run in parallel |
| **Next step** | Resume §4.3.5 subsections S3–S5 (Emergency, Constraints, AIFF Availability) → §4.3.1–§4.3.4 (SAM, STT, TWS, ACM) → §4.3.6 (TGP A-A) → populate 6 hotastable tables → review → final → approved |

**Chapter 4 Progress - PAUSED DUE TO ISSUE #44:**
- ✅ C4:§4.3.5 (TMS and IFF Interrogation) introduction refined
- ✅ C4:§4.3.5.1 (SCAN Interrogation Mode) narrative completed
- ✅ C4:§4.3.5.2 (LOS Interrogation Mode) narrative completed
- ✅ Dash-34 cross-references validated: §2.2.4.4.2.1, §2.2.4.4.2.1.1, §2.2.4.4.2.1.2, §2.2.4.4.2.2, §2.3.1.5.1.6.2
- 🟡 Pending: §4.3.5.3 (Emergency Mode), §4.3.5.4 (Constraints), §4.3.5.5 (AIFF Availability)
- 🟡 Pending: §4.3.1–§4.3.4 (SAM, STT, TWS, ACM), §4.3.6 (TGP A-A)
- 🟡 Pending: Populate 6 hotastable tables (0/6 complete)

**Style Revision Progress - v0.4.2.0:**
- 🔄 C5 (CMS) — author review in progress (`wip/chapter-C5-style-rev-review-2026-02-26.tex`, §5.1–§5.2.4 approved, §5.3 pending #48)
- 🟡 C1 (Introduction) — pending
- 🟡 C2 (HOTAS Fundamentals) — pending
- 🟡 C3 (DMS) — pending

---

### Version Roadmap

| Version | Content | Bump Type | Status |
|---------|---------|-----------|--------|
| v0.4.0.0 | C2 HOTAS Fundamentals + C3↔C4 reorganization | MINOR | ✅ Released |
| v0.4.1.0 | Infrastructure improvements (hotastable v2.1, List of HOTAS Tables, cross-refs, PDF metadata) | PATCH | ✅ Released |
| v0.4.1.1 | Repetition cleanup (9 corrections across C1–C5) + hotastable `\label` fixes | SUBPATCH | ✅ Released |
| v0.4.2.0 | Style revision: remove AI-speak across C1, C2, C3, C5 | PATCH | 🔄 In Progress (Issue #44, due 2026-03-20) |
| v0.4.2.0-alpha.1 | First alpha pre-release — C5 style revision (triggered after #48 resolved + author approval) | pre-release | 📋 Planned (alpha release infrastructure integrated; no pre-release tags yet) |
| v0.5.0.0 | C4 TMS integration | MINOR | ⏸️ Pending v0.4.2.0 (due 2026-04-20) |

---

## 5. NOTES

### Structural Decisions

**2026-02-13:** C4 WIP files updated. Main chapter file renamed to `chapter-C4-tms-structure-dev-2026-02-13.tex` (52,056 bytes). Section file `section-C4-S3-tms-aa-dev-2026-02-13.tex` (33,612 bytes) created, covering §4.3 — TMS in Air-to-Air. Structure validated: 6 subsections (§4.3.1 SAM, §4.3.2 STT, §4.3.3 TWS, §4.3.4 ACM, §4.3.5 IFF, §4.3.6 TGP A-A), labels consistent (`sec:C4-S3-S*`), cross-refs functional, 6 hotastable placeholders defined. Content state: structural outline with bullet points and technical accuracy, NOT narrative prose. Critical gap identified: current text uses itemized lists, not continuous narrative as required by C3/C5 style standard. Next phase: (1) transform to flowing prose, (2) fill tables with Dash-34 data, (3) validate all technical refs. File remains `dev` status. Total commits: 523.

**2026-02-15:** C4 WIP advancement continues. Section file `section-C4-S3-tms-aa-review-2026-02-15.tex` promoted to `review` status after §4.3 introduction finalization (39,095 bytes, +16.3% from 33,612 bytes). Introduction text validated for grammar accuracy, Dash-34 cross-references (§2.3.1.5.7-12), internal cross-references (→C2:§2.1.3, →C3:§3.1.1, →C3:§3.1.3), and prose cadence. Corrections applied: replaced "exclusively" with "restricted to" (para 2, precision), added "primary" qualifier to FCR mode description (para 3, clarity). **Critical dependency identified:** TGP (Targeting Pod) first mention should occur in C2 conceptual layer, not C4 operational layer. New WIP file created: `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (20,493 bytes, status `final`). Establishes §2.1.3 (TGP as equipment-dependent SOI: AN/AAQ-33 Sniper XR ATP, AN/AAQ-14 LANTIRN), cross-references Dash-34 §2.6 and →C4:§4.3.6 (TGP A-A tracking). Dependency resolution ensures architectural consistency: C2 establishes concepts, C3/C4 provide operational details. §4.3 subsections (§4.3.1–§4.3.6: SAM, STT, TWS, ACM, IFF, TGP A-A) remain in draft status with bullet-point structure; 6 hotastable tables (0/6 complete) pending data population from Dash-34 §2.3.1.5.x, §2.5, §2.6.1.7.5, §4.3.2.4.3.12 and BMS Training Manual missions. Integration target: v0.5.0.0 (simultaneous integration of C2:§2.1.3 + C4:§4.3 introduction). Issues #38 (REVIEW) and #40 (APPROVED — integration checklist) updated with progress. Total commits: 558.

**2026-02-17:** C4 WIP advancement continues. Section file renamed to `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,744 bytes). §4.3.5 (TMS and IFF Interrogation) introduction refined: "cockpit identification methods" substituted for "identification procedures" (precision improvement). §4.3.5.1 (SCAN Interrogation Mode) narrative completed: TMS Left short press (<0.6s) activation, SCAN configuration via DED INTG page and FCR CNTL OSB 10 (decouple/couple to radar scan volume), symbology identification (green circle = friendly, yellow square = bogey/unknown), tactical context (BVR intercepts, ROE compliance, multiple unknown contacts). Dash-34 cross-references validated: §2.2.4.4.2.1.1 (SCAN behavior), §2.3.1.5.1.6.2 (FCR CNTL OSB 10). **§4.3.5.2 (LOS Interrogation Mode) narrative completed:** concept (beam coverage area, cursor-directed, 2 beams vs SCAN), behavior (TMS Left ≥0.6s, 16 replies, beam geometry nuance, range filtering), configuration (DED INTG + DCS right SEQ→LOS page, independent from SCAN), symbology (cross-ref to §4.3.5.1, reduced redundancy), tactical context (BVR designated target; unsupported "VID passes" claim removed). Dash-34 cross-references validated: §2.2.4.4.2.1, §2.2.4.4.2.1.2, §2.2.4.4.2.2. §4.3.5.5 (AIFF Availability) marked with Link 16 context note for future development. Narrative completion: 25% → ~28.57% (4 subsections complete: §4.3 intro, §4.3.5 intro, §4.3.5.1, §4.3.5.2). Subsections §4.3.1–§4.3.4 (SAM, STT, TWS, ACM), §4.3.5.3–§4.3.5.5 (Emergency, Constraints, AIFF Availability), §4.3.6 (TGP A-A) remain in draft. 6 hotastable tables (0/6 complete) pending. Total commits: 582.

**2026-02-18:** Repetition audit session. First external contribution to the project: forum user Daddyk identified content repetitions in v0.4.1.0 via [BMS forum post #450980](https://forum.falcon-bms.com/post/450980). Systematic chapter-by-chapter analysis of the full guide (C1–C5) conducted. **10 repetitions catalogued** in `misc/notes-repetition-analysis-v0_4_1_1-20260218.md`: R-01 (C2: SOI definition duplicated in 2.1/2.1.1), R-02 (C2: master mode "determines" re-stated in 2.2.1), R-03 (C2/C3: DMS physical description repeated), R-04 (C2/C5: CMS boilerplate in 3 locations), R-05 (C3: NAV/A-G PRE DMS Down paragraphs literally identical), R-06 (C3: Snowplow/MARK/OFLY exception states described twice), R-07 (C3/C5: "Each table entry specifies" block repeated 4×; includes copy-paste error line 1359 "DMS hat" in CMS table), R-08 (C5: CMS Down joint consent stated twice consecutively), R-09 (C5: high-G rationale paraphrased in 5.2.4), R-10 (C5: IDIAS/CMS Left distinction — classified Aceitável, no action). Issue #42 opened and structured with prioritized checklist. Milestone 6 active. Forum reply posted. C4 WIP (Issues #38–#40) suspended; v0.4.1.1 takes priority. Total commits: 587.

**2026-02-19 → 2026-02-23:** Style revision decision and C5 completion. Community feedback received on BMS Forum (users Van and mirv) prompted v0.4.2.0 style revision pass. Issue #44 opened. Milestone "v0.4.2.0 — Style Revision" created (due 2026-03-20). TMS milestone due date updated from 2026-03-10 to 2026-04-20. STYLE-GUIDE created and promoted to public (`misc/STYLE-GUIDE.md`). BRIEFING §5.3 updated with mandatory STYLE-GUIDE reference. WIP file: `wip/chapter-C5-style-rev-review-2026-02-22.tex` (36,771 bytes). C5 style revision completed (§5.1–§5.3): full prose rewrite, hotastable cells revised, Dash-34 validation pass executed (imprecisions corrected, Program 5 mention added, RF Switch Override rewritten). Sub-issue #48 opened: BYP and STBY modes not covered in §5.2.1 — cascade impacts mapped across C5. WIP status: **review** (pending #48 + author final check → final). Total commits: 603 → **649** (+46 commits).

**2026-02-24:** Author review pass (C5) — in progress. WIP file updated to `wip/chapter-C5-style-rev-review-2026-02-24.tex` (36,343 bytes). Author review started: §5.1 approved (session 2026-02-23). Session 2026-02-24: §5.2 opening, §5.2.1 opening, §5.2.1.1–§5.2.1.3 prose and tables approved. Session 2026-02-24 (2): §5.2.1 Program 5 sentence, §5.2.1.2 prose, §5.2.1.3 prose approved. §5.2.2–§5.3 pending. See issue #44 for full change log. Total commits: 649 → **669** (+20 commits).

**2026-02-25:** Author review pass (C5) — continued. WIP file updated to `wip/chapter-C5-style-rev-review-2026-02-25.tex`. Session 2026-02-25: §5.2.1.2 table L3 duplicate Function cell removed; §5.2.2–§5.2.4 prose and tables approved (§5.2.2 opening, §5.2.2.1–§5.2.2.2 prose and tables, §5.2.3 title/prose/table, §5.2.4 all five paragraphs). §5.3 pending. See issue #44 for full change log. Total commits: 669 → **711** (+42 commits).

**2026-02-26:** Alpha release infrastructure planning completed. Alpha flow designed as optional parallel extension to the standard WIP flow (`final → alpha → approved`); standard flow remains intact and unchanged. Planning documents created: `misc/alpha-release-impl.md` (implementation plan — Steps 1–19, 17 files to modify + 1 to create) and `misc/alpha-release-impact.md` (full repository impact analysis — all scripts, workflows, and governance files assessed). First alpha target: `v0.4.2.0-alpha.1` (triggered after C5 author review complete + issue #48 resolved + author approval). All design decisions resolved (§16 in impl.md). Implementation executed on `feat/alpha-release` and merged on 2026-03-02 (PR #50). Total commits: 711 → **732** (+21 commits).

**2026-03-02:** Alpha release infrastructure integrated into `main` (PR #50; issue #49 closed). Integrated files report regenerated.

---

**END OF PROJECT TRACKING**

{% endraw %}
