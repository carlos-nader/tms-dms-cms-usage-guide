# DASH-34 4.3 MFDS DISPLAY FORMATS - RESEARCH FOUNDATIONS

## SOURCE: TO 1F-16CMAM-34-1-1 BMS (Section 2.1.6.2 - TYPICAL MFDS FUNCTIONS)

### KEY FACTS EXTRACTED DIRECTLY FROM DASH-34

#### 1. FORMAT SLOTS PER MFD
- **Total:** 3 format slots per MFD
- **Structure:** 1 PRIMARY + 2 SECONDARY formats
- **Naming:** Primary format is HIGHLIGHTED; the two secondary formats are shown adjacent
- **Control:**
  - OSB next to secondary format name → makes it PRIMARY
  - DMS left/right → changes PRIMARY format (alternative method)
  - **Selection order: "from inside to outside"** [CRITICAL - need to verify what this means exactly]

#### 2. MASTER MENU & FORMAT CHANGING
- **Access:** Press OSB next to PRIMARY (highlighted) format name → opens MASTER MENU
- **Selection:** Press OSB next to desired format on menu → that format becomes new PRIMARY, **replacing the previous primary format**
- **Pilot Can Change In-Flight:** YES - via master menu access (in-flight format configuration is available)

#### 3. CONSTRAINT: NO DUPLICATE FORMATS
- Out of **6 available formats total** (3 on each MFD)
- **No two can be the same** (exception: BLANK formats or TEST formats during BIT)
- **Auto-substitution rule:** If a format selected from master menu already exists on the other 5 slots → **BLANK format is used instead**

#### 4. DMS RELATIONSHIP WITH PRIMARY FORMAT CYCLING - ✅ CLARIFIED
- **DMS left/right changes PRIMARY format ONLY** (from inside to outside cycling order)
- **"The selection of formats is done from inside to outside"**
- This refers to the **cycling pattern** when using DMS: PRIMARY → middle format → third format → PRIMARY (circular)
- Alternative to using OSB at bottom of MFDS
- **BLANK formats are SKIPPED in DMS cycling** (section 2.1.6.10)

#### 5. 16 AVAILABLE FORMATS (FROM TABLE IN 2.1.6.2)
Video/Text formats:
- FLIR (Navigation Pod) - Video/Text
- FLCS (Digital Flight Control System) - Text
- HAD (HARM Attack Display) - Text
- HSD (Horizontal Situation Display) - Text
- TEST - Text
- DTE (Data Transfer Equipment) - Text
- SMS (Stores Management System) - Text
- WPN (Weapon: AGM-65, AGM-88, etc.) - Video/Text
- FCR (Fire Control Radar) - Video/Text
- TGP (Targeting Pod) - Video/Text
- TCN (TACÁN Format) - Text
- TFR (Navigation Pod Terrain Following Radar) - Video/Text
- BLANK - None/Text

#### 6. SWAP FUNCTION (Section 2.1.6.9) - ✅ REVIEWED
**The MFDS include a feature that allows the exchange of displays between the two MFDs.**
- By depressing the **SWAP OSB** on **either MFD**, the information displayed on the **left MFD is swapped with that of the right MFD**
- Includes **both video and text data**
- This is a **MASTER MFD FEATURE** (exchanges between physical left/right MFDs, not within one MFD)

#### 7. BLANK FORMAT (Section 2.1.6.10) - ✅ REVIEWED
- **Can be manually selected** by depressing OSB next to a secondary blank format slot
- When blank slot is selected, it shows **blank format display** and highlights the **primary format label position**
- When blank mnemonic is displayed in secondary slot, **no text is shown** (empty label)
- **Any blank formats will be SKIPPED when using DMS left or right**
- This means: pilot can create a "dormant" slot by selecting BLANK, but won't cycle to it via DMS

#### 8. DTE CONFIGURATION
- **Pre-flight:** Master mode and format configurations programmed via DTC (Data Transfer Cartridge) during mission planning
- **In-flight:** Pilot can change formats via master menu (OSBs 14/15/16)
- **DTE Page (Section 2.1.6.13):** Allows loading DTC data, including MSMD (Master Mode Initialization)
- **Persistence:** Changes made in-flight are saved (section 2.1.1.2.1 states "Upon exiting the current master mode, the last master mode table is updated with any changes that have been made")

---

## RESEARCH COMPLETION STATUS ✅
**All critical sections reviewed. Ready to write section 4.3.**

### What WAS Researched:
- ✅ 2.1.6.2 TYPICAL MFDS FUNCTIONS (primary source)
- ✅ 2.1.6.3 SENSOR OF INTEREST (SOI)
- ✅ 2.1.6.4 SELECT OPTIONS
- ✅ 2.1.6.5 INCREMENT/DECREMENT
- ✅ 2.1.6.6 DATA ENTRY AND RECALL
- ✅ 2.1.6.7 MENU PAGE
- ✅ 2.1.6.8 OFF FORMAT
- ✅ 2.1.6.9 SWAP DISPLAYS ← KEY FINDING
- ✅ 2.1.6.10 BLANK FORMAT ← KEY FINDING

### What WAS NOT Reviewed (Not Critical for 4.3):
- Master mode display format table (not required for general MFDS explanation)
- Individual format pages (2.1.6.11+) - those go in dedicated format sections
- Sensor availability constraints - BMS-specific, not relevant to general UI mechanics

---

## KEY INSIGHTS FOR SECTION 4.3:

### UI/UX Pattern Recognition:
1. **Format Selection Hierarchy:**
   - OSB direct selection (quickest)
   - DMS left/right with cycling (fast)
   - Master menu access (full choices)

2. **No Duplicates Rule:**
   - Enforces clean display architecture
   - BLANK format used as escape valve
   - Auto-substitution on import conflicts

3. **SOI Concept:**
   - Links hands-on controls to ONE sensor
   - Visual indication on MFD (box border) and HUD (asterisk)
   - DMS up/down toggles SOI location

4. **BLANK Format Utility:**
   - Can be manually selected
   - Skipped in DMS cycling
   - Allows pilots to "reserve" a slot without viewing it
