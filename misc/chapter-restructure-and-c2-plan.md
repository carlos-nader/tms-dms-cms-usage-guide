# Chapter Structure Reorganization and C2 Integration Plan

**Document Type:** Structural Change Specification  
**Version:** 1.0  
**Date:** 2026-02-06  
**Scope:** Chapter reordering (DMS ↔ TMS) + SOI redistribution (C4 → C2) + C2 writing plan

---

## 1. Executive Summary

This document specifies:

1. **Chapter reordering:** Current C3 (TMS) ↔ Current C4 (DMS) to establish pedagogically correct sequence
2. **SOI content redistribution:** Move conceptual SOI foundation from C4:S1 to C2:S1
3. **C2 writing plan:** Structure and content guidelines for Chapter 2 (HOTAS Fundamentals)

**Rationale:** DMS manages SOI selection; TMS operates through SOI. Readers must understand "how to select which display is active" (DMS) before learning "how to manage targets on the active display" (TMS).

---

## 2. Chapter Reordering

### 2.1 Current Structure (Before Change)

```
Chapter 1 — Introduction
Chapter 2 — HOTAS Fundamentals (NOT YET WRITTEN)
Chapter 3 — TMS (Target Management Switch) (NOT YET WRITTEN)
Chapter 4 — DMS (Display Management Switch) (INTEGRATED)
Chapter 5 — CMS (Countermeasures Management Switch) (INTEGRATED)
```

### 2.2 New Structure (After Change)

```
Chapter 1 — Introduction
Chapter 2 — HOTAS Fundamentals (TO BE WRITTEN)
Chapter 3 — DMS (Display Management Switch) (RENUMBERED FROM C4)
Chapter 4 — TMS (Target Management Switch) (TO BE WRITTEN)
Chapter 5 — CMS (Countermeasures Management Switch) (NO CHANGE)
```

### 2.3 Renumbering Tasks (Manual Execution by Carlos)

1. **Rename chapter labels:**
   - Current `\label{chap:C4}` → New `\label{chap:C3}`

2. **Rename ALL section labels in current C4 (DMS):**
   - All `\label{sec:C4-*}` → `\label{sec:C3-*}`
   - All `\label{sec:C4-S1-*}` → `\label{sec:C3-S1-*}`
   - All `\label{sec:C4-S2-*}` → `\label{sec:C3-S2-*}`
   - All `\label{sec:C4-S3-*}` → `\label{sec:C3-S3-*}`
   - All `\label{sec:C4-S4-*}` → `\label{sec:C3-S4-*}`

3. **Update cross-references:**
   - Search entire guide.tex for `\ref{chap:C3}` and `\ref{chap:C4}`
   - Update accordingly (C3 refs now point to non-existent TMS, C4 refs should point to C3)

4. **Update table labels:**
   - `\label{tab:C4-*}` → `\label{tab:C3-*}`

5. **Update figure labels (if any):**
   - `\label{fig:*_c4_*}` → `\label{fig:*_c3_*}`

6. **Update chapter heading:**
   - Verify line with `\chapter{DMS -- Display Management Switch}` has correct `\label{chap:C3}`

7. **Compile and verify:**
   - Run LaTeX compilation
   - Check all cross-references resolve correctly
   - Verify Table of Contents shows correct chapter numbers

---

## 3. SOI Content Redistribution

### 3.1 Current SOI in C4:S1 (guide.tex lines 599-733, ~138 lines)

**Current structure:**
```
4.1 Concept and Sensor of Interest (SOI)
    4.1.1 SOI Definition and Master Mode Availability
        4.1.1.1 Valid SOI Formats
    4.1.2 Role of DMS in SOI Selection
    4.1.3 HUD as SOI in A-A and HMCS Capabilities
```

**Content breakdown:**
- Conceptual foundation (~30-40 lines): What SOI is, visual indicators
- Operational tables (~60 lines): SOI by master mode, valid/invalid formats
- DMS mechanics preview (~20 lines): How DMS Up/Down work
- HMCS discussion (~20 lines): HUD vs HMCS in A-A

### 3.2 New Distribution

#### C2:S1 (New — Conceptual Foundation Only)

**Section:** 2.1 Sensor of Interest (SOI) — Concept and Architecture

**What goes in C2:S1:**
- SOI definition (HOTAS input routing)
- Why SOI exists (single control point)
- Visual indicators (asterisk, box, NOT SOI text)
- Which displays can be SOI (conceptual list)
- Context dependency concept (varies by master mode)
- Forward reference to C3 for tables and operational details

**Format:** Pure text, NO tables, NO diagrams

**Length:** ~50-60 lines

---

#### New C3:S1 (Refactored — Operational Reference)

**Refactoring needed in C3:S1.1 (subsection "SOI Definition and Master Mode Availability"):**

**CURRENT opening (lines 629-636 in guide.tex):**
```latex
The Sensor of Interest (SOI) is the display or sensor that currently receives 
HOTAS cursor slew commands and, where applicable, TMS actions. At any moment, 
only one display can be the SOI. Visually, The currently active SOI is easily 
recognized:

- On the HUD: an asterisk (*) appears in the upper left corner when HUD is SOI.
- On an MFD: a border outline appears around the edges of the display when it is SOI.

The availability of displays as valid SOI varies by master mode...
```

**NEW opening (REPLACE above text with this):**
```latex
As introduced in Chapter~\ref{chap:C2}, the Sensor of Interest (SOI) is the 
display that currently receives HOTAS cursor slew commands and TMS actions. 
The availability of displays as valid SOI varies by master mode (see 
Section~\ref{sec:C2-S1} for conceptual overview). 

Table~\ref{tab:C3-S1-SOI-by-mode} below provides the complete operational 
reference for DMS selection, showing precisely which displays can be designated 
as SOI in each master mode.
```

**What to KEEP in C3:S1:**
- ✅ Table "SOI Availability by Master Mode"
- ✅ Table "Valid and Invalid SOI MFD Formats"
- ✅ Subsection 4.1.2 "Role of DMS in SOI Selection" (unchanged)
- ✅ Subsection 4.1.3 "HUD as SOI in A-A and HMCS" (unchanged)

**What to CUT/CONDENSE:**
- ❌ Lines 629-634: Full definition of SOI → replace with C2 reference (see NEW opening above)
- ❌ Lines 665-669: Extended "why SOI varies" discussion → condense to 1-2 sentences

**Estimated new length:** ~100-110 lines (cut ~25-30 lines)

---

## 4. C2 Writing Plan

### 4.1 Approved Structure

```
Chapter 2 — HOTAS Fundamentals

2.1 Sensor of Interest (SOI) — Concept and Architecture
    2.1.1 The SOI Concept
    2.1.2 SOI Indicators and Visual Feedback
    2.1.3 SOI-Capable Displays and Context Dependency

2.2 Master Modes and Context-Sensitive Behavior
    2.2.1 Master Mode Overview
    2.2.2 Master Mode Selection
    2.2.3 Why HOTAS Switches Behave Differently by Master Mode

2.3 The Three Switches: DMS, TMS, and CMS
    2.3.1 Display Management Switch (DMS) — Overview
    2.3.2 Target Management Switch (TMS) — Overview
    2.3.3 Countermeasures Management Switch (CMS) — Overview
```

**Note:** Section 2.3 presents switches in NEW chapter order (DMS → TMS → CMS)

---

### 4.2 Section 2.1 — SOI Concept and Architecture

#### 2.1.1 The SOI Concept

**Content:**
- Define SOI: display receiving HOTAS cursor slew and TMS inputs
- Purpose: single point of HOTAS input routing
- Fundamental rule: only one display is SOI at any moment
- Architectural principle: SOI manages WHERE inputs go, not WHAT they do

**Key points:**
- SOI is routing mechanism, not a sensor itself
- Enables one set of controls to manage multiple sensors
- Essential for understanding DMS and TMS behavior

**Source:** Dash-34 Section 2.1.1.2.3

**Length:** ~15-20 lines

**Format:** Pure text

---

#### 2.1.2 SOI Indicators and Visual Feedback

**Content:**
- **HUD as SOI:** Asterisk (*) in upper left corner
- **MFD as SOI:** Border outline around display edges
- **NOT SOI:** Text appears on capable formats that aren't currently SOI

**Key points:**
- Visual feedback is immediate and unambiguous
- Pilot confirms SOI status at a glance

**Source:** Dash-34 Sections 2.1.1.2.3, 2.1.6.3

**Length:** ~10-15 lines

**Format:** Pure text

---

#### 2.1.3 SOI-Capable Displays and Context Dependency

**Content:**
- SOI-capable displays: FCR, TGP, WPN, HAD, HSD, HUD/HMCS
- Context dependency: not all displays valid in all master modes
  - Example: HUD can be SOI in NAV/A-G, NOT in A-A/DGFT
  - Example: Some formats (SMS, DTE, TEST) never SOI-capable
- Rationale: restrictions align pilot attention with operational context

**Key points:**
- Provide conceptual understanding, not exhaustive tables
- Explain restrictions exist and why
- Forward reference to C3 for complete tables

**Source:** Dash-34 Sections 2.1.1.2.3, 2.1.6.3

**Length:** ~25-30 lines

**Format:** Pure text, NO tables

**Example forward reference:**
```
For complete tables showing SOI availability by master mode and valid SOI 
formats, see Chapter~\ref{chap:C3}, Section~\ref{sec:C3-S1}.
```

---

### 4.3 Section 2.2 — Master Modes and Context-Sensitive Behavior

#### 2.2.1 Master Mode Overview

**Content:**
- Four primary modes: NAV, A-A, A-G, DGFT/MSL OVRD
- Purpose: pre-configure avionics for mission phase
- Each mode sets default sensors, displays, weapons
- Master mode = highest-level context for HOTAS behavior

**Source:** Dash-34 Section 2.1.1.2.1

**Length:** ~20-25 lines

**Format:** Pure text

---

#### 2.2.2 Master Mode Selection

**Content:**
- NAV: Default (no explicit selection)
- A-A: ICP A-A button
- A-G: ICP A-G button
- DGFT: Throttle switch left/outward
- MSL OVRD: Throttle switch right/inward

**Key points:**
- Single switch action for rapid reconfiguration
- DGFT/MSL OVRD override other modes (except Emergency Jettison)
- Returning switch to center restores previous mode

**Source:** Dash-34 Section 2.1.1.2.1 (table)

**Length:** ~20-25 lines

**Format:** Text with optional small table

**Optional table:**
| Master Mode | Switch Location | Switch Position |
|-------------|-----------------|-----------------|
| NAV | Default | — |
| A-A | ICP | A-A button |
| A-G | ICP | A-G button |
| DGFT | Throttle | Left/outward |
| MSL OVRD | Throttle | Right/inward |

---

#### 2.2.3 Why HOTAS Switches Behave Differently by Master Mode

**Content:**
- HOTAS switches (TMS, DMS, CMS) are context-sensitive
- Same switch action → different results in different modes
- Examples:
  - DMS Up in NAV/A-G: designates HUD as SOI
  - DMS Up in A-A: no effect (HUD can't be SOI in A-A)
  - TMS Up varies by SOI and mode

**Key points:**
- Context-sensitivity is by design
- Master mode determines context → context determines function
- Pilot must know current mode to predict HOTAS behavior

**Source:** Dash-34 Section 2.1.5, various sensor sections

**Length:** ~30-40 lines

**Format:** Pure text

---

### 4.4 Section 2.3 — The Three Switches

#### 2.3.1 Display Management Switch (DMS) — Overview

**Content:**
- Four-way spring-loaded switch on stick
- Primary functions: SOI selection (Up/Down), format cycling (Left/Right)
- Transversal manager: controls WHICH display receives inputs
- Does not perform tactical actions (unlike TMS)

**Example text:**
```
The Display Management Switch (DMS) is a four-way, spring-loaded switch on 
the flight stick. Its primary role is SOI designation and MFD format cycling. 
Unlike TMS, which performs tactical functions, DMS is a transversal manager—it 
selects which display receives HOTAS inputs, but does not execute tactical 
actions itself. Detailed DMS functionality is in Chapter~\ref{chap:C3}.
```

**Length:** ~15-20 lines

---

#### 2.3.2 Target Management Switch (TMS) — Overview

**Content:**
- Four-way spring-loaded switch on throttle
- Primary function: target management and designation
- Context-dependent: varies by master mode, sensor mode, SOI
- Operates through current SOI

**Example text:**
```
The Target Management Switch (TMS) is a four-way, spring-loaded switch on 
the throttle grip. Its primary function is target management and designation. 
TMS behavior depends on the active master mode, sensor mode, and which display 
is SOI. For example, TMS Up with FCR as SOI designates a radar target, while 
TMS Up with TGP as SOI may break track or establish cursor zero, depending on 
A-G submode. Detailed TMS functionality is in Chapter~\ref{chap:C4}.
```

**Length:** ~15-20 lines

---

#### 2.3.3 Countermeasures Management Switch (CMS) — Overview

**Content:**
- Four-way spring-loaded switch on throttle
- Primary function: countermeasures dispensing
- Interacts with CMDS, ECM, RWR
- Relatively independent of SOI (unlike TMS/DMS)

**Example text:**
```
The Countermeasures Management Switch (CMS) is a four-way, spring-loaded 
switch on the throttle grip. Its primary function is countermeasures 
dispensing, controlling chaff/flare release from CMDS and managing ECM pod 
transmissions. Unlike TMS and DMS, CMS operates largely independently of SOI, 
instead interacting directly with defensive systems based on RWR threat 
warnings. Detailed CMS functionality is in Chapter~\ref{chap:C5}.
```

**Length:** ~15-20 lines

---

### 4.5 Total C2 Estimated Length

| Section | Lines | Compiled Pages |
|---------|-------|----------------|
| 2.1 SOI | 50-60 | ~1.5-2 |
| 2.2 Master Modes | 70-90 | ~2-2.5 |
| 2.3 Three Switches | 45-60 | ~1.5-2 |
| **Total** | **165-210** | **~5-6.5** |

---

## 5. Future C4 (TMS) Writing Guidelines

**When TMS chapter is written:**

### 5.1 SOI References in TMS

**Opening paragraph template:**
```latex
The Target Management Switch (TMS) operates through the currently active 
Sensor of Interest (SOI). TMS behavior depends fundamentally on which display 
holds the SOI designation (see Chapter~\ref{chap:C2} for SOI concept and 
Chapter~\ref{chap:C3} for DMS SOI selection mechanics).
```

**Context-specific references:**
```latex
When the Fire Control Radar (FCR) is SOI (see Section~\ref{sec:C3-S2} for 
how to designate FCR as SOI via DMS), TMS Up commands target designation...
```

**Rules:**
- ❌ Do NOT re-explain what SOI is (C2 covers this)
- ❌ Do NOT re-explain how to select SOI (C3 covers this)
- ✅ DO reference C2 for SOI concept when first mentioned
- ✅ DO reference C3 for DMS selection when relevant
- ✅ DO focus on "what TMS does when [display] is SOI"

---

## 6. Style and Formatting Guidelines

### Tone
- Third person present tense
- Active voice (passive strategic)
- Authoritative but accessible
- Assumes basic F-16/BMS familiarity

### Paragraph Structure
- Short paragraphs (2-5 sentences)
- Topic sentence + supporting details
- Clear transitions

### Technical Language
- Precise, consistent terminology
- Acronyms defined on first use
- Dash-34 references where appropriate

### LaTeX Formatting
- `\textbf{}` for key terms/labels
- `\texttt{}` for UI elements/system values
- `\textit{}` for emphasis on distinctions
- `\dashref{}` for Dash-34 references
- `\ref{}` for internal cross-references

---

## 7. Implementation Checklist

### Phase 1: Manual Renumbering (Carlos)
- [ ] Backup current guide.tex
- [ ] Rename C4 → C3 labels throughout
- [ ] Update all cross-references
- [ ] Compile and verify all refs work
- [ ] Update PROJECT-TRACKING if needed

### Phase 2: C2 Writing (AI)
- [ ] Generate C2 LaTeX following this spec
- [ ] Carlos reviews C2 content
- [ ] Revisions if needed
- [ ] Integration into guide.tex

### Phase 3: C3 Refactoring (AI + Carlos)
- [ ] AI generates refactored C3:S1 opening text
- [ ] Carlos integrates into current C4 (now C3)
- [ ] Verify forward/backward references work
- [ ] Compile and check

### Phase 4: Future C4 (TMS)
- [ ] Write following SOI reference guidelines
- [ ] Cross-reference C2 and C3 appropriately

---

**End of Specification**
