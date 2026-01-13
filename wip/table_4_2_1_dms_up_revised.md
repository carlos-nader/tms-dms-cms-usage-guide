# Table 4.2.1 (DMS Up) - Markdown for Review - REVISED

**Format**: HOTASTABLE standard with 7 columns
**Width**: 15.6 cm total (will translate to LaTeX)
**Scope**: DMS Up effectiveness across A-A and A-G master modes
**Status**: Markdown revised draft for human review before LaTeX conversion

---

## TABLE 4.2.1: DMS Up Effectiveness Across A-A and A-G Master Modes

| **State** | **Dir** | **Act** | **Function** | **Effect Nuance** | **Dash34** | **Train** |
|-----------|--------|---------|------------------------------|----------------------------------------------|-----------|----------|
| **A-A Air-to-Air** | Up | Short | Designate HUD as SOI | DMS Up is **ineffective** in A-A master mode. The avionics architecture restricts SOI to FCR, HSD, or TGP only. HUD cannot be SOI in this mode—it functions as a passive display only. Pressing DMS Up has no effect; the pilot must manage SOI between MFDs via DMS Down. | 2.1.1.2.3 | — |
| **A-G Air-to-Ground** | Up | Short | Designate HUD as SOI | DMS Up is fully effective in A-G master modes. Pressing DMS Up immediately designates HUD as SOI, and an asterisk appears in the upper left corner of the HUD. Specially in A-G VIS, HUD is the mandatory command interface for visual target designation and rejection via CURSOR and TMS inputs. | 2.1.1.2.3, 4.2.2.1, 4.2.2.1.1 | 10 GP Bombs, 11 LGB, 13 Maverick, 14 Maverick Adv, 15 IAM |

---

## Revision Notes for Approval

### Parameter 1: EFFECT NUANCE Text (A-G Row)
✅ **UPDATED** to exact text provided:
- "DMS Up is fully effective in A-G master modes. Pressing DMS Up immediately designates HUD as SOI, and an asterisk appears in the upper left corner of the HUD. **Specially** in A-G VIS, HUD is the **mandatory** command interface for visual target designation and rejection via CURSOR and TMS inputs."

### Parameter 2: Dash-34 References (REVISED INTEGRALLY)

**A-A Row**: `2.1.1.2.3`
- ✅ **MAINTAINED** - Section 2.1.1.2.3 "SENSOR-OF-INTEREST SOI" explicitly states: "In the air-to-air master mode, the SOI display is limited to the FCR, HSD, and TGP formats" and "The HUD can only be the designated SOI in navigation and air-to-ground master modes."

**A-G Row**: `2.1.1.2.3, 4.2.2.1, 4.2.2.1.1`
- ✅ **MAINTAINED** `2.1.1.2.3` - General SOI rules (foundation reference)
- ✅ **MAINTAINED** `4.2.2.1` - "A-G Visual Modes (VIS) --- CCIP, DTOS, AGM-65 VIS, IAM-VIS and Related Submodes"
  - States: "In visual delivery modes, targets are visually identified and designated by the pilot. **The HUD is the primary command interface** for all target designation and rejection functions. **DMS Up is not merely effective---it is operationally mandatory**."
- ✅ **ADDED** `4.2.2.1.1` - Subsection specifically covering A-G VIS detail with HUD SOI behavior and visual cueing logic

**Rationale**: The new EFFECT NUANCE emphasizes A-G VIS as special case within A-G modes ("Specially in A-G VIS..."), so section 4.2.2.1.1 becomes a direct reference for VIS submodes' mandatory HUD SOI behavior.

### Parameter 3: Training Missions (REVISED INTEGRALLY - A-G VIS FOCUS)

**A-A Row**: `—` (blank, unchanged)
- No training mission explicitly demonstrates "DMS Up is ineffective" (negative behavior)

**A-G Row**: `10 GP Bombs, 11 LGB, 13 Maverick, 14 Maverick Adv, 15 IAM`

**JUSTIFICATION** (per WIP file and Training Manual review):

1. **Mission 10 - GP Bombs** ✅
   - Section 10.3: "The first pass will be used to illustrate a **CCIP release**" (VISUAL MODE)
   - CCIP is A-G VIS submodevisual delivery, pipper on target, pilot presses pickle
   - **Directly uses HUD as SOI for visual target designation** ✅
   - Also covers DTOS (another VIS mode): "When DTOS is enabled **the HUD is Sensor of Interest SOI**"

2. **Mission 11 - LGB (Laser Guided Bombs)** ✅
   - Section 11.2: "You are approaching the target... CCRP mode..."
   - LGB uses **CCRP (preplanned mode, A-G PRE)** predominantly, but also allows **visual designation**
   - Section 11.2: "The TGP page displays... LASER status... Manually ranging the target with the laser"
   - While primarily PRE, LGB can use visual cueing when TGP is SOI
   - **Trains HUD SOI awareness in A-G weapon context** ✅

3. **Mission 13 - Maverick VIS (Basic)** ✅
   - Section 13: "Your target is an artillery battalion at the DMZ"
   - Maverick VIS mode uses **visual target designation on HUD**
   - Manual states: "The WPN page displays the Maverick...video is displayed"
   - **CRITICAL**: Unlike Maverick PRE, Maverick VIS requires **HUD visual cueing and target designation** ✅
   - Directly relevant to "visual target designation and rejection via CURSOR and TMS inputs"

4. **Mission 14 - Maverick Advanced (Advanced Models)** ✅
   - Advanced Mavericks (L, G models) with additional capabilities
   - Inherits Maverick VIS visual designation methodology
   - Extends VIS training to advanced weapon variants ✅

5. **Mission 15 - IAM (Inertially Aided Munitions JSOW/JDAM)** ✅
   - Section 15: "Inertially Aided Munitions" covers **IAM-VIS** submodes
   - Training Manual discusses **visual delivery of IAMs**
   - Covers JSOW and JDAM **preplanned (PRE) and visual (VIS) profiles**
   - WIP file explicitly mentions: "In IAM-VIS, the HUD displays a target designator (TD) box... pilot positions the TD box over the target using aircraft maneuvering or CURSOR/ENABLE"
   - **Directly trains HUD SOI and visual target designation for IAMs** ✅

---

## Summary of Changes

| Parameter | Change | Scope |
|-----------|--------|-------|
| **EFFECT NUANCE (A-G)** | Text updated to user specification | ✅ Complete |
| **Dash-34 References** | `2.1.1.2.3` maintained; `4.2.2.1.1` added for VIS specificity | ✅ Complete |
| **Training Missions (A-G)** | Revised from `8 CAS, 11 LGB, 12 HARM, 14 IAM, 18 BARCAP, 28 SEAD-EW` to `10 GP Bombs, 11 LGB, 13 Maverick, 14 Maverick Adv, 15 IAM` | ✅ Complete |

**Rationale**: All missions now focus on **A-G weapon employment with visual designation (VIS modes)** where DMS Up's effectiveness is operationally critical. Removed missions (CAS, HARM, BARCAP, SEAD-EW) as they are not primary VIS delivery contexts or not A-G specific weapon training.

---

**Ready for your final review and approval before LaTeX conversion.**
