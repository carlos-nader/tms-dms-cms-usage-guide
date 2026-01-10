# TRAINING MISSION REFERENCE TABLE v1.0
## TMS/DMS/CMS Usage Guide — Standardized Abbreviations

**Document Type:** Reference Standard  
**Version:** 1.0  
**Created:** 10 January 2026  
**Scope:** TMS/DMS/CMS Usage Guide Project  
**Effective Date:** 10 January 2026  

---

## PURPOSE

This document establishes standardized abbreviations for all 33 BMS 4.38.1 training missions. It serves as the authoritative reference for populating the **Train (Column 7)** column in all HOTAS tables throughout the Falcon BMS TMS/DMS/CMS Usage Guide (guide.tex v0.2.2.0 and beyond).

The abbreviations in this table are designed to:

1. **Fit within column width constraints** (1.4 cm, `\small` font, `\arraystretch = 1.25`)
2. **Maintain clarity and readability** across all table contexts
3. **Ensure consistency** in training mission references throughout the document
4. **Follow industry and BMS community standards** for acronym usage

---

## INTEGRATION

This document is adopted as a referente for the TMS/DMS/CMS Usage Guide project. It is referenced in:

- **briefing document**

Any modifications to mission abbreviations must be:
1. Reviewed by the project author
3. Documented in version control with change notes

---

## MACRO AND SYNTAX STANDARD

All training mission references shall use the LaTeX macro defined in guide.tex and the briefing document:

```latex
\newcommand{\trnref}[1]{BMS Training Mission~#1}
```

**Required Format:**

```latex
\trnref{XX (ABBREVIATION)}
```

Where:
- **XX** = Training mission number (1–28, including variants A/B/C/D)
- **ABBREVIATION** = Short form from this table (1–3 words)

**Examples:**
```latex
\trnref{1 (Ground Ops)}      % Single mission
\trnref{4D (AAR)}            % Mission with variant
\trnref{28 (SEAD-EW)}        % Mission with hyphenated concept
\trnref{9 (Failures)}, \trnref{28 (SEAD-EW)}  % Multiple missions
```

---

## TRAINING MISSION REFERENCE TABLE

| # | Full Mission Name | Standardized \trnref{} Format | Rationale |
|---|---|---|---|
| 1 | MISSION 1: GROUND OPS | `\trnref{1 (Ground Ops)}` | Core topic: ground operations, ramp start, taxi, takeoff. |
| 2 | MISSION 2: BASIC NAVIGATION | `\trnref{2 (Navigation)}` | Navigation (INS, TACAN) is primary; "basic" is understood. |
| 3 | MISSION 3: LANDING | `\trnref{3 (Landing)}` | Single word sufficient; landing procedures only. |
| 4A | MISSION 4A: FORMATIONS | `\trnref{4A (Formations)}` | Formation types and procedures. Variant 4A explicit. |
| 4B | MISSION 4B: TACTICAL TURNS | `\trnref{4B (Tactical Turns)}` | Two-ship tactical turns. Keep "Tactical" for distinction. |
| 4C | MISSION 4C: HARTS | `\trnref{4C (HARTS)}` | Single acronym; no abbreviation needed. |
| 4D | MISSION 4D: AIR TO AIR REFUELING | `\trnref{4D (AAR)}` | Industry standard: Air-to-Air Refueling → AAR. Compact. |
| 5 | MISSION 5: ILS LANDING AT NIGHT | `\trnref{5 (ILS Night)}` | Two words: focus on ILS system + night environment. |
| 6 | MISSION 6: ILS LANDING IN BAD WEATHER | `\trnref{6 (ILS Weather)}` | Two words: ILS system + adverse weather context. |
| 7 | MISSION 7: FLAMEOUT LANDING | `\trnref{7 (Flameout)}` | Single word; flameout recovery is the scenario. |
| 8 | MISSION 8: LOW LEVEL NAVIGATION - TFR – FLIR | `\trnref{8 (TFR/FLIR)}` | Core systems: Terrain Following Radar + FLIR. Two acronyms, essential. |
| 9 | MISSION 9: IN-FLIGHT FAILURES | `\trnref{9 (Failures)}` | Single word; controlled failures scenario. |
| 10 | MISSION 10: AIR TO GROUND GENERAL PURPOSE BOMBS | `\trnref{10 (GP Bombs)}` | Two words: GP (general purpose) bombs are the weapon type. |
| 11 | MISSION 11: LASER GUIDED BOMBS | `\trnref{11 (LGB)}` | Industry standard acronym: Laser Guided Bomb → LGB. |
| 12 | MISSION 12: AGM-88 HARMS | `\trnref{12 (HARM)}` | AGM-88 is the missile; HARM is the mode. Single word. |
| 13 | MISSION 13: AGM-65 MAVERICKS - Basic | `\trnref{13 (Maverick)}` | Single word; AGM-65 Maverick system. "Basic" is understood from variant. |
| 14 | MISSION 14: AGM-65 MAVERICKS – Advanced | `\trnref{14 (Maverick Advanced)}` | Two words: clarify advanced techniques beyond Mission 13. |
| 15 | MISSION 15: INERTIALLY AIDED MUNITIONS | `\trnref{15 (IAM)}` | Industry standard acronym: Inertially Aided Munition → IAM. Single. |
| 16 | MISSION 16: SPICE | `\trnref{16 (SPICE)}` | Single acronym; weapon type identifier. |
| 17A | MISSION 17A: IR MISSILES - Intercept | `\trnref{17A (IR Intercept)}` | IR (infrared) missiles; intercept scenario. Two words. |
| 17B | MISSION 17B: IFF - Intercept | `\trnref{17B (IFF)}` | Identification Friend/Foe; single acronym. Intercept understood. |
| 17C | MISSION 17C: IDM – LINK 16 | `\trnref{17C (IDM/L16)}` | Two systems: Intra-flight Data Link (IDM) + LINK 16. Slashed for compactness. |
| 18 | MISSION 18: RADAR MISSILES – BARCAP | `\trnref{18 (BARCAP)}` | Combat air patrol mission type. Single word acronym. |
| 19 | MISSION 19: GUN & HMCS/AIM-9X | `\trnref{19 (Gun/HMCS)}` | Two primary topics: gun employment + Helmet Mounted Cueing System. Slashed. |
| 20 | MISSION 20: AGM-84A HARPOON | `\trnref{20 (Harpoon)}` | Single word; AGM-84A Harpoon missile system. |
| 21 | MISSION 21: NAVIGATION FLIGHT OSAN-DAEGU: Part 1 | `\trnref{21 (Nav Osan-Daegu)}` | Two words: navigation type + route identifier. |
| 22 | MISSION 22: NAVIGATION FLIGHT OSAN-DAEGU: Part 2 | `\trnref{22 (Nav Osan-Daegu)}` | Continuation of TRN 21; same abbreviation. |
| 23 | MISSION 23: CARRIER OPS - Launch (F/A-18D) | `\trnref{23 (Carrier Launch)}` | Two words: carrier operations + launch phase. F/A-18D implicit. |
| 24 | MISSION 24: CARRIER OPS - CASE 1 RECOVERY (F/A-18C) | `\trnref{24 (Case 1 Recovery)}` | Two words: CASE 1 recovery type. Carrier ops understood. |
| 25 | MISSION 25: CARRIER OPS - CASE 3 RECOVERY (F/A-18C) | `\trnref{25 (Case 3 Recovery)}` | Two words: CASE 3 recovery type (adverse weather variant of CASE 1). |
| 26 | MISSION 26: CARRIER OPS – VERTICAL OPS (AV-8B) | `\trnref{26 (Vertical Ops)}` | Two words: vertical takeoff/landing operations (AV-8B Harrier). |
| 27 | MISSION 27: JTAC | `\trnref{27 (JTAC)}` | Single acronym: Joint Tactical Air Controller. Industry standard. |
| 28 | MISSION 28: SEAD-EW | `\trnref{28 (SEAD-EW)}` | Two linked mission types: SEAD (Suppression Enemy Air Defense) + EW (Electronic Warfare). Keep hyphenated. |

---

## APPLICATION RULES

### Single Mission Reference
```latex
CMDS AUTO & Aft & Short & Enable AUTO & ... & \dashref{2.7.2.1} & \trnref{28 (SEAD-EW)} \\
```

### Multiple Mission References (Maximum 2–3 per cell)
```latex
% Two missions:
ECM Pod & Aft & Short & Enable ECM & ... & \dashref{2.7.4.2.5} & \trnref{28 (SEAD-EW)}, \trnref{12 (HARM)} \\

% Three missions:
CMDS MAN & Up & Short & Execute Program & ... & \dashref{2.7.2.2} & \trnref{9 (Failures)}, \trnref{28 (SEAD-EW)}, \trnref{12 (HARM)} \\
```

### No Direct Mission Applicable
```latex
% Option 1: Leave blank
TMS Up & Short & ... & Designate target & ... & \dashref{...} &  \\

% Option 2: Mention closest mission in Effect/Nuance column
TMS Up & Short & ... & Designate target & Applicable in air-to-air contexts; see TRN 18 (BARCAP) & \dashref{...} &  \\
```

### Variant Missions (Always Include Letter)
```latex
% Correct:
\trnref{4A (Formations)}    ✅
\trnref{17B (IFF)}          ✅

% Incorrect:
\trnref{4 (Formations)}     ❌ Missing variant
\trnref{17 (IFF)}           ❌ Missing variant
```

---

## INTEGRATION WITH HOTAS TABLES

The Train column in all `hotastable` environments shall use this table exclusively.

**Column Specifications (from briefing-v0.2.0.1.md, Section 4.2):**

| Parameter | Value |
|---|---|
| Column Width | 1.4 cm (architecture-locked) |
| Font Size | `\small` (10 pt) |
| Row Height | `\arraystretch = 1.25` |
| Maximum Entries Per Cell | 2–3 missions |
| Separator (Multiple Entries) | Comma + space (`,`) |

---

## SPECIAL CASES AND CONVENTIONS

### Missions with Variants (4A, 4B, 4C, 4D, 17A, 17B, 17C)

Variant letters are **required** in all references. These represent distinct missions in the training progression and must not be omitted or consolidated.

### Two-Part Continuous Missions (21 & 22)

Missions 21 and 22 form a continuous navigation flight (Osan-Daegu, Part 1 and Part 2). Both use the same abbreviation (`\trnref{21 (Nav Osan-Daegu)}` and `\trnref{22 (Nav Osan-Daegu)}`) to indicate progression and continuity.

### Carrier Operations Missions (23–26)

Each carrier operations mission represents a distinct phase and aircraft type:
- TRN 23: Carrier launch (F/A-18D)
- TRN 24: CASE 1 recovery (F/A-18C)
- TRN 25: CASE 3 recovery (F/A-18C)
- TRN 26: Vertical operations (AV-8B)

Abbreviations emphasize the **operational difference**. Aircraft type is implicit in table context and not repeated in the abbreviation.

### Hyphenated Concepts (TRN 8, TRN 19, TRN 28)

Missions covering **two linked systems or concepts** use slashed notation (e.g., `TFR/FLIR`, `Gun/HMCS`, `SEAD-EW`) to indicate integration or dual focus. These are treated as single, unified abbreviations, not separate references.

---

## DOCUMENT CONTROL

| Version | Date | Change | Author |
|---|---|---|---|
| 1.0 | 10 Jan 2026 | Initial release. All 28 documented missions from BMS Training Manual 4.38.1 included. Abbreviations validated against column width constraints and approved for integration into project governing documents. | Project Author |

---

## CONFORMANCE

All future WIP files (section-C*-S*.tex) that populate HOTAS tables must conform to the abbreviations and format specified in this document.

---

**Document Reference:** training-mission-abbrev-table.md  
**Project:** TMS/DMS/CMS Usage Guide  
**Author:** Carlos "Metal" Nader (Project Author)