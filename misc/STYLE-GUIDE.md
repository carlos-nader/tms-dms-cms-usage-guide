# Writing Style Guide
## Falcon BMS TMS/DMS/CMS HOTAS Usage Guide

**Document:** STYLE-GUIDE  
**Date:** 2026-02-21  
**Status:** Official style guide for all prose content in the TMS/DMS/CMS HOTAS Usage Guide.  
**Language:** English (this document); author instructions in Portuguese  

---

## 1. Purpose and Scope

For the full scope of application and chapter-level exceptions, see §1.1 and §1.2 below.

This document does **not** cover:

- LaTeX formatting, environments, or macros (see BRIEFING)
- Table cell content rules (see BRIEFING §6)
- File naming or versioning (see WIP-FILE-NAMING and VERSION-SYSTEM)
- Project workflow (see PROJECT-TRACKING)

**Note:** Inline semantic formatting commands (`\textbf{}`, `\texttt{}`, `\textit{}`) are covered in Section 8 of this document. The BRIEFING covers LaTeX environments, macros, and structural formatting only.

Any AI assistant working on this project must read this document before generating or revising prose content.

### 1.1 Scope of application

The rules in this document apply to all prose content in the guide:

- Section introductions, subsection text, and paragraph descriptions
- Table preambles (paragraphs preceding any table)
- Prose cells in any table — including the Function and Effect/Nuance columns
  of HOTAS tables, and any descriptive cell content in non-HOTAS tables
  where the author determines that prose standards apply

The author may extend application to additional content at their discretion.

### 1.2 Chapter scope exceptions

The rules in this document apply fully to all content within the scope
defined in §1.1, with one exception.

**Chapter 1 (Introduction)** contains two distinct content types:

- **Editorial sections** — the chapter opening, §1.1 (Scope and purpose), 
  and §1.3.1 (Chapter overview) — serve an orientation function. These
  sections declare scope, describe the guide's organisation, and position
  the document for a first-time reader. Purpose statements are acceptable
  if they serve reader orientation and do not constitute marketing language.
  The prohibition on filler sentences, benefit claims, and compound
  sentences still applies.
- **Functional sections** — §1.2 (Sources and references), §1.3.2
  (Table format), §1.3.3 (Reference conventions), and all of §1.4 —
  contain reference information and are subject to the full standard.

**Chapter 2 onward** are all subject to the full standard without exception.

---

## 2. Style Anchor: The BMS Documentation Standard

The primary style reference for this guide is the **Falcon BMS Dash-34** (TO BMS 1F-16CMAM-34-1-1), produced by the BMS Docs team. Secondary references are the **BMS Comms & Nav Book** and the **ACC Multi-Command Handbook 11-F16 Vol. 5**.

These documents share a consistent prose standard that this guide emulates:

**What these documents do:**

- Open sections with information, not with introductions about information
- State what systems do, then stop
- Use conditional constructions clinically: "If X, then Y"
- Repeat technical terms deliberately — no creative synonyms
- Use passive voice when the subject is the system, not the pilot
- Write short paragraphs that each carry one idea

**What these documents never do:**

- Justify why the reader should care about a topic
- Open with dramatic or rhetorical sentences
- Use metaphors or figures of speech
- Summarize what is about to be said before saying it
- Add closing sentences that restate what was already explained

**Illustrative comparison — Dash-34 original:**

> "AUTO (automatic) mode: automatic dispensing based on RWR threat sensing. Consent is given for the system to run the selected program (1-4) continuously (as sensed) with CMS aft until it is explicitly cancelled with a CMS right, or all chaff or flare expendables are exhausted."

This sentence opens with the subject, states the mechanism, and ends when the information ends. No preamble, no conclusion.

---

## 3. Core Principles

These six principles govern all prose in the guide. They are listed in order of priority.

### P1 — Start with the information

The first sentence of every section, subsection, or paragraph must carry information. It must not announce, introduce, or contextualize what is about to be said.

> ❌ "This section explains the role of the CMS in managing the aircraft's defensive systems."  
> ✅ "The CMS controls defensive program selection, ECM operating modes, and consent authority for all defensive subsystems."

> ❌ "Understanding TMS behavior in TWS mode is important for BVR engagements."  
> ✅ "In TWS mode, TMS Right steps the acquisition cursor to the next priority track file."

### P2 — State the mechanism, not the benefit

Describe what the system does. Do not explain why it is useful, what advantage it provides, or why the pilot should use it. Operational rationale belongs in table cells (Effect/Nuance column), not in narrative prose.

> ❌ "By placing the CMS within thumb reach, the design ensures the pilot can manage defenses during high-G maneuvering without releasing the stick."  
> ✅ "The CMS is mounted on the control stick, within thumb reach during full-deflection maneuvering."

> ❌ "This unified control maximizes pilot situational awareness and frees workload during combat maneuvering."  
> ✅ "A single CMS Down press grants consent to both the ALE-47 CMDS and the external ECM pod simultaneously."

### P3 — Use precise, repeated terminology

Use the same term every time for the same concept. Do not substitute synonyms to avoid repetition. Repetition is correct in technical documentation.

- Always: **consent** (not "authorization", "permission", "approval")
- Always: **dispense** (not "release", "deploy", "expend" — unless quoting a specific system state)
- Always: **designate** (not "select", "mark", "acquire" — unless the system uses a different term)
- Always: **press** (not "actuate", "depress", "activate" when referring to switch input)
- Always: **block and variant** — when qualifying that a procedure, configuration, or system behavior differs across F-16 versions, use "block and variant" as the compound modifier. Do not use "block" alone, "variant" alone, "blocks and variants", "variants", "block configuration", "variant configuration", "block/variant" (with slash), "F-16 blocks and variants", "model", "models", "type", "types", "version", or "versions". Omit "F-16" when the aircraft context is already established.
- Always: **side-stick controller** (the F-16 stick); always **throttle** (the left-hand control). Do not use "flight stick", "control stick", "stick", "joystick", "throttle controls", or "throttle grip".

### P4 — Keep sentences short and singular

Each sentence carries one idea. When a second idea appears, start a new sentence. Compound sentences with multiple subordinate clauses are a primary source of AI-generated prose patterns.

> ❌ "When the pilot presses TMS Up with the FCR as SOI and a target is within the acquisition cursor, the radar transitions to STT, which provides a higher-quality track at the cost of situational awareness, as all other contacts are blanked from the display."  
> ✅ "TMS Up with FCR as SOI initiates STT on the target within the acquisition cursor. In STT, the radar blanks all other contacts from the display."

### P5 — Omit introductory and closing filler

Remove sentences whose only function is to introduce what follows or to summarize what was just said. Every sentence must add information that does not appear elsewhere in the same paragraph.

Filler patterns to eliminate:

- "The following [noun] [verb]..." (opening filler)
- "It is important to note that..." (emphasis filler)
- "Mastery of X is essential for Y..." (motivational filler)
- "As described above..." / "As shown in the table..." (redundant closing)
- "Pilots must understand X in order to Y..." (paternalistic filler)

### P6 — Use passive voice for system behavior

When the subject of the action is the system or the aircraft, passive voice is correct and preferred. Reserve active voice for pilot actions.

> System action (passive): "Automatic dispensing is disabled when the RF switch is moved out of NORM."  
> Pilot action (active): "The pilot presses CMS Down to grant consent."

Do not rewrite passive constructions into active voice simply to "sound more direct." In technical documentation, passive voice applied to system behavior is precise, not weak.

---

## 4. Voice and Tone

**Person:** Third person throughout. The pilot is "the pilot," not "you."  
**Tense:** Present tense for system behavior. Past tense only when describing a completed configuration step.  
**Register:** Technical and neutral. Not conversational, not formal to the point of obscurity.  
**Assumed reader:** A virtual F-16 pilot with basic BMS familiarity. The guide does not explain what an MFD is. It does not explain what BVR means. It explains what TMS, DMS, and CMS do in specific contexts.

---

## 5. Sentence and Paragraph Patterns

### 5.1 How to open a section or subsection

State the subject and its primary function in one sentence. Do not use gerunds ("Managing the CMS requires..."). Do not use "is used to" constructions when a direct verb is available.

> ❌ "This subsection covers the behavior of CMS in CMDS Manual mode."  
> ✅ "In CMDS Manual mode, each CMS direction selects or executes a specific dispenser program."

> ❌ "CMS Down is used to provide consent to the ECM system."  
> ✅ "CMS Down grants ECM transmit consent."

### 5.2 How to introduce a table

The paragraph before a table must do two things: state what the table covers, and explain any column or content decision that is not self-evident. It must not restate the table title or promise what the table will show.

> ❌ "The table below shows all DMS Left and DMS Right behaviors across all Master Modes, with references to the Dash-34 and training missions."  
> ✅ "DMS Left and DMS Right behavior is identical across all Master Modes. The table below uses a single row per direction, applicable to A-A (including DGFT and MSL OVRD), A-G, and NAV."

When explaining column selection rationale, be direct and brief:

> ✅ "One training mission was selected per Master Mode, prioritizing missions that require frequent MFD format changes during critical tactical phases."

### 5.3 How to close a subsection

Do not add a closing sentence. End the subsection when the information ends. If a cross-reference is necessary, place it at the point of relevance, not at the end as a summary.

> ❌ "For more information on CMDS modes, see Section 5.2."  
> ✅ (cross-reference placed inline, at the first mention of the relevant concept)

### 5.4 Conditional constructions

Use "If...then" or "If...[result]" for system behavior conditions. Keep the condition and result in the same sentence when both are short. Split into two sentences when either is long.

> ✅ "If the RF switch is moved out of NORM, automatic dispensing is disabled."  
> ✅ "If a BLANK slot is present in the MFD format sequence, DMS Left/Right skips it automatically and advances to the next non-BLANK format."

Do not use "should," "may," or "might" for deterministic system behavior. Use "will" or the present tense.

> ❌ "The radar may drop the track file if the target is not updated within 13 seconds."  
> ✅ "The radar drops the track file if the target is not updated within 13 seconds."

---

## 6. Prohibited Patterns

The following constructions appear in AI-generated prose and must be eliminated from all guide content. Each entry includes the pattern, the reason it fails, and a preferred alternative.

| Pattern | Problem | Alternative |
|---------|---------|-------------|
| "serves as the primary interface to..." | Redundant — just state the function | "controls..." / "manages..." |
| "is designed to..." | Weak — states intent, not function | State what it does directly |
| "plays a critical role in..." | Evaluative filler | State the role directly |
| "it is important to note that..." | Paternalistic — implies the reader would miss it | Delete. State the fact. |
| "understanding X is essential for Y..." | Motivational filler | Delete. |
| "the design ensures that..." | Implies the writer is praising the system | State the outcome directly |
| "regardless of X" (mid-sentence) | Overused qualifier; often redundant | Rephrase or delete |
| "fundamentally change/alter/affect" | Emphatic adverb that weakens precision | Use the verb alone |
| "decision engine" / "control authority" | Abstract metaphors or jargon | State the specific mechanism |
| "maximizes situational awareness" | Marketing language | State the specific effect |
| "frees pilot workload" | Vague benefit claim | State the specific action |
| "in order to" | Verbose | Replace with "to" |
| "in the event that" | Verbose | Replace with "if" |
| "at this point in time" | Verbose | Replace with "currently" or delete |
| Opening with "This section/chapter explains..." | Announces instead of informs | Open with the information |
| Closing with "As described above..." | Restates what was just said | Delete |
| Multiple subordinate clauses in one sentence | Produces run-on structure typical of AI output | Split into two sentences |

---

## 7. Permitted Deviations from the Dash-34 Standard

The guide is community documentation, not a system reference manual. The following deviations from strict Dash-34 style are acceptable:

**Didactic explanations:** Brief explanations of *why* a behavior exists are permitted when they aid understanding of the switch interaction — not to motivate the reader, but to clarify the mechanism. These must be no longer than one sentence and must follow the factual statement, not precede it.

> ✅ "BLANK slots are skipped automatically. This preserves the cycling sequence regardless of how many slots are populated."

**"The pilot" as explicit subject:** The Dash-34 often omits the pilot as subject. The guide may use "the pilot" explicitly to distinguish pilot actions from system actions.

> ✅ "The pilot presses CMS Down to grant consent. The CMDS then begins automatic dispensing."

**Cross-referencing for navigation:** The guide cross-references its own sections and the Dash-34 using macros. These references are acceptable even when the Dash-34 does not use them, because the guide serves a different navigational purpose.

**Not permitted as deviation:** Rhetorical openings, motivational statements, benefit claims, metaphors, or any of the prohibited patterns listed in Section 6.

---

## 8. Formatting Policies — Semantic Commands

### 8.1 `\textbf{}` — Bold

**Scope:** The three HOTAS switches covered by this guide and their directions only.

**Applies to:**
- Switch names: CMS, TMS, DMS (when referred to as physical controls)
- Switch directions: CMS Up, CMS Down, CMS Left, CMS Right; TMS Up, TMS Down, etc.
- Column labels in table preamble lists

**Does not apply to:**
- Mode names (MAN, AUTO, SEMI)
- Physical panel components (knobs, lights, buttons)
- System names (ALE-47, CMDS, ECM, RWR)
- Table cell content (switch directions referenced inside Effect/Nuance or Function cells are written as plain text; the column structure provides identification context)

---

### 8.2 `\texttt{}` — Monospace

**Scope:** Strings that appear literally on a system display or are generated
as system voice messages.

**Applies to:**
- Display strings: DISPENSE RDY, STBY, AVNC, ECM, NORM
- Voice messages: COUNTER
- Any string reproduced exactly as shown on HUD, MFD, RWR, TFR, or CCU

**Does not apply to:**
- Mode names used narratively (MAN, AUTO, SEMI)
- Physical control positions (OPER, XMIT 1/2/3)
- Component names (XMTR, ECM Enable)
- System abbreviations used as prose nouns

---

### 8.3 `\textit{}` — Italic

**Scope:** Emphasis on technical distinctions where sentence structure alone
does not sufficiently highlight the critical information.

**Applies to:**
- A term or phrase whose emphasis is technically necessary: removing it
  would reduce precision or obscure a distinction critical to understanding
  the system behavior (e.g. \textit{one} program per event, dispatched
  \textit{simultaneously})
- Table cell content where a critical distinction would be lost without emphasis

**Does not apply to:**
- Stylistic emphasis with no technical content ("effectively", "clearly")
- Information already unambiguous from sentence structure alone

**Guideline:** If the sentence or cell reads correctly without the emphasis and loses no technical precision, remove \textit{}.

---

## 9. Quick Review Checklist

Before submitting or approving any prose content, verify the following:

- [ ] The first sentence of every section carries information — not an announcement
- [ ] No sentence explains why the reader should care about the topic
- [ ] No sentence uses "important," "critical," "essential," or "mastery" as emphasis
- [ ] No section opens with "This section/chapter covers/explains/discusses..."
- [ ] No section closes with a summary of what was just said
- [ ] Passive voice is used for system actions; active voice for pilot actions
- [ ] Conditional system behavior uses "will" or present tense — not "may" or "might"
- [ ] No sentence contains more than two subordinate clauses
- [ ] Technical terms are consistent throughout — no creative synonyms
- [ ] No prohibited pattern from Section 6 is present
- [ ] Any permitted deviation from Section 7 is intentional and appropriate
- [ ] Prose in table cells (Function and Effect/Nuance in HOTAS table environment and any descriptive non-HOTAS cell) meets the same standard as narrative prose
- [ ] Formatting follows the semantic rules in Section 8
- [ ] "block and variant" is used as the compound modifier wherever F-16 configuration differences are qualified — not "block" alone, "variant" alone, or any prohibited synonym
- [ ] "side-stick controller" and "throttle" are used throughout — not "flight stick", "control stick", "stick", "joystick", "throttle controls", or "throttle grip"

---

## 10. AI Instruction Block

> **For AI assistants:** Copy this block as a prompt prefix when generating or revising guide prose.

---

```
You are writing technical documentation for the Falcon BMS TMS/DMS/CMS HOTAS Usage Guide.
Style reference: Falcon BMS Dash-34 (community technical documentation, not a military manual).
Scope: applies to all narrative prose AND to prose table cells (Function and Effect/Nuance in HOTAS table environment and any descriptive non-HOTAS cell). Chapter 1 editorial sections (chapter opening, §1.1, §1.3.1) permit purpose statements if they serve reader orientation — benefit claims and filler are still prohibited.

RULES — apply without exception:

1. Start every section with information, not an announcement of what follows.
2. State what the system does. Do not explain why it is useful or what advantage it provides.
3. Use the same technical term every time for the same concept. No synonyms.
4. One idea per sentence. Split compound sentences.
5. Delete: "This section explains...", "It is important to note...", "Mastery of X is essential...", "The design ensures...", "In order to", closing summaries.
6. Passive voice for system behavior. Active voice for pilot actions.
7. Conditional system behavior: use "will" or present tense. Never "may" or "might" for deterministic outcomes.
8. No metaphors. No benefit claims. No rhetorical openings.
9. Paragraphs: 2–4 sentences. Sections: 2–4 paragraphs.
10. Before submitting output, check: does any sentence exist only to sound good rather than to inform?
11. Formatting — apply semantic commands as follows:
    \textbf{}: HOTAS switch names (CMS, TMS, DMS) and their directions (CMS Up, CMS Down, etc.) only. Not mode names, not panel components, not system names.
    \texttt{}: Strings that appear literally on a system display or as system voice messages (e.g. DISPENSE RDY, COUNTER, STBY). Not mode names used narratively, not physical control positions, not component names.

Prohibited constructions (delete or rephrase):
"serves as", "is designed to", "plays a critical role", "it is important to note",
"understanding X is essential", "the design ensures", "maximizes situational awareness",
"frees pilot workload", "decision engine", "regardless of" (as mid-sentence filler),
"fundamentally change", "in order to", "in the event that", opening with "This section..."

Permitted deviation: brief one-sentence explanations of mechanism rationale, placed after the factual statement.
```

---

*End of STYLE-GUIDE*
