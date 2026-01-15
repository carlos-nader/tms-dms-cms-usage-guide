# C4 Design Notes — PDF Files Analysis (TMS vs DMS & DMS Chapter Reference)

**Prepared:** 15 January 2026, ~02:41 -03  
**Scope:** Analysis of the two legacy PDF design documents related to TMS and DMS:

- `TMS-vs-DMS.pdf`
- `DMS-chapter-reference.pdf`

Goal: Clarify how each document should (or should not) be used under the **current, unified Chapter 4 (DMS) blueprint v1.1**, and how they interact with the locked TMS structure (Chapter 3).

---

## 0. Context and Position in the Project

By the time of these PDFs (05 January 2026):

- **TMS (Chapter 3)** was being restructured and then locked.
- **DMS (Chapter 4)** still followed an older, more generic outline:
  - 4.1 Concept and SOI control
  - 4.2 DMS in Air-to-Air
  - 4.3 DMS in Air-to-Ground
  - 4.4 Block/variant notes
- The project had not yet introduced the **direction-based DMS structure** later adopted in the unified C4 blueprint v1.1:

  ```text
  4.1 Concept and SOI
  4.2 DMS Switch Actuation (Up / Down / Left / Right)
  4.2.4 Master Mode Behavior — DMS Summary
  ```

The two PDFs capture an **intermediate design stage**, where questions about symmetry between TMS and DMS were still open.

This note documents how to treat them **today**:

- What remains valid and helpful.
- What has been superseded by the new C4 blueprint.
- How each document should be used in future AI-assisted work on C3/C4.

---

## 1. `TMS-vs-DMS.pdf`

### 1.1 What this document is

- A **comparative design analysis** between the then-new **TMS structure (Chapter 3)** and the still-old **DMS structure (Chapter 4)**.
- It:
  - Locks and justifies the **TMS chapter structure** (3.1–3.6, including the new 3.2 SA displays section).
  - Presents the old DMS outline (4.1–4.4) as **“to be analyzed”**.
  - Provides a **question-driven framework** for deciding whether DMS should mirror TMS in certain aspects.
- It is essentially a **governance / architecture decision document**, not a raw Dash‑34 research extract.

### 1.2 Locked TMS structure — still authoritative

The TMS part of the document defines and locks the following structure:

```text
3.1 Concept and general behaviour
3.2 TMS and Situational Awareness displays (HSD, HSI, DED)
  3.2.1 HSD cursor control and waypoint management
  3.2.2 Integration with NAV master mode
  3.2.3 Cross-mode SA display interaction (A-A, A-G context)
3.3 TMS in Air-to-Air (6 subsections)
3.4 TMS in Air-to-Ground (4 subsections)
3.5 TMS in A-G weapon employment (6 subsections)
3.6 TMS -- Block / variant notes
```

Key implications:

- **Chapter 3 (TMS)** is explicitly centered around:
  - Concept and fundamentals (3.1).
  - A strong **Situational Awareness (SA) section** (3.2) for HSD/HSI/DED.
  - A clear separation of:
    - SA displays → Radar → Ground sensors → Weapons.
- This structure is described as **"locked"** and is still the main reference for future TMS work.

Use today:

- As the **canonical contract** for Chapter 3 layout.
- As a checklist when writing or revising TMS content.

### 1.3 DMS questions raised (and how the current blueprint answered them)

The document asks four major questions about DMS, by analogy with TMS.

#### Q1 — “DMS precisa de uma seção de SA displays (como TMS 3.2)?”

- Question in the PDF:
  - Should there be a “DMS and SA Displays (HSD, HSI, DED)” section similar to TMS 3.2?

- Current answer (C4 blueprint v1.1):
  - **No.**
  - DMS is not modeled as “o switch das SA displays”.
  - Cap. 4 is organized by **direções de DMS** (Up/Down/Left/Right) e **master modes**, com SA displays aparecendo como consumidores de SOI/formats, não como eixo primário do capítulo.

Effect:

- The proposal to create a “DMS & SA displays” section is now **historical**.
- The value of this part of the PDF is mainly to remind why TMS ganhou essa seção e DMS não.

#### Q2 — “NAV master mode merece seção explícita em DMS?”

- Question in the PDF:
  - Should there be an explicit “DMS in NAV master mode” subsection?

- Current answer:
  - **No** em forma de seção dedicada.
  - **Yes** in tabular/matrix form:
    - NAV entra como uma linha/coluna nas tabelas de 4.2.1 (Up), 4.2.2 (Down), 4.2.3 (Left/Right) e no resumo 4.2.4, mas **não** vira um grande bloco narrativo “DMS em NAV”.

Effect:

- A importância de NAV foi reconhecida.
- Mas o tratamento final é **matricial (direção × modo)**, não uma subseção “DMS & NAV”.

#### Q3 — “IAM/HARM/Harpoon como ‘special cases’ no Cap. 4?”

- Question:
  - Should special cases for IAM/HARM/Harpoon be a subsection in DMS, or move to weapon-specific chapters?

- Current answer:
  - **Armas específicas** (IAM, HARM, Harpoon, etc.) são tratadas principalmente nos capítulos de armas.
  - Cap. 4 só precisa incluir **exceções de DMS** em tabelas e notas (por exemplo, quando uma arma limita ou altera algum caminho de DMS).

Effect:

- A antiga ideia de 4.3.2 “special cases (IAM, HARM, Harpoon)” foi **abandonada** como seção estruturante.
- O PDF continua útil para lembrar que, se algo de DMS é realmente especial num certo weapon mode, isso vira **nota/exceção** e não mini-capítulo.

#### Q4 — “DMS cross-mode choreography merece seção própria?”

- Question:
  - Should there be a dedicated “DMS cross-mode choreography” section, analogous to TMS 3.2.3?

- Current answer:
  - **Sim em espírito, não em formato textual longo.**
  - O blueprint v1.1 resolveu isso com:
    - 4.2.4 Master Mode Behavior — DMS Summary
      - 4.2.4.1 Directional DMS Roles (Up / Down / Left / Right)
      - 4.2.4.2 Consolidated DMS × Master Mode Table

Effect:

- A necessidade de tratar “cross-mode behavior” foi validada.
- A resposta final é mais concisa: uma seção de resumo + tabela consolidada.

### 1.4 How to use `TMS-vs-DMS.pdf` going forward

For **Chapter 4 (DMS)** specifically:

- Treat this document as **legacy governance / decision history**:
  - It explains why DMS does **not** mirror TMS structurally.
  - It is **not** a direct source of content for current C4 sections.

For **Chapter 3 (TMS)**:

- Use the “Locked TMS Structure” portion as the **authoritative layout reference**.

For versioning:

- The versioning strategy (v0.1.2 → v0.1.3) is now outdated and should be seen only as historical context.

Practical label:

> **Classification:** Legacy design/architecture reference — keep for structural context and TMS contract, not as a content template for C4.

---

## 2. `DMS-chapter-reference.pdf`

### 2.1 What this document is

This is a **formal design reference for Chapter 4 (DMS)**, with:

- Clear separation between **Chapter 2** (HOTAS fundamentals) and **Chapter 4** (DMS specifics).
- A detailed **old C4 outline** (Option B renamed) with:
  - 4.1 Concept & SOI (4.1.1–4.1.3).
  - 4.2 DMS in MFDS format selection and SWAP (4.2.1–4.2.3).
  - 4.3 DMS in sensor/weapon context (A‑A, A‑G, HAD, IAMs).
  - 4.4 DMS Block & variant notes.
- Two global “focus points” for the chapter:
  - DMS does **not** perform tactical functions.
  - NAV/A‑A/A‑G are **contexts**, not different DMS implementations.
- A **compact Dash‑34 cross-reference table**.
- A **writing checklist** with 14 items, guiding C4 drafting.

It is half **conceptual contract**, half **writing guide**.

### 2.2 Sections that remain fully relevant

#### 2.2.1 Avoiding overlap between Chapter 2 and 4

The document defines roles:

- **Chapter 2** (HOTAS Fundamentals):
  - Defines SOI, short/long presses, master modes, overview of switches.
  - Does **not** enumerate DMS actions or detailed combinations.
- **Chapter 4** (DMS):
  - Takes the SOI concept and implements it **concretely** with DMS.
  - Focuses on MFDS mechanics, SWAP, and actual page/format handling.

This separation is still exactly what the project needs.

Use:

- As enduring governance: always check new material to avoid leaking C4-specific DMS behaviors back into Chapter 2.

#### 2.2.2 4.1.1–4.1.3 (SOI concept, DMS role, example flow)

The proposed content for:

- **4.1.1 SOI definition and scope across displays**
- **4.1.2 Role of the DMS in SOI selection**
- **4.1.3 Example SOI flow (overview)**

is highly aligned with the current blueprint and the now-final C4‑S1 section:

- 4.1.1 describes SOI in a way that:
  - Anchors to MFDS SOI (Dash‑34 2.1.6.3).
  - Anchors to HUD SOI (Dash‑34 2.1.7.5.4).
- 4.1.2 explains DMS Up/Down/Left/Right in conceptual terms, with emphasis that DMS does **not** do targeting or weapons.
- 4.1.3 presents a short example flow (NAV HSD → A‑G FCR → TGP → WPN).

Caveat:

- The description of DMS Left/Right in 4.1.2 mixes:
  - SOI movement between pages
  - With selecting primary formats.
- The unified blueprint later clarified the axes more cleanly:
  - **Up/Down:** main SOI routing axis (HUD ↔ MFDs).
  - **Left/Right:** main format cycling axis on the MFD that already has SOI.

Use:

- As a **source of phrasing, examples and key points** for C4‑S1 (already largely integrated), with minor wording adjustments to reflect the final DMS Up vs Left/Right split.

#### 2.2.3 4.4 DMS Block and Variant Notes

This part remains directly usable:

- It emphasizes:
  - Record only **real** block/variant differences.
  - Focus on MFDS page availability and SOI‑capable displays.
  - Avoid duplicating identical behavior.

Use:

- As the conceptual backbone for the final 4.4 section under the unified blueprint.

#### 2.2.4 Focus Points 1 and 2 (Section 3)

Two global principles for the entire chapter:

1. **DMS does not perform tactical functions:**
   - Does not lock, generate SPI, MARK, release weapons, command radar modes, alter weapon parameters, or perform IFF.
   - Those tasks belong to TMS, WPN/SMS logic, sensors, ICP/MARK.

2. **NAV / A‑A / A‑G are contexts, not different DMS implementations:**
   - The DMS mechanics (SOI + format + SWAP) are the same.
   - What changes is which pages tend to be SOI and how those pages behave internally.

Use:

- As **chapter-wide style rules** and as a QA checklist for every DMS HOTAS table (especially the Effect/Nuance columns).

#### 2.2.5 Dash‑34 Cross‑Reference (Section 4)

Summarizes the key Dash‑34 sections needed for C4:

- HOTAS overview, MFDS, SOI, OFF/BLANK/SWAP, SMS/WPN, pages FCR/TGP/HSD/HAD, HUD SOI, FCR A‑A modes.

Use:

- As quick index of primary references when validating any C4 text.

#### 2.2.6 Writing Checklist (Section 5)

A 14‑item checklist to validate:

- Correct anchoring to Dash‑34 sections.
- Correct separation DMS vs TMS/weapon logic.
- Correct referencing of official page names (HAD, SMS/WPN) and block differences.

Even though section numbers have shifted in the new blueprint (e.g., 4.2/4.3 vs 4.2.1–4.2.4), the **semantic intent** of each item continues valid.

Use:

- Adjust mental mapping of numbers.
- Use as **final QA pass** once C4 is drafted.

### 2.3 Sections partially superseded but still useful as content bank

#### 2.3.1 4.2 DMS in MFDS format selection and SWAP

Subsections:

- 4.2.1 MFDS format selection and cycling.
- 4.2.2 SWAP and display management.
- 4.2.3 HSD control via SOI.

Today, the unified blueprint has:

- 4.2.3 DMS Left / Right: Cycle MFD Formats
  - 4.2.3.1 Format Cycling Mechanics
  - 4.2.3.2 Available Formats by Master Mode
  - 4.2.3.3 Left/Right and SOI Independence
  - 4.2.3.4 DMS Left/Right Usage Table

Relationship:

- The old **4.2.1/4.2.2** contain good narrative descriptions of:
  - How DMS participates in format selection.
  - How SWAP and DMS interplay.
- The old **4.2.3 (HSD control via SOI)** reinforces the separation:
  - DMS makes HSD SOI.
  - HSD’s own controls do zoom/declutter/etc.

Use:

- As **content source** (phrasing and examples) for:
  - 4.2.3.1–4.2.3.4 in the new blueprint.
  - Short clarifications wherever HSD appears in C4.
- Avoid re-creating a separate “4.2.3 HSD control” section; integrate the ideas into the new structure.

#### 2.3.2 4.3 DMS in sensor and weapon context

Subsections:

- 4.3.1 SOI changes between FCR, TGP, HSD and HUD in A-A.
- 4.3.2 SOI changes between FCR, TGP, HSD, HAD and WPN in A-G.
- 4.3.3 DMS with HARM HAD page as SOI.
- 4.3.4 DMS with IAMs and SMS/WPN pages.

These subsections are essentially **narrative flows**:

- They show typical A‑A and A‑G SOI choreography.
- They reinforce the division of labor (DMS vs TMS vs weapon logic).

In the current architecture:

- Detailed flows live mainly in:
  - Chapter 6 (training flows and step-by-step sequences).
  - Weapon/sensor-specific chapters.
- Chapter 4 uses **shorter examples** (e.g. in 4.1.3) and focuses on:
  - Direction × master mode behavior (4.2.x, 4.2.4).

Use:

- As **example bank** for:
  - 4.1.3 (already a short flow example).
  - Future Chapter 6 content.
- Avoid reconstructing a large “4.3 sensor & weapon context” block in C4.

### 2.4 Overall classification for `DMS-chapter-reference.pdf`

- **Core governance & conceptual sections** (keep as living reference):
  - Separation Cap. 2 × Cap. 4.
  - 4.1.1–4.1.3 (already mostly integrated in C4‑S1).
  - 4.4 block/variant notes.
  - Focus points 1 and 2 (DMS is not tactical; modes are contexts).
  - Dash‑34 cross‑ref table.
  - Writing checklist.

- **Content-bank sections** (referenced, but re-mapped under new blueprint):
  - 4.2.x (format selection, SWAP, HSD via SOI).
  - 4.3.x (A‑A/A‑G/HAD/IAM flows).

- **Superseded structural elements:**
  - The old numbering and chapter topology (4.2/4.3 as big contextual sections) are replaced by the direction-based structure of C4 blueprint v1.1.

Practical label:

> **Classification:** High-value design/writing guide for C4; structural outline partially superseded, but conceptual constraints and examples remain very useful.

---

## 3. How to Use These Two PDFs in Future AI Sessions

When running a future AI-assisted session to work on C3/C4:

### 3.1 Load order and roles

1. **For DMS (Chapter 4):**
   - Load:
     - Unified C4 blueprint v1.1 (`C4-DMS-blueprint.md`).
     - `DMS-chapter-reference.pdf` (this analysis file as guide + original for details).
     - `section_4_3_plan-possibly-old-verify-against-blueprint.md` and `MFD-formats.md` (for MFDS technical details and format cycling).
   - Use this `pdf-files-analysis` note to:
     - Remember which parts of the PDFs are governance.
     - Remember which parts are just historical structure.

2. **For TMS (Chapter 3):**
   - Load:
     - `TMS-vs-DMS.pdf` to ensure the **locked TMS structure** is respected.

### 3.2 Practical guardrails distilled from these PDFs

- **Do not turn Chapter 4 into a second TMS chapter:**
  - No giant “DMS & SA displays” block.
  - No weapon‑centric subsections mirroring TMS 3.5.
- **Keep DMS limited to SOI/format/SWAP:**
  - Never attribute target/SPI/weapon logic to DMS.
- **Use modes (NAV/A‑A/A‑G) as contexts, not different DMS implementations:**
  - Show them through tables and short examples, not separate big narrative blocks.
- **Respect locked TMS structure:**
  - Any cross-references from C4 to C3 should align with the approved 3.1–3.6 layout.

With these interpretations consolidated, these two PDFs remain valuable **design references and QA tools**, even though their proposed “Option B” chapter layout for DMS has been superseded by the more refined, direction-based C4 blueprint v1.1.
