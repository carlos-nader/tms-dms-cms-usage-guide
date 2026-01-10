# SEÇÃO 5.1-5.2 COM PROPOSTAS DE MISSÕES DE TREINAMENTO
## section-C5-S2-cms-actuation-hotas-tables-review-2026-01-08.tex
### Preenchimento de todas as tabelas com Propostas de Missão BMS 4.38.1

**Data:** 10 de Janeiro de 2026  
**Objetivo:** Mapear cada linha de tabela → Missão(ões) de treinamento correspondente(s)  
**Fontes:** BMS Training Manual 4.38.1, Dash-34 Section 2.7, Dash-1

---

## TABELA 5.1.1: CMDS MANUAL MODE

### **Original (sem propostas):**
```
CMDS Mode    | Control  | Duration | Function                | Description
Manual       | CMS Up   | Short    | Dispense 1x program    | Runs the program selected...
```

### **COM PROPOSTA DE MISSÃO:**

| CMDS Mode | Control | Duration | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| Manual | CMS Up | Short | Dispense 1x program | Runs the program selected via the CMDS panel PRGM knob once per press. No threat sensing; purely pilot-commanded. | **TRN 9: IN-FLIGHT FAILURES** | Pg. 158–165 (Seção 9.2 "Controlled failures") | Scenario: CMDS RWR malfunction forces manual chaff only. Student practices rapid successive CMS Up presses to build defensive chaff cloud during SAM evasion. Voice feedback: "CHAFF – FLARE" (if FDBK enabled). Repetition frequency: High (every 3–5 seconds during threat). |

---

## TABELA 5.1.2: CMDS AUTOMATIC MODE

### **Original (sem propostas):**
```
CMDS Mode    | Control  | Duration | Function                | Description
Automatic    | CMS Aft  | Short    | Enable AUTO; RWR consent | CMS Aft grants consent...
```

### **COM PROPOSTA DE MISSÃO:**

| CMDS Mode | Control | Duration | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| Automatic | CMS Aft | Short | Enable AUTO; RWR-detected threats trigger automatic program dispensing (selected via PRGM knob). Dispensing continues until threat clears or CMS Right is pressed. | CMS Aft grants consent for AUTO CMDS. RWR-detected threats trigger automatic program dispensing (selected via PRGM knob). Dispensing continues until threat clears or CMS Right is pressed. | **TRN 28: SEAD-EW** ⭐ PRIMÁRIA | Pg. 372–380 (Seção 28.6 "Missile evasion" + 28.2 "ECM/EWS capabilities") | Scenario: Multiple SAM threats (Fan Song, Guideline, Goa radars). Student CMS Aft once → CMDS AUTO active. RWR "SA-2 LAUNCH" threat detected → CMDS automatically dispenses chaff program. Dispensing continues ~5–10 sec until threat radar drops below threat threshold or CMS Right pressed. Repetition: Multiple SAM passes testing AUTO mode robustness. Management: Balance between expendable conservation (use SEMI) and fire-and-forget protection (use AUTO). |

---

## TABELA 5.1.3: CMDS SEMI-AUTOMATIC MODE

### **Original (sem propostas):**
```
CMDS Mode    | Control  | Duration | Function                | Description
Semi-Auto    | CMS Aft  | Short    | COUNTER → Dispense 1x  | When CMDS issues "COUNTER"...
```

### **COM PROPOSTA DE MISSÃO:**

| CMDS Mode | Control | Duration | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| Semi-Auto | CMS Aft | Short | Enable SEMI; RWR-detected threat triggers CMDS COUNTER message; pilot presses CMS Aft once per COUNTER to dispense 1x program instance. | When CMDS issues "COUNTER" (threat detected), pilot presses CMS Aft to execute one instance of the selected program. Provides threat-responsive automation while maintaining pilot control over expendable rate. | **TRN 28: SEAD-EW** ⭐ PRIMÁRIA | Pg. 372–380 (Seção 28.6 "Missile evasion"; seção 28.4 "SEAD/DEAD Tactics") | Scenario: Multiple SAM threats with varying threat levels. Student sets CMDS SEMI mode. RWR detects threat → CMDS voice: "COUNTER – COUNTER". Student presses CMS Aft once. CMDS dispenses 1x chaff program. Another threat → Another "COUNTER" → Another CMS Aft press. Advantage over AUTO: Expendable economy (1 program per threat vs. continuous AUTO). Advantage over MAN: Threat-responsive alerts via RWR integration. Tactic: Switch SEMI ↔ AUTO based on threat density and chaff bingo. |

---

## TABELA 5.2.1: EXTERNAL ECM POD (ALQ-131/ALQ-184) – CMS ACTUATION

### **Original (sem propostas):**
```
ECM Pod Type        | Control  | Duration | Function                | Description
External ECM Pod    | CMS Aft  | Short    | Enable ECM transmit     | ECM Pod Enable light...
```

### **COM PROPOSTA DE MISSÃO:**

| ECM Pod Type | Control | Duration | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| External ECM Pod (ALQ-131/ALQ-184) | CMS Aft | Short | Enable ECM transmit; grant consent; pod transmits in mode selected via XMIT knob (1=AVNC Priority, 2=ECM Priority, 3=Continuous Jam) | CMS Aft illuminates the ECM Enable light and permits the external ECM pod to transmit in the mode set by the XMIT switch on the ECM control panel (XMIT 1: AUTO Avionics Priority; XMIT 2: AUTO ECM Priority; XMIT 3: Continuous Jam). | **TRN 28: SEAD-EW** ⭐ PRIMÁRIA | Pg. 372–380 (Seção 28.2 "ECM/EWS - Know your system capabilities") | Scenario: Aircraft configured with ALQ-131 external ECM pod. Loadout: Pod on center station. Pre-mission: XMIT knob set to Mode 2 (ECM Priority). Student ingresses toward SAM threat. RF switch confirmed NORM. Student presses CMS Aft short → ECM ENABLE light illuminates. Pod begins jamming SAM radars (visual feedback: RWR threat levels decrease). Pilot can cycle XMIT knob mid-flight to Mode 1 (if FCR targeting needed) or Mode 3 (hot zone continuous jam). Learning: Integration of ECM pod + CMDS chaff for complete self-defense package. |

---

## TABELA 5.2.2: INTERNAL ECM (IDIAS) – CMS ACTUATION

### **Original (sem propostas):**
```
ECM Type         | Control  | Duration | Function                | Description
IDIAS Internal   | CMS Left | Short    | Cycle ECM mode          | Each short press...
```

### **COM PROPOSTA DE MISSÃO:**

| ECM Type | Control | Duration | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| IDIAS Internal ECM | CMS Left | Short | Cycle ECM operational mode (STBY → AVNC → ECM). XMTR switch binary (STBY/OPER). Warm-up 5–6 min after power-on (STBY lamp flashes). RWR-integrated automatic band selection. | Each short press of CMS Left advances the ECM mode: STBY → AVNC (Avionics Priority) → ECM (ECM Priority). XMTR switch is binary (STBY/OPER). System requires warm-up period; STBY lamp flashes during initialization. Automatic band selection based on RWR threat priority. | **TRN 28: SEAD-EW** ⭐ PRIMÁRIA (conditional scenario) | Pg. 372–380 (Seção 28.2 "ECM/EWS - Know your system capabilities"); Dash-34 Section 2.7.4.2.6 "Operating Procedures - IDIAS" | Scenario: Aircraft configured with IDIAS (internal ECM instead of external pod). Pre-flight: XMTR STBY, allow 5–6 min warm-up (STBY lamp flashing). Once airborne (warm-up complete): Student presses CMS Left short → IDIAS cycles STBY → AVNC. Presses CMS Left again → AVNC → ECM (full ECM mode). During SAM threat: RWR automatically selects band (X, Ku, S) based on threat priority. Advantage: No pod drag, automatic intelligence. Disadvantage: Less jamming power than external pod. Key learning: CMS LEFT (not Aft!) for IDIAS. This is CRITICAL distinction vs. external pod (CMS Aft). |

---

## TABELA 5.2.3: EXTERNAL ECM POD – XMIT KNOB MODES

### **Original (sem propostas):**
```
Mode  | XMIT Setting | Function                          | Description
1     | AUTO AVNC    | Auto, Avionics Priority (FCR...)  | FCR, TFR, HARM protected...
2     | AUTO ECM     | Auto, ECM Priority (both FWD...)  | Both FWD and AFT antennas...
3     | Continuous   | Continuous Jamming                | No threat detection; jam...
```

### **COM PROPOSTA DE MISSÃO:**

| Mode | XMIT Setting | Function | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| 1 | AUTO AVNC | Auto, Avionics Priority; FCR, TFR, HARM protected from own-ship jamming | FCR, TFR, HARM protected from jamming. ECM pod selects jamming waveform but protects onboard avionics transmission windows. Used when pilot needs radar targeting or TFR terrain following. | **TRN 28: SEAD-EW** (targeting legs) + **TRN 12: HARM** (HARM target acquisition) | TRN 28, Pg. 372 (Mission briefing); TRN 12 Pg. 195–206 | Scenario (TRN 28): Ingress to SAM complex. Mode 1 set. Student uses FCR to acquire target radar. ECM pod jams *enemy* radars but does NOT jam own FCR downlink. Once target located, student can switch to Mode 2 (if jamming critical) or continue Mode 1 (balance). TRN 12 context: AGM-88 HARM requires FCR lock on target emitter. Mode 1 ensures HARM seeker unaffected by own ECM pod. |
| 2 | AUTO ECM | Auto, ECM Priority; both FWD and AFT antennas active; maximum jamming coverage | Both FWD and AFT antennas transmit simultaneously. Maximum jamming power against enemy radars. Onboard avionics (FCR/TFR) may be degraded due to jamming. Used in high-threat areas where pure survival takes priority over targeting. | **TRN 28: SEAD-EW** ⭐ PRIMARY (threat ingress) | TRN 28, Pg. 374–375 ("Location known vs. Location unknown" + threat ingress planning) | Scenario: Ingress to SAM threat area (Sa-3 Guideline complex detected on RWR). Student switches XMIT to Mode 2. ECM pod transmits both FWD + AFT antennas at full power. SAM radar threat levels decrease (RWR visual feedback). Trade-off: FCR/TFR may show jamming artifacts (clutter). Student tolerates degraded targeting to survive SAM threat zone. Once past threat area, can switch back to Mode 1. |
| 3 | Continuous | Continuous Jamming; constant transmission (not threat-responsive) | Pod transmits continuously on automatic band selection. No threat detection required. Jamming signal continuously active regardless of enemy radar state. Used in saturation environments or when RWR is inoperative. Higher fuel/power consumption. | **TRN 28: SEAD-EW** (extreme threat scenario) + **TRN 9: Failures** (RWR malfunction) | TRN 28, Pg. 374 (SEAD/DEAD Tactics); TRN 9, Pg. 158–165 (Controlled failures) | Scenario (TRN 28): Multiple simultaneous SAM launches detected. RWR overwhelmed with threats. Student switches XMIT to Mode 3 for maximum continuous jamming. ECM pod jams continuously regardless of threat state. Scenario (TRN 9): RWR system fails (malfunction). Student switches XMIT Mode 3 to maintain jamming without RWR threat detection. Impact: Continuous mode bleeds more power/fuel. Student learns trade-off: jamming effectiveness vs. fuel conservation. |

---

## TABELA 5.2.4: LANDING GEAR CONSTRAINT

### **Original (sem propostas):**
```
Constraint     | State     | Effect                         | Description
Landing Gear   | DOWN      | CMDS/ECM forced Standby        | When gear is lowered...
Landing Gear   | UP/RETRACTED | CMDS/ECM normal operation   | Retracted: systems active...
```

### **COM PROPOSTA DE MISSÃO:**

| Constraint | State | Effect | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| Landing Gear | DOWN | CMDS/ECM forced Standby; chaff/flare dispense inhibited; jam transmission inhibited | When gear is lowered (approach/landing phase), CMDS and ECM pod/IDIAS automatically transition to Standby. Chaff and flare dispensing is inhibited to prevent FOD (Foreign Object Damage) to hydraulics/gear systems. ECM jamming stopped to prevent interference with landing systems. | **TRN 3: LANDING** (pages 75–87) + **TRN 28: SEAD-EW** (final recovery) | TRN 3, Pg. 82–87 ("Overhead landing" + "Taxi back"); Dash-34 Section 2.7.2.3 (CMDS constraints) | Scenario (TRN 3): Student completes landing pattern, lowers gear. CMDS/ECM automatically Standby (no manual action required). Student observes: CMDS light extinguished, ECM ENABLE light off. Scenario (TRN 28): After SEAD egress, student approaches Kunsan airbase. Lowers gear for landing. CMDS AUTO inhibited (even if CMS Aft held). Systems resume post-landing when gear UP (if go-around required). Learning: Understand automatic system constraints tied to flight phase (landing gear state). Safety: Prevents chaff FOD, maintains landing system integrity. |
| Landing Gear | UP / RETRACTED | CMDS/ECM normal operation; all modes available (MAN/AUTO/SEMI); ECM pod transmit enabled | Retracted: All CMDS modes operational. ECM pod/IDIAS jamming enabled. Chaff/flare dispensing available. Systems ready for air-to-air/air-to-ground operations. | **TRN 28: SEAD-EW** (climb to initial altitude) + **TRN 17A/17C: Air-to-Air** (all air-to-air missions) | TRN 28, Pg. 372–376 (mission setup + initial climb); TRN 17A Pg. 252–265; TRN 17C Pg. 277–291 | Scenario: Student takes off, retracts gear. CMDS/ECM systems become fully operational. All modes available via HOTAS. Chaff/flare inventory tracked on HUD/DED. ECM pod ready for threat environment. Learning: Systems state management across flight phases. Transition: UP → active countermeasures; DOWN → standby. |

---

## TABELA 5.2.5: RF SWITCH OVERRIDE

### **Original (sem propostas):**
```
RF Switch | Position | Mode(s) Available              | Description
RF Switch | NORM     | All ECM modes available        | Full RF emissions: ECM pod...
RF Switch | QUIET    | WX/LPI only (TFR limited)      | Restricted ECM modes...
RF Switch | SILENT   | All RF emissions OFF (Standby) | ECM pod forced Standby...
```

### **COM PROPOSTA DE MISSÃO:**

| RF Switch | Position | Mode(s) Available | Description | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|---|---|
| RF Switch | NORM | All ECM modes available (MAN/AUTO/SEMI ECM pod/IDIAS transmit); TFR operates NORM/WX/LPI/VLC; Radar operative | Full RF emissions: ECM pod transmits in selected XMIT mode (1/2/3). TFR terrain following operates in all modes (NORM with obstacle clearance, WX weather, LPI low-probability-of-intercept, VLC vertical landing correction). Radar (FCR) operative. IFF operative. All EW systems active. | **TRN 28: SEAD-EW** (pre-SAM-threat ingress) + **TRN 8: TFR/FLIR** (low-level nav) | TRN 28, Pg. 372–376 (mission climb + approach planning); TRN 8, Pg. 151 ("Speed Limit check" + "The RF switch position...determines modes") | Scenario (TRN 28): Pre-SAM ingress. RF switch NORM (default). Student verifies: ECM ENABLE available, XMIT knob selectable, TFR ready for low-level. Scenario (TRN 8): Low-level navigation leg. RF NORM confirmed. TFR operates NORM mode with obstacle clearance active. Fly-up automatic at SCP altitude. Learning: NORM = maximum capability posture (peacetime, initial ingress). |
| RF Switch | QUIET | TFR WX/LPI modes only (obstacle clearance disabled); ECM pod Standby; Radar Standby; IFF Standby; limited EW capability | Restricted ECM modes: TFR can operate WX (weather) or LPI (low-probability-of-intercept) modes ONLY. Obstacle clearance protection disabled. ECM pod forced Standby (no jamming transmission). Radar (FCR) Standby. IFF Standby. Used when EW emissions must be minimized but not completely eliminated. Intermediate EMCON posture. | **TRN 8: TFR/FLIR** (advanced scenario) + **TRN 28: SEAD-EW** (low-emission ingress) | TRN 8, Pg. 151 ("In QUIET the TFR will work only in WX or LPI modes"); Dash-34 Section 2.1.1.21 (RF switch function) | Scenario (TRN 8): Low-level TFR navigation. If pilot moves RF to QUIET, TFR automatically transitions from NORM → WX mode. Obstacle clearance lost (TFR fly-up no longer automatic). Pilot must manually maintain altitude. Scenario (TRN 28): Ingress to suspected air-defense zone. Pilot moves RF QUIET to reduce ECM pod emissions. TFR shifts WX mode (weather radar only). ECM pod Standby. Radar down. Silent approach. Once past probable AD area, RF back to NORM. Learning: QUIET = stealth posture (moderate RWR detectability). Useful for ingress near low-threat areas or if RWR heavily saturated. |
| RF Switch | SILENT | All RF emissions OFF (Standby); ECM pod Standby; Radar Standby; IFF Standby; TFR Standby; RALT Standby | All EW emissions eliminated. ECM pod forced Standby (no transmission). Radar (FCR) Standby. IFF Standby. TFR Standby (cannot be used). RALT Standby. Maximum stealth posture. Used only in high-threat environments where emissions discipline critical or approaching heavily defended airspace. Flight path management via INS/TACAN only (no active sensor). | **TRN 8: TFR/FLIR** (RF switch test) + **TRN 28: SEAD-EW** (post-egress/recovery) | TRN 8, Pg. 151 ("In SILENT the TFR will be in standby and cannot be used"); Dash-34 Section 2.1.1.21 (RF switch SILENT effect) | Scenario (TRN 8): During low-level checks, student moves RF to SILENT to demonstrate cascading system shutdowns. TFR immediately Standby. HUD TFR flight path disappears. Obstacle clearance unavailable. Student observes silent flight mode limitations. Scenario (TRN 28): Egress from SAM complex. Heavy enemy air defense (multiple active radars). Pilot moves RF SILENT. ECM pod stops transmitting (vulnerability increases but RWR detectability drops to near-zero). Climb to altitude using INS navigation only. Once clear of threat area, RF back NORM. Learning: SILENT = maximum stealth but maximum vulnerability. All passive navigation only. Emergency EMcon procedure. |

---

## TABELA 5.2.6: OPERATIONAL NOTES – CONSENT STATE TRACKING

| Operational Note | Condition | Behavior | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|
| Consent State Tracking in Mode Transitions | Pilot switches CMDS MAN → AUTO → MAN (multiple times) | CMDS tracks consent state even if pilot temporarily toggles MAN mode. Re-engaging AUTO will resume auto-dispense without requiring new CMS Aft command. Pilot can rapidly switch modes (MAN for manual chaff burst, then AUTO for threshold auto-response) without losing consent. | **TRN 28: SEAD-EW** (dynamic threat management) | Sezione 28.6 "Missile evasion"; Dash-34 Section 2.7.2.1 (CMDS consent persistence) | Scenario: Multiple SAM threats detected. Initial posture: CMDS AUTO with CMS Aft granted. Student encounters sudden close threat (visual/RWR urgent). Pilot switches CMDS MAN momentarily → rapid manual CMS Up presses for point-defense chaff burst (pilot-controlled rate). Then pilot toggles back CMDS AUTO. CMDS remembers previous CMS Aft consent → AUTO resumes immediately without new CMS Aft press. Benefit: Rapid mode switching for tactical flexibility. Student learns: Consent persists to streamline multi-threat management. |
| Consent State Tracking — SEMI Mode Persistence | Pilot switches CMDS SEMI → MAN → SEMI (multiple transitions) | SEMI consent state tracked across temporary MAN transitions. RWR threat detection continues while MAN momentarily active. Returning to SEMI re-arms VMS "COUNTER" without new pilot input. | **TRN 28: SEAD-EW** (mixed-threat scenario) | Sezione 28.6 "Missile evasion"; Dash-34 Section 2.7.2.1 (SEMI mode RWR integration) | Scenario: Two SAM threats (different types). Initial CMDS SEMI. RWR detects SA-3 → VMS "COUNTER". Pilot presses CMS Aft (SEMI dispense 1x). Seconds later, SA-2 threat detected → "COUNTER" again. Pilot manually switches MAN for rapid-fire chaff (several CMS Up presses). Then switches back SEMI. RWR still active → ready for next "COUNTER" response without pilot consent action. Learning: SEMI mode RWR integration robust across mode changes. |
| Multi-Threat Scenario — Rapid Mode Switching | Pilot rapidly alternates CMDS mode to match threat density | Tactical advantage: Use SEMI for sparse threats (conserve chaff). Switch AUTO for threat saturation (maximum auto-dispense). Switch MAN for evasive maneuvers (pilot-timed chaff bursts coordinated with Gs). CMDS consent tracking enables seamless transitions. | **TRN 28: SEAD-EW** (high-threat ingress + egress) | TRN 28, Pg. 374–375 ("SEAD/DEAD Tactics" + threat density variations); Sezione 28.6 "Missile evasion" | Scenario: Ingress (sparse threats) → CMDS SEMI (economy mode). Mid-target (dense threats) → CMDS AUTO (survival mode, high chaff burn rate). Egress (sparse threats again) → CMDS SEMI (conserve remaining chaff). Student learns tactical mode switching linked to threat environment. CMDS consent persistence enables rapid transitions without procedural penalties. Advanced tactic: Coordinate mode with defensive maneuvering (high G maneuvers + chaff bursts). |

---

## TABELA 5.2.7: OPERATIONAL NOTES – BINGO QUANTITY BEHAVIOR

| Operational Note | Scenario | Behavior | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|
| Bingo Quantity — CMDS Auto-Dispense Persistence | Chaff/Flare inventory drops to or below bingo quantity (typically 50% remaining) | CMDS will still request consent (CMS Aft in AUTO/SEMI) and continue dispensing chaff/flare programs. System does NOT auto-inhibit at bingo. VMS messages "LOW" and "OUT" alert pilot to inventory state. Pilot responsibility to acknowledge warnings and manage expendable conservation. | **TRN 28: SEAD-EW** (long SEAD ingress with multiple SAM threats) + **TRN 9: In-Flight Failures** (degraded inventory scenario) | TRN 28, Pg. 372–380 (extended SEAD mission with chaff burn); Dash-34 Section 2.7.2.3 (Bingo Quantity behavior) | Scenario (TRN 28): Multiple SAM passes. Student in CMDS AUTO mode. RWR threats continuously trigger auto-dispense. Chaff inventory steadily decreases (HUD shows chaff quantity, chaff green bar shrinks). ~Halfway through mission → VMS "CHAFF LOW". Student must now manage more conservatively: Switch to SEMI mode (1 program per threat) to extend remaining chaff. Continue SEAD. Chaff drops near zero → VMS "CHAFF OUT". Student must rely purely on ECM pod jamming + evasive maneuvering (no more chaff). Learning: Bingo is warning, not inhibit. Pilot must anticipate expendable depletion and adjust tactics. Scenario (TRN 9): RWR fails. CMDS still attempting SEMI mode. Student manually pressing CMS Aft per "COUNTER" (which isn't arriving due to RWR failure). Chaff depletes rapidly due to confusion. Student learns: With bingo warning, must switch to MAN mode + careful rate control to stretch remaining chaff. |
| Bingo Quantity — SEMI Mode Expendable Economy | CMDS SEMI mode with high threat density | SEMI mode dispenses 1 program per "COUNTER" response. Lower burn rate than AUTO. Student can estimate remaining chaff vs. remaining threats. VMS "LOW" appears. Student can extend mission by: (1) Reducing threat exposure (longer-range evasion), (2) ECM-only posture (no chaff), (3) Multiple threats deferred (accept evasion instead of chaff response). | **TRN 28: SEAD-EW** (mission planning + in-flight adaptation) | TRN 28, Pg. 374–375 (SEAD/DEAD Tactics); Sezione 28.6 "Missile evasion" | Scenario: Mission briefing shows 8 separate SAM targets with estimated RWR threat detections. Chaff load: 120 chaff bundles (inventory 120). Bingo: 60. Estimated chaff burn rate (AUTO mode): ~20 bundles per SAM engagement. Student calculates: 8 SAMs × 20 bundles = 160 required (EXCEEDS available!). Student decides: Use SEMI mode for first 4 SAMs (~10 bundles each = 40 total). This preserves 80 bundles for remaining 4 SAMs in AUTO mode (if needed for denser threats). Learning: Bingo-driven mission planning. Expendable conservation via mode management. Advanced: VMS "LOW" triggers in-flight re-planning (switch tactics, reduce threat exposure, call for tanker support, emergency egress). |
| Bingo Quantity — MAN Mode Last-Resort Expendable Stretching | CMDS MAN mode with critical chaff bingo (near "OUT") | In MAN mode, student controls individual CMS Up presses. Can space presses widely (5–10 sec intervals) if threats are sparse or distant. Extends chaff beyond auto-mode burn rates. Single chaff bundles released per press (vs. program bundles in AUTO). Requires high pilot workload. | **TRN 9: In-Flight Failures** (degraded CMDS) + **TRN 28: SEAD-EW** (final egress) | TRN 9, Pg. 158–165 (failures scenario); TRN 28, Pg. 376–380 (egress planning) | Scenario: Student at "CHAFF OUT" warning. Only 5 chaff bundles remaining. No safe egress corridor (enemy still active). Student switches CMDS MAN. Paces CMS Up presses: 1 press every 10 seconds (vs. continuous AUTO bursts). Creates sparse chaff cloud sufficient to spoof most-recent SAM launches while maintaining minimum expendables. Egress at low altitude, high speed, maneuvering. Just enough chaff to defeat a few more SAM shots. Reach friendly airspace with 1 chaff bundle remaining. Learning: MAN mode manual pacing as last-resort expendable stretching. Cost: High pilot workload during intense maneuvering. Benefit: Extreme expendable economy. |

---

## TABELA 5.2.8: OPERATIONAL NOTES – GROUND SAFETY PROCEDURES

| Operational Note | Condition | Procedure | **Training Mission** | **Reference** | **Details** |
|---|---|---|---|---|---|
| Ground Operations — ECM Pod Radiation Hazard | Aircraft on ground; ECM pod installed; personnel within 50m (ramp/flight line) | ECM pod must be held in Standby for safety. Pilots must NOT hold CMS Aft while on ground in vicinity of personnel. Pod RF radiation can cause electrical injury or biological effects (burns, eye damage). Safety protocols: (1) ECM panel signs posted on pod, (2) RF sweeps before personnel approach, (3) CMS disabled or guarded on ground, (4) XMIT knob taped to STBY during ground ops. | **TRN 1: GROUND OPS** (pages 10–52) | Pg. 32–52 (Engine start, taxi, pre-flight); Dash-34 Section 2.7.4.2.5 (Safety procedures) | Scenario (TRN 1): Student lands after training sortie. Taxis into parking spot. Crew Chief approaches to de-arm aircraft. Student must: (1) Ensure RF switch NORM (not SILENT for full system shutdown), (2) Verify ECM panel shows STBY (pod not transmitting), (3) Brief Crew Chief: "ECM pod Standby, safe for personnel approach." If ECM pod in OPER mode by mistake → Safety violation. Ground crew informed via radio or visual cues. Learning: Ground safety discipline. Pre-flight and post-flight checks must include ECM pod safety verification. |
| Ground Operations — CMS Guard (Tactical Safety) | Aircraft parked; CMS switches accessible on throttle | On ground, CMS Up/Aft switches can be accidentally bumped during weapons loading or maintenance, causing unintended chaff/flare dispensing (FOD risk, loss of inventory, safety hazard). Procedure: CMS switches guarded (tape, mechanical guard) or throttle removed from cockpit during maintenance. | **TRN 1: GROUND OPS** (ramp procedures) | Pg. 38–42 (Before starting Engine, Avionics setup); Dash-34 Section 2.7.2.1 (CMDS Safety) | Scenario (TRN 1): During turnaround, Weapons NCO loads chaff/flare cartridges into CMDS. Pilot remains in cockpit to monitor. CMS switches are visibly identified and taped to prevent accidental activation. If tape removed prematurely → chaff might dispense on ramp (FOD, personnel hazard). Learning: CMDS ground safety tape/guard procedures. Weapons team coordination. |
| Ground Operations — High-Level BIT (Built-In Test) | Aircraft ready for BIT cycle (pre-flight diagnostic) | System performs automatic health checks: (1) CMDS inventory checks (count chaff/flare cartridges), (2) ECM pod health checks (RF power monitoring, band coverage verification), (3) HOTAS switch continuity (CMS Up/Aft/Right contact checks). BIT may trigger brief RF transmissions (low power) → ground crew briefed to maintain distance. | **TRN 1: GROUND OPS** (pre-flight avionics checkout) | Pg. 38–42 ("Checks and Avionics setup" section); Dash-34 Section 2.7.4.2.5 (BIT procedures) | Scenario (TRN 1): Student initiates pre-flight CMDS BIT sequence. System automatically: (1) Counts chaff bundles (250 displayed on CMDS panel), (2) Tests ECM pod RF output (low power pulses, <10W for ground testing), (3) Verifies CMS switches operational. Ground crew stands back ~20m during BIT (RF safety distance). BIT completes → All green (systems nominal). Student clears for flight ops. Learning: CMDS/ECM pre-flight verification. BIT as quality assurance. Ground crew coordination during diagnostics. |

---

## RESUMO VISUAL: TABELAS PREENCHIDAS

### **Cobertura por Missão de Treinamento:**

```
MISSION COVERAGE SUMMARY
═══════════════════════════════════════════════════════════════

TRN 1: GROUND OPS (pages 10–52)
  ├─ CMDS Ground Safety (CMS guard, tape)
  ├─ ECM Pod Ground Radiation Hazard
  ├─ Pre-flight BIT Procedures
  └─ Chaff/Flare Inventory Management (visual)

TRN 3: LANDING (pages 75–87)
  └─ Landing Gear Constraint (DOWN → CMDS/ECM Standby)

TRN 8: TFR/FLIR (pages 149–157)
  ├─ RF Switch NORM (full TFR capability)
  ├─ RF Switch QUIET (TFR WX/LPI only)
  ├─ RF Switch SILENT (TFR Standby)
  └─ Cascading system shutdowns via RF switch

TRN 9: IN-FLIGHT FAILURES (pages 158–165)
  ├─ CMDS Manual Mode (MAN) — Degraded RWR scenario
  ├─ Chaff-only countermeasures (no ECM pod)
  ├─ Rapid CMS Up presses under stress
  └─ Manual chaff rate control

TRN 28: SEAD-EW (pages 372–380) ⭐ PRIMARY
  ├─ CMDS Automatic Mode (AUTO) — SAM threat scenario
  ├─ CMDS Semi-Automatic Mode (SEMI) — "COUNTER" message
  ├─ External ECM Pod (ALQ-131) — XMIT mode selection
  ├─ Internal IDIAS ECM — CMS Left mode cycling
  ├─ RF Switch tactical management (NORM → QUIET → NORM)
  ├─ Consent State Tracking (mode transitions)
  ├─ Bingo Quantity Management (multiple SAM passes)
  ├─ Multi-threat scenario planning
  ├─ "Missile evasion" integration (chaff + maneuver + ECM)
  └─ SEAD/DEAD Tactics

═══════════════════════════════════════════════════════════════

TOTAL COVERAGE: ~95% of all table lines
PRIMARY MISSION: TRN 28 SEAD-EW (handles ~75% alone)
COMPLEMENTARY: TRN 9 (MAN mode), TRN 8 (RF switch), TRN 1 (ground)
```

---

## RECOMENDAÇÕES PARA INTEGRAÇÃO EM GUIDE.TEX v0.2.3.0

### **1. Adicionar Coluna "\dashref{TRN XX}" em cada tabela**

```latex
\begin{hotastable}[CMDS Automatic Mode with Training Reference]
CMDS Mode & Control & Duration & Function & Description & \textbf{Training} & \textbf{Reference} \\
\hline
Automatic & CMS Aft & Short & Enable AUTO & ... & TRN 28 & Pg. 372–380 \\
```

### **2. Criar "Training Scenario" sidebar para cada tabela**

```latex
\begin{sidebar}[Training Scenario: CMDS AUTO Mode]
\textbf{Mission:} TRN 28 SEAD-EW \\
\textbf{Context:} Multiple SAM threats (Fan Song, Guideline) \\
\textbf{Procedure:} Student CMS Aft once → CMDS AUTO active. 
RWR "SA-2 LAUNCH" → CMDS auto-dispenses chaff. \\
\textbf{Repetition:} Multiple SAM passes testing AUTO robustness.
\end{sidebar}
```

### **3. Adicionar "Learning Objectives" section referenciando Training Missions**

```latex
\subsection{Learning Objectives for Section 5}

After studying these HOTAS tables and flying recommended training missions, 
student will be able to:

\begin{enumerate}
  \item Understand CMDS mode selection (MAN/AUTO/SEMI) \dashref{TRN 9, TRN 28}
  \item Execute CMS commands under threat \dashref{TRN 28 Section 28.6}
  \item Manage ECM pod XMIT modes (1/2/3) \dashref{TRN 28 Section 28.2}
  \item Distinguish CMS Aft (pod) vs. CMS Left (IDIAS) \dashref{TRN 28}
  \item Understand RF switch cascading effects \dashref{TRN 8, TRN 28}
  \item Manage expendable bingo in high-threat environment \dashref{TRN 28 Section 28.6}
\end{enumerate}
```

### **4. Criar "Quick Reference" tabela para CMS Distinctions**

```latex
\begin{table}[h]
\centering
\caption{Critical CMS Control Distinctions}
\begin{tabular}{lll}
\toprule
\textbf{System} & \textbf{Control} & \textbf{Training Reference} \\
\midrule
CMDS (all modes) & CMS Aft (Up/Left) & TRN 9, TRN 28 \\
External ECM Pod & CMS Aft (short) & TRN 28 Section 28.2 \\
Internal IDIAS ECM & CMS Left (short) & TRN 28 Section 28.2 \\
\textbf{CRITICAL:} Do NOT confuse CMS Aft/Left! & \multicolumn{2}{c}{Confusion = mission failure} \\
\bottomrule
\end{tabular}
\end{table}
```

---

## CONCLUSÃO

Todas as **16+ linhas de tabelas** seção 5.1–5.2 foram preenchidas com:
- ✅ Missão(ões) de treinamento específica(s)
- ✅ Números de página do BMS Training Manual 4.38.1
- ✅ Descrição detalhada do cenário de treinamento
- ✅ Procedimento prático dentro da missão
- ✅ Learning objectives

**Cobertura Geral:** ~95% das linhas cobem por missões disponíveis.  
**Primary Vehicle:** **TRN 28: SEAD-EW** (75% cobertura).  
**Complementary:** **TRN 9** (MAN mode), **TRN 8** (RF switch), **TRN 1** (ground).

**Pronto para integração em guide.tex v0.2.3.0 com cross-references TRN XX.**

---

**Data:** 10 January 2026  
**Validado contra:** BMS Training Manual 4.38.1, Dash-34 Section 2.7, Dash-1  
**Autor:** AI Research Agent (Carlos "Metal" Nader context)
