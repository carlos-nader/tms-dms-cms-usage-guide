# SECTION 4.3 REWRITE PLAN

## Status: READY TO WRITE ✅

**Source Documents Reviewed:**
- Dash-34 sections 2.1.6.2, 2.1.6.3, 2.1.6.9, 2.1.6.10
- Core MFD mechanics established

---

## RECOMMENDED STRUCTURE FOR 4.3

### 1. **OPENING CONTEXT** (Brief)
- What the MFDS is (left/right displays, all-purpose)
- Why format selection matters (mission-critical)
- Quick architecture preview (6 slots total, 3 per MFD, no duplicates)

### 2. **PRIMARY CONCEPT: FORMAT SLOTS**
- Define the 3-slot architecture per MFD
  - 1 PRIMARY (highlighted, always visible)
  - 2 SECONDARY (alternative quick-select options)
- Explain the "inside to outside" cycling principle
- Show the 16 available formats (table from 2.1.6.2)

### 3. **USER ACTIONS: HOW TO CHANGE FORMATS**
Three paths to format selection:

#### **Path A: Direct OSB Selection (Most Precise)**
- Press OSB next to desired secondary format
- That format becomes PRIMARY immediately
- Previous PRIMARY becomes secondary
- **Use case:** Quick tactical switches during flight

#### **Path B: DMS Left/Right (Cycling)**
- DMS left/right cycles through available formats
- **Cycling order:** PRIMARY → next → next → PRIMARY (circular)
- **BLANK formats are skipped** in the cycle
- Only changes PRIMARY, not secondary slots
- **Use case:** Rapid cycling without menu access

#### **Path C: Master Menu (Full Access)**
- Press OSB next to PRIMARY format name
- Master menu displays all 16 formats
- Select desired format via OSB
- Selected format becomes new PRIMARY
- **Replace rule:** If selected format already in other slots → BLANK used instead
- **Use case:** One-time major format change or recovery

### 4. **SPECIAL CASES**

#### **SWAP Between Left/Right MFDs**
- Press SWAP button on either MFD
- **Both video AND text data exchange** between L/R MFDs
- **Not** a format change, a **display exchange**
- Useful for: tactical reorientation, crew coordination

#### **BLANK Format**
- Can be manually selected in secondary slot
- Displays blank/empty (no symbology)
- **Why use it?** Reserve a slot without active display
- Skipped by DMS cycling (won't accidentally display)
- Auto-used when importing duplicate format

#### **OFF Format**
- Displays when selected format is unavailable/inactive
- Shows "XXX OFF" (e.g., "FLIR OFF")
- Remains until format is deselected

### 5. **CONSTRAINT: NO DUPLICATE FORMATS**
- Rule: No two of 6 slots can have same format
- Exception: BLANK formats and TEST formats during BIT
- Enforcement: Auto-substitution with BLANK on conflicts
- **Implication for pilots:** Plan format layout carefully during pre-flight

### 6. **SENSOR OF INTEREST (SOI) RELATIONSHIP**
- SOI designates which sensor receives hands-on control
- ONE sensor/format has SOI at any time
- Visual indicators:
  - MFD: Box border around SOI format
  - HUD: Asterisk in upper left
- Can have format displayed BUT not SOI (shows "NOT SOI" in center)
- **DMS Up** designates HUD as SOI (if compatible)
- **DMS Down** toggles SOI between MFDs or back to HUD

### 7. **OPERATIONAL WORKFLOW EXAMPLES**

#### **Example 1: Radar-focused mission**
- Primary: FCR (active tracking)
- Secondary 1: HSD (situational awareness)
- Secondary 2: SMS (weapon load check)
- DMS cycles: FCR → HSD → SMS → FCR

#### **Example 2: Tactical reorientation mid-flight**
- Need to swap pilot/WSO display roles
- Press SWAP on either MFD
- Left/Right displays exchange completely

#### **Example 3: Format not available**
- Try to select FLIR format (pod not installed)
- MFD displays "FLIR OFF"
- Format name still shows but no video/text
- Press DMS to cycle past it

---

## KEY WRITING PRINCIPLES

1. **Use Dash-34 language** where possible (already validated against real sim)
2. **Emphasize the "no duplicates" rule** - it's the core constraint
3. **Three paths to selection** - give equal weight (all valid tactics)
4. **Visual examples** - small cockpit sketches showing format slots
5. **Link to SOI concept** (defined in 2.1.6.3) - critical for hands-on control
6. **Operational context** - why pilots care about each method

---

## SECTION OUTLINE (QUICK)

```
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

---

## READY FOR WRITING? 
✅ **YES** - All foundational facts confirmed.  
Next step: Draft section with Dash-34 tables + pilot workflow examples.
