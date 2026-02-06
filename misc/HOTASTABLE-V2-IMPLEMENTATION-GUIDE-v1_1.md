# HOTASTABLE v2 Implementation Guide

**Version:** 1.1  
**Date:** 2026-02-05  
**Status:** In Testing  
**Project:** Falcon BMS TMS/DMS/CMS HOTAS Guide

---

## 1. Overview

This document tracks the implementation of the new `hotastable` v2 specification into the guide. It serves as both a technical reference and a progress tracker during the testing phase.

### 1.1 Key Changes from v1

- Updated column widths for better text flow
- Explicit font size (`\small`) and row spacing (`\arraystretch{1.25}`)
- Migration from `tabular` to `longtable` for multi-page support
- **Column 6 (Dash-34): Removed requirement for `\dashref{}` macro** — now accepts free text for flexibility

### 1.2 Implementation Status

- [x] Specification defined
- [x] Test file created (`guide-preamble-test.tex`)
- [x] Preamble integrated into test environment (local machine, `.gitignore` path)
- [ ] Compile test file and verify output
- [ ] Apply to existing WIP tables
- [ ] Validate multi-page behavior
- [ ] Final review and approval
- [ ] Update BRIEFING document
- [ ] Deploy to main guide

---

## 2. Technical Specification

### 2.1 Environment

```latex
\begin{longtable}{|p{1.00cm}|p{0.90cm}|p{0.90cm}|p{3.30cm}|p{6.40cm}|p{1.40cm}|p{2.10cm}|}
```

**Total width:** 15.8 cm (including borders and padding)

### 2.2 Typography

- **Font size:** `\small` (10pt on 11pt base)
- **Row spacing:** `\arraystretch{1.25}`
- **Alignment:** Left-aligned in all columns

### 2.3 Column Definitions

| Column | Width | Content Type | Notes |
|--------|-------|--------------|-------|
| Mode | 1.00cm | Master mode abbreviation | A-A, A-G, NAV, DGFT, MSL, etc. |
| Dir. | 0.90cm | Switch direction | Up, Down, Left, Right, Fwd, Aft |
| Act. | 0.90cm | Actuation type | Short, Long, (empty) |
| Sensor/Mode | 3.30cm | Active sensor or submode | FCR, HSD, SMS, RWR, etc. |
| Effect/Nuance | 6.40cm | What happens + context | Primary description column |
| Dash-34 | 1.40cm | **Free text or reference** | **No longer requires `\dashref{}` macro** |
| Training | 2.10cm | Training mission codes | Uses `\trnref{}` macro |

### 2.4 Standard Header

```latex
\hline
\textbf{Mode} & \textbf{Dir.} & \textbf{Act.} & \textbf{Sensor/Mode} & \textbf{Effect/Nuance} & \textbf{Dash-34} & \textbf{Training} \\
\hline
\endhead
```

**Note:** `\endhead` ensures header repeats on multi-page tables.

---

## 3. Implementation Examples

### 3.1 Scenario 1: Single-Page Table (DMS Down)

```latex
{\small
\setlength{\arrayrulewidth}{0.5pt}
\renewcommand{\arraystretch}{1.25}

\begin{longtable}{|p{1.00cm}|p{0.90cm}|p{0.90cm}|p{3.30cm}|p{6.40cm}|p{1.40cm}|p{2.10cm}|}
\hline
\textbf{Mode} & \textbf{Dir.} & \textbf{Act.} & \textbf{Sensor/Mode} & \textbf{Effect/Nuance} & \textbf{Dash-34} & \textbf{Training} \\
\hline
\endhead

A-A & Down & Short & FCR & Toggles SOI: FCR ↔ SMS & 3-48 & \trnref{TE01} \\
\hline
A-G & Down & Short & HSD & Toggles SOI: HSD ↔ SMS & 3-48 & \trnref{TE02} \\
\hline

\end{longtable}
}
```

### 3.2 Scenario 2: Multi-Page Table (CMS)

Same structure as 3.1, but content extends beyond one page. The `\endhead` ensures the header repeats automatically.

### 3.3 Column 6 Example (Free Text)

**Old style (v1 with macro):**
```latex
... & \dashref{3-48} & ...
```

**New style (v2 with free text):**
```latex
... & 3-48 & ...
... & 3-48, 3-52 & ...
... & See §3.4.2 & ...
... & Multiple refs & ...
```

**Rationale:** Allows flexibility to provide context, multiple references, or explanatory notes without being constrained by macro format.

---

## 4. Migration from v1 to v2

### 4.1 Column Width Mapping

| Column | v1 Width | v2 Width | Change |
|--------|----------|----------|--------|
| Mode | 1.2cm | 1.00cm | -0.20cm |
| Dir. | 1.0cm | 0.90cm | -0.10cm |
| Act. | 1.0cm | 0.90cm | -0.10cm |
| Sensor/Mode | 3.5cm | 3.30cm | -0.20cm |
| Effect/Nuance | 6.2cm | 6.40cm | +0.20cm |
| Dash-34 | 1.5cm | 1.40cm | -0.10cm |
| Training | 2.0cm | 2.10cm | +0.10cm |

**Total:** 16.4cm → 15.8cm (-0.6cm)

### 4.2 Migration Steps

- [x] Define new column widths
- [x] Create test preamble
- [x] Integrate into test file (`guide-preamble-test.tex`)
- [x] Eliminate `\dashref{}` requirement from column 6
- [ ] Update existing tables in WIP files
- [ ] Validate compilation (no overflows)
- [ ] Visual inspection (spacing, alignment)

---

## 5. Testing Checklist

### 5.1 Environment Setup
- [x] Test file created (`guide-preamble-test.tex`)
- [x] Located in `.gitignore` path (local testing only: `C:\Users\carlo\OneDrive\Documentos\projeto-bms\misc`)
- [x] Preamble integrated
- [ ] Compiled successfully with no errors
- [ ] Visual output verified

### 5.2 Content Validation
- [ ] Apply to at least 3 existing tables
- [ ] Test single-page table
- [ ] Test multi-page table (header repetition)
- [ ] Test column 6 with free text (no `\dashref{}`)
- [ ] Verify no text overflow in any column

### 5.3 Quality Gates
- [ ] All tables compile without errors
- [ ] Visual consistency across tables
- [ ] Readable at 100% zoom
- [ ] Professional appearance
- [ ] Consistency with narrative style

---

## 6. Pending Tasks

### Before Approval
1. Complete testing checklist (Section 5)
2. Apply to representative sample of tables
3. Document any edge cases or issues
4. Final review by project lead

### After Approval
1. Update BRIEFING document (see Section 7)
2. Migrate all remaining tables
3. Archive v1 specification
4. Update PROJECT-TRACKING

---

## 7. Required BRIEFING Updates

When v2 is approved, the following sections of BRIEFING-v0.2.0.1.md must be updated:

### 7.1 Section 4.2: Table Formatting Standard (hotastable)

#### CHANGE 1: Total Table Width

**Current text (line ~85):**
```markdown
- Standard HOTAS table width: 15.6 cm.
```

**New text:**
```markdown
- Standard HOTAS table width: 15.8 cm.
```

**Rationale:** Correct calculation based on column widths (1.00 + 0.90 + 0.90 + 3.30 + 6.40 + 1.40 + 2.10 = 15.8 cm).

---

#### CHANGE 2: Add Note About longtable Environment

**Location:** After "Row height multiplier: `\arraystretch = 1.25`." (line ~87)

**Add:**
```markdown
- Environment: `longtable` (not `tabular`) for multi-page support.
- Multi-page tables: Use `\endhead` to repeat header on continuation pages.
```

**Rationale:** Clarifies that HOTAS tables use `longtable`, not `tabular`, and explains multi-page behavior.

---

### 7.2 Section 6.6: Column 6: Dash34 (1.40 cm)

#### CHANGE 3: Remove `\dashref{}` Requirement

**Current text (lines ~140-143):**
```markdown
### 6.6 Column 6: Dash34 (1.40 cm)

Reference relevant Dash-34 sections using macros:
- `\dashref{2.1.5}`
- `\dashref{2.1.5}, \dashref{2.7.1}`
```

**New text:**
```markdown
### 6.6 Column 6: Dash34 (1.40 cm)

Reference relevant Dash-34 sections. Free text format allowed for flexibility:
- Simple reference: `3-48`
- Multiple references: `3-48, 3-52`
- Contextual reference: `See §3.4.2`
- Using macro (optional): `\dashref{2.1.5}`

**Note:** The `\dashref{}` macro is available but NOT required. Use the format that best serves clarity.
```

**Rationale:** Provides flexibility to include multiple references, contextual notes, or simple section numbers without being constrained by macro formatting.

---

### 7.3 Section 12.3.9: HOTAS Table Environment (hotastable)

#### CHANGE 4: Add Width Calculation Note

**Location:** After the `\newenvironment{hotastable}` code block (line ~320)

**Add:**
```markdown
**Total width calculation:** 1.00 + 0.90 + 0.90 + 3.30 + 6.40 + 1.40 + 2.10 = **15.8 cm**
```

**Rationale:** Explicitly documents the total width for verification and troubleshooting.

---

### 7.4 Complete List of Required BRIEFING Changes

#### CHANGE 1: Line 153 — Section 4.1 Geometry Configuration

**BEFORE:**
```markdown
- Standard HOTAS table width: 15.6 cm.
```

**AFTER:**
```markdown
- Standard HOTAS table width: 15.8 cm.
```

---

#### CHANGE 2: Line 168 — Section 4.2 Table Formatting Standard (Column Layout)

**BEFORE:**
```markdown
- **Dash34** (1.40 cm): Dash-34 section references using `\\dashref{}`.
```

**AFTER:**
```markdown
- **Dash34** (1.40 cm): Dash-34 section references (free text or `\\dashref{}` macro).
```

---

#### CHANGE 3: Lines 230-234 — Section 6.6 Column 6: Dash34 (1.40 cm)

**BEFORE:**
```markdown
### 6.6 Column 6: Dash34 (1.40 cm)

Reference relevant Dash-34 sections using macros:
- `\\dashref{2.1.5}`
- `\\dashref{2.1.5}, \\dashref{2.7.1}`
```

**AFTER:**
```markdown
### 6.6 Column 6: Dash34 (1.40 cm)

Reference relevant Dash-34 sections. Free text format allowed for flexibility:
- Simple reference: `3-48`
- Multiple references: `3-48, 3-52`
- Contextual reference: `See §3.4.2`
- Using macro (optional): `\\dashref{2.1.5}`

**Note:** The `\\dashref{}` macro is available but NOT required. Use the format that best serves clarity.
```

---

#### CHANGE 4: Line 599 — Section 12.3.9 HOTAS Table Environment (hotastable)

**BEFORE:**
```markdown
- **Column widths:** Optimized for 15.6 cm total width (Mode 1.00, Dir. 0.90, Act. 0.90, Function 3.30, Effect/Nuance 6.40, Dash34 1.40, Train. 2.10)
```

**AFTER:**
```markdown
- **Column widths:** Optimized for 15.8 cm total width (Mode 1.00 + Dir. 0.90 + Act. 0.90 + Function 3.30 + Effect/Nuance 6.40 + Dash34 1.40 + Train. 2.10 = 15.8 cm)
```

---

#### CHANGE 5: Line 615 — Section 12.3.10 Simple Reference Macros

**BEFORE:**
```markdown
- **dashref:** Dash-34 section references (`\dashref{2.1.5}` → "Dash-34 § 2.1.5")
```

**AFTER:**
```markdown
- **dashref:** Optional Dash-34 section references (`\dashref{2.1.5}` → "Dash-34 § 2.1.5"). Free text also allowed in Column 6.
```

---

#### Summary Table

| # | Line | Section | Change Type | Description |
|---|------|---------|-------------|-------------|
| 1 | 153 | 4.1 | Correction | Update total width: 15.6 cm → 15.8 cm |
| 2 | 168 | 4.2 | Update | Dash34 column now accepts free text or macro |
| 3 | 230-234 | 6.6 | Replacement | Complete rewrite of Column 6 guidelines |
| 4 | 599 | 12.3.9 | Correction | Fix total width calculation with formula |
| 5 | 615 | 12.3.10 | Update | Note that dashref macro is optional |

---

## 8. Version History

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-02-05 | Initial specification |
| v1.1 | 2026-02-05 | Added: Column 6 free text change, testing progress checkboxes, complete BRIEFING update specification with exact line numbers and replacement text |

---

**Document Status:** 🟡 In Testing  
**Next Review:** After compilation of test file and visual verification  
**Approved By:** Pending
