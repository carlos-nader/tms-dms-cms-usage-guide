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

**Document Version:** PROJECT-TRACKING-v5.0.0  
**Regime:** Pre-publication (0.x.x.x)  
**Project Start:** 2026-01-05  
**Last Updated:** 2026-02-18  
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

**Last updated:** 2026-02-18

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.4.1.0 |
| **Phase** | Phase 0 — Chapter Scaffolding |
| **Chapters Planned** | 7 |
| **Chapters Integrated** | 4/7 (C1, C2, C3, C5) |
| **Chapters In Development** | 1/7 (C4) |
| **Chapters Pending** | 2/7 (C6, C7) |
| **Total Commits** | 587 |
| **Latest Release** | v0.4.1.0 (2026-02-11) |

### Chapter Status

| Ch | Title | Status | Notes |
|----|-------|--------|-------|
| 1 | Introduction | ✅ Integrated | Revised and integrated (v0.3.3.0) |
| 2 | HOTAS Fundamentals | ✅ Integrated | Complete (v0.4.0.0) |
| 3 | DMS | ✅ Integrated | Complete (v0.4.0.0, renumbered from Ch 4) |
| 4 | TMS | 🔄 **review** | WIP: Main chapter file `chapter-C4-tms-structure-dev-2026-02-13.tex`. Section file: `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,744 bytes, §4.3 A-A intro + §4.3.5 IFF intro + §4.3.5.1 SCAN Mode + §4.3.5.2 LOS Mode: **~28.57% complete**) + dependency `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (TGP intro for C2, status **final**). Subsections §4.3.1–§4.3.4, §4.3.5.3–§4.3.5.5, §4.3.6 remain in draft. **C4 WIP suspended** pending v0.4.1.1 repetition cleanup (Issue #42). |
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
| 2026-02-13 | — | **C4 WIP Progress:** Main chapter file renamed to `chapter-C4-tms-structure-dev-2026-02-13.tex` (52,056 bytes). Section file `section-C4-S3-tms-aa-dev-2026-02-13.tex` (33,612 bytes) created, covering §4.3 — TMS in Air-to-Air. Covers TMS behavior in A-A contexts: FCR modes (SAM, STT, TWS), ACM modes (BORE, 10×60, 30×20, SLEW with HMCS integration), IFF interrogation, and TGP A-A mode. Structure complete: 6 subsections (§4.3.1–§4.3.6), 6 table placeholders, cross-references validated. Content state: structural outline with bullet points (not narrative prose). Pending: transform to narrative (C3/C5 style) + fill 6 hotastable tables with Dash-34/Training Manual data. Total commits: 523. |
| 2026-02-15 | — | **C4 WIP Progress (continued):** Section file promoted from `dev` to `review`: `section-C4-S3-tms-aa-review-2026-02-15.tex` (39,095 bytes, +16.3% size increase). §4.3 introduction finalized and validated: grammar corrections, Dash-34 cross-references (§2.3.1.5.7-12) verified, internal cross-references (→C2:§2.1.3, →C3:§3.1.1, →C3:§3.1.3) confirmed, prose cadence refined. Corrections applied: "exclusively" → "restricted to" (para 2), added "primary" qualifier to "FCR provides four **primary** tracking modes" (para 3). **Dependency WIP created:** `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (20,493 bytes, status `final`). Establishes TGP (Targeting Pod) introduction in C2 fundamentals (§2.1.3), defines TGP as equipment-dependent (AN/AAQ-33 Sniper XR ATP, AN/AAQ-14 LANTIRN), cross-references →C4:§4.3.6 (TGP A-A tracking) and Dash-34 §2.6. Rationale: First TGP mention should occur in C2 conceptual layer, not C4 operational layer. §4.3 subsections §4.3.1–§4.3.6 (SAM, STT, TWS, ACM, IFF, TGP A-A) remain in draft status; 6 hotastable tables (0/6 complete) pending population. Integration target: **v0.5.0.0** (simultaneous integration of C2:§2.1.3 + C4:§4.3 introduction). Issues #38 (REVIEW — in progress) and #40 (APPROVED — integration checklist) updated. Total commits: 558. |
| 2026-02-17 | — | **C4 WIP Progress (continued):** Section file updated and renamed: `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,744 bytes). §4.3.5 (TMS and IFF Interrogation) introduction refined: "cockpit identification methods" substituted "identification procedures" for precision. §4.3.5.1 (SCAN Interrogation Mode) narrative completed and approved: TMS Left short press (<0.6s) behavior, SCAN configuration (DED INTG page, FCR CNTL OSB 10), symbology (green circle = friendly, yellow square = bogey/unknown), tactical context (BVR intercepts, ROE compliance, multiple contacts). Dash-34 cross-references validated (§2.2.4.4.2.1.1, §2.3.1.5.1.6.2). **§4.3.5.2 (LOS Interrogation Mode) narrative completed and approved:** concept (beam coverage area, cursor-directed, 2 beams, comparison vs SCAN), behavior (TMS Left ≥0.6s, 16 replies, beam geometry nuance, range filtering), configuration (DED INTG + DCS right SEQ→LOS page, independent from SCAN), symbology (cross-ref to §4.3.5.1), tactical context (BVR designated target; unsupported "VID passes" claim removed). Dash-34 cross-references validated (§2.2.4.4.2.1, §2.2.4.4.2.1.2, §2.2.4.4.2.2). §4.3.5.5 (AIFF Availability) updated with Link 16 context marking for future development. Narrative completion: 25% → **~28.57%** (4 subsections complete: §4.3 intro, §4.3.5 intro, §4.3.5.1, §4.3.5.2). Subsections §4.3.1–§4.3.4 (SAM, STT, TWS, ACM), §4.3.5.3–§4.3.5.5 (Emergency, Constraints, AIFF Availability), §4.3.6 (TGP A-A) remain in draft. 6 hotastable tables (0/6 complete) pending. Total commits: 558 → **582** (+24 commits). |
| 2026-02-18 | — | **Editorial Audit — Repetition Analysis:** Community feedback from forum user [Daddyk](https://forum.falcon-bms.com/user/daddyk) ([post #450980](https://forum.falcon-bms.com/post/450980)) identified content repetitions in v0.4.1.0. First external community review contribution to the project. Systematic audit of Chapters 1–5 conducted across two sessions. **10 repetitions identified:** R-01 to R-09 actionable (4 Alta, 3 Média, 1 Baixa, 1 Alta-estrutural); R-10 classified Aceitável (intentional safety-critical repetition). Analysis document committed: `misc/notes-repetition-analysis-v0_4_1_1-20260218.md`. Issue #42 opened with full checklist and resolution order. Milestone 6 ("Review identified repetitions for version bump to v0.4.1.1", due 2026-02-22) active. Forum reply posted acknowledging Daddyk's contribution. **C4 WIP suspended** pending v0.4.1.1 resolution (Issue #42 takes precedence over Issue #38). Total commits: 582 → **587**. |

---

## 4. NEXT TARGETS

### Target 1: Repetition Cleanup → v0.4.1.1 (SUBPATCH) ⚠️ Priority

| Item | Value |
|------|-------|
| **Reference Document** | [`misc/notes-repetition-analysis-v0_4_1_1-20260218.md`](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/misc/notes-repetition-analysis-v0_4_1_1-20260218.md) |
| **Status** | Open — pending implementation |
| **Milestone** | Milestone 6: "Review identified repetitions for version bump to v0.4.1.1" (due 2026-02-22, progress 0/1) |
| **Open Issues** | #42 (Repetitions cleaning up — in progress) |
| **Version Bump** | SUBPATCH: wording corrections and cross-reference insertions within existing chapters; no new sections, no structural additions |
| **Repetitions** | 10 identified (R-01 to R-10); R-10 classified Aceitável — no action required |
| **Next step** | Implement corrections in order: R-07 → R-01 → R-05 → R-08 → R-04 → R-02 → R-06 → R-09 → R-03. Additional human review of full v0.4.1.0 recommended to catch any remaining repetitions. |

---

### Target 2: Chapter 4 — TMS → v0.5.0.0 (MINOR)

| Item | Value |
|------|-------|
| **WIP Files** | `chapter-C4-tms-structure-dev-2026-02-13.tex` (main), `section-C4-S3-tms-aa-review-2026-02-17.tex` (§4.3: **review**), `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (dependency: **final**) |
| **Status** | **Suspended** pending v0.4.1.1 (Issue #42). Active status: `review` (C4:§4.3 intro, C4:§4.3.5 intro, C4:§4.3.5.1, C4:§4.3.5.2), `dev` (remaining subsections) |
| **Milestone** | Integrate C4:S3 (TMS — AA) — Guide Version v0.5.0.0 (Due: 2026-03-10, progress 0/3) |
| **Open Issues** | #38 (REVIEW — suspended), #39 (FINAL), #40 (APPROVED) |
| **Version Bump** | MINOR (new chapter entry) |
| **Content** | TMS concept, situational awareness, A-A employment, A-G employment, weapon-specific behavior, block/variant notes. Most complex HOTAS switch (13+ specialized tables). |
| **Dependencies** | ✅ v0.4.1.0 completed (infrastructure ready); ⚠️ v0.4.1.1 must be completed first |
| **Next step** | After v0.4.1.1: resume §4.3.5 subsections S3–S5 (Emergency, Constraints, AIFF Availability) → §4.3.1–§4.3.4 (SAM, STT, TWS, ACM) → §4.3.6 (TGP A-A) → populate 6 hotastable tables → review → final → approved |

**Recent Progress (2026-02-15):**
- ✅ C4:§4.3 introduction finalized and validated (grammar, Dash-34 refs §2.3.1.5.7-12, cadence)
- ✅ File promoted: `section-C4-S3-tms-aa-dev-2026-02-13.tex` → `section-C4-S3-tms-aa-review-2026-02-15.tex`
- ✅ File size increase: 33,612 → 39,095 bytes (+16.3%, introduction expanded and refined)
- ✅ Dependency WIP created: `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (20,493 bytes)
- ✅ TGP introduction added to C2:§2.1.3 (establishes equipment dependency before C4:§4.3.6 reference)
- ✅ Cross-references validated: C2:§2.1.3 ↔ C4:§4.3.6, Dash-34 §2.6, §2.3.1.5.7-12
- ✅ Corrections: "exclusively" → "restricted to", added "primary" to FCR mode description
- 🟡 Pending (suspended): Transform §4.3 subsections §4.3.1–§4.3.6 from bullet points to narrative prose (C3/C5 style)
- 🟡 Pending (suspended): Populate 6 hotastable tables with Dash-34/Training Manual data (0/6 complete)
- 🟡 Pending (suspended): Validate all Dash-34 refs (2.3.1.5.x, 2.5, 2.6.1.7.5, 4.3.2.4.3.12)
- ✅ Total commits: 479 → 558 (+79 commits since last PROJECT-TRACKING update)

**Recent Progress (2026-02-17):**
- ✅ C4:§4.3.5 (TMS and IFF Interrogation) introduction refined: "cockpit identification methods" substituted "identification procedures"
- ✅ C4:§4.3.5.1 (SCAN Interrogation Mode) narrative completed: TMS Left short press behavior, configuration (DED INTG/FCR CNTL OSB 10), symbology, tactical context (BVR/ROE)
- ✅ C4:§4.3.5.2 (LOS Interrogation Mode) narrative completed: concept (beam coverage, cursor-directed, 2 beams), behavior (TMS Left ≥0.6s, 16 replies), configuration (DED INTG + DCS right SEQ→LOS), symbology (cross-ref to §4.3.5.1), tactical context (BVR designated target)
- ✅ Dash-34 cross-references validated: §2.2.4.4.2.1.1 (SCAN), §2.3.1.5.1.6.2 (FCR CNTL OSB 10), §2.2.4.4.2.1 and §2.2.4.4.2.1.2 and §2.2.4.4.2.2 (LOS)
- ✅ §4.3.5.5 (AIFF Availability) marked with Link 16 context note for future development
- ✅ File renamed: `section-C4-S3-tms-aa-review-2026-02-16.tex` → `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,744 bytes)
- ✅ Narrative completion: 25% → **~28.57%** (4 of 12 subsections complete: §4.3 intro, §4.3.5 intro, §4.3.5.1, §4.3.5.2)
- 🟡 Pending (suspended): §4.3.5.3 (Emergency Mode), §4.3.5.4 (Constraints), §4.3.5.5 (AIFF Availability) narrative
- 🟡 Pending (suspended): §4.3.1–§4.3.4 (SAM, STT, TWS, ACM), §4.3.6 (TGP A-A) narrative
- 🟡 Pending (suspended): Populate 6 hotastable tables (0/6 complete)
- ✅ Total commits: 558 → **582** (+24 commits since last update)

---

### Version Roadmap

| Version | Content | Bump Type | Status |
|---------|---------|-----------|--------|
| v0.4.0.0 | C2 HOTAS Fundamentals + C3↔C4 reorganization | MINOR | ✅ Released |
| v0.4.1.0 | Infrastructure improvements (hotastable v2.1, List of HOTAS Tables, cross-refs, PDF metadata) | PATCH | ✅ Released |
| v0.4.1.1 | Repetition cleanup — 9 editorial corrections across C2, C3, C5 | SUBPATCH | 🔄 **In Progress** (Issue #42, Milestone 6) |
| v0.5.0.0 | C4 TMS integration | MINOR | ⏸️ Suspended pending v0.4.1.1 |

---

## 5. NOTES

### Structural Decisions

**2026-02-13:** C4 WIP files updated. Main chapter file renamed to `chapter-C4-tms-structure-dev-2026-02-13.tex` (52,056 bytes). Section file `section-C4-S3-tms-aa-dev-2026-02-13.tex` (33,612 bytes) created, covering §4.3 — TMS in Air-to-Air. Structure validated: 6 subsections (§4.3.1 SAM, §4.3.2 STT, §4.3.3 TWS, §4.3.4 ACM, §4.3.5 IFF, §4.3.6 TGP A-A), labels consistent (`sec:C4-S3-S*`), cross-refs functional, 6 hotastable placeholders defined. Content state: structural outline with bullet points and technical accuracy, NOT narrative prose. Critical gap identified: current text uses itemized lists, not continuous narrative as required by C3/C5 style standard. Next phase: (1) transform to flowing prose, (2) fill tables with Dash-34 data, (3) validate all technical refs. File remains `dev` status. Total commits: 523.

**2026-02-15:** C4 WIP advancement continues. Section file `section-C4-S3-tms-aa-review-2026-02-15.tex` promoted to `review` status after §4.3 introduction finalization (39,095 bytes, +16.3% from 33,612 bytes). Introduction text validated for grammar accuracy, Dash-34 cross-references (§2.3.1.5.7-12), internal cross-references (→C2:§2.1.3, →C3:§3.1.1, →C3:§3.1.3), and prose cadence. Corrections applied: replaced "exclusively" with "restricted to" (para 2, precision), added "primary" qualifier to FCR mode description (para 3, clarity). **Critical dependency identified:** TGP (Targeting Pod) first mention should occur in C2 conceptual layer, not C4 operational layer. New WIP file created: `section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex` (20,493 bytes, status `final`). Establishes §2.1.3 (TGP as equipment-dependent SOI: AN/AAQ-33 Sniper XR ATP, AN/AAQ-14 LANTIRN), cross-references Dash-34 §2.6 and →C4:§4.3.6 (TGP A-A tracking). Dependency resolution ensures architectural consistency: C2 establishes concepts, C3/C4 provide operational details. §4.3 subsections (§4.3.1–§4.3.6: SAM, STT, TWS, ACM, IFF, TGP A-A) remain in draft status with bullet-point structure; 6 hotastable tables (0/6 complete) pending data population from Dash-34 §2.3.1.5.x, §2.5, §2.6.1.7.5, §4.3.2.4.3.12 and BMS Training Manual missions. Integration target: v0.5.0.0 (simultaneous integration of C2:§2.1.3 + C4:§4.3 introduction). Issues #38 (REVIEW) and #40 (APPROVED — integration checklist) updated with progress. Total commits: 558.

**2026-02-17:** C4 WIP advancement continues. Section file renamed to `section-C4-S3-tms-aa-review-2026-02-17.tex` (51,744 bytes). §4.3.5 (TMS and IFF Interrogation) introduction refined: "cockpit identification methods" substituted for "identification procedures" (precision improvement). §4.3.5.1 (SCAN Interrogation Mode) narrative completed: TMS Left short press (<0.6s) activation, SCAN configuration via DED INTG page and FCR CNTL OSB 10 (decouple/couple to radar scan volume), symbology identification (green circle = friendly, yellow square = bogey/unknown), tactical context (BVR intercepts, ROE compliance, multiple unknown contacts). Dash-34 cross-references validated: §2.2.4.4.2.1.1 (SCAN behavior), §2.3.1.5.1.6.2 (FCR CNTL OSB 10). **§4.3.5.2 (LOS Interrogation Mode) narrative completed:** concept (beam coverage area, cursor-directed, 2 beams vs SCAN), behavior (TMS Left ≥0.6s, 16 replies, beam geometry nuance, range filtering), configuration (DED INTG + DCS right SEQ→LOS page, independent from SCAN), symbology (cross-ref to §4.3.5.1, reduced redundancy), tactical context (BVR designated target; unsupported "VID passes" claim removed). Dash-34 cross-references validated: §2.2.4.4.2.1, §2.2.4.4.2.1.2, §2.2.4.4.2.2. §4.3.5.5 (AIFF Availability) marked with Link 16 context note for future development. Narrative completion: 25% → ~28.57% (4 subsections complete: §4.3 intro, §4.3.5 intro, §4.3.5.1, §4.3.5.2). Subsections §4.3.1–§4.3.4 (SAM, STT, TWS, ACM), §4.3.5.3–§4.3.5.5 (Emergency, Constraints, AIFF Availability), §4.3.6 (TGP A-A) remain in draft. 6 hotastable tables (0/6 complete) pending. Total commits: 582.

**2026-02-18:** Repetition audit session. First external contribution to the project: forum user Daddyk identified content repetitions in v0.4.1.0 via [BMS forum post #450980](https://forum.falcon-bms.com/post/450980). Systematic chapter-by-chapter analysis of the full guide (C1–C5) conducted. **10 repetitions catalogued** in `misc/notes-repetition-analysis-v0_4_1_1-20260218.md`: R-01 (C2: SOI definition duplicated in 2.1/2.1.1), R-02 (C2: master mode "determines" re-stated in 2.2.1), R-03 (C2/C3: DMS physical description repeated), R-04 (C2/C5: CMS boilerplate in 3 locations), R-05 (C3: NAV/A-G PRE DMS Down paragraphs literally identical), R-06 (C3: Snowplow/MARK/OFLY exception states described twice), R-07 (C3/C5: "Each table entry specifies" block repeated 4×; includes copy-paste error line 1359 "DMS hat" in CMS table), R-08 (C5: CMS Down joint consent stated twice consecutively), R-09 (C5: high-G rationale paraphrased in 5.2.4), R-10 (C5: IDIAS/CMS Left distinction — classified Aceitável, no action). Issue #42 opened and structured with prioritized checklist. Milestone 6 active. Forum reply posted. C4 WIP (Issues #38–#40) suspended; v0.4.1.1 takes priority. Total commits: 587.

---

**END OF PROJECT TRACKING v5.0.0**

{% endraw %}
