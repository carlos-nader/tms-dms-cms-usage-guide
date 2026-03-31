---
description: HOTAS Fundamentals — Sensor of Interest (SOI), Master Modes, and switch overview.
---

# 2. HOTAS Fundamentals

The F-16 HOTAS (Hands On Throttle And Stick) controls consist of switches on the throttle and side-stick controller. The Display Management Switch (DMS), Target Management Switch (TMS), and Countermeasures Management Switch (CMS) — the three HOTAS switches covered in this guide — control display management, sensor management, and defensive systems.

SOI and Master Mode determine how HOTAS inputs are interpreted:

* [**Sensor of Interest (SOI)**](#21-sensor-of-interest-soi): determines which display receives HOTAS inputs.
* [**Master Modes (NAV, A-A, A-G)**](#22-master-modes): define the available weapon systems and sensor configurations.

For the complete HOTAS control reference, see Dash-34 §§ 2.1.1.1.4 and 2.1.5.

## 2.1 Sensor of Interest (SOI)

The F-16 cockpit contains three displays: the Head-Up Display (HUD) and two Multifunction Displays (MFD). The Sensor of Interest (SOI) determines which of these displays currently receives HOTAS inputs. At any moment, _only one_ display can be designated as SOI. The active format on the display determines how the input is interpreted.

### 2.1.1 SOI Fundamentals

The SOI mechanism manages _where_ HOTAS inputs are directed, not _what_ those inputs do. The specific function of a HOTAS input — for example, whether TMS Up designates a target, breaks a track, or cycles through a mode — depends on delivery modes, current Master Mode, and active sensor format.

### 2.1.2 SOI Symbology

SOI designation is indicated by a visual marker on each display:

* **HUD as SOI:** An asterisk symbol (`*`) appears in the upper left corner of the HUD, above the airspeed scale.
* **MFD as SOI:** A border outline is drawn around the edges of the MFD display, forming a box that distinguishes the SOI display from the non-SOI display.
* **NOT SOI indication:** The text `NOT SOI` appears in the center of any SOI-capable MFD format that is not currently designated as SOI. This indicator does not appear on MFD formats that cannot be designated as SOI.

### 2.1.3 SOI-Capable Displays

SOI designation depends on Master Mode and MFD format.

Master Mode determines SOI eligibility. MFD formats can be designated as SOI in all Master Modes. The HUD, however, can be designated as SOI only in NAV and A-G Master Modes.

MFD format determines SOI eligibility _within_ the MFD. Sensor formats that accept targeting and cursor control inputs — such as FCR, TGP, and WPN — can be designated as SOI. Informational and configuration formats, however — such as DTE, TCN, and FLCS — cannot be designated as SOI.

For SOI availability by Master Mode and MFD format, see [Section 3.1](c3-dms.md).

## 2.2 Master Modes

Master Mode defines the active sensor, display, and weapon configuration of the F-16 avionics suite. It also determines SOI availability and switch functions.

### 2.2.1 Primary and Override Master Modes

Three primary Master Modes (NAV, A-A, and A-G) and two override modes (DGFT and MSL OVRD) are available in the F-16:

* **Navigation (NAV):** The default Master Mode, active when no other mode is selected. Both air-to-air and air-to-ground sensor modes are available in NAV. Navigation symbology is displayed on the HUD.
* **Air-to-Air (A-A):** Selected via the A-A button on the ICP. Only air-to-air sensor modes are available in A-A. Air-to-air weapon selection and engagement symbology are displayed on the HUD.
* **Air-to-Ground (A-G):** Selected via the A-G button on the ICP. Both air-to-air and air-to-ground sensor modes are available in A-G. Air-to-ground weapon delivery symbology is displayed on the HUD.
* **Dogfight (DGFT) and Missile Override (MSL OVRD):** Selected via the Dogfight/Missile Override switch on the throttle — DGFT outboard, MSL OVRD inboard. Only air-to-air sensor modes are available in both modes. DGFT and MSL OVRD take precedence over all other Master Modes except Emergency Jettison.

HOTAS switch inputs are interpreted within the active master mode configuration — sensor, display, and weapon options —, which can be pre-configured via the Data Transfer Cartridge (DTC) or adjusted manually in-flight. For complete Master Mode details, see Dash-34 § 2.1.1.2.1.

## 2.3 DMS, TMS, and CMS

DMS, TMS, and CMS — including all HOTAS tables — are covered in [Chapter 3](c3-dms.md) (DMS), [Chapter 4](c4-tms.md) (TMS), and [Chapter 5](c5-cms.md) (CMS).

### 2.3.1 Display Management Switch (DMS)

The Display Management Switch (DMS) is a four-way hat switch on the side-stick controller. Its primary functions are SOI designation and MFD format cycling (see Dash-34 § 2.1.5). The DMS selects _which display or sensor_ receives HOTAS inputs. It does not designate targets or control sensor modes.

### 2.3.2 Target Management Switch (TMS)

The Target Management Switch (TMS) is a four-way hat switch on the side-stick controller. Its primary functions are target designation, sensor management, and markpoint creation (see Dash-34 § 2.1.5). The function of each TMS direction depends on the Master Mode, the active sensor mode, and the current SOI display.

### 2.3.3 Countermeasures Management Switch (CMS)

The Countermeasures Management Switch (CMS) is a four-way hat switch on the side-stick controller. Its primary functions are countermeasures dispensing and ECM control (see Dash-34 § 2.1.5). CMS actuation is independent of both SOI designation and Master Mode.
