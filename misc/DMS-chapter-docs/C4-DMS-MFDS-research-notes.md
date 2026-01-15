# C4 DMS — Research Notes on MFDS Formats and Section 4.2.3 Planning

**Prepared:** 15 January 2026, ~02:28 -03  
**Purpose:** Centralize analysis of `section_4_3_plan.md` and `MFD-formats.md` against the **unified Chapter 4 (DMS) blueprint v1.1**, to guide future work on Sections **4.2.2, 4.2.3 and 4.2.4**.

---

## 0. Context

### 0.1 Blueprint Reference

The **unified C4 blueprint v1.1** defines the final structure for DMS:

```text
4 DMS — Display Management Switch

  4.1 Concept and Sensor of Interest (SOI)
    4.1.1 SOI Definition and Scope Across Displays
    4.1.2 Role of the DMS in SOI Selection
    4.1.3 HUD as SOI in A-A and HMCS Capabilities

  4.2 DMS Switch Actuation

    4.2.1 DMS Up: Designate HUD as SOI
      [Intro: Function and visual indication — no subsubsection]
      4.2.1.1 DMS Up Effectiveness in All Master Modes
      4.2.1.2 DMS Up Usage Table
      4.2.1.3 DMS Up Exception States (SP PRE, MARK/OFLY)

    4.2.2 DMS Down: Toggle SOI Between Displays
      [Intro: Core toggle logic HUD / Right MFD / Left MFD — no subsubsection]
      4.2.2.1 DMS Down Effectiveness in All Master Modes
      4.2.2.2 DMS Down Usage Table
      4.2.2.3 DMS Down Exception States

    4.2.3 DMS Left / Right: Cycle MFD Formats
      4.2.3.1 Format Cycling Mechanics
      4.2.3.2 Available Formats by Master Mode
      4.2.3.3 Left/Right and SOI Independence
      4.2.3.4 DMS Left/Right Usage Table

    4.2.4 Master Mode Behavior — DMS Summary
      4.2.4.1 Directional DMS Roles (Up / Down / Left / Right)
      4.2.4.2 Consolidated DMS × Master Mode Table
```

Sections **4.1** and **4.2.1 (DMS Up)** are already implemented and frozen as final LaTeX WIPs. The **next major work** will be:

- 4.2.2 — DMS Down.
- 4.2.3 — DMS Left/Right.
- 4.2.4 — Summary.

The two research files in this note (`section_4_3_plan.md` and `MFD-formats.md`) were originally written when a standalone “4.3 MFDS Display Formats” section was envisioned. This note evaluates how to reuse them cleanly under the new blueprint.

### 0.2 Files Considered Here

1. `section_4_3_plan.md`  
   – Old plan for a section tentatively called **4.3 MFDS DISPLAY FORMAT SELECTION**.

2. `MFD-formats.md`  
   – Research extraction from **Dash‑34 2.1.6.x** (TYPICAL MFDS FUNCTIONS, SWAP, BLANK, etc.).

Both are still **highly relevant**, but their content must now be mapped into **4.2.3 / 4.2.4**, not into a separate chapter section "4.3".

---

## 1. Analysis of `section_4_3_plan.md`

### 1.1 What the file contains

This file is a structured **writing plan** for a section named:

> **4.3 MFDS DISPLAY FORMAT SELECTION**

Key elements:

- Short opening context about the MFDS:
  - Left/right displays, 3+3 slots, “all-purpose” nature.
  - Why format selection matters operationally.

- A **primary concept**: “FORMAT SLOTS”
  - 3 slots per MFD: 1 PRIMARY + 2 SECONDARY.
  - Slot architecture and inside→outside cycling principle.
  - Reference to the 16 available formats from Dash‑34 2.1.6.2.

- **User actions: how to change formats** (three main paths):
  - Path A: Direct OSB selection of secondary format.
  - Path B: DMS Left/Right cycling through formats.
  - Path C: Master Menu (full 16‑format menu).

- **Special cases:**
  - SWAP between left/right MFDs.
  - BLANK format behaviour.
  - OFF format behaviour.

- **Constraint:** No duplicate formats across the 6 total slots; BLANK as escape.

- **Relationship to SOI:**
  - SOI as “who gets HOTAS control”, vs format as “what is displayed”.
  - Visual indicators (MFD border, HUD asterisk).
  - Interaction with DMS Up/Down.

- **Operational workflows:**
  - Radar-focused mission setup.
  - Tactical reorientation with SWAP.
  - Handling an unavailable format (“OFF”).

- **Key writing principles:**
  - Use Dash‑34 language.
  - Emphasize no-duplicates rule.
  - Treat the three selection paths symmetrically.
  - Link to SOI concept without re‑explaining it fully.

- A final **outline**:

  ```text
  4.3 MFDS DISPLAY FORMAT SELECTION
  ├─ 4.3.1 Format Architecture
  │  └─ Slot Structure (3+3, no duplicates)
  ├─ 4.3.2 Selecting Formats
  │  ├─ Direct OSB Selection
  │  ├─ DMS Left/Right Cycling
  │  └─ Master Menu Access
  ├─ 4.3.3 Special Operations
  │  ├─ SWAP Between MFDs
  │  ├─ BLANK Format
  │  └─ OFF Format
  ├─ 4.3.4 Format Availability
  │  └─ No Duplicates Rule (+ BLANK exception)
  └─ 4.3.5 Interaction with SOI
     └─ Format vs SOI distinction
  ```

### 1.2 Alignment/conflict with the current blueprint

Under the **unified C4 blueprint v1.1**:

- The old “4.3 MFDS Display Formats” section **no longer exists** as a separate major section.
- All MFDS format selection/cycling content must now live primarily in:
  - **4.2.3 DMS Left / Right: Cycle MFD Formats**, and secondarily in
  - **4.2.4 Master Mode Behavior — DMS Summary** (short recaps + consolidated table).

Consequence: the **structure** proposed in this file is obsolete (as a chapter outline), but the **content** remains extremely valuable. It needs to be remapped to the new 4.2.3 subsections.

### 1.3 Direct mapping to 4.2.3 subsections

#### 4.2.3.1 Format Cycling Mechanics

Use from `section_4_3_plan`:

- “Primary concept: format slots”
  - 3 slots per MFD: 1 PRIMARY + 2 SECONDARY.
  - Explanation of slot architecture.
- “Inside to outside” cycling principle.
- Emphasis on the **cycling behaviour** when using DMS Left/Right:
  - PRIMARY → next → next → PRIMARY (circular), skipping BLANK.

Here, the file gives good prose building blocks for:

- A clear, high‑level explanation of the **slot system**, independent of master mode.
- An intuitive explanation of the **cycling order** that will be critical for pilots.

#### 4.2.3.2 Available Formats by Master Mode

Use from `section_4_3_plan`:

- The reference to **16 available formats** (from Dash‑34 2.1.6.2):
  - FCR, TGP, WPN, HAD, HSD, SMS, DTE, TEST, FLIR, TFR, TCN, BLANK, etc.
- The idea of an overview table (though the exact table layout may be handled in `MFD-formats.md`).

In 4.2.3.2, the plan can be adapted to:

- Give a short **descriptive paragraph** of what kinds of formats exist.
- Optionally, a compact table listing formats vs “Video/Text/Both” (if needed for clarity).
- Without trying to fully restate master-mode‑by‑format details (those belong more to sensor/weapon chapters).

#### 4.2.3.3 Left/Right and SOI Independence

Use from `section_4_3_plan`:

- Section “SENSOR OF INTEREST (SOI) RELATIONSHIP”.
- The distinction "format displayed vs SOI".
- Clarification that a format may be displayed but not SOI (`NOT SOI` indication).

Caution:

- SOI is **already fully defined** in **4.1**.
- The role of DMS in SOI selection is covered by **4.1.2**, **4.2.1** (Up) and **4.2.2** (Down).

Therefore, in 4.2.3.3 this material should be **used only to reinforce the independence** of horizontal DMS (format cycling) from vertical DMS (SOI selection), for example:

- “DMS Left/Right does not change which display is SOI; it only changes which format is currently shown on each MFD.”

The old plan’s deeper SOI exposition should **not** be repeated; just **reference** 4.1 and 4.2.1–4.2.2.

#### 4.2.3.4 DMS Left/Right Usage Table

Use from `section_4_3_plan`:

- The three paths to format selection (OSB, DMS, Master Menu) as **nuance text** in the table’s Effect/Nuance column for DMS Left/Right.
- The “special operations” (SWAP, BLANK, OFF) as specific notes attached to lines or notes following the table.

Example mapping:

- NAV / A‑A / A‑G rows describing:
  - “DMS Left/Right cycles PRIMARY format along the configured slots. BLANK slots are skipped (see BLANK format behaviour). SWAP exchanges L/R MFD content but is not a format change.”

### 1.4 What should be discarded or treated as legacy

- The **section numbering** and “4.3.x” labels in this file are obsolete.
- Any implication that SOI would be **redefined** in this section should be dropped.
- Detailed master mode tables that try to replicate sensor‑oriented behaviour are better placed in:
  - Chapter 3 (TMS) or
  - Sensor/weapon‑specific chapters/tables, not in 4.2.3.

The file is best treated as:

> A **topic plan** for MFDS format handling, whose content is now spread across 4.2.3.1–4.2.3.4 under the new blueprint.

---

## 2. Analysis of `MFD-formats.md`

### 2.1 What the file contains

`MFD-formats.md` is essentially a **research digest** of Dash‑34 Section 2.1.6.x:

- **Format slots per MFD:**
  - 3 per MFD (1 PRIMARY, 2 SECONDARY).
  - Behaviour of OSBs adjacent to secondary formats.
  - DMS Left/Right as a mechanism to change PRIMARY only.
  - Clarification of “selection from inside to outside” as the cycling pattern.

- **Master Menu & format changing:**
  - Access via OSB next to PRIMARY mnemonic.
  - New selection replaces the previous PRIMARY.
  - In‑flight configuration allowed.

- **Constraint: No duplicate formats:**
  - Across 6 total slots (3+3), no two can be the same.
  - BLANK or TEST as special cases.
  - Auto‑substitution with BLANK on conflicts.

- **DMS relationship with PRIMARY format cycling:**
  - DMS Left/Right changes PRIMARY only.
  - Cycling pattern PRIMARY → middle → third → PRIMARY.
  - BLANK skipped.

- **List of 16 available formats** (video/text/both).

- **SWAP function:**
  - Swaps entire left/right MFD content (video + text).

- **BLANK format:**
  - Manually selectable.
  - Shows blank display.
  - Skipped during DMS cycling.

- **DTE configuration:**
  - Pre‑flight via DTC.
  - In‑flight persistence of changes.

- **Research coverage** of 2.1.6.2–2.1.6.10 (with notes on what was not reviewed).

### 2.2 Alignment with the current blueprint

This file is **exactly** the type of factual foundation required to implement:

- **4.2.3.1 Format Cycling Mechanics**
- **4.2.3.2 Available Formats by Master Mode** (at least the “available formats” part)
- **4.2.3.4 DMS Left/Right Usage Table**

It is also a good cross‑check for 4.2.4 when summarising “what DMS can do” by master mode.

There is no structural conflict with the current blueprint; the only care needed is to:

- Avoid re‑explaining SOI in 4.2.3 (that’s in 4.1 / 4.2.1–4.2.2).
- Keep DMS Left/Right focused on **format cycling**, not on SOI.

### 2.3 Direct mapping to 4.2.3 subsections

#### 4.2.3.1 Format Cycling Mechanics

Use from `MFD-formats.md`:

- Slot architecture:
  - 3 slots per MFD (PRIMARY + 2 SECONDARY).
- Behaviour of OSBs next to secondary labels.
- DMS Left/Right role:
  - Changes PRIMARY only.
  - Inside→outside cycling.
  - BLANK skipped.

These points can be turned almost directly into a concise narrative:

- Describe how pilots configure the three slots (often pre‑flight via DTC, but adjustable in flight).
- Describe how, once slots are populated, DMS Left/Right allows rapid cycling between them during operations.

#### 4.2.3.2 Available Formats by Master Mode

Use from `MFD-formats.md`:

- The enumerated list of formats from 2.1.6.2:
  - FCR, TGP, WPN, HAD, HSD, SMS, DTE, TEST, FLIR, TFR, TCN, BLANK, etc.

In 4.2.3.2, this list can provide the **baseline universe of formats**. The text can then briefly comment on which formats are commonly used in NAV, A‑A, and A‑G, without reproducing full master‑mode tables from Dash‑34.

#### 4.2.3.3 Left/Right and SOI Independence

Use from `MFD-formats.md` only indirectly:

- The section “SOI Concept” in this file is mainly a **reminder** to maintain correct conceptual separation:
  - SOI is a routing mechanism for HOTAS.
  - DMS Up/Down manage SOI.
  - DMS Left/Right manage formats.

No detailed SOI exposition from this file should be copied into 4.2.3; instead, 4.2.3.3 can simply refer back to 4.1 / 4.2.1 / 4.2.2.

#### 4.2.3.4 DMS Left/Right Usage Table

Use from `MFD-formats.md`:

- “UI/UX Pattern Recognition” section:
  - Format selection hierarchy: OSB → DMS → Master Menu.
  - No‑duplicates rule.
  - BLANK behaviour.

These become ideal material for the **Effect / Nuance** column in the DMS Left/Right HOTAS table:

- For NAV:
  - “DMS Left/Right cycles between configured NAV/SA formats on each MFD (e.g. HSD, FCR, SMS). BLANK slots are skipped, allowing pilots to reserve dormant slots.”

- For A‑A:
  - “DMS Left/Right provides rapid cycling between FCR/HSD/SMS in the MFD that currently hosts those formats, independent of which display is SOI.”

- For A‑G:
  - “DMS Left/Right is used to quickly toggle between TGP/WPN/HAD/FCR formats on each MFD, while DMS Up/Down and TMS manage SOI and targeting.”

### 2.4 What should be treated cautiously

- Any parts of `MFD-formats.md` that attempt to re‑specify **SOI behaviour** or DMS Up/Down logic must be reconciled with the now‑final 4.1 and 4.2.1 sections:
  - They should be used only as cross-checks or reminders, not as new primary text.
- Very detailed DTE configuration discussion may be beyond the intended scope of Chapter 4 (DMS) and may be better placed in:
  - Chapter 2 (HOTAS Fundamentals / Mission Setup), or
  - An appendix about **DTC / MSMD** usage.

---

## 3. Practical Guidance for Future C4 Work

When writing **4.2.2, 4.2.3, 4.2.4**, these two research files should be used in the following way:

### 3.1 For 4.2.2 DMS Down

These files are **indirectly** helpful:

- They remind that:
  - Left/Right MFD concepts must be used carefully (state of SOI vs format).
  - DMS Down moves SOI between **HUD / Right MFD / Left MFD**, not formats.

But there is **little direct text** to lift from them for DMS Down. They serve more as:

- A check that any mention of MFDs in 4.2.2 does not accidentally conflate **SOI movement** with **format cycling**.

### 3.2 For 4.2.3 DMS Left / Right

These files are the **primary source** of:

- Slot architecture description.
- DMS Left/Right mechanics.
- SWAP, BLANK, OFF behaviours.
- Non‑duplicate rules.
- Format universe description.
- User workflow examples.

In practice, when drafting 4.2.3:

- Start from `MFD-formats.md` for factual, Dash‑34‑aligned statements.
- Use `section_4_3_plan` for narrative structure, examples and phrasing ideas.
- Always cross‑check that **SOI mentions** in 4.2.3 are brief and reference 4.1/4.2.1/4.2.2.

### 3.3 For 4.2.4 Master Mode Summary

From these notes, 4.2.4 can inherit:

- Short, high‑level descriptions that capture:
  - “In NAV, DMS Left/Right mainly manages SA formats (HSD/FCR/SMS).”
  - “In A‑A, DMS Left/Right cycles radar/SA/system pages while SOI stays on combat‑critical surfaces.”
  - “In A‑G, DMS Left/Right is often used to keep TGP/WPN/HAD available on one side while HUD/HMCS plus DMS Up/Down and TMS drive targeting.”

These will feed into the **consolidated DMS × Master Mode** table and help keep the summary grounded in real MFDS behaviour.

---

## 4. Summary of Usefulness

### 4.1 `section_4_3_plan.md`

- **Structural plan:** obsolete (4.3 no longer exists as a standalone section).
- **Content:** highly reusable for **4.2.3**, especially:
  - Conceptual explanations (slots, 3 paths to selection).
  - Special cases (SWAP, BLANK, OFF).
  - Operational examples.
- **Best usage:** treat as a **conceptual outline** for drafting the narrative parts of 4.2.3, mapping its subtopics into 4.2.3.1–4.2.3.4.

### 4.2 `MFD-formats.md`

- **Structural content:** N/A (it is a research digest, not an outline).
- **Content:** primary factual backbone for **4.2.3** and support for 4.2.4:
  - Slot mechanics, DMS Left/Right behaviour, SWAP, BLANK, OFF, no-duplicates rule, format list.
- **Best usage:** treat as the **authoritative technical source** when writing 4.2.3.1/4.2.3.2/4.2.3.4, ensuring all claims match Dash‑34 2.1.6.x.

---

## 5. Recommended Workflow for Future Sessions

When a future AI session continues Chapter 4 (DMS) work:

1. **Load references:**
   - Unified C4 blueprint v1.1 (`C4-DMS-blueprint.md`).
   - This note (`C4-DMS-MFDS-research-notes.md`).
   - `MFD-formats.md` (for raw Dash‑34 data).
   - `section_4_3_plan.md` (for example flows and phrasing).

2. **Draft 4.2.3 in this order:**
   - Write 4.2.3.1 (mechanics) from `MFD-formats.md`.
   - Write 4.2.3.2 (available formats) using the list of formats and adding light contextual text.
   - Write 4.2.3.3 explicitly stating Left/Right ≠ SOI change; reference 4.1/4.2.1/4.2.2.
   - Design 4.2.3.4 HOTAS table using insights from both research files.

3. **Only then** derive any short phrases needed for 4.2.4.

This preserves architectural clarity (vertical vs horizontal DMS axes) while taking full advantage of the research already done in these two files.
