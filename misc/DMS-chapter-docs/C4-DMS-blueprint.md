# Falcon BMS TMS/DMS/CMS Guide — Chapter 4 (DMS) Unified Blueprint v1.1
## CORRECTED & REORGANIZED

**Date:** 15 January 2026, ~02:06 -03  
**Status:** Unified, updated blueprint (supersedes `Chapter-4-DMS-Complete-Blueprint.md` and `blueprint-C4-incremental.md`)  
**Version:** 1.1 (CORRECTED 2026-01-16)  
**Based on:** Dash-34 (§2.1.1.2.3, §2.1.5, §2.1.6, §2.1.7.5.x, §2.5.6.x), C4‑S1 final, C4‑S2 DMS Up final, deprecated C4‑S2 (Up/Down), deprecated C4‑S3 (format cycling)

---

## 0. Purpose of This Blueprint

This document is the **single, authoritative blueprint** for **Chapter 4 (DMS)** of the Falcon BMS TMS/DMS/CMS Usage Guide. It:

1. Defines the **final structure** of Chapter 4 (sections and subsections).  
2. Documents the **current implementation status** of each section (final / review / TODO).  
3. Consolidates content decisions from the previous **full blueprint** and the **incremental blueprint**, removing contradictions.  
4. Guides all future work on DMS (including new WIP files and integration into `guide.tex`).

This blueprint is written so that a future AI session can join the project mid‑stream and immediately know:

- What Chapter 4 must contain.  
- What already exists in final/review WIP files.  
- What remains to be written or refactored.

---

## 1. Final Chapter 4 Structure — Complete Hierarchy

### 1.1 Chapter 4 Organization Overview

Chapter 4 is organized in **two main subsections** (4.1 and 4.2), followed by five **direction-based sections** (4.2 through 4.5):

```
4 DMS — Display Management Switch
│
├── 4.1 Concept and Sensor of Interest (SOI)
│   ├── 4.1.1 SOI Definition and Scope Across Displays
│   ├── 4.1.2 Role of the DMS in SOI Selection
│   └── 4.1.3 HUD as SOI in A-A and HMCS Capabilities
│
├── 4.2 DMS Up: Designate HUD as SOI
│   ├── [Intro: Function and visual indication — no subsubsection]
│   ├── 4.2.1 DMS Up Effectiveness in All Master Modes
│   ├── 4.2.2 DMS Up Usage Table
│   └── 4.2.3 DMS Up Exception States (SP PRE, MARK/OFLY)
│
├── 4.3 DMS Down: Toggle SOI Between Displays
│   ├── [Intro: Core toggle logic HUD / Right MFD / Left MFD — no subsubsection]
│   ├── 4.3.1 DMS Down Effectiveness in All Master Modes
│   ├── 4.3.2 DMS Down Usage Table
│   └── 4.3.3 DMS Down Exception States
│
├── 4.4 DMS Left / Right: Cycle MFD Formats
│   ├── 4.4.1 Format Cycling Mechanics
│   ├── 4.4.2 Available Formats by Master Mode
│   ├── 4.4.3 Left/Right and SOI Independence
│   └── 4.4.4 DMS Left/Right Usage Table
│
└── 4.5 Master Mode Behavior — DMS Summary
    ├── 4.5.1 Directional DMS Roles (Up / Down / Left / Right)
    └── 4.5.2 Consolidated DMS × Master Mode Table
```

### 1.2 Key Architectural Principles

- **No separate block/variant section** — Block/variant identity is addressed once in 4.1; TMS/DMS integration is handled briefly inside each relevant subsection and in Chapter 3 (TMS) where weapon‑specific flows belong.

- **Direction-centric organization** — Sections 4.2–4.5 are organized by physical DMS direction (Up, Down, Left/Right), not by master mode. Master modes appear inside each directional section as constraints and examples.

- **Orthogonal control axes:**
  - **Vertical (Up / Down):** Selects which display is SOI.
  - **Horizontal (Left / Right):** Cycles format pages on MFDs, independent of SOI.

---

## 2. Section 4.1 — Concept and Sensor of Interest (SOI)

**Current implementation:** `section-C4-S1-concept-soi-approved-2026-01-15.tex` (integration into `guide.tex`).

**Status:**
- ✅ Integrated into `guide.tex`

### 2.1 Structure in Document Terms

```
4.1 Concept and Sensor of Interest (SOI)
  4.1.1 SOI Definition and Scope Across Displays
  4.1.2 Role of the DMS in SOI Selection
  4.1.3 HUD as SOI in A-A and HMCS Capabilities
```

### 2.2 Section 4.1.1 — SOI Definition and Scope Across Displays

**Content:**

- Defines Sensor of Interest (SOI) as the **single display/sensor that receives SOI‑dependent HOTAS inputs** (cursor slew, TMS actions, etc.).
- Lists **valid SOI displays:**
  - FCR, TGP, HSD, HAD, WPN, HUD.
- Lists **non‑SOI formats:** SMS, DTE, TEST, blank/inactive MFDS.  
- Describes **visual cues:**
  - HUD: asterisk (`*`) in upper left corner.  
  - MFD: border outline; `NOT SOI` text when not selected.
- Includes **Table 4.1.x – Valid SOI Displays by Master Mode** (`\label{tab:C4-S1-SOI-by-mode}`):
  - NAV: HUD, FCR, TGP, HSD, WPN, HAD.  
  - A‑A: FCR, HSD, TGP (**HUD cannot be SOI**).  
  - A‑G (PRE): HUD, FCR, TGP, WPN, HAD, HSD.  
  - A‑G (VIS): HUD, FCR, TGP, WPN (visual‑driven context).  
  - DGFT: FCR, HSD, TGP (**HUD cannot be SOI**).  
  - MSL OVRD: FCR, HSD, TGP (**HUD cannot be SOI**).

### 2.3 Section 4.1.2 — Role of the DMS in SOI Selection

**Content:**

- Explains the **orthogonal axes** of DMS:
  - **Vertical (Up / Down):** chooses **which display** is SOI.  
  - **Horizontal (Left / Right):** cycles **format pages** on each MFD, independent of SOI.
- Summarises baseline actions:
  - DMS Up → attempts to designate HUD/HMCS as SOI (when permitted).  
  - DMS Down → toggles SOI between HUD and MFDs.  
  - DMS Left/Right → change formats on left/right MFD without changing SOI.

### 2.4 Section 4.1.3 — HUD as SOI in A‑A and HMCS Capabilities

**Content:**

- Clarifies that **HUD cannot be SOI in A‑A/DGFT/MSL OVRD** — this is an **SOI routing restriction**, not a loss of HUD/HMCS capability.
- Explains how **HMCS** provides off‑boresight cueing in A‑A **independently of SOI:**
  - AIM‑9 boresight/slave to HMCS LOS.  
  - FCR ACM BORE slaved to HMCS LOS when conditions allow.
- Links this architecture to DMS:
  - DMS Up is **ineffective** in A‑A because HUD is not a valid SOI candidate.  
  - SOI must be managed via DMS Down (MFD↔MFD) in air‑to‑air‑driven modes.

---

## 3. Section 4.2 — DMS Up: Designate HUD as SOI

**Current implementation:** `section-C4-S2-dms-up-approved-2026-01-15.tex` (integrated into `guide.tex`).

**Status:**
- ✅ Integrated into `guide.tex`

### 3.1 Structure in Document Terms

```
4.2 DMS Up: Designate HUD as SOI
  [Intro: Function and visual indication — no subsubsection]
  4.2.1 DMS Up Effectiveness in All Master Modes
  4.2.2 DMS Up Usage Table
  4.2.3 DMS Up Exception States (SP PRE, MARK/OFLY)
```

### 3.2 Section 4.2 Intro (unnumbered) — Function and Visual Indication

**Content (one or two paragraphs, no `\subsubsection` heading):**

- DMS Up attempts to designate **HUD (and HMCS, as an extension)** as SOI.  
- When successful, **HUD SOI asterisk** appears, MFD SOI border disappears, as detailed in Section 4.1.1.  
- All SOI‑dependent HOTAS inputs (CURSOR/ENABLE, TMS) now act on HUD/HMCS symbology, not on any MFD format.

### 3.3 Section 4.2.1 — DMS Up Effectiveness in All Master Modes

**Content:**

- States that **DMS Up is only effective when HUD is a valid SOI candidate**, as per Table 4.1.x (Section 4.1.1).  
- Focuses on **contexts where HUD SOI is operationally sensitive** vs contexts where it is just a convenience.

**Sub‑structure (using `\paragraph*` and `\subparagraph*`):**

**Master Modes Where DMS Up is Effective (HUD as SOI Permitted):**

- **NAV (Navigation)**
  - HUD is primary reference for flight path, steering and basic SA.  
  - Short DMS Up → HUD becomes SOI.  
  - With HUD/HMCS SOI:
    - CURSOR/ENABLE slews HUD/HMCS cursor/designator.  
    - In HUD/HMCS MARK, TMS Up stabilises LOS and stores markpoints.  
    - MFDs provide background navigation/systems info.

- **A‑G Visual Modes (VIS) — CCIP, DTOS, AGM‑65 VIS, IAM‑VIS**
  - Visual deliveries are HUD/HMCS‑centric; HUD SOI is often a **prerequisite** for correct TMS/CURSOR behaviour.  
  - DMS Up is **operationally critical** whenever SOI has migrated to an MFD (TGP, WPN, etc.).

  Examples (bullets):

  - **CCIP visual deliveries:**
    - HUD pipper = primary aiming reference.  
    - CURSOR/ENABLE (HUD SOI) can refine visual aimpoint when allowed.

  - **AGM‑65 VIS:**
    - HUD TD box slaves Maverick seeker.  
    - With HUD SOI, CURSOR/ENABLE slews TD box; TMS Up commands seeker lock.  
    - If SOI remains on WPN MFD, TMS acts on WPN page and visual HUD control fails until DMS Up.

  - **IAM‑VIS (JDAM/JSOW visual):**
    - HUD TD box + IAM solution cues.  
    - HUD SOI + CURSOR/ENABLE refine TD; TMS Up designates/stabilizes.  
    - If SOI is on an MFD, TMS does not update HUD until DMS Up.

- **A‑G non‑VIS (CCRP, preplanned IAM)**
  - DMS Up functions (HUD can be SOI), but HUD SOI is **convenience, not requirement:**
    - Preplanned targeting, sensor SPI, sighting‑point control can be managed 100% via FCR/TGP/HSD SOI.

**Master Modes Where DMS Up is Ineffective (HUD as SOI Prohibited):**

- **A‑A, DGFT, MSL OVRD**
  - In air-to-air employment modes, HUD is not a valid SOI candidate.  
  - Pressing DMS Up **does not alter** SOI — remains on FCR, HSD or TGP.  
  - Architectural rationale and HMCS role detailed in Section 4.1.3.

### 3.4 Section 4.2.2 — DMS Up Usage Table

**Content:**

- `\subsubsection{DMS Up Usage Table}` introduces a `hotastable` that summarises DMS Up in three main rows:

  - **NAV** – Up / Short / Designate HUD as SOI  
    - Effect / Nuance: DMS Up fully effective; HUD/HMCS SOI, MARK, CURSOR/ENABLE and TMS Up; MFDs for background.  
    - Dash‑34 refs: 2.1.1.2.3, 2.1.7.5.1, 2.1.7.5.4, 2.5.6.1.  
    - Train: `---` (no specific NAV+DMS Up training mission).

  - **A‑A** – Up / Short / Designate HUD as SOI  
    - Effect / Nuance: DMS Up ineffective; architecture restricts SOI to FCR/HSD/TGP; HUD always passive as display.  
    - Dash‑34 refs: 2.1.1.2.3.  
    - Train: `---`.

  - **A‑G** – Up / Short / Designate HUD as SOI  
    - Effect / Nuance: DMS Up effective; HUD asterisk; in VIS, HUD is critical interface for CURSOR/TMS; loss of HUD SOI implies loss of visual control until new DMS Up.  
    - Dash‑34 refs: 2.1.1.2.3, 4.2.2.1, 4.2.2.1.1 (AGM‑65 VIS/IAM‑VIS).  
    - Train: `\trnref{10 (GP Bombs)}, \trnref{11 (LGB)}, \trnref{13 (Maverick)}, \trnref{14 (Maverick Adv)}, \trnref{15 (IAM)}`.

- New page (`\newpage`) before table to ensure fresh page start.

### 3.5 Section 4.2.3 — DMS Up Exception States

**Content (bullets):**

- **Snowplow (SP) PRE state (unstabilised):**
  - When entering SP and before stabilizing with TMS Up, FCR/TGP show `NOT SOI`.  
  - SOI is effectively "none"; DMS Up/Down have no effect until stabilized.  
  - After stabilization, SOI returns to previous state and DMS Up becomes active again.

- **MARK/OFLY Submode:**
  - In MARK/OFLY, SOI cannot be designated (Dash‑34 §2.1.1.2.3).  
  - DMS inputs that would normally change SOI have no effect.  
  - Rare exception in normal operations.

---

## 4. Section 4.3 — DMS Down: Toggle SOI Between Displays

**Current implementation:**
- No active WIP yet.  
- Deprecated content exists in `section-C4-S2-dms-up-down-deprecated-2026-01-14.tex` (archived for audit).

**Status alvo:**
- Create new WIP `section-C4-S3-dms-down-review-2026-01-xx.tex`.  
- Reuse valid text from deprecated file, adjusting to structure below.  
- Remove redundancies with 4.1.

### 4.1 Structure (final)

```
4.3 DMS Down: Toggle SOI Between Displays
  [Intro: Core toggle logic HUD / Right MFD / Left MFD — no subsubsection]
  4.3.1 DMS Down Effectiveness in All Master Modes
  4.3.2 DMS Down Usage Table
  4.3.3 DMS Down Exception States
```

### 4.2 Section 4.3 Intro (unnumbered) — Core Toggle Logic

**Content (in running text, no heading):**

- DMS Down alters **who is the SOI**, alternating between:
  - HUD,  
  - MFD right,  
  - MFD left.
- In modes where HUD is valid SOI (NAV, A‑G), typical cycle:  
  HUD → Right MFD → Left MFD → HUD.  
- In A‑A/DGFT/MSL OVRD, HUD is outside cycle; DMS Down alternates MFDs only.

- **Clear phrase to avoid confusion with DMS Left/Right:**

  > "In this section, 'left MFD' and 'right MFD' refer only to which display currently holds SOI when DMS Down is pressed. Format cycling on each MFD is described separately in Section 4.4 (DMS Left/Right)."

### 4.3 Section 4.3.1 — DMS Down Effectiveness in All Master Modes

**Content:**

- Similar in spirit to Section 4.2.1, but for DMS Down:
  - Describe for each mode group how SOI alternates when DMS Down is pressed.

**Target content:**

- **NAV**
  - HUD is in cycle.  
  - Typical alternation pattern: HUD → MFD right → MFD left → HUD.  
  - DMS Down is primary way to exit HUD SOI and alternate SOI between MFDs.

- **A‑G PRE/VIS**
  - Similar to NAV: HUD in cycle, but emphasize:
    - Rapidly alternate from HUD (visual) to TGP, WPN or HAD as SOI on one MFD.  
    - Return to HUD with more DMS Down press(es), per cycle logic.

- **A‑A / DGFT / MSL OVRD**
  - HUD is not valid SOI; cycle is **MFD‑only:**
    - Example: FCR (Right MFD) ↔ HSD (Left MFD) ↔ TGP, etc.  
  - DMS Down is primary tool to switch priority between FCR, HSD and TGP.

### 4.4 Section 4.3.2 — DMS Down Usage Table

**Content:**

- `\subsubsection{DMS Down Usage Table}` introduces `hotastable` parallel to DMS Up:

  - **NAV** — Down / Short / Toggle SOI between HUD and MFDs  
    - Describe cycle pattern and use in navigation and SA management.

  - **A‑A** — Down / Short / Toggle SOI between MFDs only  
    - HUD outside cycle; FCR, HSD, TGP as candidates.  

  - **A‑G** — Down / Short / Toggle SOI between HUD and A‑G sensor pages  
    - Emphasis on HUD↔TGP↔WPN↔HAD cycling, etc.
    - Dash‑34 column with refs to 2.1.1.2.3 (SOI), 2.1.6 (MFDS), other useful sections.  
    - Train column with relevant TRN (likely same as A‑G VIS, plus NAV if appropriate).

### 4.5 Section 4.3.3 — DMS Down Exception States

**Content:**

- Parallel to Section 4.2.3, focusing on how special states affect DMS Down:

  - **Snowplow (SP) PRE**:
    - When neither FCR nor TGP has SOI (both `NOT SOI`), DMS Down cannot transfer SOI between MFDs.  
    - Only after stabilizing SP (TMS Up) does SOI cycle become valid again.

  - **MARK/OFLY**:
    - In MARK/OFLY, SOI cannot be designated; DMS Down does not alter SOI.  
    - Same ineffectivity as DMS Up.

  - Other special states may be added if identified (but intent is to keep only cases truly distinct from nominal behavior).

---

## 5. Section 4.4 — DMS Left / Right: Cycle MFD Formats

**Current implementation:**
- Old `section-C4-S3-dms-format-cycling-dev-2026-01-13.tex` renamed to `section-C4-S3-dms-format-cycling-deprecated-2026-01-13.tex` and moved to ARCHIVE.  
- No new active WIP yet.

**Status alvo:**
- Create new WIP `section-C4-S4-dms-left-right-review-2026-01-xx.tex` to implement 4.4 from scratch, aligned to this blueprint.

### 5.1 Structure (final)

```
4.4 DMS Left / Right: Cycle MFD Formats
  4.4.1 Format Cycling Mechanics
  4.4.2 Available Formats by Master Mode
  4.4.3 Left/Right and SOI Independence
  4.4.4 DMS Left/Right Usage Table
```

### 5.2 Section 4.4.1 — Format Cycling Mechanics

**Content:**

- Explain in general terms:
  - DMS Left → cycles formats on **left MFD** (primary → secondary → tertiary).  
  - DMS Right → same for **right MFD**.  
  - Does not change who is SOI; changes only **what** is displayed on that MFD.

### 5.3 Section 4.4.2 — Available Formats by Master Mode

**Content:**

- Qualitative description (no separate table needed) of typical combinations:
  - NAV: FCR/HSD/SMS/etc.  
  - A‑A: FCR, HSD, SMS, etc.  
  - A‑G: FCR, TGP, HAD, WPN, SMS, HSD.

### 5.4 Section 4.4.3 — Left/Right and SOI Independence

**Content:**

- Make crystal clear that **DMS Left/Right do not change SOI**.  
- Explain typical pattern:
  - Move SOI with Up/Down.  
  - Change format on MFD where SOI is (or is not) with Left/Right.

### 5.5 Section 4.4.4 — DMS Left/Right Usage Table

**Content:**

- `hotastable` summarizing:
  - NAV — Left/Right / Short / Cycle formats on left/right MFD.  
  - A‑A — same, with emphasis on FCR/HSD.  
  - A‑G — same, with emphasis on FCR/TGP/WPN/HAD.

---

## 6. Section 4.5 — Master Mode Behavior — DMS Summary

**Current implementation:** None yet.

**Status alvo:** Short summary section + consolidated table.

### 6.1 Structure (final)

```
4.5 Master Mode Behavior — DMS Summary
  4.5.1 Directional DMS Roles (Up / Down / Left / Right)
  4.5.2 Consolidated DMS × Master Mode Table
```

### 6.2 Section 4.5.1 — Directional DMS Roles

**Content:**

- Brief recapitulation (1–2 paragraphs) of roles:
  - **Up:** HUD/HMCS SOI when permitted.  
  - **Down:** toggle SOI between HUD↔MFDs.  
  - **Left/Right:** cycle formats on MFDs.

### 6.3 Section 4.5.2 — Consolidated DMS × Master Mode Table

**Content:**

- Summary table:
  - Rows: NAV, A‑A, A‑G PRE, A‑G VIS, DGFT, MSL OVRD.  
  - Columns (example): Up / Down / Left / Right / Notes.

- Objective: give reader a "what does DMS do in each direction" view per master mode, with cross-references to 4.2–4.4 and SOI table in 4.1.

---

## 7. WIP File Mapping and To-Do List

### 7.1 Integrated (Approved) WIP Files, moved to ARCHIVE

- `section-C4-S1-concept-soi-approved-2026-01-15.tex`
  - Section 4.1 (entire).  
  - Status: integrated into `guide.tex`.

- `section-C4-S2-dms-up-approved-2026-01-15.tex`
  - Section 4.2 (DMS Up).  
  - Status: integrated into `guide.tex`.

### 7.2 Deprecated WIP Files

- `section-C4-S2-dms-up-down-deprecated-2026-01-14.tex`
  - Source of legacy DMS Down text; must **not** be re‑used directly.  
  - Relevant DMS Down content already copied to separate scratch file.

- `section-C4-S3-dms-format-cycling-deprecated-2026-01-13.tex`
  - Old attempt at format cycling; not to be used as is.

### 7.3 New WIP Files to Create

1. **`section-C4-S3-dms-down-review-2026-01-xx.tex`**
   - Implements Section 4.3 per this blueprint.  
   - Uses extracted DMS Down content from deprecated file as raw material, but rewritten for clarity and to avoid redundancy with 4.1.

2. **`section-C4-S4-dms-left-right-review-2026-01-xx.tex`**
   - Implements Section 4.4 from scratch (format cycling, independent of SOI).  
   - May borrow ideas from deprecated C4‑S3, but not structure.

3. **`section-C4-S5-dms-summary-review-2026-01-xx.tex`** (or similar naming)
   - Implements Section 4.5 summary and consolidated table.

### 7.4 Project Tracking Updates (to be done in `project-tracking-v5.0.0.md`)

Mark Chapter 4 status:
- C4‑S1 (Section 4.1): **INTEGRATED** (approved).  
- C4‑S2 (Section 4.2 DMS Up): **INTEGRATED** (approved).  
- C4‑S3 (Section 4.3 DMS Down): **IN PROGRESS** (TO DO, WIP not yet created).  
- C4‑S4 (Section 4.4 Left/Right): **NOT STARTED**.  
- C4‑S5 (Section 4.5 Summary): **NOT STARTED**.

Note archival of deprecated files and establishment of `section-C4-S2-dms-up-approved-2026-01-15.tex` as canonical DMS Up section.

---

## 8. Numbering Reconciliation — guide.tex vs Blueprint

| Blueprint Reference | guide.tex Structure | Content | Status |
|---|---|---|---|
| Section 4.1 | `\subsection{Concept and Sensor of Interest (SOI)}` | SOI definition, displays, master modes | ✅ Integrated |
| Section 4.2 | `\subsection{DMS Up: HUD Designation as SOI}` | DMS Up functionality, usage table, exception states | ✅ Integrated |
| Section 4.3 | (to be created) `\subsection{DMS Down: Toggle SOI Between Displays}` | DMS Down toggle logic, effectiveness, usage table, exception states | ⏳ Pending |
| Section 4.4 | (to be created) `\subsection{DMS Left / Right: Cycle MFD Formats}` | Format cycling mechanics, independence from SOI, usage table | ⏳ Pending |
| Section 4.5 | (to be created) `\subsection{Master Mode Behavior — DMS Summary}` | Directional roles summary, consolidated table | ⏳ Pending |

---

_End of unified Chapter 4 (DMS) blueprint v1.1 — CORRECTED & REORGANIZED 2026-01-16_
