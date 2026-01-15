# Falcon BMS TMS/DMS/CMS Guide — Chapter 4 (DMS) Unified Blueprint v1.1

**Date:** 15 January 2026, ~02:06 -03  
**Status:** Unified, updated blueprint (supersedes `Chapter-4-DMS-Complete-Blueprint.md` and `blueprint-C4-incremental.md`)  
**Version:** 1.1  
**Based on:** Dash-34 (§2.1.1.2.3, §2.1.5, §2.1.6, §2.1.7.5.x, §2.5.6.x), C4‑S1 final, C4‑S2 DMS Up final, deprecated C4‑S2 (Up/Down), deprecated C4‑S3 (format cycling)

---

## 0. Purpose of This Blueprint

This document is the **single, authoritative blueprint** for **Chapter 4 (DMS)** of the Falcon BMS TMS/DMS/CMS Usage Guide. It:

1. Defines the **final structure** of Chapter 4 (sections and subsections).  
2. Documents the **current implementation status** of each section (final / review / TODO).  
3. Consolidates content decisions from the previous **full blueprint** and the **incremental blueprint**, removing contradictions.  
4. Guides all future work on DMS (including new WIP files and integration into `guide.tex`).

This blueprint is written so that a future AI session can join the project mid‑stream and immediately know:

- What Chapter 4 must contain.  
- What already exists in final/review WIP files.  
- What remains to be written or refactored.

---

## 1. Final Chapter 4 Structure

### 4 DMS — Display Management Switch

Chapter 4 is organised in two main parts:

1. **4.1 Concept and Sensor of Interest (SOI)** — conceptual foundation and architecture.  
2. **4.2 DMS Switch Actuation** — direction‑based behaviour (Up, Down, Left/Right) and master‑mode constraints.

There is **no separate block/variant section** and **no long integration section with TMS** inside Chapter 4. Block/variant identity is addressed once in 4.1; TMS/DMS integration is handled briefly inside each relevant subsection and in Chapter 3 (TMS) where weapon‑specific flows belong.

---

### 4.1 Concept and Sensor of Interest (SOI)

**Current implementation:** `section-C4-S1-concept-soi-approved-2026-01-14.tex` (integration into `guide.tex`).

**Status:**
- ✅ Integrated into `guide.tex`

**Structure:**

```text
4.1 Concept and Sensor of Interest (SOI)
  4.1.1 SOI Definition and Scope Across Displays
  4.1.2 Role of the DMS in SOI Selection
  4.1.3 HUD as SOI in A-A and HMCS Capabilities
```

**4.1.1 SOI Definition and Scope Across Displays**

- Defines Sensor of Interest (SOI) as the **single display/sensor that receives SOI‑dependent HOTAS inputs** (cursor slew, TMS actions, etc.).
- Lists **valid SOI displays**:
  - FCR, TGP, HSD, HAD, WPN, HUD.
- Lists **non‑SOI formats**: SMS, DTE, TEST, blank/inactive MFDS.  
- Describes **visual cues**:
  - HUD: asterisk (`*`) in upper left corner.  
  - MFD: border outline; `NOT SOI` text when not selected.
- Includes **Table 4.1.x – Valid SOI Displays by Master Mode** (`\label{tab:C4-S1-SOI-by-mode}`):
  - NAV: HUD, FCR, TGP, HSD, WPN, HAD.  
  - A‑A: FCR, HSD, TGP (**HUD cannot be SOI**).  
  - A‑G (PRE): HUD, FCR, TGP, WPN, HAD, HSD.  
  - A‑G (VIS): HUD, FCR, TGP, WPN (visual‑driven context).  
  - DGFT: FCR, HSD, TGP (**HUD cannot be SOI**).  
  - MSL OVRD: FCR, HSD, TGP (**HUD cannot be SOI**).

**4.1.2 Role of the DMS in SOI Selection**

- Explains the **orthogonal axes** of DMS:
  - Vertical (Up / Down): chooses **which display** is SOI.  
  - Horizontal (Left / Right): cycles **format pages** on each MFD, independent of SOI.
- Summarises baseline actions:
  - DMS Up → attempts to designate HUD/HMCS as SOI (when permitted).  
  - DMS Down → toggles SOI between HUD and MFDs.  
  - DMS Left/Right → change formats on left/right MFD without changing SOI.

**4.1.3 HUD as SOI in A‑A and HMCS Capabilities**

- Clarifies that **HUD cannot be SOI in A‑A/DGFT/MSL OVRD** — this is an **SOI routing restriction**, not a loss of HUD/HMCS capability.
- Explains how **HMCS** provides off‑boresight cueing in A‑A **independently of SOI**:
  - AIM‑9 boresight/slave to HMCS LOS.  
  - FCR ACM BORE slaved to HMCS LOS when conditions allow.
- Links this architecture to DMS:
  - DMS Up is **ineffective** in A‑A because HUD is not a valid SOI candidate.  
  - SOI must be managed via DMS Down (MFD↔MFD) in air‑to‑air‑driven modes.

---

### 4.2 DMS Switch Actuation

**Goal:** describe DMS behaviour by **direction** (Up, Down, Left/Right) in terms of:

- Which display becomes SOI.  
- How master mode constrains what DMS can do.  
- Where DMS is operationally critical (e.g., A‑G VIS) vs convenience (e.g., NAV, A‑G preplanned).  
- How special states (Snowplow PRE, MARK/OFLY) temporarily disable SOI designation.

The organisation is **direction‑centric**, not master‑mode‑centric.  Master modes appear inside each directional section as constraints and examples.

Final high‑level structure:

```text
4.2 DMS Switch Actuation
  4.2.1 DMS Up: Designate HUD as SOI
  4.2.2 DMS Down: Toggle SOI Between Displays
  4.2.3 DMS Left / Right: Cycle MFD Formats
  4.2.4 Master Mode Behavior — DMS Summary
```

---

## 2. Section 4.2.1 — DMS Up: Designate HUD as SOI

**Current implementation:** `section-C4-S2-dms-up-integrated.tex` (integrated into `guide.tex`).  
**Status:**
- ✅ Integrated into `guide.tex`

**Structure in document terms:**

```text
4.2.1 DMS Up: Designate HUD as SOI
  [Intro: Function and visual indication — no subsubsection]
  4.2.1.1 DMS Up Effectiveness in All Master Modes
  4.2.1.2 DMS Up Usage Table
  4.2.1.3 DMS Up Exception States (SP PRE, MARK/OFLY)
```

### 4.2.1 Intro (unnumbered) — Function and Visual Indication

- One or two paragraphs, no `\subsubsection` heading.
- Content:
  - DMS Up attempts to designate **HUD (and HMCS, as an extension)** as SOI.  
  - When successful, **HUD SOI asterisk** appears, MFD SOI border disappears, as detailed in Section 4.1.1.  
  - All SOI‑dependent HOTAS inputs (CURSOR/ENABLE, TMS) now act on HUD/HMCS symbology, not on any MFD format.

### 4.2.1.1 DMS Up Effectiveness in All Master Modes

- States that **DMS Up is only effective when HUD is a valid SOI candidate**, as per Table 4.1.x (C4‑S1).  
- Focuses on **contexts where HUD SOI is operationally sensitive** vs contexts where it is just a convenience.

Sub‑structure (using `\paragraph*` and `\subparagraph*`):

1. **Master Modes Where DMS Up is Effective (HUD as SOI Permitted)**

   - NAV (Navigation)
     - HUD is primary reference for flight path, steering and basic SA.  
     - Short DMS Up → HUD becomes SOI.  
     - With HUD/HMCS SOI:
       - CURSOR/ENABLE slews HUD/HMCS cursor/designator.  
       - In HUD/HMCS MARK, TMS Up stabilises LOS and stores markpoints.  
       - MFDs provide background navigation/systems info.

   - A‑G Visual Modes (VIS) — CCIP, DTOS, AGM‑65 VIS, IAM‑VIS
     - Visual deliveries are HUD/HMCS‑centric; HUD SOI is often a **prerequisite** for correct TMS/CURSOR behaviour.  
     - DMS Up is **operationally critical** whenever SOI has migrated to an MFD (TGP, WPN, etc.).

     Examples (bullets):

     - CCIP visual deliveries:
       - HUD pipper = primary aiming reference.  
       - CURSOR/ENABLE (HUD SOI) can refine visual aimpoint when allowed.

     - AGM‑65 VIS:
       - HUD TD box slaves Maverick seeker.  
       - With HUD SOI, CURSOR/ENABLE slews TD box; TMS Up commands seeker lock.  
       - If SOI remains em WPN MFD, TMS acts on WPN page and visual HUD control falha até DMS Up.

     - IAM‑VIS (JDAM/JSOW visual):
       - HUD TD box + IAM solution cues.  
       - HUD SOI + CURSOR/ENABLE refinam TD; TMS Up designa/estabiliza.  
       - Se SOI está em um MFD, TMS não atualiza HUD até DMS Up.

   - A‑G non‑VIS (CCRP, preplanned IAM)
     - DMS Up funciona (HUD pode ser SOI), mas HUD SOI é **conveniência**, não requisito:  
       - Preplanned targeting, sensor SPI, sighting‑point control podem ser geridos 100% via FCR/TGP/HSD SOI.

2. **Master Modes Where DMS Up is Ineffective (HUD as SOI Prohibited)**

   - A‑A, DGFT, MSL OVRD
     - Em modos de emprego ar‑ar, HUD não é candidato válido a SOI.  
     - Pressionar DMS Up **não altera** SOI — permanece em FCR, HSD ou TGP.  
     - Explica que o racional arquitetural e o papel do HMCS estão em 4.1.3.

### 4.2.1.2 DMS Up Usage Table

- `\subsubsection{DMS Up Usage Table}` introduz uma `hotastable` que resume DMS Up em três linhas principais:

  - **NAV** – Up / Short / Designate HUD as SOI  
    - Efeito / nuance: DMS Up totalmente efetivo; HUD/HMCS SOI, MARK, CURSOR/ENABLE e TMS Up; MFDs para background.  
    - Dash‑34 refs: 2.1.1.2.3, 2.1.7.5.1, 2.1.7.5.4, 2.5.6.1.  
    - Train: `---` (sem TRN específica de NAV+DMS Up).

  - **A‑A** – Up / Short / Designate HUD as SOI  
    - Efeito / nuance: DMS Up inefetivo; arquit. restringe SOI a FCR/HSD/TGP; HUD sempre passivo como display.  
    - Dash‑34 refs: 2.1.1.2.3.  
    - Train: `---`.

  - **A‑G** – Up / Short / Designate HUD as SOI  
    - Efeito / nuance: DMS Up efetivo; HUD asterisco; em VIS, HUD é interface crítica para CURSOR/TMS; perda de HUD SOI implica perda de controle visual até novo DMS Up.  
    - Dash‑34 refs: 2.1.1.2.3, 4.2.2.1, 4.2.2.1.1 (AGM‑65 VIS/IAM‑VIS).  
    - Train: `\trnref{10 (GP Bombs)}, \trnref{11 (LGB)}, \trnref{13 (Maverick)}, \trnref{14 (Maverick Adv)}, \trnref{15 (IAM)}`.

- Há um `\newpage` antes da tabela para garantir início em página nova.

### 4.2.1.3 DMS Up Exception States (SP PRE, MARK/OFLY)

- `\subsubsection{DMS Up Exception States}` com bullets para:

  - **Snowplow (SP) PRE state (unstabilised)**:
    - Ao entrar em SP e antes de estabilizar com TMS Up, FCR/TGP mostram `NOT SOI`.  
    - SOI efetivo é "nenhum"; DMS Up/Down não têm efeito até estabilizar.  
    - Após estabilização, SOI volta ao estado anterior e DMS Up volta a funcionar.

  - **MARK/OFLY Submode**:
    - Em MARK/OFLY, SOI não pode ser designado (Dash‑34 §2.1.1.2.3).  
    - DMS que normalmente mudariam SOI não têm efeito.  
    - Exceção rara na operação normal.

---

## 3. Section 4.2.2 — DMS Down: Toggle SOI Between Displays

**Current implementation:**
- Nenhum WIP ativo ainda.  
- Conteúdo parcial de DMS Down existe apenas em arquivo deprecated (`section-C4-S2-dms-up-down-deprecated-2026-01-14.tex`) e foi salvo à parte (fora da estrutura oficial) para futura criação de `section-C4-S2-dms-down-review-2026-01-xx.tex`.

**Status alvo:**
- Criar novo WIP `section-C4-S2-dms-down-review-2026-01-xx.tex`.  
- Reutilizar o texto válido do deprecated, ajustando à estrutura abaixo.  
- Remover redundâncias com 4.1.

**Structure (final):**

```text
4.2.2 DMS Down: Toggle SOI Between Displays
  [Intro: Core toggle logic HUD / Right MFD / Left MFD — no subsubsection]
  4.2.2.1 DMS Down Effectiveness in All Master Modes
  4.2.2.2 DMS Down Usage Table
  4.2.2.3 DMS Down Exception States
```

### 4.2.2 Intro (unnumbered) — Core Toggle Logic

- Explicar em texto corrido (sem heading):
  - DMS Down altera **quem é o SOI**, alternando entre:
    - HUD,  
    - MFD direito,  
    - MFD esquerdo.
  - Em modos onde HUD é SOI válido (NAV, A‑G), o ciclo típico é something like:  
    HUD → Right MFD → Left MFD → HUD.  
  - Em A‑A/DGFT/MSL OVRD, HUD está fora do ciclo; DMS Down alterna apenas entre MFDs.

- Incluir uma frase clara para evitar confusão com DMS Left/Right:

  > “In this section, ‘left MFD’ and ‘right MFD’ refer only to which display currently holds SOI when DMS Down is pressed. Format cycling on each MFD is described separately in Section 4.2.3 (DMS Left/Right).”

### 4.2.2.1 DMS Down Effectiveness in All Master Modes

- Similar em espírito a 4.2.1.1, mas para DMS Down:
  - Descrever para cada grupo de modos como o SOI alterna quando DMS Down é pressionado.

Conteúdo alvo:

- **NAV**
  - HUD está no ciclo.  
  - Padrão de alternância típico: HUD → MFD direito → MFD esquerdo → HUD.  
  - DMS Down é a forma primária de sair de HUD SOI para um MFD e de alternar o SOI entre MFDs.

- **A‑G PRE/VIS**
  - Semelhante a NAV: HUD no ciclo, mas com ênfase em:
    - Alternar rapidamente de HUD (visual) para TGP, WPN ou HAD como SOI em um dos MFDs.  
    - Voltar ao HUD com mais um(s) DMS Down, conforme a lógica do ciclo.

- **A‑A / DGFT / MSL OVRD**
  - HUD não é SOI válido; o ciclo é **MFD‑only**:
    - Ex.: FCR (Right MFD) ↔ HSD (Left MFD) ↔ TGP, etc.  
  - DMS Down é a ferramenta principal para trocar a prioridade entre FCR, HSD e TGP.

### 4.2.2.2 DMS Down Usage Table

- `\subsubsection{DMS Down Usage Table}` introduz `hotastable` paralela à de DMS Up:

  - NAV — Down / Short / Toggle SOI between HUD and MFDs  
    - Descrever o padrão de ciclo e como isso é usado em navegação e gestão de SA.

  - A‑A — Down / Short / Toggle SOI between MFDs only  
    - HUD fora do ciclo; FCR, HSD, TGP como candidatos.  

  - A‑G — Down / Short / Toggle SOI between HUD and A‑G sensor pages  
    - Ênfase em passar HUD↔TGP↔WPN↔HAD, etc.

- Coluna Dash‑34 com refs a 2.1.1.2.3 (SOI), 2.1.6 (MFDS), outras seções úteis.  
- Coluna Train com TRN relevantes (provavelmente os mesmos de A‑G VIS, mais algum de NAV se fizer sentido).

### 4.2.2.3 DMS Down Exception States

- Paralelo a 4.2.1.3, focando em como os estados especiais afetam DMS Down:

  - **Snowplow (SP) PRE**:
    - Quando nem FCR nem TGP têm SOI (ambos `NOT SOI`), DMS Down não consegue transferir SOI entre MFDs.  
    - Somente após estabilizar SP (TMS Up) o ciclo de SOI volta a ser válido.

  - **MARK/OFLY**:
    - Em MARK/OFLY, SOI não pode ser designado; DMS Down não altera SOI.  
    - Igual a DMS Up em termos de inefetividade.

  - Outros estados especiais podem ser adicionados se identificados (mas a intenção é manter aqui apenas casos realmente distintos do comportamento nominal).

---

## 4. Section 4.2.3 — DMS Left / Right: Cycle MFD Formats

**Current implementation:**
- Antigo `section-C4-S3-dms-format-cycling-dev-2026-01-13.tex` foi renomeado para `section-C4-S3-dms-format-cycling-deprecated-2026-01-13.tex` e movido para ARCHIVE.  
- Nenhum novo WIP ativo ainda.

**Status alvo:**
- Criar novo WIP `section-C4-S3-dms-left-right-review-2026-01-xx.tex` para implementar 4.2.3 do zero, alinhado a este blueprint.

**Structure (final):**

```text
4.2.3 DMS Left / Right: Cycle MFD Formats
  4.2.3.1 Format Cycling Mechanics
  4.2.3.2 Available Formats by Master Mode
  4.2.3.3 Left/Right and SOI Independence
  4.2.3.4 DMS Left/Right Usage Table
```

### 4.2.3.1 Format Cycling Mechanics

- Explicar, em termos gerais:
  - DMS Left → cicla formatos no **MFD esquerdo** (primário → secundário → terciário).  
  - DMS Right → idem para **MFD direito**.  
  - Não muda quem é SOI; muda apenas **o que** está exibido naquele MFD.

### 4.2.3.2 Available Formats by Master Mode

- Descrição qualitativa (não precisa tabela separada) das combinações típicas:
  - NAV: FCR/HSD/SMS/etc.  
  - A‑A: FCR, HSD, SMS, etc.  
  - A‑G: FCR, TGP, HAD, WPN, SMS, HSD.

### 4.2.3.3 Left/Right and SOI Independence

- Deixar cristalino que **DMS Left/Right não mudam SOI**.  
- Explicar o padrão típico:
  - Mover SOI com Up/Down.  
  - Mudar formato no MFD onde o SOI está (ou não está) com Left/Right.

### 4.2.3.4 DMS Left/Right Usage Table

- `hotastable` resumindo:
  - NAV — Left/Right / Short / Cycle formats on left/right MFD.  
  - A‑A — idem, com ênfase em FCR/HSD.  
  - A‑G — idem, com ênfase em FCR/TGP/WPN/HAD.

---

## 5. Section 4.2.4 — Master Mode Behavior — DMS Summary

**Current implementation:** None yet.

**Status alvo:** Short summary section + consolidated table.

**Structure (final):**

```text
4.2.4 Master Mode Behavior — DMS Summary
  4.2.4.1 Directional DMS Roles (Up / Down / Left / Right)
  4.2.4.2 Consolidated DMS × Master Mode Table
```

### 4.2.4.1 Directional DMS Roles (Up / Down / Left / Right)

- Breve recapitulação (1–2 parágrafos) dos papéis:
  - Up: HUD/HMCS SOI quando permitido.  
  - Down: alternar SOI HUD↔MFDs.  
  - Left/Right: ciclar formatos nos MFDs.

### 4.2.4.2 Consolidated DMS × Master Mode Table

- Uma tabela resumen:

  - Linhas: NAV, A‑A, A‑G PRE, A‑G VIS, DGFT, MSL OVRD.  
  - Colunas (exemplo): Up / Down / Left / Right / Notas.

- Objetivo: dar ao leitor uma visão de “o que DMS faz em cada direção” por master mode, com referências cruzadas para 4.2.1–4.2.3 e para a tabela de SOI em 4.1.

---

## 6. WIP File Mapping and To-Do List

**Integrated (Aprroved) WIP files, moved to ARCHIVE\:**

- `section-C4-S1-concept-soi-approved-2026-01-14.tex`
  - Section 4.1 (entire).  
  - Status: integrated into `guide.tex`.

- `section-C4-S2-dms-up-approved.tex`
  - Section 4.2.1 (DMS Up).  
  - Status: integrated into `guide.tex`.

**Deprecated WIP files:**

- `section-C4-S2-dms-up-down-deprecated-2026-01-14.tex`
  - Source of legacy DMS Down text; must **not** be re‑used directly.  
  - Relevant DMS Down content already copied to a separate scratch file.

- `section-C4-S3-dms-format-cycling-deprecated-2026-01-13.tex`
  - Old attempt at format cycling; not to be used as is.

**New WIP files to create:**

1. `section-C4-S2-dms-down-review-2026-01-xx.tex`
   - Implements 4.2.2 per this blueprint.  
   - Uses extracted DMS Down content from deprecated file as raw material, but rewritten for clarity and to avoid redundancy with 4.1.

2. `section-C4-S3-dms-left-right-review-2026-01-xx.tex`
   - Implements 4.2.3 from scratch (format cycling, independent of SOI).  
   - May borrow ideas from deprecated C4‑S3, but not structure.

3. `section-C4-S4-dms-summary-review-2026-01-xx.tex` (or similar naming)
   - Implements 4.2.4 summary and consolidated table.

**Project Tracking updates (to be done in `project-tracking-v5.0.0.md`):**

- Mark Chapter 4:
  - C4‑S1: INTEGRATED (approved).  
  - C4‑S2 (DMS Up): INTEGRATED (approved).  
  - C4‑S2 (DMS Down): IN PROGRESS (TO DO, WIP not yet created).  
  - C4‑S3 (Left/Right): NOT STARTED.  
  - 4.2.4 Summary: NOT STARTED.

- Note archival of deprecated files and creation of `section-C4-S2-dms-up-approved.tex` as the canonical DMS Up section.

---

_End of unified Chapter 4 (DMS) blueprint v1.1_
