# Repetition Analysis — TMS/DMS/CMS Usage Guide

**Document type:** Editorial Notes — Repetition Audit  
**Target guide version:** v0.4.1.1 (SUBPATCH from v0.4.1.0)  
**Version bump rationale:** Wording and cross-reference corrections within existing chapters — no new sections, no structural additions. Per VERSION-SYSTEM § 3.2.2: "Fix typos, punctuation, small wording adjustments → SUBPATCH."  
**Scope:** Chapters 1–5 (Chapters 4, 6, 7 are placeholders — skipped)  
**Date:** 2026-02-18  
**Triggered by:** Community feedback — forum user Daddyk identified "certain number of repetitions, for example, page 6" in guide v0.4.1.0  
**Status:** Open — pending resolution

---

## How to Use This Document

Each repetition entry contains:

- **ID** — reference code for tracking
- **Location** — chapters/sections and line numbers in `guide-v0_4_1_0-20260211.tex`
- **Severity** — Alta / Média / Baixa / Aceitável
- **Description** — what the repetition is and why it is a problem
- **Recommended action** — concrete editorial direction for resolution
- **Status** — Open / Resolved

Severity criteria:

- **Alta** — reader encounters substantially the same content twice; immediate fix required
- **Média** — reader may notice the overlap; fix recommended before v1.0
- **Baixa** — minor overlap; acceptable but worth monitoring
- **Aceitável** — repetition is deliberate (pedagogical reinforcement of a safety-critical point); no action needed

---

## Quick-Reference Summary Table

| ID | Chapter | Sections | Severity | Summary | Status |
|----|---------|---------|----------|---------|--------|
| R-01 | C2 | 2.1 ↔ 2.1.1 | **Alta** | "Only one display holds SOI" — definition repeated almost verbatim | ✅ Resolved |
| R-02 | C2 | 2.2 intro ↔ 2.2.1 closing | **Média** | "Master mode determines..." — premise of 2.2 re-stated as conclusion of 2.2.1 | ✅ Resolved |
| R-03 | C2 / C3 | 2.3.1 ↔ C3 intro | **Baixa** | DMS physical description repeated in nearly identical wording | Aceitável |
| R-04 | C2 / C5 | 2.3.3 ↔ 5.1 ↔ 5.2 | **Alta** | CMS physical description boilerplate appears three times | ✅ Resolved |
| R-05 | C3 | 3.3.1.1 NAV ↔ A-G PRE | **Alta** | DMS Down NAV and A-G PRE paragraphs are literally identical except the last sentence | ✅ Resolved |
| R-06 | C3 | 3.2.3 ↔ 3.3.3 | **Média** | Snowplow and MARK/OFLY exception states described in full twice | ✅ Resolved |
| R-07 | C3 / C5 | Before each hotastable | **Alta (structural)** | "Each table entry specifies" block of 7 bullets appears 4× identically | Aceitável |
| R-08 | C5 | 5.2.3 table ↔ 5.2.4 "Consent vs. CMDS Consent" | **Alta** | "CMS Down grants consent to both CMDS and ECM" stated twice in consecutive subsections | ✅ Resolved |
| R-09 | C5 | 5.1 ↔ 5.2.4 | **Média** | High-G rationale for CMS thumb access paraphrased in 5.2.4 after full development in 5.1 | ✅ Resolved |
| R-10 | C5 | 5.2.2 intro, 5.2.2.2 intro, 5.2.4 | **Aceitável** | "IDIAS uses CMS Left, not CMS Down" — repeated three times; safety-critical distinction, likely intentional | Monitoring |

---

## Detailed Analyses

---

### R-01 — "Only one display holds SOI designation"

**Location:** Section 2.1 (line 589) ↔ Section 2.1.1 (line 599)
**Severity:** Alta
**Status:** Resolved (2026-02-18) — sentença definitória removida da abertura de 2.1.1; subsection abre diretamente com "The F-16 cockpit contains three basic displays..."

**What repeats:**

Section 2.1 opening paragraph (line 589):

> *"The Sensor of Interest (SOI) is a designation that identifies which display currently receives HOTAS cursor slew commands and Target Management Switch (TMS) inputs. **At any moment, only one display can hold SOI designation.** This single-point control architecture enables the pilot to interact with multiple sensors and displays using HOTAS controls without manually selecting different switches for different sensors."*

Section 2.1.1 opening paragraph (line 599):

> *"The Sensor of Interest (SOI) is the designation that identifies which display currently receives HOTAS inputs. **At any moment, only one display holds SOI designation.** When the pilot slews the cursor or presses TMS Up, the command is directed to whichever display is designated as SOI."*

**Why it is a problem:**

The two paragraphs open with essentially the same definitional sentence and the same key assertion ("only one display"). The section 2.1 heading is "SOI — Concept and Architecture" and section 2.1.1 is "The SOI Concept" — so the reader encounters a conceptual definition of SOI, then immediately encounters another conceptual definition of SOI. The unique contribution of 2.1.1 — the HOTAS input routing explanation and the conceptual distinction between *where* inputs go vs *what* they do — is buried after the repeated opening. This is the specific repetition flagged by forum user Daddyk ("page 6").

Note: a third instance appears in C3-S1-S1 (line 765) with `\secref{sec:C2-S1}` attribution ("As introduced in..."). That instance is not a problem — it is a proper cross-reference with explicit back-reference to the source section.

**Recommended action:**

Remove the opening definitional sentence from 2.1.1. The subsection should open directly with its unique content — the cockpit display architecture (HUD + two MFDs) and the HOTAS input routing logic. The "only one display" assertion has already been made in the parent section 2.1 and does not need restatement 10 lines later.

Proposed new opening for 2.1.1:

> *"The F-16 cockpit contains three basic displays: the Head-Up Display (HUD) and two Multifunction Displays (MFD). The MFD can present various formats or pages, including radar, targeting pod, weapon management and tactical information. When the pilot slews the cursor or presses TMS Up, the command is directed to whichever display is currently designated as SOI."*

---

### R-02 — "Master mode determines..." re-stated as conclusion of 2.2.1

**Location:** Section 2.2 intro (lines 643–645) ↔ Section 2.2.1 closing paragraph (line 665)
**Severity:** Média
**Status:** Resolved (2026-02-18) — parágrafo de encerramento de 2.2.1 reescrito: mantém DTC, encurta a tese, adiciona \secref{sec:C2-S2-S2} como forward reference. Exemplo de TMS Up removido.

**What repeats:**

Section 2.2 opening (lines 643–645):

> *"...master mode is the highest-level configuration state of the F-16 avionics system, determining not only SOI availability but also which HOTAS functions are active and how switch inputs are interpreted. [...] **The master mode determines which displays can be designated as SOI, which HOTAS functions are available, and how individual switch inputs are interpreted by the avionics suite.** Understanding master modes is essential to understanding why HOTAS switches behave differently in different operational contexts."*

Section 2.2.1 closing paragraph (line 665):

> *"Each master mode establishes default configurations for sensors, displays, and weapons. [...] **The master mode determines not only what the pilot sees on the displays, but also how HOTAS switches function.** A single HOTAS input — such as TMS Up — produces different results in NAV, A-A, and A-G modes because the underlying sensor and weapon context has changed."*

**Why it is a problem:**

Section 2.2 states its central thesis at the opening: master mode determines SOI availability, available HOTAS functions, and switch interpretation. Section 2.2.1 lists the five master modes (NAV, A-A, A-G, DGFT, MSL OVRD) — which is its unique contribution — but then closes by re-asserting the same thesis from 2.2, rephrased. The reader encounters the argument, reads an example list, and then encounters the same argument again. This creates a circular structure where the conclusion of 2.2.1 repeats the premise of 2.2 without advancing the reasoning.

Section 2.2.2 ("Why HOTAS Switches Behave Differently by Master Mode") then opens with yet another statement of the same idea (line 673), which is appropriate there because it is the title of that subsection. But arriving at 2.2.2 after the closing of 2.2.1 has already restated the thesis makes the transition feel redundant.

**Recommended action:**

Remove or replace the closing paragraph of 2.2.1 (line 665, from "Each master mode establishes..."). The paragraph's unique information — that DTC allows pre-programming defaults — can be kept as a standalone sentence. The thesis statement ("master mode determines...") should be cut entirely from 2.2.1 since it belongs in the 2.2 intro and in 2.2.2. A clean forward reference to 2.2.2 would serve better:

Proposed replacement closing for 2.2.1:

> *"Each master mode pre-configures default sensor, display, and weapon options, which can be set in advance via the Data Transfer Cartridge (DTC) or adjusted manually in-flight. The implications for HOTAS behavior are developed in \secref{sec:C2-S2-S2}."*

---

### R-03 — DMS physical description repeated in C3 intro

**Location:** Section 2.3.1 (line 693) ↔ Chapter 3 intro (line 738)
**Severity:** Baixa
**Status:** Aceitável (2026-02-18) — repetição deliberada; capítulos são unidades independentes de leitura. Leitor que entra direto no C3 precisa da re-introdução. Mesma lógica de R-07. Nenhuma ação necessária.

**What repeats:**

Section 2.3.1 (line 693):

> *"The Display Management Switch (DMS) is a **four-way, spring-loaded hat switch located on the flight stick**. Its primary functions are SOI selection and MFD format cycling."*

Chapter 3 intro (line 738):

> *"The **Display Management Switch (DMS) is a four-direction spring-loaded hat located on the flight stick**. Its primary role is to manage which display or sensor receives hands-on control inputs, known as the Sensor of Interest (SOI), and to cycle through the Multifunction Display (MFD) formats."*

**Why it is a problem:**

The physical description ("four-way/four-direction spring-loaded hat on the flight stick") and functional summary (SOI selection + MFD format cycling) are repeated nearly verbatim. Chapter 3 opening does add unique content not in 2.3.1 — the contrast with TMS, the figure of the flight stick, block/variant notes, and switch response characteristics — so the repetition is confined to the first sentence.

This is lower severity because chapters naturally re-introduce their subject. However, the wording overlap is close enough that a reader who has just read 2.3.1 will notice it immediately on turning to Chapter 3.

**Recommended action:**

Revise the first sentence of Chapter 3 intro to differentiate it from 2.3.1 or to make an explicit forward build on it. Options:

- Replace with a cross-reference: *"As introduced in \secref{sec:C2-S3-S1}, the DMS is a four-direction hat switch responsible for SOI selection and MFD format cycling."*
- Or open with the contrast directly, skipping the physical boilerplate: *"Unlike the TMS, which performs tactical functions through the active SOI display (\chapref{chap:C4}), the DMS is a transversal SOI manager..."*

---

### R-04 — CMS physical description boilerplate appears three times

**Location:** Section 2.3.3 (line 717) ↔ Section 5.1 (line 1315) ↔ Section 5.2 (line 1353)
**Severity:** Alta
**Status:** Resolved (2026-02-18) — sentença de re-identificação removida de 5.2; seção abre diretamente com o scope statement. 2.3.3 e 5.1 mantidas.

**What repeats:**

Section 2.3.3 (line 717):

> *"The Countermeasures Management Switch (CMS) is a **four-way, spring-loaded hat switch located on the flight stick**. Its primary function is countermeasures dispensing..."*

Section 5.1 (line 1315):

> *"The Countermeasures Management Switch (CMS) is a **four-direction hat switch mounted on the control stick** that serves as the pilot's primary control interface to the F-16's integrated electronic warfare (EW) defensive systems..."*

Section 5.2 (line 1353):

> *"The Countermeasures Management Switch (CMS) is a **four-direction hat switch located at the flight stick** that provides pilots with rapid, direct control over the F-16's defensive systems during demanding tactical situations. This section tabulates all CMS button combinations..."*

**Why it is a problem:**

Three definitional openings for the same switch in three different locations, each with minor wording variation ("four-way" vs "four-direction"; "mounted on" vs "located at"). Each instance adds slightly different content — 5.1 develops the tactical rationale; 5.2 scopes the section — but all begin by re-defining the physical nature of the switch.

The boilerplate ("four-direction hat switch on the flight stick") is not adding value by the third occurrence. More critically, section 5.2 re-identifies the switch one section after 5.1 has just done so. The reader has not left the chapter.

**Recommended action:**

- Keep the full opening in **5.1** — this is the chapter's canonical introduction to the CMS, and the high-G rationale developed there (lines 1317–1318) is unique and genuinely important.
- In **5.2**, cut the re-identification entirely. Open directly with the scope statement: *"This section tabulates all CMS button combinations, organized by operational layer: CMDS (manual/automatic/semi modes) and ECM (external pods ALQ-131/ALQ-184 and internal IDIAS). CMS actuation is independent of the Master Mode currently selected."*
- In **2.3.3**, the description is appropriate as an overview — but could optionally open with a forward reference to 5.1 for readers who want more context.

---

### R-05 — DMS Down: NAV and A-G PRE paragraphs are literally identical

**Location:** Section 3.3.1.1, NAV paragraph (line 990) ↔ A-G PRE paragraph (line 993)
**Severity:** Alta
**Status:** Resolved (2026-02-18) — parágrafo A-G PRE substituído por referência cruzada ao NAV com notação compacta da sequência (HUD $\rightarrow$ Left MFD $\leftrightarrow$ Right MFD).

**What repeats:**

NAV paragraph (line 990):

> *"In NAV, valid SOI candidates are the HUD and both MFD. If the HUD is SOI, DMS Down transitions SOI from HUD to the Left MFD on first press. Subsequent DMS Down presses toggle SOI between the two MFD (Left MFD ↔ Right MFD). Once SOI leaves the HUD, it remains on the MFD cycle until DMS Up is pressed to restore HUD as SOI."*

A-G PRE paragraph (line 993):

> *"In A-G PRE, valid SOI candidates are the HUD and both MFD. If the HUD is SOI, DMS Down transitions SOI from HUD to the Left MFD on first press. Subsequent DMS Down presses toggle SOI between the two MFD (Left MFD ↔ Right MFD). Once SOI leaves the HUD, it remains on the MFD cycle until DMS Up is pressed to restore HUD as SOI. **This allows the pilot to shift hands-on control focus while examining different sensor pages."***

The only difference is the last sentence of A-G PRE. The sentence immediately following (line 996, A-G VIS) even acknowledges this explicitly: *"DMS Down toggles through the same pattern as in NAV and A-G PRE."* — meaning the text itself proves the duplication was unnecessary.

**Why it is a problem:**

The reader encounters two consecutive paragraphs with four identical sentences. A-G VIS then opens by saying the behavior is the same as both preceding modes, making the repetition even more conspicuous. This is structural redundancy — the same toggle sequence described three times (NAV in full, A-G PRE in full, A-G VIS by reference), when one full description and two references would suffice.

**Recommended action:**

Establish the toggle sequence once under NAV, then reference it for A-G PRE, adding only the operational nuance:

> **NAV (Navigation) Master Mode:**  
> *"In NAV, valid SOI candidates are the HUD and both MFD. If the HUD is SOI, DMS Down transitions SOI to the Left MFD on first press; subsequent presses toggle SOI between the two MFD (Left MFD ↔ Right MFD). Once SOI leaves the HUD, it remains in the MFD cycle until DMS Up is pressed to restore HUD as SOI."*

> **A-G in PRE (Preplanned Air-to-Ground) Mode:**  
> *"In A-G PRE, DMS Down follows the same toggle sequence as NAV (HUD → Left MFD → Left MFD ↔ Right MFD). This allows the pilot to shift hands-on control focus between the HUD and MFD sensor pages during weapon pre-planning."*

> **A-G in VIS (Visual Air-to-Ground):**  
> *"In A-G VIS modes, DMS Down follows the same toggle pattern, but becomes **operationally critical** rather than merely convenient..."* [continues as existing]

---

### R-06 — Snowplow and MARK/OFLY exception states described twice in full

**Location:** Section 3.2.3 "DMS Up Exception States" (lines 958–959) ↔ Section 3.3.3 "DMS Down Exception States" (lines 1054–1056)
**Severity:** Média
**Status:** Resolved (2026-02-18) — items de 3.3.3 substituídos por versões compactas com \secref{sec:C3-S2-S3} + delta específico do DMS Down. 3.2.3 mantida.

**What repeats:**

Section 3.2.3 — Snowplow (line 958):

> *"When the pilot enters Snowplow mode [...] and the SP position has not yet been stabilised with TMS Up, the SOI is effectively 'nowhere'. Both the A-G radar and TGP display `NOT SOI` on the MFDs, and **DMS Up/Down** commands are ineffective until the SP position is stabilised. Once stabilised, SOI returns to its previous state, and DMS Up becomes effective again (\dashref{4.2.1.4})."*

Section 3.3.3 — Snowplow (line 1054):

> *"When the pilot enters Snowplow mode [...] and the SP position has not yet been stabilised with TMS Up, the SOI is effectively 'nowhere.' Both the A-G radar and TGP MFD displays show `NOT SOI`, and neither display is designated as SOI. As a result, **DMS Down has no effect** in this state: the toggle mechanism has nowhere to advance SOI to. Once the SP position is stabilised with TMS Up (pressing TMS Up on the HUD), SOI returns to its previous designated display, and DMS Down resumes normal toggling behaviour."*

The same applies to MARK/OFLY at lines 959 and 1056.

**Why it is a problem:**

Section 3.3.3 already opens with the acknowledgement that these states are "a direct reflection of DMS Up (see \secref{sec:C3-S2-S3})" — which means the document itself recognizes the relationship. Despite this cross-reference, both states are then re-described in full, word-for-word, with only the switch name changed ("DMS Up" → "DMS Down"). The re-description adds nothing that the cross-reference + one sentence of delta wouldn't cover.

**Recommended action:**

In section 3.3.3, reduce the exception state descriptions to a cross-reference plus the operationally specific consequence for DMS Down:

> **Snowplow (SP) PRE State (not stabilised):**  
> *"As described in \secref{sec:C3-S2-S3}, the SOI is effectively 'nowhere' in the unstabilised SP state. Consequently, **DMS Down has no effect** — the toggle mechanism has no valid display to advance SOI to. Once the SP position is stabilised with TMS Up, SOI returns to its previous display and DMS Down resumes normal toggling."*

> **MARK/OFLY Submode:**  
> *"As described in \secref{sec:C3-S2-S3}, SOI cannot be designated or changed in MARK/OFLY. **DMS Down has no effect** in this state. This submode is rare in normal operations."*

This approach preserves the section's purpose (documenting DMS Down-specific behavior) while eliminating the redundant re-narration of the exception condition itself.

---

### R-07 — "Each table entry specifies" block repeated 4× across the document

**Location:** Before each hotastable — lines 929 (C3-S2), 1018 (C3-S3), 1244 (C3-S4), 1355 (C5-S2)
**Severity:** Alta (structural)
**Status:** Aceitável (2026-02-18) — repetição deliberada; tabelas auto-contidas permitem leitura direta sem retornar à Seção 1.3.2. Nenhuma ação necessária.

**What repeats:**

An identical block of 7 bullet points appears before every hotastable in Chapters 3 and 5:

```
Each table entry specifies:
• Mode: The operational context (Master Mode).
• Direction: The physical direction for pressing the DMS hat (Up, Down, Left, Right).
• Action: The press type (Short, Long, Long Hold).
• Function: What the DMS/CMS command activates or controls.
• Effect / Nuance: The resulting system behavior, including tactics and constraints.
• Dash34: Reference section in the Dash-34 manual.
• Training: Identification of recommended BMS training mission(s) for hands-on practice...
```

**Why it is a problem:**

This block is structurally redundant because the column definitions already appear in Section 1.3.2 ("Table format"), where `\tabref{tab:C1-hotastable-format}` provides the definitive reference. The reader who has read Section 1 does not need the columns re-explained before every table. The reader who jumps directly to a table can consult Section 1.3.2 via a short cross-reference.

As the guide grows — Chapters 4, 6, and 7 are yet to be developed — this pattern will compound. Chapter 4 (TMS) is expected to have significantly more tables than Chapters 3 and 5 combined. If the current pattern is maintained, the guide will contain this block potentially 8–12 more times.

Additionally, one instance contains an error: line 1359 reads "pressing the **DMS** hat" in the Direction bullet of the **CMS** table — a copy-paste artifact.

**Recommended action:**

Remove the 7-bullet block from all pre-table positions. Replace with a single-sentence cross-reference that can also serve as a paragraph transition:

> *"The table below follows the standard hotastable format; for column definitions, see \secref{sec:C1-S3-S2}."*

If a Training selection rationale paragraph exists (e.g., lines 941–942 for DMS Up, lines 1256–1258 for DMS Left/Right), that paragraph has genuine unique content and should be kept immediately before the table. Only the redundant column definition block should be removed.

Note: also fix the copy-paste error on line 1359 ("DMS hat" → "CMS hat").

---

### R-08 — "CMS Down grants consent to both CMDS and ECM" stated twice consecutively

**Location:** Section 5.2.3 table cell (line 1474) ↔ Section 5.2.4 "Consent vs. CMDS Consent" paragraph (line 1498)  
**Severity:** Alta  
**Status:** Resolved as per recommendation A below

**What repeats:**

Section 5.2.3 table — "Joint Consent (CMDS + ECM)" cell (line 1474):

> *"Single CMS Down command grants consent to both the ALE-47 CMDS (AUTO/SEMI) and the external ECM pod. There's no distinction between the two; both systems respond to the same CMS Down press. This unified control maximizes pilot situational awareness and frees workload during combat maneuvering."*

Section 5.2.4 — "Consent vs. CMDS Consent" paragraph (line 1498):

> *"A single CMS Down press grants consent to both the ALE-47 CMDS and the external ECM pod. The pilot does not issue separate commands; the CMS Down action is unified. However, internal IDIAS uses CMS Left for mode cycling, not CMS Down. This distinction is critical for aircraft configured with IDIAS."*

**Why it is a problem:**

The first two sentences of the 5.2.4 paragraph are a paraphrase of the 5.2.3 table cell. The genuinely new content in 5.2.4 is the IDIAS distinction — that IDIAS does *not* use CMS Down — which is the critical safety note. But to get there, the reader must wade through a re-statement of what the table already established.

Additionally, section 5.2.3 is a single-row table labelled "CMS Interaction with CMDS and ECM (Consent and Constraints)" that exists solely to state this unified consent. It is questionable whether a single-row table with this content justifies an entire subsection, or whether its content would be better absorbed into 5.2.4 as prose.

**Recommended action (two options):**

**Option A (preferred):** Keep the 5.2.3 table, cut the opening of 5.2.4 "Consent vs. CMDS Consent" paragraph to go directly to the IDIAS distinction:

> *"The unified CMS Down consent described in \tabref{tab:...} does not apply to IDIAS-equipped aircraft: internal IDIAS uses CMS Left for mode cycling, not CMS Down. This distinction is critical for aircraft configured with IDIAS and must not be confused with the external ECM pod workflow."*

**Option B:** Dissolve section 5.2.3 entirely. Move the unified consent explanation as a prose sentence into 5.2.4, preceding the IDIAS distinction. Remove the single-row table. This produces a cleaner 5.2.4 paragraph with no duplication.

---

### R-09 — High-G rationale for CMS thumb access paraphrased in 5.2.4

**Location:** Section 5.1, second paragraph (line 1317) ↔ Section 5.2.4, opening sentence (line 1482)
**Severity:** Média
**Status:** Resolved (2026-02-18) — primeira sentença de 5.2.4 substituída por scope statement; rationale high-G permanece exclusivamente em 5.1.

**What repeats:**

Section 5.1 (line 1317):

> *"Its role is to grant the pilot **rapid tactical control** over the aircraft's defensive posture. This control is operationally critical because defensive decisions frequently occur during **high-G maneuvering** when hand position cannot be redirected to distant cockpit panels. A pilot executing a 6-G defensive turn cannot simultaneously reach the CMDS MODE knob on the left console or the ECM control panel without abandoning aircraft control. By placing the CMS within thumb reach during full-stick maneuver, the design ensures that no tactical scenario regardless of G-load or workload forces the pilot to choose between aircraft control and defensive system authority."*

Section 5.2.4 opening (line 1482):

> *"The CMS provides **rapid, tactile access** to CMDS program selection and ECM transmit authority **without requiring the pilot to manipulate distant panels during high-G maneuvering**. Mastery of CMS actuation across all CMDS modes (MAN, SEMI, AUTO) and ECM configurations (external pod, IDIAS) is essential for effective defensive operations."*

**Why it is a problem:**

Section 5.2.4 ("Important Operational Notes") opens by re-stating the core rationale already developed in 5.1. The rationale — high-G access, distant panels, thumb reach — is 5.1's central argument. In 5.2.4 it appears as a compacted one-sentence echo before transitioning to the actual operational notes (State Tracking, Bingo Quantity, RF Switch, etc.). Those operational notes are the real content of 5.2.4 and would stand perfectly well without the rationale recap.

**Recommended action:**

Cut the first sentence of 5.2.4 and open directly with the scope of the subsection:

> *"The following notes clarify key behavioral interactions between CMS actuation, CMDS consent states, and ECM transmit authority."*

Then proceed to the first `\paragraph{State Tracking:}` as currently written. The operational notes are strong on their own and do not need the rationale re-introduction.

---

### R-10 — "IDIAS uses CMS Left, not CMS Down" — three occurrences

**Location:** Section 5.2.2 intro (line 1434) ↔ Section 5.2.2.2 intro (line 1455) ↔ Section 5.2.4 (line 1498)  
**Severity:** Aceitável  
**Status:** Monitoring (no action required at this time)

**What repeats:**

- **5.2.2 intro (line 1434):** *"The CMS Down position controls transmit authority for external pods; **CMS Left cycles modes for internal IDIAS**."*
- **5.2.2.2 intro (line 1455):** *"CMS Left cycles through operational modes [...]. **CMS Down is not used for IDIAS**; mode control is via CMS Left and the XMTR button on the ECM panel."*
- **5.2.4 (line 1498):** *"However, **internal IDIAS uses CMS Left for mode cycling, not CMS Down**. This distinction is critical for aircraft configured with IDIAS."*

**Why this is acceptable:**

The distinction between CMS Down (external ECM pod) and CMS Left (IDIAS) is a habit-transfer safety issue. A pilot accustomed to CMS Down for ECM consent who transitions to an IDIAS-equipped variant and reflexively presses CMS Down will fail to activate jamming. The three-occurrence pattern appears to be deliberate: each instance serves a specific structural context — the section overview (5.2.2), the subsection detail (5.2.2.2), and the consolidated safety note (5.2.4). Repeating a safety-critical distinction across multiple structural levels is sound technical writing practice in this context.

**No action recommended.** If the document's overall repetition level is reduced through R-01 through R-09, this pattern will stand out less and its pedagogical intent will be clearer.

---

## Implementation Notes

### Suggested resolution order

1. **R-07 first** — removing the "Each table entry specifies" block is a mechanical find-and-replace that affects every chapter with tables. Doing this first reduces visual clutter and makes subsequent editing cleaner.
2. **R-01** — the Daddyk-cited repetition; highest visibility to community feedback.
3. **R-05** — the NAV/A-G PRE paragraph duplication; straightforward prose merge.
4. **R-08** — the CMS consent double-statement; choose Option A or B and implement.
5. **R-04** — the three-location CMS boilerplate; revise 5.2 opening.
6. **R-02, R-06, R-09** — medium-severity items; tackle together.
7. **R-03** — lowest severity; can be deferred.

### Version bump

All corrections in R-01 through R-09 are wording adjustments, cross-reference insertions, and paragraph removals within existing chapters. No new sections, no structural additions, no new tables. Per VERSION-SYSTEM § 3.2.2:

> *"Fix typos, punctuation, small wording adjustments → SUBPATCH"*

**Target version: v0.4.1.1**

LaTeX macros to update in `guide.tex` / snapshot:

```latex
\newcommand{\docversion}{0.4.1.1}
\newcommand{\docbuild}{2026XXXX}   % update with actual integration date
```

Snapshot file: `wip/guide/guide-v0.4.1.1-2026XXXX.tex`

### WIP file naming

If changes are significant enough to warrant a dedicated WIP file before integration, suggested name pattern:

```
section-C2-S1-soi-concept-repetition-fix-dev-2026-02-XX.tex
section-C3-S3-dms-down-repetition-fix-dev-2026-02-XX.tex
```

For global structural changes (R-07), changes can be applied directly to the guide snapshot given their mechanical nature (find-and-replace + cross-reference insertion).

---

*End of document*
