# LIST OF HOTAS TABLES — IMPLEMENTATION GUIDE (Automated, Explicit, Full Examples)
**Version:** v2.0  
**Date:** 2026-02-05  
**Status:** Ready for integration (FULL STANDARD: HOTASTABLE-V2)  
**Author:** [Seu Nome Aqui]  
**Project:** Falcon BMS TMS/DMS/CMS Guide

---

## SUMMARY

This guide delivers the **complete, explicit implementation** of the HOTAS table environment and index for LaTeX, **all code and documentation included**—no steps skipped, no references to external files.  
All macros, package calls, example usages, troubleshooting, Python lint script, and migration instructions are here, tailored to HOTASTABLE-V2-IMPLEMENTATION-GUIDE-v1_0.md.  
Suited for onboarding, governance, and CI/CD at scale.

---

## 1. OBJECTIVES

- **Automate and “idiot-proof” all HOTAS tables:**  
  — Enforce layout, font, padding, row height, column widths, color header, multipage continuity.  
  — Dedicated HOTAS table index.  
  — Impossible to break by accident, copy-paste, or human error.  
  — Validatable by linter.  
  — Documented for all contributors.

---

## 2. WHY THIS DESIGN? — RATIONALE

**Hardcoded as prescribed in HOTASTABLE-V2-*.md (lines 89–119):**

- `\footnotesize` = 8pt (not `\small` = 9pt).
- `\setlength{\tabcolsep}{3pt}` (not default 2pt).
- `\renewcommand{\arraystretch}{1.35}` (not default 1.0 or hotspot 1.25).
- Exact column specs.
- Strong color header, white bold, centralized layout.
- True multipage continuity (firsthead, head, foot, lastfoot).
- Only argument-based use; forbidden manual captions.
- Automated index registration via `.lot` file, HOTAS-only.

---

## 3. DEPENDENCIES — TECHNICAL REQUIREMENTS

### 3.1.  LaTeX Packages (Preamble)

Copy BEFORE any table (in your project or template):

```latex
% ESSENTIAL FOR HOTASTABLE-V2
\usepackage{array}       % L{width} column type & vertical alignment
\usepackage{longtable}   % Multipage tables
\usepackage{xcolor}      % Colors and row coloring

% COLOR DEFINITION
\definecolor{headerblue}{HTML}{003366}
```

### 3.2. Custom Column Type

Define the L column type once for precision (ragged right):

```latex
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
```

---

## 4. FULL AUTOMATED ENVIRONMENT — HOTASTABLE-V2

Paste directly into your preamble:

```latex
% ========== HOTAS TABLES DEDICATED INDEX SECTION ==========
\newcommand{\listofhotastables}{%
  \section*{List of HOTAS Tables}
  \addcontentsline{toc}{section}{List of HOTAS Tables}
  \input{hotas.lot}
}

% ========== HOTASTABLE-V2 ENVIRONMENT ==============
%
% Usage:
%   \begin{hotastable}{Caption/Title Text}
%      ... hotas rows ...
%   \end{hotastable}
%

\newenvironment{hotastable}[1]{%
  % Font: 8pt enforced
  \footnotesize
  % Cell padding: 3pt
  \setlength{\tabcolsep}{3pt}
  % Row height: 1.35x
  \renewcommand{\arraystretch}{1.35}
  % Begin table, forced column layout
  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{1.60cm}}
    % Caption with argument; HOTAS .lot registration
    \caption{#1}\label{hotas:#1}%
    \addcontentsline{hotas.lot}{table}{HOTAS Table: #1}
    % HEADER ROW FIRST PAGE — colored, bold, white, centered
    \rowcolor{headerblue}
    \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
    \endfirsthead
    % HEADER ROW FOR FOLLOWING PAGES
    \rowcolor{headerblue}
    \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
    \multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
    \endhead
    % FOOTER FOR PAGES (except last)
    \multicolumn{7}{r}{\small\emph{Continued on next page}}\\
    \endfoot
    % FOOTER FOR LAST page
    \endlastfoot
}{%
  % End table
  \end{longtable}
}
```

**Every parameter (font, padding, columns, header style, multipage, index registration) is included—no dependency omitted.**

---

## 5. EXAMPLES — USAGE & VARIANTS

### 5.1. Standard Table Example

```latex
\begin{hotastable}{CMS Switch Modes Overview}
Mode & Dir. & Act. & Function & Effect / Nuance & Dash34 & Train. \\
AUTO & Up & Short & Executes auto CMDS & Dispenses program X automatically & 2.7.1.1 & \trnref{9 (Failures)} \\
SEMI & Down & Short & Manual semi CMDS & Pilot selects program & 2.7.2.2 & \trnref{12 (HARM)} \\
MAN & Up & Long & Manual & Direct CMD control & N/A & \trnref{5 (Chaff)} \\
\end{hotastable}
```

### 5.2. Multi-page Table Variant (with long content)

```latex
\begin{hotastable}{Long HOTAS Table Example}
Mode & Dir. & Act. & Function & Effect / Nuance & Dash34 & Train. \\
AUTO & Up & Short & Text... & Text... & ... & ... \\
% ... dozens of rows, multi-page ...
\end{hotastable}
```
- Header is repeated, footers show page continuity.

### 5.3. Table with Footnotes and Labels

```latex
\begin{hotastable}{ECM Modes and Notes}
Mode & Dir. & Act. & Function & Effect/Nuance\footnote{Explanatory footnotes allowed!} & Dash34 & Train. \\
\label{tab:ecm-modes}
AUTO & Up & Short & ... & ... & ... & ... \\
SEMI & Down & Short & ... & ... & ... & ... \\
\end{hotastable}
```

### 5.4. Cross-reference

```latex
See Table~\ref{hotas:CMS Switch Modes Overview} for details.
```

### 5.5. Using the HOTAS Index

```latex
\listofhotastables
```
—Will show HOTAS-only tables, never any generic or legacy tables.

---

## 6. TROUBLESHOOTING & COMMON ERRORS

| Error                           | Cause                            | Fix                                            |
|----------------------------------|-----------------------------------|------------------------------------------------|
| Table format broken              | Omitted packages                  | Ensure `array`, `xcolor`, `longtable` imported |
| Columns wrong/label missing      | Manual edits                      | Use ONLY hotastable environment, argument title|
| Caption/manual outside env       | Legacy table code                 | Migrate to new env and remove caption          |
| Color header missing             | `headerblue` undefined            | Ensure `\definecolor{headerblue}{HTML}{003366}`|
| Multipage breaks                 | Not using `longtable`             | Only use inside hotastable, not table/figure   |
| Padding or font too tight        | Default settings active           | Env auto-fixes (`\footnotesize`, `\tabcolsep`) |
| Table not in HOTAS index         | Env not used or index not inserted| Use hotastable and `\listofhotastables`        |

---

## 7. MIGRATION — LEGACY TO HOTASTABLE-V2

**Checklist:**
- [ ] Backup all `.tex` and template files.
- [ ] Add package calls and macros shown above.
- [ ] Replace ALL legacy tables (`\begin{table}`, `\begin{longtable}`) with `\begin{hotastable}{Caption}`.
- [ ] Remove ALL manual caption/header rows.
- [ ] Supply the table title as environment argument.
- [ ] Insert `\listofhotastables` where HOTAS index is needed.
- [ ] Test for conformance (output, index, format).
- [ ] Run lint script before merge/release.
- [ ] Update governance docs (BRIEFING, SYSTEM).
- [ ] Onboard contributors using SPECIFIC examples.

---

## 8. PYTHON LINT/AUDIT SCRIPT EXAMPLES

### 8.1. Basic Linter: Detects Legacy and Manual Tables

```python name=lint_hotastables.py
import re
from pathlib import Path

def scan_tex_files():
    correct_env = r'\\begin{hotastable}\{'
    legacy_table = r'\\begin{table}'
    legacy_longtable = r'\\begin{longtable}'
    manual_caption = r'\\caption\{'
    issues = []

    for tex_file in Path('.').rglob('*.tex'):
        text = tex_file.read_text(encoding='utf-8', errors='ignore')
        if re.search(legacy_table, text) or re.search(legacy_longtable, text):
            issues.append(f'✗ Legacy table/longtable detected in {tex_file}')
        if re.search(manual_caption, text) and not re.search(correct_env, text):
            issues.append(f'✗ Manual caption detected in {tex_file} (should only use hotastable env)')
    if issues:
        for issue in issues:
            print(issue)
        exit(1)
    else:
        print("✔ All HOTAS tables are conformant.")

if __name__ == "__main__":
    scan_tex_files()
```

### 8.2. Advanced Linter: Checks Column Structure, Header, Index registration

```python name=lint_hotastables_advanced.py
import re
from pathlib import Path

def check_columns(text):
    pattern = r'\\begin{longtable}\{L\{1\.00cm\} L\{0\.90cm\} L\{0\.90cm\} L\{3\.30cm\} L\{6\.40cm\} L\{1\.40cm\} L\{1\.60cm\}\}'
    return bool(re.search(pattern, text))

def scan_tex_files():
    issues = []
    for tex_file in Path('.').rglob('*.tex'):
        text = tex_file.read_text(encoding='utf-8', errors='ignore')
        if '\\begin{hotastable}' not in text:
            issues.append(f'✗ Missing hotastable environment in {tex_file}')
        if not check_columns(text):
            issues.append(f'✗ Incorrect columns in {tex_file}')
        if '\\rowcolor{headerblue}' not in text:
            issues.append(f'✗ Missing header color in {tex_file}')
        if '\\addcontentsline{hotas.lot}' not in text:
            issues.append(f'✗ Missing HOTAS .lot registration in {tex_file}')
    if issues:
        for issue in issues:
            print(issue)
        exit(1)
    else:
        print("✔ All tables FULLY conformant.")

if __name__ == "__main__":
    scan_tex_files()
```

---

## 9. EDGE CASES, TESTS & FUTURE PROOFING

- Variant for footnotes, wide cells, unusual content: Test multi-line, math, or special symbols inside any cell.
- For future new types (training, reference): Copy env, change columns, header, index file.
- For multi-language/caption: Adapt only the argument to environment, header row remains locked.

---

## 10. GOVERNANCE, MAINTENANCE, ONBOARDING

- Document this guide in team folders and `.github/copilot-instructions.md`.
- Prohibit any manual table edits except through environment.
- Require linter run (Python scripts above) before every PR/merge.
- Template-wip MUST reference the explicit example above.
- Encourage peer review for all table additions/changes.
- Audit and update macros if any spec changes.

---

## 11. CHANGE LOG

**v2.0 (2026-02-05):**  
- First explicit, full-detail guide and idiom-proof implementation aligned with HOTASTABLE-V2.

---

## END OF GUIDE