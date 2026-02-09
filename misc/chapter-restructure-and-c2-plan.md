# Chapter Structure Reorganization and C2 Integration Plan

**Document Type:** Structural Change Specification  
**Date:** 2026-02-09 (Updated from v1.0 2026-02-06)  
**Scope:** Chapter reordering (DMS ↔ TMS) + SOI redistribution (C4 → C2) + C2 writing plan

**Change Log:**

This version updates the specification to reflect actual implementation decisions made during C2 development (2026-02-06 to 2026-02-09). All changes documented below are based on comparison between original spec and final implemented text in `chapter-C2-hotas-fundamentals-review-2026-02-09.tex`.

**Major Structural Changes:**
- Section 2.2.2 "Master Mode Selection" was REMOVED (out of scope)
- Section 2.2.3 renumbered to 2.2.2
- Section 2.2 gained introductory paragraphs linking to Section 2.1

**Section 3.2 — C3:S1 Refactoring:**
- Updated NEW opening text to preserve "at any moment, only one display" (operationally relevant)
- Updated visual indicators handling (condense to one sentence with C2 forward ref, not complete removal)
- Updated lines to CUT (extended rationale lines 665-669 → forward ref to C2:S1.3)
- Updated estimated length (~90-100 lines, cutting ~35-40 instead of ~25-30)

**Section 4.2 — C2:S1 (SOI Concept):**
- 2.1.1: Updated length estimate (~20 lines, not ~15-20) and implementation notes
- 2.1.2: Confirmed itemized list format (not pure paragraph text)
- 2.1.3: Changed approach from "explicit acronym lists" to "generic categories"
  - Removed: "FCR, TGP, WPN, HAD, HSD, HUD/HMCS" explicit listing
  - Added: "sensor formats vs informational formats" conceptual categories
  - Updated length (~15-20 lines, not ~25-30)
  - Added implementation approach (4 paragraphs structure)
  - Updated forward reference wording

**Section 4.3 — C2:S2 (Master Modes):**
- Added Section 2.2 introduction specification (NEW, ~10 lines, 2 paragraphs)
- 2.2.1: Changed "four primary modes" to "three primary + two override"
- 2.2.1: Added content (DTC programming, priority hierarchy, Dash-34 ref)
- 2.2.1: Updated length (~30-35 lines, not ~20-25)
- 2.2.1: Changed format (itemized list with paragraphs, not pure text)
- 2.2.2: Marked as REMOVED with rationale
- 2.2.3 → 2.2.2: Renumbered due to 2.2.2 removal
- 2.2.2 (ex-2.2.3): Simplified from example-driven to principle-driven
- 2.2.2 (ex-2.2.3): Updated length (~15 lines, not ~30-40)
- 2.2.2 (ex-2.2.3): Removed specific DMS/TMS examples (moved to C3/C4)

**Section 4.5 — Total C2 Length:**
- Updated total estimate (150-185 lines, down from 165-210)
- Updated Section 2.2 estimate (55-65 lines, down from 70-90)
- Added note explaining reduction (2.2.2 removal + 2.2.3 simplification)

**Section 6 — Style Guidelines:**
- Added "Avoid exhaustive acronym lists in conceptual sections"

**Section 7 — Implementation Checklist:**
- Phase 2: Updated status (C2 generated, reviewed, revised; integration pending)

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
Chapter 1 – Introduction
Chapter 2 – HOTAS Fundamentals (NOT YET WRITTEN)
Chapter 3 – TMS (Target Management Switch) (NOT YET WRITTEN)
Chapter 4 – DMS (Display Management Switch) (INTEGRATED)
Chapter 5 – CMS (Countermeasures Management Switch) (INTEGRATED)
```

### 2.2 New Structure (After Change)

```
Chapter 1 – Introduction
Chapter 2 – HOTAS Fundamentals (TO BE WRITTEN)
Chapter 3 – DMS (Display Management Switch) (RENUMBERED FROM C4)
Chapter 4 – TMS (Target Management Switch) (TO BE WRITTEN)
Chapter 5 – CMS (Countermeasures Management Switch) (NO CHANGE)
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

#### C2:S1 (New – Conceptual Foundation Only)

**Section:** 2.1 Sensor of Interest (SOI) – Concept and Architecture

**What goes in C2:S1:**
- SOI definition (HOTAS input routing)
- Why SOI exists (single control point)
- Visual indicators (asterisk, box, NOT SOI text)
- Which displays can be SOI (conceptual categories, not exhaustive lists)
- Context dependency concept (varies by master mode and MFD format)
- Forward reference to C3 for tables and operational details

**Format:** Pure text, NO tables, NO diagrams

**Length:** ~50-60 lines

---

#### New C3:S1 (Refactored – Operational Reference)

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
As introduced in Chapter~\ref{chap:C2}, the Sensor of Interest (SOI) is the display 
that currently receives HOTAS cursor slew commands and TMS actions. At any moment, 
only one display can be the SOI. The SOI is indicated visually by an asterisk on the 
HUD or a border outline on the MFD (see Section~\ref{sec:C2-S1-S2} for complete details).

The availability of displays as valid SOI varies by master mode (see 
Section~\ref{sec:C2-S1-S3} for the conceptual rationale behind these restrictions). 
Table~\ref{tab:C3-S1-SOI-by-mode} below provides the complete operational reference 
for DMS selection, showing precisely which displays can be designated as SOI in each 
master mode.
```

**What to KEEP in C3:S1:**
- ✅ Table "SOI Availability by Master Mode"
- ✅ Table "Valid and Invalid SOI MFD Formats"
- ✅ Subsection 4.1.2 "Role of DMS in SOI Selection" (unchanged)
- ✅ Subsection 4.1.3 "HUD as SOI in A-A and HMCS" (unchanged)

**What to CUT/CONDENSE:**
- ❌ Lines 629: Full definition of SOI → replace with C2 reference (see NEW opening above)
- ✅ Lines 629-630: "At any moment, only one display" → KEEP (operationally relevant)
- ⚠️ Lines 631-634: Visual indicators → CONDENSE to one sentence with C2 forward reference
- ❌ Lines 665-669: Extended "why SOI varies" discussion → condense to forward reference

**NEW condensed rationale (replace lines 665-669):**
```latex
Table~\ref{tab:C4-S1-SOI-by-mode} shows which displays can be designated as SOI in 
each master mode. For the conceptual rationale behind these restrictions, see 
Section~\ref{sec:C2-S1-S3}.
```

**Estimated new length:** ~90-100 lines (cut ~35-40 lines)

---

## 4. C2 Writing Plan

### 4.1 Approved Structure

```
Chapter 2 – HOTAS Fundamentals

2.1 Sensor of Interest (SOI) – Concept and Architecture
    2.1.1 The SOI Concept
    2.1.2 SOI Indicators and Visual Feedback
    2.1.3 SOI-Capable Displays and Context Dependency

2.2 Master Modes and Context-Sensitive Behavior
    2.2.1 Master Mode Overview
    2.2.2 Why HOTAS Switches Behave Differently by Master Mode

2.3 The Three Switches: DMS, TMS, and CMS
    2.3.1 Display Management Switch (DMS) – Overview
    2.3.2 Target Management Switch (TMS) – Overview
    2.3.3 Countermeasures Management Switch (CMS) – Overview
```

**Note:** 
- Section 2.2.2 "Master Mode Selection" was REMOVED (out of scope for TMS/DMS/CMS guide)
- Section 2.2.3 renumbered to 2.2.2
- Section 2.3 presents switches in NEW chapter order (DMS → TMS → CMS)

---

### 4.2 Section 2.1 – SOI Concept and Architecture

#### 2.1.1 The SOI Concept

**Content:**
- Define SOI: display receiving HOTAS cursor slew and TMS inputs
- Purpose: single point of HOTAS input routing
- Fundamental rule: only one display is SOI at any moment
- Architectural principle: SOI manages WHERE inputs go, not WHAT they do

**Key points:**
- SOI is designation/routing mechanism, not a sensor itself
- Enables one set of controls to manage multiple sensors
- Essential for understanding DMS and TMS behavior

**Source:** Dash-34 Section 2.1.1.2.3

**Length:** ~20 lines (4 paragraphs)

**Format:** Pure text

**Implementation notes:**
- First paragraph introduces HUD and two MFDs explicitly
- Second paragraph defines SOI and "only one display" rule
- Third paragraph explains WHERE vs WHAT principle
- Fourth paragraph states HOTAS philosophy

---

#### 2.1.2 SOI Indicators and Visual Feedback

**Content:**
- **HUD as SOI:** Asterisk (*) in upper left corner
- **MFD as SOI:** Border outline around display edges
- **NOT SOI:** Text appears on SOI-capable sensor formats

**Key points:**
- Visual feedback is immediate and unambiguous
- Pilot confirms SOI status at a glance

**Source:** Dash-34 Sections 2.1.1.2.3, 2.1.6.3

**Length:** ~12 lines

**Format:** Itemized list with introductory/closing paragraphs

---

#### 2.1.3 SOI-Capable Displays and Context Dependency

**Content:**
- SOI-capable displays: Conceptual categories (sensor formats vs informational formats)
- Context dependency: not all displays valid in all master modes
  - Rationale: Master mode restrictions align pilot attention with mission phase
  - Rationale: Format restrictions align SOI with operational function
- Forward reference to C3 for complete tables

**Key points:**
- Provide conceptual understanding, not exhaustive tables
- Explain restrictions exist and why (master mode AND MFD format dependencies)
- No explicit acroyms lists (FCR, TGP, etc.) — use generic categories instead

**Source:** Dash-34 Sections 2.1.1.2.3, 2.1.6.3

**Length:** ~15-20 lines (4 paragraphs)

**Format:** Pure text, NO tables, NO exhaustive acronym lists

**Implementation approach:**
- First paragraph: States two dependencies (master mode, MFD format)
- Second paragraph: Master mode dependency (HUD allowed in some contexts, not others)
- Third paragraph: MFD format dependency (sensor formats vs informational formats)
- Fourth paragraph: Forward reference to C3

**Forward reference:**
```latex
For complete operational reference tables showing SOI availability by master mode 
and the full list of valid and invalid MFD formats, see Chapter~\ref{chap:C3}, 
Section~\ref{sec:C3-S1}.
```

---

### 4.3 Section 2.2 – Master Modes and Context-Sensitive Behavior

#### Section 2.2 Introduction (NEW)

**Content:**
- Link to Section 2.1 (SOI varies by master mode)
- Establish master mode as broader principle
- Master mode determines SOI availability, HOTAS functions, switch interpretation
- Pre-configures displays, sensors, weapons for mission phases

**Length:** ~10 lines (2 paragraphs)

**Format:** Pure text

**Implementation text:**
```latex
\section{Master Modes and Context-Sensitive Behavior}
\label{sec:C2-S2}

Section~\ref{sec:C2-S1} established that SOI designation varies by master mode—some 
master modes permit HUD as SOI, while others restrict SOI to MFD formats only. This 
variation reflects a broader principle: master mode is the highest-level configuration 
state of the F-16 avionics system, determining not only SOI availability but also which 
HOTAS functions are active and how switch inputs are interpreted.

Each master mode pre-configures the cockpit displays, sensor modes, and weapon options 
for specific mission phases. The master mode determines which displays can be designated 
as SOI, which HOTAS functions are available, and how individual switch inputs are 
interpreted by the avionics suite. Understanding master modes is essential to understanding 
why HOTAS switches behave differently in different operational contexts.
```

---

#### 2.2.1 Master Mode Overview

**Content:**
- Three primary Master Modes: NAV, A-A, A-G
- Two override modes: DGFT, MSL OVRD
- Purpose: pre-configure avionics for mission phase
- Each mode sets default sensors, displays, weapons
- Master mode = highest-level context for HOTAS behavior
- DTC programming and manual adjustment
- Priority hierarchy (DGFT/MSL OVRD > NAV/A-A/A-G; Emergency Jettison > all)
- Reversion behavior (switch to center → previous mode)
- Dash-34 reference for complete details

**Source:** Dash-34 Section 2.1.1.2.1

**Length:** ~30-35 lines

**Format:** Itemized list with introductory/closing paragraphs

**Additions implemented:**
- DGFT/MSL OVRD described as "similar to A-A Master Mode" with specific weapon configs
- Default configurations via DTC
- Priority hierarchy explanation
- Reversion behavior (switch to center → previous mode)
- Forward reference: `\dashref{2.1.1.2.1}`

**Implementation notes:**
- Opening sentence distinguishes "three primary" vs "two override"
- Each mode described in itemized list
- DGFT/MSL OVRD item includes "similar to A-A Master Mode" language
- Closing paragraph mentions DTC, context-sensitivity, example (TMS Up varies by mode)

---

#### 2.2.2 Master Mode Selection

**Status:** REMOVED — out of scope for TMS/DMS/CMS guide.

**Rationale:** Master mode selection uses ICP buttons (not HOTAS switches). This guide 
focuses exclusively on TMS, DMS, and CMS behavior. Selection mechanics are covered in 
BMS User Manual.

**Content incorporated into 2.2.1:** Priority hierarchy and reversion behavior mentioned 
briefly in final paragraph of Master Mode Overview.

---

#### 2.2.2 Why HOTAS Switches Behave Differently by Master Mode (renumbered from 2.2.3)

**Content:**
- HOTAS switches (TMS, DMS, CMS) are context-sensitive
- Rationale: Single switch supports different tactical functions
- Design choice: Master mode reinterprets same input based on mission phase
- Benefit: Limited HOTAS controls perform wide range of tasks
- Pilot awareness requirement (not cognitive burden)
- Forward reference to C3/C4/C5 for detailed tables

**Key points:**
- Context-sensitivity is by design
- Master mode determines context → context determines function
- Pilot must know current mode to predict HOTAS behavior
- Awareness is not cognitive burden (natural reflection of mission phase)

**Source:** Dash-34 Section 2.1.5, various sensor sections

**Length:** ~15 lines (2 paragraphs)

**Format:** Two paragraphs (principle explanation + forward reference)

**Approach:** Principle-driven (conceptual foundation only)

**Rationale for simplification:** Detailed examples belong in C3/C4/C5. C2 establishes 
conceptual foundation only.

**Implementation notes:**
- First paragraph: WHY switches behave differently (master mode = operational context)
- Second paragraph: Pilot awareness + forward reference to detailed chapters
- No specific examples (DMS Up, TMS Up variations) — those go in C3/C4

---

### 4.4 Section 2.3 – The Three Switches

#### 2.3.1 Display Management Switch (DMS) – Overview

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

#### 2.3.2 Target Management Switch (TMS) – Overview

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

#### 2.3.3 Countermeasures Management Switch (CMS) – Overview

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

### 4.5 Total C2 Estimated Length (Updated)

| Section | Lines | Compiled Pages |
|---------|-------|----------------|
| 2.1 SOI | 50-60 | ~1.5-2 |
| 2.2 Master Modes | 55-65 (reduced from 70-90) | ~2 |
| 2.3 Three Switches | 45-60 | ~1.5-2 |
| **Total** | **150-185** | **~5-6** |

**Note:** Total reduced from original estimate (165-210 lines) due to:
- Removal of 2.2.2 Master Mode Selection (~20-25 lines)
- Simplification of 2.2.3 → 2.2.2 (~30-40 lines → ~15 lines)

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
- Avoid exhaustive acronym lists in conceptual sections

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

### Phase 2: C2 Writing (AI + Carlos)
- [x] Generate C2 LaTeX following this spec
- [x] Carlos reviews C2 content
- [x] Revisions applied
- [ ] Integration into guide.tex (pending)

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
