# Phase 3 Technical Plan — Falcon BMS TMS/DMS/CMS Guide

**Purpose:** Define the technical work plan for **Phase 3** of the Falcon BMS TMS/DMS/CMS HOTAS Usage Guide project, starting from guide version `v0.2.2.0` and focusing on content implementation (especially CMS tables) under the 0.x.x.x pre-publication regime.

---

## 1. Starting Point

### 1.1 Project Status at Phase 3 Start

- **Guide version:** `v0.2.2.0+20260108` (active)
- **Regime:** Pre-publication (`0.x.x.x`)
- **Phase:** 0 — Chapter scaffolding (in Version System terminology)
- **Chapters:**
  - Ch. 1 — Introduction: narrative complete.
  - Ch. 2 — HOTAS Fundamentals: scaffolded (structure WIP).
  - Ch. 3 — TMS: structure complete, content pending.
  - Ch. 4 — DMS: structure complete, content pending.
  - Ch. 5 — CMS: Section 5.1 integrated; 5.2 and 5.3 in WIP.
  - Ch. 6 — Training References: outline exists.
  - Ch. 7 — HOTAS Visual Reference: outline exists.

### 1.2 Governance Baseline

- **Version System:** `VERSION-SYSTEM v4.2` (English, Markdown and `.docx`).
- **WIP Naming:** `WIP-FILE-NAMING v1.3` (status codes and filename patterns).
- **Brief:** `BRIEFING v0.1.4.1` (scope, style, layout, structure).
- **Tracking:** `PROJECT-TRACKING v4.1.2` (to be updated as Phase 3 progresses).

Phase 3 assumes these documents are stable and used as the reference for all decisions.

---

## 2. Phase 3 Objectives

### 2.1 Primary Technical Goals

1. **Complete CMS Chapter Core Content**
   - Finalize narrative and tables for Chapter 5 (CMS), specifically Sections 5.2 and 5.3.
   - Integrate CMS WIP sections into the main guide.

2. **Prepare the Project for Table-Driven Phases**
   - Establish and validate patterns for `hotastable` usage via CMS tables.
   - Use CMS as the **template** for later TMS and DMS table development.

3. **Maintain Structural and Layout Integrity**
   - Ensure all new tables conform to the locked layout standard:
     - Geometry Option D.
     - `hotastable` width 15.6 cm.
     - `\small` + `\arraystretch = 1.25`.
   - Keep chapter structure and numbering aligned with `BRIEFING`.

### 2.2 Secondary Goals

- Refine references to Dash-34, Dash-1, and Training Manual in CMS sections.
- Strengthen notes on block/variant behavior for CMS.
- Improve internal cross-references (from CMS to TMS/DMS where relevant and justified).

---

## 3. Work Packages

### 3.1 WP1 — CMS 5.2: Actuation & HOTAS Tables

**Scope:** Complete Section 5.2, including its `hotastable` implementations.

- **Inputs:**
  - `section-C5-S2-cms-actuation-hotas-tables-review-2026-01-08.tex`
  - Dash-34 sections for CMDS and ECM behavior.
  - BRIEFING rules for column meanings.

- **Tasks:**
  1. Validate conceptual structure of 5.2 against Dash-34.
  2. For each relevant CMDS/ECM state, define table rows with:
     - State (AUTO, SEMI, MAN, BYPASS, ECM pod states).
     - Direction (Up, Down, Left, Right).
     - Action (Short, Long, etc.).
     - Function (short label, pilot-centric).
     - Effect / Nuance (1–3 sentences, technically precise).
     - Dash34 (section references via `\dashref{}` / `\dashrefs{}`).
     - Train (training mission references via `\trnref{}`).
  3. Ensure wording is consistent, neutral, and aligned with BRIEFING style.
  4. Mark any cells with incomplete information as **deliberate gaps**, not accidental omissions.

- **Deliverables:**
  - `section-C5-S2-...-final-YYYY-MM-DD.tex` (status `final`).
  - Integrated content in `guide-v0.2.x.x-YYYYMMDD.tex`.

### 3.2 WP2 — CMS 5.3: Block and Variant Notes

**Scope:** Provide a concise but technically accurate overview of CMS differences across main F-16 variants in BMS.

- **Inputs:**
  - `section-C5-S3-blocks-and-variants-review-2026-01-07.tex`.
  - Dash-34 and Dash-1 variant-specific notes.

- **Tasks:**
  1. Confirm which blocks/variants are explicitly supported by the CMS chapter (e.g., CM Block 50/52, MLU).
  2. Identify any **meaningful differences** in CMS behavior between variants:
     - Program availability.
     - ECM pod integration.
     - Default CMDS programs.
  3. Document differences briefly, focusing on what changes for the **pilot using CMS**.
  4. Avoid overwhelming detail; keep narrative to a few paragraphs plus focused notes.

- **Deliverables:**
  - `section-C5-S3-...-final-YYYY-MM-DD.tex` (status `final`).
  - Integrated Section 5.3 in the main guide.

### 3.3 WP3 — CMS Chapter Integration & Version Bumps

**Scope:** Integrate the final CMS WIP sections into the main guide and update version numbers.

- **Tasks:**
  1. Integrate Sections 5.2 and 5.3 into `guide-v0.2.x.x-YYYYMMDD.tex`.
  2. Evaluate whether the integration requires:
     - **PATCH increment** (structural changes within Chapter 5).
     - Or a **MINOR increment** if the work is deemed to complete a major step in Chapter 5 development.
     - Decision must follow `VERSION-SYSTEM v4.2`.
  3. Update:
     - `\docversion` and `\docbuild` in the LaTeX preamble.
     - The file name of the main guide (`guide-v0.a.b.c-YYYYMMDD.tex`).
     - `PROJECT-TRACKING` with the new version and description.
  4. Move integrated WIP files from `WIP/` to `ARCHIVE/` with status `approved`.

- **Deliverables:**
  - New active guide version (`v0.2.x.x` or `v0.3.0.0`, depending on decision).
  - Tracking entries and archived WIP files.

### 3.4 WP4 — Template Extraction for TMS and DMS Tables

**Scope:** Use the completed CMS tables as a **pattern** for TMS (Ch. 3) and DMS (Ch. 4).

- **Tasks:**
  1. Identify generic patterns in CMS tables that apply to all HOTAS tables:
     - Column wording and style.
     - Typical length and density of Effect / Nuance.
     - Referencing style for Dash-34 and training missions.
  2. Draft initial `table-C3-...` and `table-C4-...` WIP files that:
     - Use the same `hotastable` architecture.
     - Introduce TMS/DMS-specific states and functions.
  3. Keep these TMS/DMS table files in `dev` or `review` status until Phase 4.

- **Deliverables:**
  - A small set of `table-C3-*` and `table-C4-*` WIP files (status `dev/review`).
  - Notes in `PROJECT-TRACKING` describing pattern decisions.

---

## 4. Versioning Strategy for Phase 3

### 4.1 Expected Version Line

Phase 3 is likely to cover:

- **From:** `v0.2.2.0` (layout optimization)
- **To:** Somewhere between `v0.2.x.x` and `v0.3.0.0`, depending on:
  - How CMS integration is classified (PATCH vs MINOR).
  - Whether a new chapter beyond CMS is started during this phase.

### 4.2 Decision Rules (from Version System v4.2)

- **MINOR increment (0.a.0.0 → 0.b.0.0):**
  - When a **new chapter** enters the main guide, or
  - When a major structural milestone in a chapter is reached (editorial judgment).

- **PATCH increment (0.a.b.0 → 0.a.(b+1).0):**
  - Structural changes inside active chapters (new sections, major table reorganization).

- **SUBPATCH increment (0.a.b.c → 0.a.b.(c+1)):**
  - Typos, micro wording improvements, small table cell adjustments.

Phase 3 should explicitly document each version bump in `PROJECT-TRACKING` with:

- Affected chapters (primarily CMS).
- Brief description of changes.
- Rationale for choosing MINOR vs PATCH vs SUBPATCH.

---

## 5. Risks and Mitigations

### 5.1 Risk: Over-Detailed CMS Tables

- **Issue:** CMS tables may become excessively detailed, harming readability.
- **Mitigation:**
  - Limit Effect / Nuance to 1–3 short sentences.
  - Offload deeper tactical notes to footnotes or a later tactics-oriented appendix.

### 5.2 Risk: Drift from Dash-34 / Dash-1

- **Issue:** Paraphrased content might drift away from primary sources.
- **Mitigation:**
  - For each CMS behavior row, keep Dash-34 section references up to date.
  - Periodically cross-check against the latest BMS manuals.

### 5.3 Risk: Inconsistent Style Across Chapters

- **Issue:** CMS may diverge stylistically from future TMS/DMS tables.
- **Mitigation:**
  - Treat CMS tables as the **style reference** for TMS/DMS.
  - Use this plan and BRIEFING to enforce consistent wording and column usage.

---

## 6. Phase 3 Completion Criteria

Phase 3 can be considered complete when:

1. CMS Section 5.2 (Actuation & HOTAS tables) is fully implemented and integrated.
2. CMS Section 5.3 (Block / variant notes) is complete and integrated.
3. A new guide version reflecting CMS integration is active (e.g. `v0.2.x.x` or `v0.3.0.0`).
4. At least one small set of **pattern tables** for TMS and/or DMS exists in WIP as templates.
5. PROJECT-TRACKING and ARCHIVE folders are updated to reflect:
   - Integrated CMS WIP files (`approved`).
   - The new guide version and its description.

Once these criteria are met, the project can transition to the next phase (likely focused on TMS/DMS tables and broader table population across the guide).