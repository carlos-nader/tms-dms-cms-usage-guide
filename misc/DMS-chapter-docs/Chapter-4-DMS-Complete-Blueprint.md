# Falcon BMS TMS/DMS/CMS Guide — Chapter 4 (DMS) Complete Blueprint

**Date:** 14 January 2026, 11:21 AM -03  
**Status:** Final strategic blueprint for comprehensive chapter development  
**Version:** 1.0  
**Based on:** Dash-34 (§2.1.1.2.3, §2.1.5, §2.1.6), C4-S1 (approved), C4-S2 (DMS Up only), MCH 11-F16 Vol5

---

## Executive Summary

This document provides a **complete blueprint for Chapter 4 (DMS)** including:

1. **Final structure** (4 sections, no 4.3 or large 4.4)
2. **Content allocation** per section with word count targets
3. **Integration of existing WIP files** (C4-S1, C4-S2) with minimal refactoring
4. **New WIP files needed** (C4-S2 DMS Down, C4-S2 Left/Right, etc.)
5. **Table architecture** (one HOTAS table per direction)
6. **What should be in the complete chapter** beyond existing files

---

## Part 1: Final Chapter 4 Structure

### 1.1 Approved Structure

```
4.1 Concept and Sensor of Interest (SOI)
    [Existing: C4-S1 concept-soi-review-2026-01-13.tex]
    [Status: final (minor copyedit only)]
    
4.2 DMS Switch Actuation — Organized by Direction
    4.2.1 DMS Up: Designate HUD as SOI
        [Existing: C4-S2 dms-up-down-review (subset)]
        [New narrative + table needed]
    
    4.2.2 DMS Down: Toggle SOI Between Displays
        [Existing: C4-S2 dms-up-down-review (subset)]
        [New table needed]
    
    4.2.3 DMS Left / Right: Cycle MFD Formats
        [Existing: None (C4-S3 dms-format-cycling-dev exists but needs alignment)]
        [Complete rewrite + table needed]
    
    4.2.4 Integration with TMS (Brief Overview)
        [New: ~500 words, 2-3 examples max]
        [Pointer to TMS Chapter 3 for weapon-specific details]
    
    4.2.5 Exception States & Operational Notes
        [Consolidate from existing C4-S2, expand slightly]
        
4.3 [DELETED - not needed per C4-S1 statement on block/variant identity]

4.4 [DELETED - weapon-specific integration moves to TMS Chapter 3]
```

**Why this structure:**
- **Direction-based organization** reflects Dash-34 terminology (DMS Up, Down, Left, Right).
- **Master modes appear as contextual constraints**, not organizational dividers.
- **Orthogonal axes** (vertical SOI / horizontal format) remain distinct and clear.
- **Integration with TMS is brief** — detailed weapon-specific procedures belong in TMS Chapter 3.

---

## Part 2: Integration of Existing WIP Files

### 2.1 C4-S1 (Concept and SOI) — Status: KEEP, MINIMAL EDITS

**Current file:** `section-C4-S1-concept-soi-review-2026-01-13.tex`

**Assessment:**
- ✅ Correctly defines SOI across displays.
- ✅ Master mode × valid SOI table is accurate.
- ✅ Paragraph on block/variant identity is **perfect** (eliminates need for 4.3).
- ✅ Distinction between SOI routing architecture and functional capability (HUD in A-A) is well explained.

**Edits needed:**
1. **No substantive changes.** Content is solid.
2. **Optional clarification:** In the section "HUD as SOI in A-A and HMCS Capabilities," consider adding one sentence:
   > "Consequently, DMS Up (which designates HUD as SOI) is ineffective in A-A master mode; the pilot must manage SOI exclusively via DMS Down (MFD-to-MFD toggle)."
   
   This primes the reader for 4.2.1 content.

3. **Copyedit:** Minor grammar pass (non-critical).

**Integration into guide.tex:**
- This section becomes **4.1** (unchanged).
- Extract content from WIP preamble, keep narrative and table.
- Status: move to ARCHIVE as `section-C4-S1-concept-soi-final-approved-2026-01-14.tex`.

---

### 2.2 C4-S2 (DMS Up/Down) — Status: REFACTOR & SPLIT

**Current file:** `section-C4-S2-dms-up-down-review-2026-01-13.tex`

**Assessment:**
- ✅ DMS Up content (4.2.1) is well-written and detailed.
- ✅ DMS Down content (4.2.2) is solid with good toggle logic explanations.
- ✅ HOTAS tables are properly formatted (hotastable environment).
- ❌ Some redundancy with C4-S1 (master mode rules explained twice).
- ❌ Exception states (Snowplow, MARK/OFLY) are scattered; should consolidate.
- ❌ Lacks Left/Right content (those should be separate).

**Refactoring strategy:**

**Step 1: Reduce redundancy with C4-S1**
- In 4.2.1 (DMS Up), remove detailed re-explanation of "HUD can be SOI only in NAV/A-G."
- Instead, use forward-reference: "See Table 4.1.x for valid SOI displays by master mode."
- Shorten narrative by ~20-30%, keeping examples and scenarios.

**Step 2: Consolidate exception states**
- Currently, Snowplow/MARK/OFLY appear in 4.2.1 and 4.2.2 subsections.
- **Create single 4.2.5 subsection** for all exception states (Snowplow, MARK/OFLY).
- Remove from 4.2.1 and 4.2.2; add cross-reference: "See Section 4.2.5 for exception states."

**Step 3: Keep DMS Up and DMS Down tables**
- Table 4.2.1 (DMS Up) — keep, ensure it's in correct hotastable format.
- Table 4.2.2 (DMS Down toggle logic) — refine slightly; ensure clarity on master mode cycling behavior.

**Result after refactoring:**
- Narrative for 4.2.1: ~1,200–1,500 words (down from ~2,000).
- Narrative for 4.2.2: ~1,500–2,000 words (down from ~2,500).
- Total 4.2.1 + 4.2.2: ~2,700–3,500 words (much leaner).

**Integration into guide.tex:**
- 4.2.1 and 4.2.2 extracted from refactored C4-S2.
- Keep original HOTAS tables, verify they fit final chapter layout.
- Status: move refactored version to ARCHIVE as `section-C4-S2-dms-up-down-final-2026-01-14.tex`.

---

### 2.3 C4-S3 (DMS Format Cycling) — Status: REWRITE & INTEGRATE

**Current file:** `section-C4-S3-dms-format-cycling-dev-2026-01-13.tex`

**Assessment:**
- ❌ Status is "dev" — incomplete and likely not aligned with direction-based structure.
- ❌ Needs full review against final architecture.
- ✅ Conceptually, format cycling is the right content for Left/Right.

**Action:**
- **Do not use existing C4-S3 as-is.** Instead, create new WIP file for 4.2.3 (DMS Left/Right).
- Learn from C4-S3 structure if useful, but rewrite from scratch per the blueprint below.

---

## Part 3: New Content Needed (Not in C4-S1 or C4-S2)

### 3.1 Section 4.2.2 — DMS Down (Needs Full Development)

**Current status:** Partially in C4-S2; needs extraction and minor refinement.

**Target word count:** 1,500–2,000 words (narrative) + HOTAS table.

**Content outline:**

**4.2.2.1 Core Logic (toggle mechanics)**
- Explain the three possible SOI states: HUD, Left MFD, Right MFD.
- Show the transition logic:
  - From HUD → moves to one MFD.
  - From one MFD → moves to other MFD.
  - From final MFD → may return to HUD (if available) or loop back.
- Master mode determines: "Can HUD be part of the cycle?" (Yes in NAV/A-G, No in A-A/DGFT).

**4.2.2.2 Toggle Patterns by Master Mode (brief overview)**
- NAV: full cycle including HUD.
- A-G PRE/VIS: full cycle including HUD.
- A-A/DGFT/MSL OVRD: MFD-only toggle (no HUD).
- Table reference: "See Table 4.2.x for detailed master mode behavior."

**4.2.2.3 Practical Scenarios**
- Rapid sensor toggle in NAV (HUD nav → FCR check → HSD status → HUD).
- MFD-only toggle in A-A (FCR ↔ HSD for threat assessment).
- A-G VIS HUD-to-WPN transition (visual cueing → weapon status → back to visual).

**HOTAS Table 4.2.2:**
- Columns: State (master mode), Dir (Down), Act (Short), Function, Effect/Nuance, Dash34, Train.
- Rows: One row per master mode showing toggle behavior.
- Example rows:
  ```
  NAV | Down | Short | Toggle SOI | Cycles HUD ↔ Left MFD ↔ Right MFD ↔ HUD (repeating) | §2.1.1.2.3 | TRN 1,4,5
  A-A | Down | Short | Toggle SOI | Cycles Left MFD ↔ Right MFD; HUD not available | §2.1.1.2.3 | TRN 17,18
  ```

---

### 3.2 Section 4.2.3 — DMS Left / Right (NEW, Needs Full Development)

**Current status:** Partial in C4-S3 (dev status); needs rewrite and alignment.

**Target word count:** 1,200–1,500 words (narrative) + HOTAS table.

**Content outline:**

**4.2.3.1 Format Cycling Mechanics (unified)**
- DMS Left cycles the **left MFD** formats (primary → secondary → tertiary → wrap).
- DMS Left cycles the **right MFD** formats (primary → secondary → tertiary → wrap).
- **Blank formats are skipped** (Dash-34 §2.1.6.10).
- **Independent of SOI**: You can cycle Left/Right without affecting which display is SOI.

**4.2.3.2 Available Formats by Master Mode**
- Explain that each master mode has a predefined set of available formats per MFD slot.
- Reference Dash-34 master mode display format table.
- Example:
  - NAV: Left MFD might have [FCR, TGP, HSD]; Right MFD might have [SMS, WPN, HSD].
  - A-A: Left MFD might have [FCR]; Right MFD might have [SMS, HSD].
  - A-G: Left MFD might have [FCR, TGP, HAD]; Right MFD might have [WPN, TGP, SMS].
- Note: The specific set varies by DTC configuration and master mode.

**4.2.3.3 Left/Right Does Not Affect SOI**
- Critical clarification: You can cycle formats on one MFD while SOI is on another.
- Example:
  - SOI is on Left MFD (FCR).
  - You press DMS Right to cycle Right MFD formats.
  - Right MFD changes format, but SOI remains on Left MFD (FCR).
  - This independence is the key to efficient cockpit management.

**4.2.3.4 Practical Scenarios**
- Rapid format access without menu navigation (using DMS Left/Right instead of OSBs).
- Transitioning from radar to targeting pod without moving SOI.
- Accessing weapon pages (WPN) and HARM attack pages (HAD) via format cycling.

**HOTAS Table 4.2.3:**
- Columns: State (master mode), Dir (Left / Right), Act (Short, Repeated), Function, Effect/Nuance, Dash34, Train.
- Rows: Show Left and Right behavior (likely identical per master mode, but listed separately for clarity).
- Example rows:
  ```
  NAV | Left  | Short Rptd | Cycle left MFD formats | Rotates primary → secondary → tertiary; blanks skipped | §2.1.6.2 | TRN 1,4
  NAV | Right | Short Rptd | Cycle right MFD formats | Rotates primary → secondary → tertiary; blanks skipped | §2.1.6.2 | TRN 1,4
  A-A | Left  | Short Rptd | Cycle left MFD formats | Limited formats in A-A (FCR); cycling has minimal effect | §2.1.6.2 | TRN 17,18
  ```

---

### 3.3 Section 4.2.4 — Integration with TMS (Brief Overview, NEW)

**Current status:** None (was conceptually part of old "4.4").

**Target word count:** 400–500 words (narrative only, no table).

**Purpose:** Bridge between DMS and TMS without duplicating detailed weapon procedures.

**Content outline:**

**4.2.4.1 How DMS and TMS Interact**
- Foundational principle: DMS selects SOI; TMS acts upon SOI.
- One-paragraph explanation:
  > "DMS determines which display is the Sensor of Interest (SOI). TMS always acts upon the current SOI. Therefore, changing SOI via DMS directly changes what TMS does. This coupling is operationally critical in several sensor and weapon contexts. For example, in AGM-65 Visual mode, the HUD must be SOI (via DMS Up) for TMS Down to reject the target. Without HUD as SOI, TMS Down acts on the WPN or TGP display instead, and the rejection fails."

**4.2.4.2 Five Critical Contexts (2–3 sentences each, no deep procedural detail)**
- **AGM-65 VIS:** HUD must be SOI via DMS Up for target rejection (TMS Down).
- **HARM POS/HAD:** HAD must be SOI via DMS Down for threat selection (TMS Up/Right).
- **Link 16 PDLT:** HSD must be SOI via DMS Down for PDLT creation (TMS Up).
- **DTOS/CCIP Visual:** HUD must be SOI via DMS Up for TMS-based designation.
- **IAM PRE (TGP → WPN):** WPN must be SOI via DMS Down for seeker refinement (TMS + Cursor).

Each bullet includes:
- What must be SOI (via DMS).
- What TMS does when SOI is correct.
- Brief consequence if DMS step is skipped.

**4.2.4.3 Forward Reference**
> "For detailed weapon employment procedures involving DMS and TMS, refer to TMS Chapter 3, Section 3.5 (TMS in Weapon Employment). This section describes complete procedures for each weapon system and when DMS SOI management is critical."

---

### 3.4 Section 4.2.5 — Exception States & Operational Notes (Consolidate & Expand)

**Current status:** Scattered in C4-S2; needs consolidation.

**Target word count:** 600–800 words (narrative) + no separate table.

**Content outline:**

**4.2.5.1 Snowplow (SP) PRE State (Unstabilized)**
- When A-G radar enters Snowplow mode, SOI is "nowhere."
- DMS Up/Down are **ineffective** until SP position is stabilized via TMS Up.
- Brief explanation of why (SP is a specialized ground-stabilization mode; SOI waits for pilot action).
- Reference: Dash-34 §4.2.1.4.

**4.2.5.2 MARK / OFLY Submode**
- In certain marking/overfly contexts, SOI cannot be designated.
- DMS commands are ignored.
- Rare occurrence; mention for completeness.

**4.2.5.3 Operational Notes**
- **Rapid SOI switching:** Pilots often cycle DMS Down repeatedly during dynamic situations (radar check, sensor switch, weapon status). Practice makes it smooth.
- **SOI and workload:** Designating the correct SOI reduces head-down time and menu navigation.
- **Block/variant note:** DMS behavior is identical across all F-16 blocks (see Section 4.1).

---

## Part 4: HOTAS Table Architecture

### 4.1 Table per Direction (Not per Master Mode)

**Rationale:**
- Each direction (Up, Down, Left, Right) has a **unified rule** that applies across all master modes.
- Master mode determines **availability** (constraint), not **the rule itself**.
- This mirrors Dash-34's directional nomenclature.

**Table layout:**

| State | Dir | Act | Function | Effect / Nuance | Dash34 | Train |
|-------|-----|-----|----------|-----------------|--------|-------|
| (Master Mode) | (Direction) | (Short/Long/Rptd) | (Informal title) | (1–3 sentences explanation + master mode variations) | (§ref) | (TRN list) |

**Example for DMS Up:**
```
NAV | Up | Short | Designate HUD as SOI | DMS Up designates HUD as SOI (asterisk on HUD). In NAV, this is fully effective. | §2.1.1.2.3 | TRN 1,4,5
A-G | Up | Short | Designate HUD as SOI | DMS Up designates HUD as SOI. In A-G modes, this is fully effective and often mandatory (especially in VIS modes for target control). | §2.1.1.2.3 | TRN 10-15
A-A | Up | Short | (No Effect) | DMS Up is ineffective in A-A master mode. HUD cannot be SOI; pilot must manage SOI via DMS Down (MFD-only toggle). | §2.1.1.2.3 | —
DGFT | Up | Short | (No Effect) | Same as A-A: HUD not available as SOI; DMS Up has no effect. | §2.1.1.2.3 | —
```

### 4.2 Summary Table (Optional End-of-Chapter Reference)

**Purpose:** Readers who want "all DMS at a glance" can consult one comprehensive table.

**Format:** Single table (possibly multi-page longtable) with **all directions × all master modes**.

**Usage:** Reference lookup, not primary learning tool. Primary tables (per section) are the source of truth.

---

## Part 5: What the Complete Chapter 4 Should Contain

### 5.1 Minimum Required Content

| Element | Where | Word Count | Status |
|---------|-------|-----------|--------|
| **Conceptual foundation (SOI definition, visual indicators, master mode constraints)** | 4.1 | 1,500–2,000 | Existing (C4-S1) |
| **DMS Up explanation (function, effectiveness, scenarios, HOTAS table)** | 4.2.1 | 1,200–1,500 | Existing (C4-S2, needs trim) |
| **DMS Down explanation (toggle logic, master mode behavior, scenarios, HOTAS table)** | 4.2.2 | 1,500–2,000 | Partial (C4-S2, needs extraction) |
| **DMS Left/Right explanation (format cycling, independence from SOI, scenarios, HOTAS table)** | 4.2.3 | 1,200–1,500 | None (needs new WIP) |
| **DMS + TMS integration (brief overview, 5 critical contexts, forward reference to TMS)** | 4.2.4 | 400–500 | None (needs new WIP) |
| **Exception states and operational notes (Snowplow, MARK/OFLY, rapid switching)** | 4.2.5 | 600–800 | Partial (C4-S2, needs consolidation) |
| **HOTAS summary table (all directions × master modes, optional)** | End | Varies | New table |

**Total chapter word count:** ~7,000–8,500 words narrative + 4 HOTAS tables.

### 5.2 What Should NOT Be in Chapter 4

- ❌ Detailed weapon employment procedures (AGM-65, HARM, IAM, DTOS at procedure level).
- ❌ Block/variant notes section (unnecessary per C4-S1 statement).
- ❌ Large "Integration with TMS" section (only brief overview in 4.2.4; detailed procedures in TMS Chapter 3).
- ❌ Repetition of master mode rules (reference C4-S1 instead).

---

## Part 6: WIP File Roadmap (What to Create/Refactor)

### 6.1 Files to Archive (No Changes Needed)

| File | Status | Action |
|------|--------|--------|
| `section-C4-S1-concept-soi-review-2026-01-13.tex` | FINAL | Archive as `section-C4-S1-concept-soi-final-2026-01-14.tex` (minimal copyedit). Extract to 4.1 in guide.tex. |

### 6.2 Files to Refactor (Extract, Trim, Split)

| File | Extract To | Changes | New Status |
|------|-----------|---------|------------|
| `section-C4-S2-dms-up-down-review-2026-01-13.tex` | 4.2.1 + 4.2.2 | Trim redundancy with C4-S1 (~20-30%); consolidate exceptions to 4.2.5; keep HOTAS tables. | `section-C4-S2-dms-up-down-final-2026-01-14.tex` |

### 6.3 Files to Create (New WIP)

| Section | File Name (Proposed) | Content | Status | Target |
|---------|---------------------|---------|--------|--------|
| 4.2.3 | `section-C4-S2-dms-left-right-dev-2026-01-14.tex` | DMS Left/Right format cycling (new WIP, from scratch) | dev | 4.2.3 |
| 4.2.4 | `section-C4-S2-dms-tms-integration-dev-2026-01-14.tex` | DMS + TMS brief overview (new WIP) | dev | 4.2.4 |
| 4.2.5 | (Consolidate in refactored C4-S2) | Exception states and operational notes | part of final C4-S2 | 4.2.5 |

---

## Part 7: Integration Workflow

### 7.1 Phase 1: Prepare Existing Files (This Week)

1. **C4-S1:** Copyedit only. Add one clarifying sentence on DMS Up in A-A (optional).
   - Status: review → final
   - Archive as `section-C4-S1-concept-soi-final-2026-01-14.tex`

2. **C4-S2:** Refactor in place.
   - Remove redundancy with C4-S1.
   - Consolidate exception states.
   - Keep HOTAS tables (verify format).
   - Status: review → dev (refactoring in progress)

### 7.2 Phase 2: Create New WIP Files (Mid-next week)

1. **C4-S2 DMS Left/Right (4.2.3):** New WIP file.
   - Write from scratch per outline in Part 3.2.
   - Create HOTAS table for Left/Right.
   - Status: dev

2. **C4-S2 DMS+TMS Integration (4.2.4):** New WIP file.
   - Write brief overview per outline in Part 3.3.
   - No table, narrative only.
   - Status: dev

### 7.3 Phase 3: Consolidate and Finalize (End of next week)

1. Refactored C4-S2 → move to ARCHIVE, status final.
2. New WIP files → review for consistency, then status final.
3. Extract all content into guide.tex as sections 4.1–4.2.5.
4. Create optional summary HOTAS table (4.2 end).
5. Update version macro in guide.tex (likely v0.3.1.0 or similar).

---

## Part 8: Critical Points for Success

### 8.1 Maintain Direction-Based Organization

- Every section (4.2.1–4.2.5) is about **what a DMS input does**, not about **a master mode context**.
- Master modes appear as **constraints**, never as organizational dividers.
- This keeps the chapter lean and focused.

### 8.2 Avoid Redundancy

- C4-S1 is authoritative for master mode × valid SOI rules. Reference, don't repeat.
- Exception states belong in one place (4.2.5).
- DMS + TMS integration is brief; weapon-specific procedures belong in TMS Chapter 3.

### 8.3 Leverage Existing High-Quality Content

- C4-S1 is excellent; keep it.
- C4-S2 DMS Up/Down content is solid; trim and refactor, don't rewrite.
- Build only new sections (Left/Right, DMS+TMS overview, consolidated exceptions).

### 8.4 HOTAS Tables Are Single Source of Truth

- Each table (4.2.1, 4.2.2, 4.2.3) shows **all master modes for that direction**.
- No separate summary table is needed during development (optional at the end for reference).
- Consistency check: every direction should have one table covering all modes.

---

## Conclusion

This blueprint delivers a **focused, direction-based Chapter 4** that:
- ✅ Uses existing C4-S1 and C4-S2 with minimal refactoring.
- ✅ Organizes by physical direction (Up/Down/Left/Right), not master mode.
- ✅ Keeps DMS complete and coherent without sprawling into weapon-specific detail.
- ✅ Leaves weapon procedures to TMS Chapter 3.
- ✅ Totals ~7,000–8,500 words + 4 HOTAS tables.
- ✅ Ready for pilot understanding: "What does each DMS direction do?"
