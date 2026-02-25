
# AI Agent Instructions — Falcon BMS TMS/DMS/CMS Guide Project

## Project Overview

This is a **LaTeX-based technical documentation project** developing a comprehensive usage guide for F-16 HOTAS switches (TMS/DMS/CMS) in Falcon BMS 4.38.1 flight simulator. The project uses a strict governance framework with version control, WIP file lifecycles, and AI-assisted content development.

**Current Status:** Pre-publication phase (v0.3.3.0), 3/7 chapters completed, targeting v1.0 publication

**Primary Languages:** LaTeX (content), Python (automation), PowerShell (validation)


## Critical Governance & Style Documents (Read These First)

All governance and style documents são leitura obrigatória antes de qualquer alteração. Eles estão distribuídos principalmente em `/docs/` e `/misc/`:

1. **[briefing.md](../docs/briefing.md)** — Estrutura do projeto, guidelines de LaTeX, macros, layout, padrões de tabelas e ambientes.
2. **[version-system.md](../docs/version-system.md)** — Versionamento (pré e pós-publicação), regras de bump, snapshots.
3. **[wip-naming.md](../docs/wip-naming.md)** — Convenção de nomes para arquivos WIP, ciclo de vida (dev → review → final → approved → deprecated).
4. **[project-tracking.md](../docs/project-tracking.md)** — Rastreamento de progresso, status de capítulos, log de desenvolvimento.
5. **[STYLE-GUIDE.md](../misc/STYLE-GUIDE.md)** — Guia oficial de estilo para toda prosa do projeto (introduções, descrições, células de tabela com texto corrido, etc.).

**Importante:**
- O STYLE-GUIDE.md cobre apenas prosa e narrativa. O BRIEFING cobre apenas estrutura LaTeX, macros e layout.
- Sempre consulte ambos antes de gerar conteúdo textual ou estrutural.
- Nunca modifique documentos de governança sem aprovação explícita.


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
- **Status codes:** `dev` (draft) → `review` (under review) → `final` (approved) → `approved` (integrated & archived) → `deprecated` (retired)

**Workflow:**
1. Copy `template/template-wip.tex` to `wip/`
2. Rename following the pattern above
3. Edit content (development status: `dev`)
4. Human review (status: `review`)
5. Finalize (status: `final`)
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
- Siga rigorosamente o STYLE-GUIDE.md para toda prosa: introduções, descrições, células de tabela com texto corrido, etc.
- Prosa deve ser direta, sem justificativas, sem frases introdutórias, sem sinônimos criativos, sem conclusões redundantes.
- Exemplos e princípios estão detalhados no STYLE-GUIDE.md.

### LaTeX & Estrutura (docs/briefing.md)
- Use sempre o preâmbulo consolidado (docs/tex-preamble-consolidated.md).
- Siga padrões de ambiente, macros e layout definidos no briefing.md.
- HOTAS tables: sempre usar \begin{hotastable} (15.6cm), colunas e alinhamento padronizados.
- Referências cruzadas: \dashlnk, \trglnk, \imglink, conforme briefing.md.
- Nunca use placeholders como "TBD" ou "TODO".
- Todo conteúdo em inglês; instruções para AI em português.


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
3. Check cross-references (`\dashlnk`, `\trglnk`) are valid
4. Ensure `hotastable` environments are properly formatted
5. Validate training mission abbreviations against `training-mission-abbrev-table-v1.0.md`

### Updating Documentation

1. **Governance docs** (`docs/*.md`) — Consult human before modifying
2. **README.md** — Update only for major changes (usually automated)
3. **INTEGRATED-FILES.md** — Auto-generated, do NOT edit manually


## Project-Specific Patterns

### HOTAS Table Structure (Key Pattern)

The `hotastable` environment uses a 7-column longtable structure (15.6cm total width):

```latex
\begin{hotastable}{Caption Text Here}
\label{tab:switch-action}
% Columns: Mode (1.00cm) | Dir. (0.90cm) | Act. (0.90cm) | Function (3.30cm) | Effect/Nuance (6.40cm) | Dash34 (1.40cm) | Train. (2.10cm)
\midrule
A-A CRM & Up & Short & Bug target & Moves cursor to designate target in FCR. & \dashref{2.1.5} & \trnref{18 (BARCAP)} \\
A-G PRE & Down & Long & Break lock & Releases current designation and returns to search. & \dashref{2.7.1} & \trnref{28 (SEAD-EW)} \\
\bottomrule
\end{hotastable}
```

For complete column specifications, see BRIEFING Section 4.2 and Section 12.3.9.

### Version Metadata Macros

```latex
\newcommand{\docversion}{0.3.3.0}
\newcommand{\docbuild}{20260202}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{02 February 2026}
\newcommand{\chapterscompletedof}{3/7}
```


## What NOT to Do

1. ❌ **Never** integrate WIP content into `guide.tex` without human approval
2. ❌ **Never** modify `template/template-wip.tex` (it's the canonical template)
3. ❌ **Never** create WIP files without using the template
4. ❌ **Never** bump versions without following the decision tables
5. ❌ **Never** modify governance documents (`docs/*.md`) without explicit approval
6. ❌ **Never** write content in Portuguese (content must be English)
7. ❌ **Never** use generic placeholders like "TODO" in LaTeX content
8. ❌ **Never** edit `INTEGRATED-FILES.md` manually (it's auto-generated)


## Quick Reference Links

- **Diagramas e fluxos:** Consulte docs/ para diagramas SVG/PNG já existentes antes de criar novos. Prefira Mermaid apenas para fluxos simples; exporte para SVG se necessário.
- **Scripts:** scripts/ contém automações críticas. Nunca edite scripts sem consulta explícita.
- **Imagens:** fig/ e docs/ armazenam imagens e diagramas. Sempre verifique licenciamento antes de usar.

- **Source Materials:** `misc/fontes/` (Dash-34, Dash-1, training manual PDFs)
- **Figures:** `fig/` (images for the guide)
- **Templates:** `template/` (canonical WIP template, guide structure template)
- **Active Work:** `wip/` (chapter/section files in development)
- **Archive:** `archive/WIP/` (integrated files), `archive/GUIDE/` (old guide versions)


## Questions to Ask Before Making Changes

1. Consultei todos os arquivos de governança e style-guide relevantes?
2. Estou seguindo o padrão correto de prosa (STYLE-GUIDE.md) e estrutura (briefing.md)?
3. O fluxo de WIP, integração e versionamento está sendo respeitado?
4. Estou usando o template correto para novos arquivos?
5. O conteúdo está em inglês e as instruções em português?
6. Estou considerando diagramas, scripts e imagens já existentes no projeto?
7. Estou respeitando o licenciamento CC BY-NC 4.0?
8. Estou atento ao status de revisão textual do projeto?

1. Which governance document defines the rules for this change?
2. Is this a WIP file or the canonical `guide.tex`?
3. Does this require a version bump? Which level (MINOR/PATCH/SUBPATCH)?
4. Have I verified the naming convention against `wip-naming.md`?
5. Is the content in English and instructions in Portuguese?
6. Am I following the BRIEFING style guidelines?

---

**Remember:** This project has a strict governance framework. When in doubt, consult the governance documents in `/docs/` or ask the human author for clarification.
