# Falcon BMS 4.38.1 — TMS, DMS and CMS Usage Guide: Project Brief

**Brief Version:** v0.2.0.1 (WIP File Template Specification + New Preamble Documentation + Training Mission Reference Integration — 17 January 2026)

---

## Repository Identification

- GitHub repository name: `carlos-nader/tms-dms-cms-usage-guide`
- Primary URL: https://github.com/carlos-nader/tms-dms-cms-usage-guide/tree/main/docs
- Default branch: `main`
- Canonical guide file: `guide.tex` (repository root)
- Versioned snapshots: `WIP/GUIDE/guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex`

---

## 0. Context and Working Assumptions

This brief describes how the TMS/DMS/CMS Usage Guide is being built, including:

- Scope, goals and structure of the document.
- Source material and style rules.
- Layout parameters and table standards.
- High-level overview of the Version System v4.2.1 and how it interacts with GitHub.

All instructions to the assistant are given in **Portuguese**. All content that goes into the **LaTeX document** (text, tables, captions, macros) is in **English**.

The guide is currently in **pre-publication regime (0.x.x.x)** and under active development.

---

## 1. Scope and Goals

- The guide focuses only on three HOTAS switches: **TMS, DMS and CMS**.
- Other HOTAS controls (for example NWS/MSL STEP, MAN RNG/UNCAGE, etc.) may be mentioned only when strictly necessary to understand TMS/DMS/CMS behaviour.
- The document is not a full HOTAS or full avionics manual; it is a usage guide for these three switches, organised by context and supported by tables.
- The language of the document is English; style is clear, concise and manual-like, not chatty.

### 1.1 Main Goals

- Reorganise information that is spread across the BMS Dash-1, Dash-34 and the BMS Training Manual into context-based tables and short explanations.
- Make it easy for a virtual pilot to answer: "In this mode/sensor/weapon, what does each direction of TMS/DMS/CMS do?"
- Cross-reference each table line to:
  - The relevant Dash-34 (and sometimes Dash-1) section.
  - One or more BMS training missions where the behaviour can be practised.

---

## 2. Sources to Align With (But Never Limited To)

When generating or refining content, conceptually align with (but do not copy):

### 2.1 Falcon BMS Dash-34 (TO BMS 1F-16CMAM-34-1-1)

Especially, but never limited to:

- Hands-On Controls (HOTAS) section.
- SOI behaviour.
- Defensive avionics (ALE-47, ECM, CMS).
- Weapon-specific chapters (HARM, Maverick, IAMs, SPICE, Harpoon, etc.).

### 2.2 Falcon BMS Dash-1 (TO BMS 1F-16CMAM-1)

Where relevant (overall aircraft systems, master modes, etc.).

### 2.3 Falcon BMS Training Manual 4.38.1

Especially, but never limited to:

- Mission descriptions and learning objectives.
- Missions involving SEAD/EW, HARM, IAMs, LGBs, BARCAP, IFF, etc.

**Critical rule:** Never reproduce copyrighted text; always paraphrase in original words.

---

## 3. Document Structure (LaTeX Already Prepared)

Assume there is already a LaTeX template with this structure. Do not change the overall structure or helper macros unless explicitly requested, but suggestions may be made when technically justified. Always generate complete LaTeX files when ordered to generate one.

### 3.1 Chapter Breakdown

**1. Introduction**

- 1.1 Scope and purpose.
- 1.2 Version, authorship and AI assistance.
- 1.3 Sources and references.
- 1.4 Document structure and how to read it.

**2. HOTAS Fundamentals**

- 2.1 Sensor of Interest (SOI) and display logic.
- 2.2 Short vs long presses and timing.
- 2.3 Master modes and context-sensitive behaviour.
- 2.4 Overview of TMS, DMS and CMS.
- Table with: switch, location (stick/throttle), general role, detailed chapter.

**3. TMS — Target Management Switch**

- 3.1 Concept and general behaviour.
- 3.2 TMS and Situational Awareness displays (HSD, HSI, DED).
  - 3.2.1 HSD cursor control and waypoint management.
  - 3.2.2 Integration with NAV master mode.
  - 3.2.3 Cross-mode SA display interaction (A-A, A-G context).
- 3.3 TMS in Air-to-Air.
  - FCR CRM (RWS / ULS / VSR).
  - SAM / DT-SAM.
  - TWS.
  - STT.
  - ACM (30×20, 10×60, BORE, SLEW).
  - IFF interrogations (SCAN / LOS).
- 3.4 TMS in Air-to-Ground — sensors and SPI.
  - FCR A-G (GM / GMT / SEA / AGR).
  - TGP A-G.
  - HUD / HMCS (SPI, Snowplow, CZ, VIP/VRP cues).
  - Markpoints and steerpoint management.
- 3.5 TMS in A-G weapon employment.
  - Unguided bombs and rockets (CCIP / CCRP / DTOS).
  - EO weapons — Maverick (VIS / PRE / BORE).
  - IAMs (JDAM / JSOW / WCMD / SPICE / others).
  - LGBs and laser employment (single ship / buddy).
  - Anti-radiation (HARM POS / HAS / HAD).
  - Naval weapons (Harpoon, others).
- 3.6 TMS — Block / variant notes.

**4. DMS — Display Management Switch**

- 4.1 Concept and Sensor of Interest (SOI).
  - 4.1.1 SOI definition and scope across displays.
  - 4.1.2 Role of the DMS in SOI selection.
  - 4.1.3 Example SOI flow (overview).
- 4.2 DMS in MFDS format selection and SWAP.
  - 4.2.1 MFDS format selection and cycling.
  - 4.2.2 SWAP and display management.
  - 4.2.3 HSD control via SOI and MFDS functions.
- 4.3 DMS in sensor and weapon context.
  - 4.3.1 SOI changes between FCR, TGP, HSD and HUD in Air-to-Air.
  - 4.3.2 SOI changes between FCR, TGP, HSD, HAD and WPN in Air-to-Ground.
  - 4.3.3 DMS with HARM — HAD page as SOI.
  - 4.3.4 DMS with IAMs and other weapon-driven MFDS pages (SMS/WPN).
- 4.4 DMS — Block and variant notes.

**5. CMS — Countermeasures Management Switch**

- 5.1 Concept and interaction with CMDS / ECM.
  - 5.1.1 Concept.
  - 5.1.2 Interaction with CMDS / ECM.
- 5.2 CMS Switch Actuation — main table in subsections using `hotastable`.
  - 5.2.1 CMS Actuation with CMDS.
  - 5.2.2 CMS Actuation with ECM.
  - 5.2.3 CMS Consent & Constraints.
  - 5.2.4 Important Operational Notes.
- 5.3 CMS — Block and variant notes.

**6. Training References and Practical Flows**

- 6.1 How to use this guide with BMS training missions.
- 6.2 Recommended progression.
- 6.3 Example flows for typical missions.
- 6.4 Checklist: "what to practise next".
- Two-column table: Topic × Recommended training missions.
  - Example: "TMS A-A CRM" → TRN 18, TRN 17B.

**7. HOTAS Visual Reference**

- 7.1 F-16 HOTAS overview.
  - Single illustrative figure of stick + throttle, only labelling TMS, DMS and CMS positions (no other buttons).
- 7.2 TMS diagrams.
  - Close-ups of the TMS hat with arrows and short labels per direction, grouped by broad context (A-A radar, A-G sensors/SPI, SA displays).
- 7.3 DMS diagrams.
  - Close-ups of the DMS hat showing SOI / format control directions.
- 7.4 CMS diagrams.
  - Close-up of the CMS hat with arrows and short text per direction (up/left/right/aft) for CMDS/ECM interaction.

### 3.2 Appendices

- Block / variant overview (how behaviour is the same or slightly different across main BMS F-16 variants).
- Tables index (list of all major TMS/DMS/CMS tables and where to find them).

### 3.3 LaTeX Preamble (Architecture Overview)

The LaTeX preamble is a **locked, architecture-stable component** that includes:

- Document class (`report` with `twoside` for double-sided layout).
- Complete UTF-8 encoding stack with language support.
- Professional fonts (Latin Modern) and microtypography.
- Page geometry (A4, 2.0 cm left/right, 2.5 cm top/bottom margins).
- Advanced header/footer management for two-sided documents.
- Chapter and section formatting via `titlesec`.
- Custom table environment (`hotastable`) with 7-column HOTAS layout.
- Helper macros for cross-references, training missions, and document metadata.
- Graphics support with figure float control.

**Detailed preamble architecture is documented in Section 11.**

---

## 4. Layout Parameters (Updated January 17, 2026)

### 4.1 Geometry Configuration (Guide Standard)

- Page: A4 paper.
- Left margin: 2.0 cm.
- Right margin: 2.0 cm.
- Top margin: 2.5 cm.
- Bottom margin: 2.5 cm.
- Available text width: 17.0 cm.
- Standard HOTAS table width: 15.6 cm (sum of column widths).
- Horizontal safety margin: 1.4 cm between table and text width.
- Line spacing: 1.5× (via `\onehalfspacing`).

**Rationale:**

- 2.0 cm left/right margins are consistent with typical technical manual practice (including Falcon BMS Dash-1 and Dash-34 styling).
- Compared to the previous 2.5 cm margins, this layout:
  - Preserves a professional look while avoiding a cramped page.
  - Increases available width from 16.0 cm to 17.0 cm, providing more breathing room around the 15.6 cm-wide HOTAS table.
  - Reduces the risk of overfull boxes and awkward `longtable` breaks.
- 1.5× line spacing improves readability without excessive page bloat.

### 4.2 Table Formatting Standard (hotastable)

- Font size: `\small` (10 pt).
- Row height multiplier: `\arraystretch = 1.25`.

**Rationale:**

- `\arraystretch = 1.25` slightly reduces vertical spacing relative to 1.3, improving page economy while preserving legibility.
- This value is within recommended ranges for dense technical tables using `longtable`.
- The combination of `\small` + `\arraystretch = 1.25` is the project-wide standard for all TMS/DMS/CMS tables implemented via `hotastable`.

### 4.3 Scope of Application (Layout Standard)

- The geometry and `hotastable` parameters defined here apply to:
  - The **canonical guide file in the repository root**: `guide.tex`.
  - Any **standalone WIP section files** that define their own page geometry and HOTAS tables.
  - Any **versioned guide snapshots** under `WIP/GUIDE/` (see Section 10), which must remain byte-identical to `guide.tex` for a given version.
- Column widths for `hotastable` are considered architecture-locked by this brief:
  - `L{1.6cm}`, `L{1.0cm}`, `L{1.0cm}`, `L{3.4cm}`, `L{5.8cm}`, `L{1.4cm}`, `L{1.4cm}`.
- Future layout tuning for HOTAS tables should be done only through:
  - Global page geometry (margins).
  - `\arraystretch` (row height), within a safe readability range.

---

## 5. Style and Content Rules

### 5.1 General Style

- **Language:** English, neutral and technical, similar to a good community manual.
- **Length:**
  - Most sections: 2–4 short paragraphs.
  - Avoid long walls of text; use lists when they improve clarity.
- **Tone:**
  - Explanatory, not conversational; no chatty expressions.
- **Terminology:**
  - Always define an acronym on first use in the document (for example "Sensor of Interest (SOI)").
  - Use consistent naming: TMS, DMS, CMS, CMDS, ECM, IAM, TGP, FCR, etc.

### 5.2 Focus

Focus is always TMS, DMS and CMS.

- Mention other controls or panels only when strictly needed to understand what these three switches are doing (for example, CMDS panel mode, RF switch position, etc.).
- Do not drift into full tactics textbooks. A short tactical note is allowed in the "Effect / Nuance" column or in a brief sentence, but the primary purpose is to document what the hat does in each context.

### 5.3 Intro and "How to Read" Sections

The Introduction should clearly explain:

- The unofficial and community-made nature.
- Scope (TMS/DMS/CMS only).
- The role of tables and training-mission references.
- That the visual chapter is a quick reference, not the primary source of truth.

"Document structure and how to read it" should:

- Explain where the big tables are.
- Explain how to interpret the columns.
- Indicate where to look for training missions.
- Explain how to use the visual reference chapter together with the tables.

---

## 6. Column Filling Guidelines for hotastable (v0.1.3)

For every TMS/DMS/CMS table, use the following conventions.

### 6.1 Column 1: State (1.6 cm)

- Describe the condition or context where this action applies, combining master mode and the relevant sensor/weapon.
- Use a short, structured format, for example:
  - A-A CRM — FCR RWS.
  - A-A ACM — BORE.
  - A-G — FCR GM.
  - A-G — TGP.
  - A-G — HUD/HMCS SPI.
  - NAV — HSD.
  - IAM — PRE.
  - HARM — POS.
  - LGB — TGP.
- This column is the "address" of the behaviour; keep it concise.
- If the behaviour is the same in all submodes of a given master mode, it is acceptable to write, for example:
  - A-A CRM — any.
  - A-G — any FCR mode.

### 6.2 Column 2: Direction (1.0 cm)

- Use physical directions of the hat: Up, Down, Left, Right.
- If a behaviour is truly independent of direction (rare), write "Any" and explain in Effect / Nuance.
- Do not include timing here.

### 6.3 Column 3: Action (1.0 cm)

- Describe the type of press, usually:
  - Short — quick tap, up to about 0.5–0.6 s.
  - Long — press longer than about 0.5–0.6 s, when the simulator distinguishes short vs long.
- Variants:
  - Short, repeated — for cycling actions.
  - Long (hold) — for actions that only stay active while held.
- Timing hints may be added if important, for example: `Long (>0.5 s)`.
- Do not describe system behaviour here, only the nature of the press.

### 6.4 Column 4: Function (3.4 cm)

- Provide a short name for what the switch does in that context, for example:
  - Bug / designate target.
  - Drop track / RTS.
  - Set / update SPI.
  - Break track / CZ.
  - Cycle SOI between MFDs.
  - Give ECM consent.
  - Update waypoint.
- Think of this as the row's "title" — what a pilot might say informally.

### 6.5 Column 5: Effect / Nuance (5.8 cm)

- Brief explanation (1–3 short sentences) of what actually happens:
  - How radar/TGP/HUD state changes (lock type, SPI, SOI, etc.).
  - Interactions with other systems (CMDS AUTO/SEMI, ECM pod, IAM state, etc.).
  - Conditions or exceptions (for example "only with an existing track", "no effect if no target").
- Include nuances:
  - First press vs subsequent presses.
  - What happens when there is no valid target.
  - Very short tactical remarks if they help understanding the use.

### 6.6 Column 6: Dash34 (1.4 cm)

- Reference the most relevant sections in Dash-34 (or Dash-1 when needed).
- Use macros instead of prose, for example:
  - `\dashref{2.1.5}` for HOTAS hands-on controls.
  - `\dashref{2.7.1}` for CMS/ECM operation.
- Multiple sections can be comma-separated: `\dashref{2.1.5}, \dashref{2.7.1}`.
- Keep it short and purely referential.

### 6.7 Column 7: Train (1.4 cm)

Link behaviour to one or more BMS training missions. **All training mission references in this column must conform to the standardized abbreviations defined in Section 6.7.1 below.**

**Example references:**
- `\trnref{28 (SEAD-EW)}`.
- `\trnref{12 (HARM)}`.
- `\trnref{18 (BARCAP)}`.
- `\trnref{11 (LGB)}`.

If several missions cover the behaviour, list 2–3:
- `\trnref{18 (BARCAP)}, \trnref{17B (IFF Intercept)}`.

If there is no direct mission, either:
- leave the column blank, or
- reference the closest one and mention that in Effect / Nuance.

#### 6.7.1 Training Mission Abbreviations Standard

All training mission references in the Train column **must conform** to the standardized abbreviations defined in:

**Training Mission Reference Table v1.0** (`training-mission-abbrev-table-v1.0.md`)  
*Effective Date: 10 January 2026*

This document establishes the authoritative list of abbreviations for all 33 BMS 4.38.1 training missions, ensuring consistency and compliance with column width constraints (1.4 cm, `\small` font, `\arraystretch = 1.25`).

**Required Reference Format:**

```latex
\trnref{XX (ABBREVIATION)}
```

Where `XX` is the mission number (including variants A/B/C/D) and `ABBREVIATION` is taken directly from the Training Mission Reference Table v1.0.

**Examples:**
- `\trnref{1 (Ground Ops)}`
- `\trnref{4D (AAR)}`
- `\trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)}`

For detailed abbreviation rules, variant conventions, and multi-mission guidelines, refer directly to the Training Mission Reference Table v1.0.

---

## 7. Rules for the HOTAS Visual Reference Chapter

- All figures are illustrative, not official; style should be schematic, similar to technical drawings.

### 7.1 F-16 HOTAS Overview

- Show a generic stick + throttle layout.
- Only label TMS, DMS and CMS positions; do not label other buttons.
- Example caption: "F-16 HOTAS overview — TMS, DMS and CMS positions (illustrative, generic F-16CM Block 50/52 layout)."

### 7.2 TMS Diagrams

- Each diagram shows only the TMS hat, with arrows and very short labels per direction.
- Group diagrams by broad context, for example:
  - "TMS — Air-to-Air radar contexts".
  - "TMS — Air-to-Ground sensor/SPI contexts".
  - "TMS — Situational Awareness displays".
- The label for each direction must be consistent with the Function column in the corresponding tables.

### 7.3 DMS Diagrams

- Show the DMS hat with arrows and short labels, for example:
  - HUD/HMCS SOI.
  - Left/right MFD SOI/format cycling.
- Again, text must match the Function column in DMS tables.

### 7.4 CMS Diagrams

- Show the CMS hat with arrows and short labels, for example:
  - Up (manual programs).
  - Left (program 6).
  - Aft (ECM/CMDS consent).
  - Right (cancel AUTO, inhibit).
- Match labels with the CMS tables.

In all diagrams, keep text extremely short (a few words per arrow) and rely on the tables for detailed explanations.

---

## 8. Professional Standards for AI-Assisted Content Development

### 8.1 Communication Principles

When collaborating on this project, the following communication standards apply:

1. **Professional rigour**  
   All analysis, recommendations, and structural proposals must be grounded in primary sources and technical accuracy, not assumptions or simplifications.

2. **No condescension**  
   Treat the human author as the subject-matter expert and decision-maker. The AI's role is to provide deep analysis, identify sources of potential error (including its own), and present options with supporting evidence — not to guide or direct.

3. **Error identification**  
   When the human corrects an analysis, acknowledge the correction explicitly, explain the flawed reasoning, and reference which sources or logic should have been consulted. This documents learning and improves future responses.

4. **Primary source grounding**  
   All statements about TMS/DMS/CMS behaviour must be traceable to:
   - TO BMS 1F-16CMAM-34-1-1 (Dash-34).
   - TO BMS 1F-16CMAM-1 (Dash-1).
   - BMS Training Manual 4.38.1.
   - BMS User Manual 4.38.

   Avoid inference or generalisation from partial information.

5. **Structural integrity**  
   When proposing changes to chapter organisation or section placement, analyse against:
   - The actual use cases (NAV, A-A, A-G, DGFT).
   - Which master modes rely on which switches.
   - Where functionality overlaps vs where it is exclusive.
   - The learning progression for virtual pilots.
   - Whether a display/feature is primary to that context or incidental.

6. **Explicit scope boundaries**  
   Clearly distinguish between:
   - What applies to all blocks/variants vs specific ones.
   - What is primary TMS/DMS/CMS function vs incidental.
   - What is in scope (these three switches) vs out of scope (other HOTAS controls).

### 8.2 Application Examples

**Session 1 — HSD section placement**

- Initial error: proposed HSD section placement as 4.4 (after A-G SPI, before weapons), framing it as an A-G planning tool.
- Correction: HSD is a transversal NAV/PLANNING tool used across all master modes, with primary relevance in NAV, not as an A-G-specific feature.
- Flawed reasoning: confused "tool used during A-G missions" with "A-G-specific tool"; failed to distinguish between primary context (NAV) and incidental context (A-G backup/reference).
- Implication: section should appear early in Chapter 3 (after Concept), positioned as a transversal display that spans master modes, not in the A-G subsection.
- Learning: context of display use (master mode → then sensor → then purpose) should be the primary organising principle, not mission phase or tactical application.

**Session 4 — DMS structure decision**

- Problem identified: DMS structure was ambiguous (three candidate organisations: A, B, C).
- Resolution methodology: used Dash-34 (sections 2.1.5, 2.1.6.2–2.1.6.3, 2.1.7.5.4) as the authoritative arbiter.
- Technical validation: confirmed that DMS is a transversal SOI/MFDS manager, not a sensor-specific or mode-specific switch.
- Decision: adopted Option B ("Transversal SOI architecture") with Dash-34 terminology.
- Result structure:
  - 4.1 Concept and Sensor of Interest (SOI).
  - 4.2 DMS in MFDS format selection and SWAP.
  - 4.3 DMS in sensor and weapon context.
  - 4.4 DMS — Block and variant notes.
- Enforcement: two critical focus points: DMS does not perform tactical functions; NAV/A-A/A-G are contexts, not three different DMS implementations.

---

## 9. How to Work With This Brief

- The human author will issue instructions in Portuguese, for example:
  - "Preencha a seção 'CMS — Concept and interaction with CMDS / ECM' no LaTeX."
  - "Crie a tabela de ações do CMS para os modos AUTO/SEMI/MAN dentro do hotastable."
- The assistant should:
  - Generate or modify LaTeX snippets that fit cleanly into the existing template.
  - Keep sections, labels and references consistent with this brief.
  - Use the helper macros and the `hotastable` environment as defined.
  - Provide rigorous analysis grounded in primary sources.
- The assistant may suggest structural improvements grounded in technical analysis and primary sources, but should not apply them unless explicitly approved.

When in doubt, ask concise clarification and wait for the answer before making large refactors.

---

## 10. Version Control System (VERSION_SYSTEM_v4.2.1 — Overview)

This section provides a high-level overview of the versioning model used for the TMS/DMS/CMS guide. The authoritative rules are defined in the standalone document "Falcon BMS TMS/DMS/CMS Guide Version System v4.2.1". In case of any discrepancy between this brief and that document, Version System v4.2.1 is the single source of truth.

### 10.1 Purpose and Scope

- Ensure that the guide, its LaTeX sources and tracking documents use a consistent versioning scheme.
- Provide a quick reference so that AI-assisted and human edits do not invent ad-hoc version numbers.
- Clarify how the version macros in the LaTeX preamble relate to file names, snapshots, and to the project tracking document.

### 10.2 Repository Structure for the Guide

To integrate versioning with GitHub and keep diffs readable, the project uses two levels for the main guide source:

- **Canonical file in the repository root:**
  - `guide.tex`.
  - This is the file Git and GitHub track as the main history of the document.
  - It always contains the latest accepted version of the guide.

- **Versioned snapshots in `WIP/GUIDE/`:**
  - For each version, there is a snapshot named:

    ```text
    WIP/GUIDE/guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex
    ```

  - The snapshot for the active version must be byte-identical to `guide.tex`.
  - Older snapshots are kept for safety and traceability.

### 10.3 LaTeX Version Macros

The LaTeX preamble of the guide (both in `guide.tex` and in its snapshot under `WIP/GUIDE/`) must contain, at minimum:

- `\newcommand{\docversion}{...}`.
- `\newcommand{\docbuild}{YYYYMMDD}`.
- `\newcommand{\fulldocversion}{\docversion+\docbuild}`.

These fields must always match:

- The version encoded in the **snapshot file name** under `WIP/GUIDE/`.
- The entry for that version in the **PROJECT-TRACKING** document.

### 10.4 Two Regimes: Pre-publication (0.x.x.x) and Post-publication (≥ 1.0)

Version System v4.2.1 defines two distinct regimes:

- **Pre-publication regime (0.x.x.x):**
  - Used while the guide is still being built and no public edition has been declared.
  - `MAJOR = 0` always.
  - `MINOR` roughly tracks the order in which chapters are integrated into the guide.
  - `PATCH` marks structural changes within those chapters (new sections, reorganisation, major table changes).
  - `SUBPATCH` records small refinements (typos, wording, small table cell adjustments) that do not change the overall architecture.

- **Post-publication regime (≥ 1.0, x.y.z):**
  - Used after the first public edition (`1.0.0`) of the guide is declared.
  - `MAJOR` = edition number of the guide (1st, 2nd, 3rd...).
  - `MINOR` = significant but compatible revisions within the same edition.
  - `PATCH` = local corrections and polish (errata, clarity, minor table fixes).

The exact decision tables for when to increment each digit are defined in Version System v4.2.1 and should not be reimplemented here.

### 10.5 Quick Operational Rules

The following rules are intended as a working checklist; always refer to Version System v4.2.1 for the full logic and examples.

- Only content integrated into the guide snapshot in `WIP/GUIDE/` and propagated to `guide.tex` can change its version.
  - Work done only in WIP files (`section-`, `table-`, `visual-`, `notes-`) does not affect the guide version until it is integrated into the snapshot and copied over `guide.tex`.
- Pre-publication (0.x.x.x):
  - New chapter structure integrated into the guide → typically a MINOR increment.
  - Structural changes inside existing chapters (new sections, major table reorganisation) → typically a PATCH increment.
  - Typos, wording and small formatting fixes → typically a SUBPATCH increment.
- Post-publication (≥ 1.0):
  - Widening scope or large reorganisations that feel like a new edition → MAJOR increment.
  - Substantial expansions within the same edition (new chapter, large content additions) → MINOR increment.
  - Local corrections, improved clarity, small table fixes → PATCH increment.
- Build date (`\docbuild` and `YYYYMMDD` in the snapshot file name) is updated every time a new version number is established.

### 10.6 Synchronisation Between Files

To avoid divergence between different artefacts, the following three elements must always be synchronised whenever a new guide version is created:

1. **LaTeX macros** in the guide preamble (snapshot and `guide.tex`):
   - `\docversion` and `\docbuild` must reflect the new version and build date.
2. **Snapshot file name** in `WIP/GUIDE/`:
   - Must match the version and date, for example `WIP/GUIDE/guide-v0.2.2.0-20260108.tex`.
3. **PROJECT-TRACKING entry**:
   - Must record the same version number, date, affected chapters/sections, and a concise description of the changes.

Git and GitHub always see `guide.tex` as the canonical file. The snapshot in `WIP/GUIDE/` is the working copy that is edited; when ready, it is copied over `guide.tex` so that the Git history shows the evolution of a single, stable file.

---

## 11. WIP File Template and LaTeX Preamble Architecture

### 11.1 Purpose and Location

All work-in-progress files (chapters, sections, tables, visuals) **MUST** be created by copying and adapting the canonical template:

```text
TEMPLATES/template-wip-V1.0.tex
```

This requirement ensures that:

- All WIP files inherit a **standardised, validated preamble** identical to the main guide structure.
- **Metadata blocks** follow a consistent, machine-readable format.
- **Content structures** (sections, subsections, tables) align with the brief's expectations.
- **Integration into guide.tex** can be automated or semi-automated without structural surprises.

Template use is **mandatory** for AI-assisted WIP file creation and **strongly recommended** for human-authored WIP files.

### 11.2 What the Template Provides

The template is a complete, compilable LaTeX document containing:

1. **Standard preamble** (packages, geometry, macros):
   - Identical to `guide.tex` preamble to ensure WIP files and guide are always synchronised.
   - Includes all necessary packages, organised by functional category (encoding, fonts, geometry, colors, headers/footers, chapter formatting, tables, graphics).
   - Geometry locked: A4, 2.0 cm left/right margins, 2.5 cm top/bottom, 1.5× line spacing.
   - Custom helpers: `\dashref{}`, `\dashone{}`, `\trnref{}`, `\trnman`, `\bmsver`, `\dashrefs{}`.
   - Professional header/footer configuration for two-sided layout.
   - Chapter and section formatting via `titlesec` for consistent styling.
   - Figure and table support with float positioning control.

2. **Metadata block** (non-rendered, for tracking):
   - Structured comments at lines following `\begin{document}` (approximately lines 52–75).
   - Contains: target chapter/section, WIP file status, creation date, author/AI indication, development notes, cross-references.
   - Metadata is **never rendered** in compiled output; used only for human/automation reference.

3. **Section/subsection skeleton**:
   - Empty sections and subsections with proper hierarchy (`\section{}`, `\subsection{}`, `\subsubsection{}`).
   - Ready to be filled with narrative content, tables, or both.
   - Structured to match the chapter breakdown defined in this brief (Section 3.1).

4. **Configured hotastable environment**:
   - Pre-configured 7-column layout with locked dimensions.
   - Column widths: 1.6 cm, 1.0 cm, 1.0 cm, 3.4 cm, 5.8 cm, 1.4 cm, 1.4 cm (State, Direction, Action, Function, Effect/Nuance, Dash34, Train).
   - Font size: `\small` (10 pt).
   - Row height: `\arraystretch = 1.25`.
   - Template includes one **empty example row** (commented out) for quick reference during table population.

### 11.3 Preamble Configuration (Locked Architecture)

The preamble is considered **architecture-locked** and should not be modified except in extraordinary circumstances (requires explicit approval in this brief or by human override).

#### 11.3.1 Document Class and Two-Sided Layout

**Specification:**

```latex
\documentclass[11pt, a4paper, twoside]{report}
```

**Migration rationale (article → report):**

- `article` class is suitable for short, single-topic documents; it lacks built-in chapter support and features for longer technical manuals.
- `report` class provides `\chapter{}` command, enabling hierarchical document structure (chapters → sections → subsections).
- `twoside` option activates mirrored margins and header/footer logic for double-sided printing, improving professional appearance and enabling distinct left/right page headers.

**When to use `report`:**
- Document has 5+ logical chapters or sections.
- Document uses `\chapter{}` command.
- Double-sided printing or presentation is expected.
- Page count exceeds 30–40 pages.

**Impact on LaTeX structure:**
- `\chapter{}` becomes the top-level sectioning command (previously `\section{}`).
- `\section{}` becomes level 2, `\subsection{}` becomes level 3, etc.
- Headers and footers can distinguish between odd and even pages (via `[LO,RE]`, `[RO,LE]` positioning).

#### 11.3.2 Encoding, Fonts, and Language

**Specification:**

```latex
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{lmodern}
\usepackage{microtype}
```

**Rationale:**

- `inputenc[utf8]`: Allows direct input of UTF-8 encoded characters (é, ñ, ü, etc.) without explicit LaTeX commands.
- `fontenc[T1]`: Ensures proper font encoding for output (improves hyphenation, ligatures, and special character support).
- `babel[english]`: Activates English language rules (hyphenation, spacing, typographic conventions).
- `lmodern`: Replaces default Computer Modern fonts with Latin Modern — a high-quality serif family optimized for on-screen and print rendering.
- `microtype`: Enables advanced microtypographic features (character protruding, font expansion, font shrinking) for improved typography and reduced hyphenation.

**Impact:**
- Document is more readable on screen and in print.
- Hyphenation and line breaking follow English conventions.
- Special characters (accents, diacritics) are rendered correctly.

#### 11.3.3 Page Geometry and Spacing

**Specification:**

```latex
\usepackage{geometry}
\geometry{a4paper, left=2.0cm, right=2.0cm, top=2.5cm, bottom=2.5cm}
\usepackage{setspace}
\onehalfspacing
```

**Rationale:**

- `geometry` package provides absolute control over page margins (preferable to default LaTeX mechanisms).
- 2.0 cm left/right margins: consistent with technical manual standards; reduces text width to 17.0 cm (ample for 15.6 cm HOTAS tables).
- 2.5 cm top/bottom margins: accommodates headers, footers, and page numbering without cramping.
- `\onehalfspacing`: increases line spacing to 1.5×, improving readability without excessive page bloat; important for dense technical tables.

**Impact:**
- Professional appearance consistent with Falcon BMS official documentation.
- Sufficient whitespace around HOTAS tables for legibility.
- Better readability for extended document consumption.

#### 11.3.4 Colors and Hyperlinks

**Specification:**

```latex
\usepackage[table]{xcolor}
\definecolor{linkblue}{HTML}{004488}
\definecolor{linkred}{HTML}{882222}
\definecolor{headerblue}{HTML}{003366}
\definecolor{rowgray}{HTML}{F5F5F5}
\definecolor{subheadgray}{HTML}{E0E0E0}

\usepackage[pdfencoding=auto, psdextra, colorlinks=true, linkcolor=linkblue, citecolor=linkred, urlcolor=linkblue, breaklinks=true]{hyperref}
\usepackage{bookmark}
```

**Rationale:**

- `xcolor[table]`: Enables `\rowcolor{}` for table row coloring (used in `hotastable` headers).
- Custom colors: professional palette (dark blue for headers, lighter grays for row alternation, consistent link colors).
- `hyperref`: Creates clickable table of contents, cross-references, and URLs in PDF output. `colorlinks=true` colors links instead of boxing them.
- `breaklinks=true`: Allows links to wrap across lines (improves page layout).
- `bookmark`: Enhanced PDF bookmarks for PDF readers; improves navigation.

**Impact:**
- Professional table appearance with colored headers.
- Clickable PDF navigation (TOC, cross-references).
- Improved user experience in PDF viewers.

#### 11.3.5 Headers and Footers (Two-Sided Layout)

**Specification:**

```latex
\usepackage{fancyhdr}
\setlength{\headheight}{25pt}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LO,RE]{\small\textit{\leftmark}}     % Outer edge (odd left, even right): chapter name
\fancyhead[RO,LE]{\small\thepage}               % Inner edge (odd right, even left): page number
\fancyfoot{}                                      % No footer
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}
```

**Rationale (Two-Sided Layout):**

- `\headheight=25pt`: Accommodates longer chapter names without "Overfull \vbox" warnings.
- `[LO,RE]`: **Outer edges** (Left on Odd pages, Right on Even pages) — chapter name appears on the outside margin for easy navigation during page flipping.
- `[RO,LE]`: **Inner edges** (Right on Odd pages, Left on Even pages) — page number appears on the inside margin for visual symmetry.
- `\leftmark`: Expands to current chapter name (set automatically by `\chapter{}` command).
- `\thepage`: Current page number.
- No footers: all information in headers (cleaner layout).
- `\headrulewidth=0.4pt`: Subtle line separating header from content.

**Impact:**
- Professional two-sided document appearance.
- Clear navigation (chapter names and page numbers visible on all pages).
- Proper PDF navigation when printed or viewed double-sided.

#### 11.3.6 Chapter and Section Formatting (titlesec)

**Specification:**

```latex
\usepackage{titlesec}

\titleformat{\chapter}[display]
  {\normalfont\Large\bfseries}
  {\chaptertitlename~\thechapter}
  {20pt}
  {\Large}

\titlespacing{\chapter}
  {0pt}
  {10pt}      % Space BEFORE chapter title
  {20pt}      % Space AFTER chapter title
  [0pt]

\titlespacing{\section}
  {0pt}
  {15pt}
  {10pt}
  [0pt]
```

**Rationale:**

- `titlesec` provides fine-grained control over section formatting (alternative to default LaTeX which is hard-coded).
- **Chapter format (`[display]`)**: places chapter number and title on separate lines, enabling large, visually prominent chapter headings.
- **Chapter spacing**: `10pt` before (compact) and `20pt` after (breathing room) chapters for clear visual separation.
- **Section spacing**: `15pt` before and `10pt` after sections for consistent hierarchy.
- Reduced spacing compared to defaults (which can be 50pt before chapters) saves page real estate while maintaining readability.

**Impact:**
- Professional section hierarchy (chapters visually distinct from sections).
- Optimized page economy (less wasted whitespace).
- Consistent, predictable spacing across document.

#### 11.3.7 Tables and Column Types

**Specification:**

```latex
\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage{tabularx}

\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}
```

**Rationale:**

- `booktabs`: Professional table styling (optimal line weights, spacing); recommended for publication-quality tables.
- `array`: Advanced column formatting options.
- `longtable`: Tables that span multiple pages (essential for multi-page HOTAS tables).
- `tabularx`: Tables that automatically resize to fit available width (used for future table variants).
- Custom columns `L`, `C`, `R` with fixed widths: enable precise alignment (left, center, right) within fixed-width cells (essential for hotastable 7-column layout).

**Impact:**
- Professional table appearance.
- Multi-page table support (HOTAS tables can extend across page breaks).
- Precise column width control (15.6 cm total for `hotastable`).

#### 11.3.8 Graphics and Float Positioning

**Specification:**

```latex
\usepackage{graphicx}
\graphicspath{{fig/}}
\usepackage{float}
```

**Rationale:**

- `graphicx`: Enables `\includegraphics{}` command for inserting images.
- `\graphicspath{{fig/}}`: Tells LaTeX to search the `fig/` subfolder for image files (relative path).
- `float`: Provides `[H]` float placement option, which forces figures/tables to appear **exactly** where defined in code (no floating). Essential for controlling figure placement in technical manuals.

**Impact:**
- Support for diagrams, screenshots, and reference images.
- Predictable figure placement (no automatic repositioning by LaTeX).

#### 11.3.9 HOTAS Table Environment (hotastable)

**Specification (CORRECT, per 17 January 2026 preamble):**

```latex
\newenvironment{hotastable}[1]{%
  \small
  \renewcommand{\arraystretch}{1.25}
  \begin{longtable}{L{1.6cm} L{1.0cm} L{1.0cm} L{3.4cm} L{5.8cm} L{1.4cm} L{1.4cm}}
  \caption{#1}\\
  \rowcolor{headerblue}
  \textbf{\color{white}State} &
  \textbf{\color{white}Dir} &
  \textbf{\color{white}Act} &
  \textbf{\color{white}Function} &
  \textbf{\color{white}Effect / Nuance} &
  \textbf{\color{white}Dash34} &
  \textbf{\color{white}Train} \\
  \endfirsthead
  \rowcolor{headerblue}
  \textbf{\color{white}State} &
  \textbf{\color{white}Dir} &
  \textbf{\color{white}Act} &
  \textbf{\color{white}Function} &
  \textbf{\color{white}Effect / Nuance} &
  \textbf{\color{white}Dash34} &
  \textbf{\color{white}Train} \\
  \endhead
  \multicolumn{7}{r}{\small\emph{Continued on next page}}\\
  \endfoot
  \endlastfoot
}{%
  \end{longtable}
}
```

**Rationale:**

- `\small` + `\arraystretch=1.25`: Optimized font size and row height for dense technical tables.
- **7-column fixed widths**: `L{1.6cm}` (State), `L{1.0cm}` (Dir), `L{1.0cm}` (Act), `L{3.4cm}` (Function), `L{5.8cm}` (Effect/Nuance), `L{1.4cm}` (Dash34), `L{1.4cm}` (Train).
  - Total: 15.6 cm (fits within 17.0 cm text width with 1.4 cm safety margin).
- **Header order (CRITICAL):**
  - `\caption{#1}\\` placed FIRST (inside `longtable`, per official `longtable` documentation).
  - First-page header content, then `\endfirsthead` (marks END of first-page header).
  - Subsequent-pages header (identical), then `\endhead` (marks END of subsequent-pages header).
  - Footer material (`\multicolumn`, `\endfoot`, `\endlastfoot`) follows.
  - **This order ensures correct table numbering across page breaks.**
- `\rowcolor{headerblue}`: Dark blue header background for visual distinction.
- `\color{white}`: White text on blue background for contrast.
- `\endfirsthead` / `\endhead`: Distinguish first-page header from subsequent-page headers (allows different content if needed, though identical here).
- `\endfoot` / `\endlastfoot`: Footer displays "Continued on next page" for multi-page tables.

**Column semantics (locked):**

| Column | Width | Name | Content |
|--------|-------|------|---------|
| 1 | 1.6 cm | State | Master mode + sensor context |
| 2 | 1.0 cm | Dir | Hat direction (Up/Down/Left/Right) |
| 3 | 1.0 cm | Act | Press type (Short/Long/etc.) |
| 4 | 3.4 cm | Function | What the switch does (informal title) |
| 5 | 5.8 cm | Effect / Nuance | Technical explanation + interactions |
| 6 | 1.4 cm | Dash34 | Reference to Dash-34 sections |
| 7 | 1.4 cm | Train | Training mission references |

#### 11.3.10 Reference Macros

**Specification:**

```latex
\providecommand{\dashref}[1]{Dash-34~\S~#1}
\providecommand{\dashone}[1]{Dash-1~\S~#1}
\providecommand{\trnref}[1]{TRN~#1}
\providecommand{\trnman}{BMS Training Manual 4.38.1}
\providecommand{\bmsver}{Falcon BMS~4.38.1}
\providecommand{\dashrefs}[1]{\textit{TO 1F-16CMAM-34-1-1}, Dash-34, sections \texttt{#1}}
```

**Rationale:**

- `\providecommand` vs `\newcommand`: `\providecommand` does not override if macro already exists; allows `guide.tex` to redefine with enhanced formatting while WIP files work standalone.
- `\dashref{2.1.5}`: Expands to "Dash-34 § 2.1.5" (compact reference format for table cells).
- `\dashone{1.2.3}`: Expands to "Dash-1 § 1.2.3" (for rare Dash-1 references).
- `\trnref{18 (BARCAP)}`: Expands to "TRN 18 (BARCAP)" (training mission reference).
- `\trnman`: Reusable expansion "BMS Training Manual 4.38.1".
- `\bmsver`: Reusable expansion "Falcon BMS 4.38.1".
- `\dashrefs{2.1.5, 2.1.6}`: Expands to full reference with section numbers, for use in prose (vs table cells).

**Impact:**
- Consistency across document.
- Easy to update reference format globally (e.g., change "§" to "section").
- Shorter, more readable source code.

#### 11.3.11 Version Control Macros

**Specification:**

```latex
\newcommand{\docversion}{0.3.0.1}
\newcommand{\docbuild}{20260117}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{17 January 2026}
\newcommand{\chapterscompletedof}{3/7}
\newcommand{\tablesfilledpct}{Chapter 5 and Chapter 4 - 4.2}
\newcommand{\fulldocversion}{\docversion+\docbuild}
```

**Rationale:**

- `\docversion`: Version number (follows Version System v4.2.1).
- `\docbuild`: Build date (YYYYMMDD format for machine readability).
- `\docstartdate` / `\docenddate`: Development timeline.
- `\chapterscompletedof`: Progress tracking (e.g., "3/7" chapters integrated).
- `\tablesfilledpct`: Percentage of tables populated.
- `\fulldocversion`: Combines version and build date for title page or headers.

**Impact:**
- Single source of truth for version metadata.
- Automatic title page updates.
- Easy tracking of development progress.

### 11.4 Metadata Block Format

The metadata block is a **commented-out section** at the top of the document body (after `\begin{document}`), structured as follows:

```latex
\begin{document}

% ============================================================================
% METADATA BLOCK (non-rendered, for tracking and automation)
% ============================================================================
% Target: Chapter C, Section S, Subsection S
% Status: dev
% Date: YYYY-MM-DD
% Author: AI / Human Name
% Notes: TBD: Table population. Known issues: None.
% Cross-ref: Guide v0.2.2.0, guides-section-C-S-*.tex
% ============================================================================

\section{Section Title}

Content starts here...
```

**Mandatory fields:**

| Field | Format | Example | Notes |
|-------|--------|---------|-------|
| Target | `Chapter C[, Section S[, Subsection S]]` | `Chapter 5, Section 2, Subsection 1` | Identifies where in guide structure this WIP belongs. |
| Status | `dev \| review \| final \| approved` | `dev` | Status per WIP-NAMING-v1.4. Approved files should be in ARCHIVE/. |
| Date | `YYYY-MM-DD` | `2026-01-09` | Creation or last-edit date. Updated whenever status changes. |
| Author | `AI` or `Human Name` | `AI (Session 9)` | Indicates authorship for traceability. |

**Optional fields (but recommended):**

| Field | Purpose | Example |
|-------|---------|---------| 
| Notes | Development notes, TBD items, known issues | `TBD: Populate rows 5–12. Known issue: CMS ECM column needs Dash-34 validation.` |
| Cross-ref | Links to related WIP files, guide versions, or source sections | `See also: section-C5-S2-*.tex. Reference: Dash-34 §2.1.7.` |

**Rationale:**
- Metadata stays in the file, making it self-documenting.
- Non-rendered comments prevent cluttering compiled output.
- Format is simple enough for regex/automation to parse, but human-readable for manual inspection.

### 11.5 Integration Workflow: What Happens When Integrated into guide.tex

When a WIP file (for example, `section-C5-S2-cms-actuation-final-2026-01-09.tex`) is promoted to `final` status and ready for integration into `guide.tex`, the following **extraction and integration procedure** is applied:

**Step 1: Extract Content from WIP**
- Delete preamble (`\documentclass` through `\begin{document}`).
- Delete metadata block (commented-out lines after `\begin{document}`).
- Preserve: all `\section`, `\subsection`, narrative, tables, and remove `\end{document}`.

**Step 2: Merge into guide.tex**
- Identify target location in `guide.tex` (for example, after Section 5.1, before Section 5.3).
- Insert extracted content (sections through tables).
- Merge any helper macros (`\dashref{}`, etc.) into guide.tex's definition set; WIP's `\providecommand` placeholders are **overridden** by guide.tex's `\newcommand` definitions.

**Step 3: Archive and Record**
- Move WIP file from `WIP/` to `ARCHIVE/section-C5-S2-cms-actuation-approved-2026-01-XX.tex`.
- Update metadata block status to `approved`.
- Record integration in PROJECT-TRACKING.
- Update `guide-v*.tex` version and build date.

**Why this workflow works:**
- Standalone compilation: WIP files are always compilable (thanks to preamble).
- Integration hygiene: preamble is never carried over; only content is merged.
- Macro safety: `\providecommand` in WIP allows override by guide.tex without conflicts.

### 11.6 Template Versioning and Maintenance

The template itself is **versioned independently** of the guide version, allowing template improvements without changing guide version numbers.

- **Current template version:** `template-wip-V1.0.tex` (locked as of 17 January 2026).
- **Template updates:** When packages, preamble, or structure change, increment to `template-wip-V2.0.tex`, etc.
- **Guidance for WIP creators:** Always use the latest template version unless explicitly directed to use an older one.

---

## 12. Professional Standards for AI-Assisted Content Development

### 12.1 Communication Principles (SAME AS SECTION 8)

[Section 8 content repeated for convenience in final sections]

---

## 13. How to Work With This Brief (SAME AS SECTION 9)

[Section 9 content repeated for convenience in final sections]

---

## CHANGE SUMMARY:

**Date:** 17 January 2026, 23h45 -03

### Major Updates:

1. **Section 11 — Complete Redesign:**
   - Reorganized from single-section format to hierarchical subsections (11.1–11.6).
   - Added 11.3 with detailed preamble documentation (11.3.1–11.3.11):
     - Document class migration (article → report).
     - Two-sided layout configuration.
     - Encoding and fonts.
     - Page geometry and spacing.
     - Colors and hyperlinks.
     - Headers and footers for two-sided documents.
     - Chapter and section formatting (titlesec).
     - Tables and column types.
     - Graphics and float positioning.
     - hotastable environment (CORRECTED CODE).
     - Reference macros.
     - Version control macros.

2. **Section 4 — Updated:**
   - Added line spacing (1.5×) to layout parameters.

3. **New preamble code:**
   - Complete preamble listing from 17 January 2026 version (`guidetest.tex`).
   - Includes all new packages and configurations.
   - Corrected `hotastable` environment with proper `longtable` header ordering.

### Rationale:

- Previous brief (v0.2.0.1) documented preamble only at high level; new developers could not replicate preamble exactly.
- New preamble significantly enhanced (report class, twoside, titlesec, improved headers/footers, float positioning).
- Detailed subsections enable precise preamble reproduction and maintenance.
- Corrected hotastable code resolves table numbering issues.

---

**Brief Version:** v0.2.0.1  
**Status:** Ready for use  
**Next Steps:** Integrate into project repository and update all cross-references in WIP-NAMING and VERSION-SYSTEM documents.
