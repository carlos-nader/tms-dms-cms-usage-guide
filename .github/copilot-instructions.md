
# AI Agent Instructions — Falcon BMS TMS/DMS/CMS Guide Project

## Project Overview

This is a **LaTeX-based technical documentation project** developing a comprehensive usage guide for F-16 HOTAS switches (TMS/DMS/CMS) in Falcon BMS 4.38.1 flight simulator. The project uses a strict governance framework with version control, WIP file lifecycles, and AI-assisted content development.

**Current Status:** Pre-publication phase (v0.4.1.1), 4/7 chapters completed, targeting v1.0 publication

**Primary Languages:** LaTeX (content), Python (automation), PowerShell (validation)


## Critical Governance & Style Documents (Read These First)

All governance and style documents are mandatory reading before making any changes. They are distributed mainly in `/docs/` and `/misc/`:

1. **[briefing.md](../docs/briefing.md)** — Project structure, LaTeX guidelines, macros, layout, table standards, and environments.
2. **[version-system.md](../docs/version-system.md)** — Versioning (pre- and post-publication), bump rules, snapshots.
3. **[wip-naming.md](../docs/wip-naming.md)** — Naming conventions for WIP files, lifecycle (dev → review → final → approved → deprecated).
4. **[project-tracking.md](../docs/project-tracking.md)** — Progress tracking, chapter status, development log.
5. **[STYLE-GUIDE.md](../misc/STYLE-GUIDE.md)** — Official style guide for all project prose (introductions, descriptions, continuous text table cells, etc.).

**Important:**
- STYLE-GUIDE.md covers only prose and narrative. BRIEFING covers only LaTeX structure, macros, and layout.
- Always consult both before generating textual or structural content.
- Never modify governance documents without explicit approval.


## Project Structure & Workflows


### Main Folders & Their Roles

- **archive/**: Snapshots históricos, WIP aprovados, versões antigas do guia.
- **docs/**: Documentos de governança, diagramas de fluxo, documentação auxiliar, arquivos SVG/PNG de referência.
- **fig/**: Imagens, figuras, fontes visuais, arquivos de licenciamento de imagens.
- **misc/**: Decisões de projeto, style-guide, fontes externas, análises.
- **scripts/**: Scripts de automação (geração de relatórios, validação, rastreamento). Nunca editar sem consulta explícita.
- **template/**: Templates oficiais. Apenas template-wip.tex deve ser usado para novos WIP.
- **wip/**: Arquivos em desenvolvimento, PDFs gerados, estrutura ativa.

**Outros arquivos importantes:**
- **README.md**: Status do projeto, links principais, aviso de revisão de estilo em andamento.
- **SETUP.md**: Guia de preparação do ambiente e ferramentas.
- **LICENSE**: CC BY-NC 4.0. Todo conteúdo deve ser compatível.
- **INTEGRATED-FILES.md**: Relatório gerado automaticamente. Nunca editar manualmente.


### WIP File Lifecycle

All WIP files **MUST** be created from `template/template-wip.tex` (canonical template).

**Naming Pattern:** `{type}-C{N}[-S{M}]-{title}-{status}-{date}.tex`

- **Example:** `section-C4-S2-dms-up-final-2026-01-14.tex`
- **Status codes (standard flow):** `dev` (draft) → `review` (under review) → `final` (ready to integrate) → `approved` (integrated & archived) → `deprecated` (retired)
- **Alpha status (parallel, optional):** `alpha` — approved by the author; integrated into the alpha pre-release snapshot; WIP file remains in `wip/` until official integration into `guide.tex`. Active only when pre-release infrastructure is in progress.

**Workflow:**
1. Copy `template/template-wip.tex` to `wip/`
2. Rename following the pattern above
3. Edit content (development status: `dev`)
4. Human review (status: `review`)
5. Finalize (status: `final`)
5A. **Alpha** *(parallel, optional)* — Human renames to `alpha` status after creating the alpha pre-release snapshot. Only used when pre-release infrastructure is active.
6. **Human integrates** into `guide.tex` (AI assists but does NOT perform integration)
7. Move to `archive/WIP/` with status `approved`


### Version Bumping Rules (0.x.x.x Pre-publication)

**When to bump versions:**
- **MINOR (0.x.0.0)** — New chapter integrated
- **PATCH (0.x.x.0)** — Structural change within existing chapter (e.g., first major table)
- **SUBPATCH (0.x.x.x)** — Small refinements, typo fixes, local polish

**Process:**
1. Update macros in `guide.tex` preamble: `\docversion`, `\docbuild`, `\docenddate`
2. Save snapshot to `wip/guide/guide-v{VERSION}-{YYYYMMDD}.tex`
3. Copy snapshot to `guide.tex` (must be identical)
4. Update `docs/project-tracking.md`
5. Move previous snapshot to `archive/GUIDE/`
6. Create GitHub tag and release

**Never** manually increment versions — follow the decision tables in [version-system.md](../docs/version-system.md).


## Style, LaTeX & Content Standards

### Prose Style (misc/STYLE-GUIDE.md)
- Strictly follow STYLE-GUIDE.md for all prose: introductions, descriptions, continuous text table cells, etc.
- Prose must be direct, without justifications, without introductory phrases, without creative synonyms, without redundant conclusions.
- Examples and principles are detailed in STYLE-GUIDE.md.

### LaTeX & Structure (docs/briefing.md)
- Always use the consolidated preamble (docs/tex-preamble-consolidated.md).
- Follow the environment standards, macros, and layout defined in briefing.md.
- HOTAS tables: always use \begin{hotastable} (15.50cm width) with standardized columns and alignment.
- Cross-references in tables: \dashref{X.Y.Z}, \trnref{NN}, \dashone{X.Y.Z}, \dashrefs{...}. Document references: \secref{}, \chapref{}, \tabref{}, \figref{}, \imglink{}.
- Never use placeholders like "TBD" or "TODO".
- **Language Policy:** All LaTeX document content must be written in English. All chat responses, explanations, and planning discussed with the user must be in Portuguese.


## Scripts & Automation

### `generate-integrated-files.py`

Auto-generates tracking reports (`INTEGRATED-FILES.md` and `.json`) showing:
- Tracked files in `wip/`, `archive/`, `docs/`
- Recent commits, tags, releases
- Open issues and milestones

**Triggered by:** GitHub Actions on push (see `.github/workflows/generate-integrated-files.yml`)

### `update-readme-version.py`

Updates README.md version badges when new tags are created.

**Triggered by:** GitHub Actions on tag creation

### PowerShell Validation

`check-guide-integrity.ps1` — Validates byte-identical match between `guide.tex` and active snapshot.


## Development & Automation Commands

### Compile LaTeX

```powershell
# In TeXstudio (preferred) or command line
pdflatex guide.tex
```

### Run Integrity Check

```powershell
.\check-guide-integrity.ps1
```

### Generate Tracking Report

```powershell
python scripts/generate-integrated-files.py
```


## Common Tasks for AI Agents

### Creating New WIP Content

1. Copy `template/template-wip.tex` to `wip/`
2. Rename: `section-C{N}-S{M}-{descriptive-title}-dev-{YYYY-MM-DD}.tex`
3. Edit metadata section (file identification, description, status)
4. Develop content following BRIEFING style guidelines
5. **Never** integrate into `guide.tex` without human approval

### Reviewing Existing WIP Files

1. Check naming compliance with `wip-naming.md`
2. Verify content follows BRIEFING style rules
3. Check cross-references (`\dashref`, `\trnref`) are valid
4. Ensure `hotastable` environments are properly formatted

### Updating Documentation

1. **Governance docs** (`docs/*.md`) — Consult human before modifying
2. **README.md** — Update only for major changes (usually automated)
3. **INTEGRATED-FILES.md** — Auto-generated, do NOT edit manually


## Project-Specific Patterns

### HOTAS Table Structure (Key Pattern)

The `hotastable` environment uses a 7-column longtable structure (15.50cm total width):

```latex
\begin{hotastable}{Caption Text Here}
\label{tab:switch-action}
% Columns: Mode (1.00cm) | Dir. (0.90cm) | Act. (0.90cm) | Function (3.30cm) | Effect/Nuance (6.40cm) | Dash34 (1.40cm) | Train. (1.60cm)
\midrule
A-A CRM & Up & Short & Bug target & Moves cursor to designate target in FCR. & \dashref{2.1.5} & \trnref{18 (BARCAP)} \\
A-G PRE & Down & Long & Break lock & Releases current designation and returns to search. & \dashref{2.7.1} & \trnref{28 (SEAD-EW)} \\
\bottomrule
\end{hotastable}
```

For complete column specifications, see BRIEFING Section 4.2 and Section 12.3.9.

### Version Metadata Macros

```latex
\newcommand{\docversion}{0.4.1.1}
\newcommand{\docbuild}{20260218}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{18 February 2026}
\newcommand{\chapterscompletedof}{4/7}
```


## What NOT to Do

1. ❌ **Never** integrate WIP content into `guide.tex` without human approval
2. ❌ **Never** modify `template/template-wip.tex` (it's the canonical template)
3. ❌ **Never** create WIP files without using the template
4. ❌ **Never** bump versions without following the decision tables
5. ❌ **Never** modify governance documents (`docs/*.md`) without explicit approval
6. ❌ **Never** write LaTeX document content in Portuguese (all guide content must be English)
7. ❌ **Never** use generic placeholders like "TODO" in LaTeX content
8. ❌ **Never** edit `INTEGRATED-FILES.md` manually (it's auto-generated)


## Quick Reference Links

- **Source Materials:** `misc/fontes/` (Dash-34, Dash-1, training manual PDFs)
- **Figures & Assets:** `fig/` (images for the guide). Always verify licensing before use.
- **Diagrams & Flows:** Check `docs/` for existing SVG/PNG diagrams before creating new ones. Prefer Mermaid only for simple flows; export to SVG if necessary.
- **Templates:** `template/` (canonical WIP template, guide structure template)
- **Active Work:** `wip/` (chapter/section files in development)
- **Archive:** `archive/WIP/` (integrated files), `archive/GUIDE/` (old guide versions)
- **Scripts:** `scripts/` contains critical automations. Never edit scripts without explicit consultation.


## Questions to Ask Before Making Changes

1. Have I consulted all relevant governance files and style guides?
2. Am I following the correct prose standards (STYLE-GUIDE.md) and LaTeX structure (briefing.md)?
3. Is the WIP lifecycle, integration, and versioning flow being respected?
4. Am I using the canonical template for new files?
5. Is the generated LaTeX content in English, while my chat communication with the user is in Portuguese?
6. Am I considering existing diagrams, scripts, and images in the project?
7. Am I respecting the CC BY-NC 4.0 licensing for all assets?
8. Am I aware of the project's current text revision status?

---

**Remember:** This project has a strict governance framework. When in doubt, consult the governance documents in `/docs/` or ask the human author for clarification.
