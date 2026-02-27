# Alpha Release Infrastructure — Implementation Plan (Definitive)

**Created:** 2026-02-26
**Author:** Research + Implementation Plan — Claude Sonnet 4.6
**Source spec:** [`misc/alpha-release-handoff.md`](alpha-release-handoff.md)
**Research base:** [`misc/alpha-release-impact.md`](alpha-release-impact.md)
**Status:** Production ready after (§16) decisions are made

> **Guiding principle:** The alpha flow is a **parallel, optional** extension to the standard
> flow. Standard flow (`dev → review → final → approved`) remains **intact and unchanged**.
> The alpha flow (`final → alpha → approved`) is activated only when pre-release
> infrastructure is in progress. Every change must make this distinction explicit.

---

## 0. Before You Start

### 0.0 Pre-Branch Commit (on `main`, before creating the feature branch)

1. Commit `misc/alpha-release-impl.md` and `misc/alpha-release-impact.md` to `main`
2. Update `docs/project-tracking.md`:
   - **§3 Development Log** — add entry for `2026-02-26` (see template below)
   - **§4 Version Roadmap** — add `v0.4.2.0-alpha.1` row between `v0.4.2.0` and `v0.5.0.0`
3. Commit project-tracking.md to `main`
4. Only then: create `feat/alpha-release` branch

**§3 Development Log entry template (2026-02-26):**

> **2026-02-26:** Alpha release infrastructure planning completed. Alpha flow designed as optional parallel extension to the standard WIP flow (`final → alpha → approved`). Planning documents created: `misc/alpha-release-impl.md` (implementation plan — Steps 1–19, 17 files to modify + 1 to create) and `misc/alpha-release-impact.md` (full repository impact analysis). First alpha target: `v0.4.2.0-alpha.1` (triggered after C5 author review complete + issue #48 resolved). Feature branch `feat/alpha-release` to be created on implementation start. Total commits: **[update at commit time]**.

---

### 0.1 Branch Setup

```bash
git checkout main
git pull origin main
git checkout -b feat/alpha-release
```

All implementation work happens on `feat/alpha-release`. The branch is completely isolated
from all automated workflows (see [impact.md §9](alpha-release-impact.md)). No automated
workflow targets this branch.

### 0.2 Resolved Design Decisions

Decisions confirmed by the author (2026-02-26). These are **final** and must be
reflected in all file changes.

**D1 — Alpha content model: cumulative**
Each `alpha.N` snapshot contains **all** previously integrated alpha-approved chapters
plus any new ones — identical to how the official guide accumulates content. `alpha.2`
= everything in `alpha.1` + new chapters.

**D2 — Trigger to move WIP to `alpha`**
Same mechanism as the standard flow: the human renames the WIP file from `-final-` to
`-alpha-` in the filename when the content is ready for pre-release integration. No
additional pre-condition. The rename IS the decision.

**D3 — `alpha → deprecated` procedure**
If a WIP file with `alpha` status is abandoned before official integration:
1. Move file to `archive/WIP/` with `deprecated` status (same as standard flow)
2. Update and close the corresponding GitHub issue with a note
3. The GitHub pre-release tag stays as-is (it reflects the historical state at
   that moment — no removal needed)
No special cleanup of snapshots or tags required.

**D4 — Release description template: optional standard**
There is no mandatory template. However, a standard format may be adopted if desired:
```
v0.4.2.0-alpha.1 — [Chapter title(s)]

INCLUDED in this pre-release:
- ✅ C5 — CMS (style revision complete)

PENDING official integration:
- ⏳ C1, C2, C3 — style revision in progress
- ⏳ C4 — TMS (paused)

⚠️ Pre-release — not the official guide.
Based on: wip/guide-v0.4.2.0-alpha.1-YYYYMMDD.tex
```
Using this format is recommended for consistency but not enforced.

**D5 — Alpha PDF build: manual**
The alpha snapshot is compiled to PDF locally by the author. No GitHub Actions workflow
for alpha PDF generation. Workflow: compile locally → validate → upload to the GitHub
pre-release as a release asset. The PDF is not committed to the repository.

---

### 0.3 Decisions (Resolved — see §16 for detail)

| Decision | Resolved |
|----------|---------|
| `generate-integrated-files.py` — Alpha Snapshots section | **Option B** — separate section (§16.A) |
| `generate-integrated-files.py` — Pre-release Tags section | **Option B** — add section (§16.D) |
| `validate-wip-naming.yml` test strategy | **Option B** — test after merge (§16.C) |
| Milestones | **Option A** — use existing `v0.4.2.0` (§16.B) |

### 0.4 Consistency Glossary

These are the **canonical definitions** that must be used verbatim in all files.
Do not paraphrase or vary the wording.

**Alpha status — single-line definition:**
> Parallel flow only: approved by the author; integrated into the alpha pre-release
> snapshot. WIP file remains in `wip/` until official integration into `guide.tex`.

**Alpha status — table row (wip-naming.md §3.1 format):**
```
| `alpha` | `wip/` | Parallel flow only: approved by the author; integrated into the alpha snapshot; awaiting official integration into guide.tex |
```

**Standard flow vs. Alpha flow (Step 3 / status progression blocks):**
```
STANDARD FLOW (always applicable):
dev → review → final → approved

ALPHA FLOW (parallel, optional — active only when pre-release infrastructure is in progress):
final → alpha → approved
```

**Alpha snapshot file naming:**
```
wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]-YYYYMMDD.tex
Examples:
  wip/guide-v0.4.2.0-alpha.1-20260227.tex      ← new chapter (N only)
  wip/guide-v0.4.2.0-alpha.1.1-20260303.tex    ← patch within same chapter set
  wip/guide-v0.4.2.0-alpha.2-20260310.tex      ← next chapter added (M disappears)
```
Note: in `wip/` ROOT — NOT in `wip/guide/`.

**Alpha tag format:**
```
v0.4.2.0-alpha.1          ← chapter-level release
v0.4.2.0-alpha.1.1        ← patch release within same chapter set
vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]
```

---

### 0.5 Prohibitions

These must NOT be touched by anything related to alpha infrastructure:

- **`wip/guide/`** and its behavior: continues with a single file, all existing workflows intact.
- **`guide.tex`**: not touched by anything related to alpha.
- **Current official snapshot** (`wip/guide/guide-v0.4.1.1-20260218.tex`): untouched.
- **Semantics of `approved`**: continues to mean official integration into `guide.tex`.
- **Any GitHub Action that processes `wip/guide/`**: do not modify.

---

### 0.6 Alpha Release Trigger Map (linked to issue #44)

This infrastructure is activated when chapters from issue #44 complete the style
revision cycle. Each completed chapter triggers one alpha release.

**C5 current status (2026-02-26):**

| Section | H+AI pass | Human-only pass |
|---------|-----------|-----------------|
| §5.1–§5.2.1.3 | ✅ | ✅ |
| §5.2.2–§5.2.4 | ✅ | ❌ |
| §5.3 | ❌ | ❌ |

Sub-issue #48 (BYP/STBY modes): open — **blocks C5 → `final`**

**Trigger sequence:**

| WIP chapter | Expected tag | Trigger condition |
|-------------|-------------|-------------------|
| C5 | `alpha.1` | #48 resolved + §5.3 complete + author approval → `final` → `alpha` |
| Next chapter (C1, C2, or C3) | `alpha.2` | Style revision complete (order TBD) |
| Remaining chapters | `alpha.3[, 4]` | Each subsequent chapter (order TBD) |

Official release `v0.4.2.0` = all chapters `approved` + integrated into `guide.tex`.

**Issue #44 update:** Add alpha flow note to issue body after `feat/alpha-release`
is merged to `main`. No change to issue #44 required before that.

---

## 1. Dependency Graph

```
[0.1] Branch creation
        │
        ├──► [Step 1] validate-wip-naming.yml      ◄── CRITICAL (CI blocker)
        │         (no dependencies)
        │
        ├──► [Step 2] generate-wip-snapshot.py     ◄── CRITICAL (CI blocker)
        │         (no dependencies)
        │
        ├──► [Step 2B] update-alpha-badge workflow  ◄── CRITICAL (badge visibility)
        │         (no dependencies — independent of Step 2)
        │
        ├──► [Step 3] wip-naming.md                ◄── HIGH (source of truth)
        │         (no dependencies — sets canonical wording)
        │         │
        │         ├──► [Step 4] version-system.md  (wording consistent with Step 3)
        │         ├──► [Step 5] briefing.md         (wording consistent with Step 3)
        │         ├──► [Step 6] README.md           (wording consistent with Step 3)
        │         ├──► [Step 7] copilot-instructions.md
        │         ├──► [Step 8] WIP-Snapshot-Generator HTML
        │         ├──► [Step 9] template-wip.tex
        │         └──► [Steps 10-14] SVG diagrams
        │
        ├──► [Step 15] generate-integrated-files.py (§16.A + §16.D — Option B, see §16)
        │
        ├──► [Steps 16-17] Issue templates
        │         (after governance docs)
        │
        └──► [Manual/Deferred] PNG recreation (post-alpha), milestones
                  (MANUAL — cannot be done via text editing)
```

**Recommended implementation order:**
Steps 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15 → 16 → 17

Steps 18–19 are meta-steps (Validation Checklist + PR Strategy). PNG diagrams and milestones are manual/deferred — handle separately.

---

## 2. Consistency Clusters

Groups of files that must express the same concept in consistent language.

| Cluster | Concept | Files |
|---------|---------|-------|
| **A** | `alpha` status definition | wip-naming.md §3.1, briefing.md §14, copilot-instructions.md, template-wip.tex (×2), WIP-Snapshot-Generator HTML, README.md (Status Codes table) |
| **B** | Standard flow vs. Alpha flow (two-flow block) | wip-naming.md §0.5 Step 3, version-system.md §6.5.4, copilot-instructions.md (workflow) |
| **C** | Folder structure (directory trees) | wip-naming.md §0.4, version-system.md §1.5, briefing.md §11.1, README.md (Project Structure) |
| **D** | Alpha snapshot naming pattern | version-system.md §2.1, version-system.md §2.3, wip-naming.md §0.3 |
| **E** | Alpha tag and pre-release format | version-system.md §6.5.1, version-system.md §6.5.2, version-system.md §6.5.4 |

When implementing Cluster A, copy the canonical wording from §0.4 exactly. Do not vary it between files.

---

## 3. Step 1 — `.github/workflows/validate-wip-naming.yml`

**Priority:** 🔴 Critical
**Why first:** Fails on first push with any alpha file. No path filter — triggers on every
push to `main` or `develop`.

### 3.1 Changes Required

**A. Add `alpha` to status enum in 4 patterns** (lines 89, 95, 101, 113):

Current regex fragment (appears 4 times, in CHAPTER/SECTION/TABLE/VISUAL patterns):
```
(dev|review|final|approved|deprecated)
```
Replace with:
```
(dev|review|final|alpha|approved|deprecated)
```

Affected lines:
- Line 89: CHAPTER pattern
- Line 95: SECTION pattern
- Line 101: TABLE pattern
- Line 113: VISUAL pattern

Note: NOTES pattern (line 107) has no status code — no change needed.

**B. Add ALPHA SNAPSHOT pattern** (new elif block, insert before "Unknown WIP file" else at line 118):

```bash
# ALPHA SNAPSHOT Pattern (guide-v*-alpha.N[.M]-YYYYMMDD.tex in wip/ root)
elif [[ "$FILENAME" =~ ^guide-v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+-alpha\.[0-9]+(\.[0-9]+)?-[0-9]{8}\.(tex|pdf)$ ]]; then
  echo "  ✅ Valid ALPHA SNAPSHOT"
  TYPE="ALPHA_SNAPSHOT"
  VALID=1
```

Note: the optional `(\.[0-9]+)?` group allows both `alpha.1` (chapter release) and
`alpha.1.1` (patch release within same chapter set).

**C. Update PR comment body** (line 168):

In the `Comment on PR` step, the hardcoded string lists:
```
Status: dev, review, final, approved, deprecated
```
Change to:
```
Status: dev, review, final, alpha, approved, deprecated
```

Note: `alpha` goes between `final` and `approved` to reflect the parallel flow position.

**D. Add ALPHA SNAPSHOT pattern to GUIDE block** (lines 67–82 — `WIP/GUIDE` and `ARCHIVE/GUIDE`):

Alpha snapshots archived to `archive/GUIDE/` keep their original name (e.g.,
`guide-v0.4.2.0-alpha.1-20260227.tex`). The existing GUIDE regex
`^guide-v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+-[0-9]{8}\.(tex|pdf)$` does NOT match
the `-alpha.N[.M]-` segment. Add an elif before the else:

```bash
# Alpha snapshot pattern: guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]-YYYYMMDD.tex or .pdf
elif [[ "$FILENAME" =~ ^guide-v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+-alpha\.[0-9]+(\.[0-9]+)?-[0-9]{8}\.(tex|pdf)$ ]]; then
  echo "  ✅ Valid GUIDE alpha snapshot"
  VALID=1
```

Also update the error message in the else branch to mention both valid formats:
```
Expected: guide-vMAJOR.MINOR.PATCH.SUBPATCH-YYYYMMDD.(tex|pdf)
           or guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]-YYYYMMDD.(tex|pdf)
Example: guide-v0.2.3.1-20260125.tex or guide-v0.4.2.0-alpha.1-20260227.tex
```

Note: Change D was not in the original spec — identified during implementation as a
gap (alpha snapshots would fail validation when archived to `archive/GUIDE/`).
Same `(\.[0-9]+)?` optional group as Change B handles both `alpha.1` and `alpha.1.1`.

### 3.2 Test Strategy

The workflow does NOT trigger on `feat/alpha-release` (no path filter, but branch not listed).

**Decision: Option B** (§16.C) — Test after merging to `main` via `workflow_dispatch`
or by pushing a test commit to `main` in a controlled way.

**Option A (not chosen):** Temporarily add `feat/alpha-release` to trigger during development.

### 3.3 Secondary Impacts

None — this workflow has no output artifacts. Changes are self-contained.

---

## 4. Step 2 — `scripts/generate-wip-snapshot.py`

**Priority:** 🔴 Critical
**Why:** Alpha WIP files appear in WIP table with blank status. Alpha snapshot (`guide-v*-alpha.*.tex`) appears in WIP table as a content file — confusing.

### 4.1 Changes Required

**A. Add `alpha` to STATUS_EMOJI dict** (line 12–16):

```python
# Current:
STATUS_EMOJI = {
    'dev': '🟠',
    'review': '🟡',
    'final': '⚪'
}

# Replace with:
STATUS_EMOJI = {
    'dev': '🟠',
    'review': '🟡',
    'final': '⚪',
    'alpha': '🟢'
}
```

**B. Update `parse_status()` regex** (line 29):

```python
# Current:
match = re.search(r'-(dev|review|final)-', fname)

# Replace with:
match = re.search(r'-(dev|review|final|alpha)-', fname)
```

**C. Filter alpha snapshots from WIP table in `get_wip_files()`** (lines 19–25):

```python
# Current:
def get_wip_files():
    files = []
    for fname in os.listdir(WIP_DIR):
        fpath = os.path.join(WIP_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith('.tex'):
            files.append(fname)
    return files

# Replace with:
def get_wip_files():
    files = []
    for fname in os.listdir(WIP_DIR):
        fpath = os.path.join(WIP_DIR, fname)
        if os.path.isfile(fpath) and fname.endswith('.tex') and not fname.startswith('guide'):
            files.append(fname)
    return files
```

**D. Update legend in README WIP section** (line 81):

The `update_readme()` function generates the legend line:
```python
# Current:
'**Legend:**  🟠 dev\t🟡 review\t⚪ final\n\n'

# Replace with:
'**Legend:**  🟠 dev\t🟡 review\t⚪ final\t🔵 alpha\n\n'
```

### 4.2 Secondary Impacts

- README.md WIP Snapshot section: legend auto-updates when script runs.
- No other scripts depend on `get_wip_files()` output.

---

## 4B. Step 2B — Alpha Badge Workflow (new)

**Priority:** 🔴 Critical
**Why:** Quando um alpha snapshot existe em `wip/guide/`, isso deve ser refletido automaticamente em README.md e docs/index.html. Não pode ser manual — o badge deve aparecer/desaparecer com base na presença do arquivo.

**Novos arquivos:**

- `.github/workflows/update-alpha-badge.yml`
- `scripts/update-alpha-badge.py`

**Arquivos modificados:**

- `README.md` (placeholders + rename do heading da seção)
- `docs/index.html` (placeholder)

---

### 4B.1 Workflow — `.github/workflows/update-alpha-badge.yml`

**Triggers:**

- `push: branches: main, paths: wip/guide*alpha*.tex` — automático só quando snapshot alpha é adicionado/removido
- `workflow_dispatch` — manual (fallback)

**Steps:**

1. Checkout (SSH key)
2. Set up Python 3.11
3. Run `scripts/update-alpha-badge.py`
4. Configure Git
5. Commit + push README.md + docs/index.html (se houve mudança)

> Não toca em `generate-wip-snapshot.yml` nem em `update-readme-on-tag.yml`.

---

### 4B.2 Script — `scripts/update-alpha-badge.py`

**Lógica:**

1. Escaneia `wip/` (raiz) por arquivos com padrão `guide*alpha*.tex`
2. **Se encontrado:** extrai versão alpha do nome do arquivo
   - Padrão: `guide-v{VERSION}-{DATE}.tex` → extrai `{VERSION}` (ex: `v0.4.2.0-alpha.1`)
   - Escaneia também `wip/` por `guide*.pdf` → obtém nome do PDF para o link
   - Gera links dinamicamente:
     - README: `https://github.com/carlos-nader/tms-dms-cms-usage-guide/releases` (página genérica — evita link quebrado por erro de nomenclatura da tag)
     - index.html: `https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/wip/{pdf_filename}` (blob direto do PDF em `wip/`)
   - Insere/atualiza conteúdo entre os blocos delimitadores em README.md e docs/index.html
3. **Se não encontrado:** esvazia os blocos delimitadores (badge desaparece)

**Extração do nome do arquivo:**

```python
# Exemplo: guide-v0.4.2.0-alpha.1-20260301.tex → extrai: v0.4.2.0-alpha.1
# Exemplo: guide-v0.4.2.0-alpha.1.1-20260301.tex → extrai: v0.4.2.0-alpha.1.1
pattern = r'^guide-(v[\d.]+-alpha\.[\d.]+)-\d{8}\.tex$'
```

> ⚠️ **Convenção obrigatória:** A tag de release no GitHub deve ser criada com o nome **exato** extraído do filename (ex: tag `v0.4.2.0-alpha.1` para arquivo `guide-v0.4.2.0-alpha.1-*.tex`). Link 404 caso contrário.

---

### 4B.3 README.md — Mudanças

**Campo 1 — Badge alpha (linha ~29)**

Adicionar placeholder `<!-- ALPHA-BADGE-START/END -->` imediatamente abaixo do badge oficial:

```markdown
[![Version](https://img.shields.io/badge/LATEST%20version-v0.4.1.1-yellow?style=for-the-badge&logo=tag&logoColor=black)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/releases)
<!-- ALPHA-BADGE-START -->
<!-- ALPHA-BADGE-END -->
```

Quando alpha ativo, script preenche:

```markdown
<!-- ALPHA-BADGE-START -->
[![Alpha](https://img.shields.io/badge/alpha-v0.4.2.0--alpha.1-orange?style=for-the-badge&logo=flask&logoColor=white)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/releases)
<!-- ALPHA-BADGE-END -->
```

**Campo 2 — Footer (linha ~289)**

Adicionar placeholder `<!-- ALPHA-FOOTER-START/END -->` abaixo da linha do footer:

```markdown
**License:** CC BY-NC 4.0 | **Guide Status:** Pre-publication v0.4.1.1
<!-- ALPHA-FOOTER-START -->
<!-- ALPHA-FOOTER-END -->
```

Quando alpha ativo, script preenche:

```markdown
<!-- ALPHA-FOOTER-START -->
Alpha pre-release available: v0.4.2.0-alpha.1
<!-- ALPHA-FOOTER-END -->
```

> Sem link, sem emoji — manter padrão visual da linha existente.

**Campo 3 — Rename do heading da seção (linha ~47)**

Mudança pontual feita no mesmo commit dos placeholders. O script `update-readme-version.py`
procura o padrão `| **Guide Version** | v... |` **na célula da tabela**, não no heading da
seção — portanto o heading pode ser renomeado livremente sem quebrar o script.

```markdown
# Atual:
## 📊 Current Status

# Substituir por:
## 📊 Current Version — Official Guide
```

> Alpha não aparece nessa seção. O rename torna explícito que o conteúdo é sempre da versão oficial.
> A célula `| **Guide Version** | v0.4.1.1 |` permanece intacta — o script continua funcionando.

---

### 4B.4 docs/index.html — Mudanças

**Campo 4 — Badge alpha (linha ~305)**

Adicionar placeholder `<!-- ALPHA-BADGE-START/END -->` imediatamente após o `</span>` do badge oficial (dentro do mesmo `<div>`):

```html
<!-- badge oficial (não tocado) -->
<span style="background: linear-gradient(135deg, #007bff, #0056b3); ...">
  v0.4.1.1 • 660KB • 50+ pages
</span>
<!-- ALPHA-BADGE-START -->
<!-- ALPHA-BADGE-END -->
```

Quando alpha ativo, script preenche:

```html
<!-- ALPHA-BADGE-START -->
<a href="https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/wip/{pdf_filename}"
   target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
  <span style="background: linear-gradient(135deg, #ff8c00, #e65c00);
               color: white; padding: 0.4em 0.8em; border-radius: 20px;
               font-weight: bold; font-size: 0.85rem;
               box-shadow: 0 2px 4px rgba(255,140,0,0.3);
               display: inline-block; margin-top: 0.4em;">
    Alpha v0.4.2.0-alpha.1 — Pre-release PDF
  </span>
</a>
<!-- ALPHA-BADGE-END -->
```

> Campo 5 (atributo `title` do badge oficial) — **não tocado**. Tooltip exclusivo da versão oficial.

---

### 4B.5 scripts/update-readme-version.py — Nenhuma alteração necessária

O script procura `| **Guide Version** | v... |` na **célula** da tabela, não no heading da
seção. Como Campo 3 apenas renomeia o heading (§4B.3), a célula permanece intacta e o
script continua funcionando sem modificação.

---

### 4B.6 Secondary Impacts

- `generate-wip-snapshot.yml` — não tocado
- `update-readme-on-tag.yml` — não tocado
- Campos de versão oficial em README/index.html — não tocados pelo script alpha
- `docs/contributing.html` — sem referências de versão, não tocado
- `docs/WIP-Snapshot-Generator-v3.1.html` — coberto pelo Step 8

> **⚠️ Design correction (2026-02-27):** The initial spec described alpha WIP status as
> "awaiting official integration into guide.tex", implying individual re-integration of
> each WIP chapter. This was incorrect. The alpha snapshot (`wip/guide-v*-alpha.*-*.tex`)
> accumulates chapters progressively and becomes `guide.tex` directly when promoted.
> Individual WIP files are **not** re-integrated; they are archived in batch (renamed to
> `approved`) at the moment the alpha snapshot is promoted to an official release.
> This correction is reflected in `docs/wip-naming.md` (updated 2026-02-27).

---

## 5. Step 3 — `docs/wip-naming.md`

**Priority:** 🟠 High — sets canonical wording for all other files.

### 5.1 Section §0.3 — Scope

After the paragraph "This convention does **NOT** apply to:", add a note clarifying alpha snapshots:

```markdown
**Note on alpha snapshots:** Files following the pattern
`wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N-YYYYMMDD.tex` are alpha pre-release
snapshots. They reside in `wip/` root (not `wip/guide/`) and are governed by
VERSION-SYSTEM. They are **not** WIP content files under this convention, but they
coexist in `wip/` with WIP files when pre-release infrastructure is active.
```

### 5.2 Section §0.4 — File Organization Structure

In the directory tree, add one line under `├── visual-*.*`:

```text
│   ├── guide-v*-alpha.*-*.tex   (Alpha snapshots — only when pre-release active)
│   │
│   └── guide/                   (Guide snapshots — VERSION-SYSTEM)
```

### 5.3 Section §0.5 Step 3 — Status Progression

Replace the current status list:
```
- `dev` → when first created from template
- `review` → when human begins iteration
- `final` → when human decides "this is solid, ready to integrate"
- `approved` → after human integrates into guide (move to `archive/WIP/`)
```

With:
```
**STANDARD FLOW (always applicable):**
- `dev` → when first created from template
- `review` → when human begins iteration
- `final` → when human decides "this is solid, ready to integrate"
- `approved` → after human integrates into guide.tex (move to `archive/WIP/`)

**ALPHA FLOW (parallel, optional — active only when pre-release infrastructure is in progress):**
- `alpha` → after human approves content and integrates into alpha snapshot; WIP
  file remains in `wip/` awaiting official integration
- `approved` → after official integration into guide.tex (move to `archive/WIP/`)

The standard flow remains intact and unaffected by the alpha flow. Use `alpha` only
when explicitly working with pre-release infrastructure.
```

### 5.4 Section §3.1 — Status Definitions

Add one row to the table between `final` and `approved`:

```markdown
| `alpha` | `wip/` | Parallel flow only: approved by the author; integrated into the alpha snapshot; awaiting official integration into guide.tex | `approved` or `deprecated` |
```

### 5.5 Section §3.2 — Lifecycle Diagram (ASCII)

The current ASCII diagram ends at `approved`. Add alpha as a parallel branch:

After the current diagram, add:

```
═══════════════════════════════════════════════════
ALPHA FLOW  (parallel, optional)
═══════════════════════════════════════════════════

    ┌───────┐
    │ final │  ← same "final" node as Standard Flow
    └───┬───┘
        │
        │  (human approves + creates alpha snapshot)
        │
    ┌───▼───┐
    │ alpha │
    │(wip/) │
    └───┬───┘
        │
   ┌────┴────────────┐
   │                 │
(official         (abandon)
 integration)         │
   │              ┌──▼─────────┐
┌──▼──────┐       │ deprecated │
│approved │       │(archive/WIP)│
│(archive/│       └────────────┘
│  WIP/)  │
└─────────┘
```

### 5.6 Section §3.3 — Transition Rules

After the existing **Forbidden** block, add:

```markdown
**Alpha Flow Transitions (parallel flow only):**

Allowed:
- `final → alpha` (human approves + integrates into alpha snapshot; see §0.2 D2)
- `alpha → approved` (after official integration into guide.tex)
- `alpha → deprecated` (abandon before official integration; the GitHub pre-release
  tag stays as a historical record — no removal needed; see §0.2 D3)

Forbidden:
- `alpha → final` (cannot revert approval)
- `alpha → review` (cannot revert to review stage)
- `alpha → dev` (cannot revert to draft)

Note: The standard flow transitions are unchanged. `alpha` is not a step
in the standard flow — it is only valid in the parallel pre-release flow.
```

### 5.7 Section §3.4 — Success Path Example

After the current example block, add:

```markdown
**Success Path — Alpha Flow:**

```text
2026-02-24: chapter-C5-style-rev-review-2026-02-24.tex
            (Human: "Style review approved — ready for alpha")

2026-02-27: chapter-C5-style-rev-alpha-2026-02-27.tex
            (Human renames to alpha status)

2026-02-27: Human creates: wip/guide-v0.4.2.0-alpha.1-20260227.tex
            (Alpha snapshot with C5 integrated)

2026-02-27: Human creates tag v0.4.2.0-alpha.1 + pre-release on GitHub
            WIP file stays in wip/ (NOT moved to archive yet)

(Future):   Human integrates into guide.tex, bumps to v0.4.2.0
            Human moves chapter-C5-style-rev-alpha-*.tex to archive/WIP/
            renamed: chapter-C5-style-rev-approved-*.tex
```
```

### 5.8 Section §4.2 — Integration into Main Document

Keep existing section intact. Add new §4.3 after §4.3 Archival (renumber existing §4.3 to §4.4):

```markdown
### 4.3 Alpha Integration Workflow

**This is a parallel, optional workflow.** Use only when pre-release
infrastructure is active. The standard workflow in §4.2 remains unchanged.

1. **Human decides:** "Ready to create alpha pre-release for [chapter]"
2. **Human renames** WIP file from `final` to `alpha` status
3. **Human creates** alpha snapshot in `wip/` root:
   `wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N-YYYYMMDD.tex`
   (This is a copy of the current `wip/guide/guide-v*.tex` snapshot with
   **all** alpha-approved chapters integrated — **cumulative**: alpha.2 includes
   everything in alpha.1 plus any new chapters. See §0.2 D1.)
4. **Human compiles** the alpha snapshot and generates the alpha PDF
5. **Human creates** Git tag `vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N`
6. **Human creates** GitHub pre-release with:
   - Marked explicitly as **pre-release** (not a release)
   - PDF generated from alpha snapshot (not from guide.tex)
   - Description listing which chapters are included and which are pending
7. **WIP file stays in `wip/`** — NOT moved to `archive/WIP/` yet
8. **`approved` status and archival** happen only after official integration
   into `guide.tex` (standard workflow §4.2, step 8)
```

### 5.9 Section §4.3 Archival (now §4.4) — Secondary note

Add a note at the end of the archival section:

```markdown
**Alpha WIP files:** Files with status `alpha` remain in `wip/` until the official
integration into `guide.tex` is complete. At that point they transition to `approved`
and are moved to `archive/WIP/`, following the standard archival rule.
```

### 5.10 Section §5.3 — Workflow

After the current workflow diagram, add:

```markdown
**Alpha Flow (parallel, optional):**

```text
Issue created → WIP file created (dev)
      ↓
Issue updated → WIP iterated (review)
      ↓
Issue ready → WIP approved (final)
      ↓
[ALPHA BRANCH: only when pre-release active]
WIP renamed → alpha status
      ↓
Alpha snapshot created (wip/guide-v*-alpha.N-*.tex)
      ↓
Tag v*.*.*.*-alpha.N + GitHub pre-release
      ↓
WIP stays in wip/ (awaiting official integration)
      ↓
[RESUMES STANDARD FLOW]
Official integration → Tag + Release → Close Issue → Close Milestone
WIP moved to archive/WIP/ (renamed to approved)
```
```

### 5.11 Section §6 — Responsibility Matrix

Add three rows to the matrix table:

```markdown
| Decide `final → alpha` | ❌ Cannot | ✅ Must decide |
| Create alpha snapshot | ❌ Cannot | ✅ Must do |
| Create pre-release tag and GitHub pre-release | ❌ Cannot | ✅ Must do |
```

### 5.12 Section §7.2 — Status Codes Quick Reference

Add row between `final` and `approved`:

```markdown
| `alpha` | `wip/` | Parallel flow: approved, in pre-release snapshot |
```

### 5.13 Section §7.3 — Folder Structure

Add row to table:

```markdown
| `wip/` (root) | Active WIP files + alpha snapshots (when pre-release active) |
```

Update the `wip/` row note or add a note below:

```markdown
**Note:** `wip/` may contain both WIP content files (`chapter-*`, `section-*`, etc.)
and alpha snapshots (`guide-v*-alpha.*-*.tex`) when pre-release infrastructure is active.
```

### 5.14 Section §7.4 — Checklist for AI

Change the status validation line:
```
# Current:
✅ Status is valid (`dev`, `review`, `final`, `approved`, `deprecated`)

# Replace with:
✅ Status is valid (`dev`, `review`, `final`, `alpha`, `approved`, `deprecated`)
   Note: `alpha` is valid only in the parallel pre-release flow — human decides
```

### 5.15 Secondary Impacts from wip-naming.md changes

- SVG `wip-naming-diagram.svg`: status cards + lifecycle flowchart + forbidden box
- SVG `wip-life-cycle.svg`: status flow nodes
- SVG `wip-creation-workflow.svg`: status progression panel
- SVG `wip-integration-flow.svg`: integration flow + parallel alpha path
- All PNG diagrams: need manual recreation
- copilot-instructions.md: workflow section must match §0.5 Step 3 wording
- README.md WIP Lifecycle: must match §0.5 Step 3 wording
- briefing.md §14 and §15: must be consistent

---

## 6. Step 4 — `docs/version-system.md`

**Priority:** 🟠 High

### 6.1 Section §1.5 — Repository Structure and GitHub Workflow

After:
> The directory `wip/guide/` contains the **current snapshot** named with the full version pattern

Add:

```markdown
When pre-release infrastructure is active, `wip/` (root, **not** `wip/guide/`) may
additionally contain alpha pre-release snapshots:
- `wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N-YYYYMMDD.tex`
These coexist with WIP content files and are governed by this document (§2.1, §6.5).
They are NOT subject to the single-file rule of `wip/guide/`.
```

### 6.2 Section §2.1 — Snapshot File Name Rule

After the current rule, add:

```markdown
**Alpha pre-release snapshots** follow a separate pattern and reside in `wip/` root:
```text
wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]-YYYYMMDD.tex
```
- `N` is the chapter-level counter: increments when a new chapter enters the snapshot
- `M` (optional) is the patch-level counter: increments for any correction below
  chapter level (structural or minor) within the same chapter set; when `N` increments,
  `M` disappears (e.g., `alpha.1.2` → `alpha.2`, not `alpha.2.0`)
- `YYYYMMDD` is the **build date** (date the snapshot is compiled — same rule as
  official snapshots per version-system.md §6.1; do NOT recreate with a new date
  if content is unchanged)
- The file lives in `wip/` root — NOT in `wip/guide/`
- Multiple alpha snapshots may coexist in `wip/` (one per pre-release increment)
```

### 6.3 Section §2.3 — Examples

Add examples:

```markdown
- Pre-release alpha snapshots (in `wip/` root):
  - `wip/guide-v0.4.2.0-alpha.1-20260227.tex`   ← C5 enters snapshot (N=1)
  - `wip/guide-v0.4.2.0-alpha.1.1-20260303.tex` ← correction in C5 (M=1)
  - `wip/guide-v0.4.2.0-alpha.2-20260310.tex`   ← C1 enters snapshot (N=2, M gone)
```

### 6.4 Section §6.2 — File Naming and Snapshot Workflow

After the standard 8-step workflow, add:

```markdown
**Alpha Snapshot Workflow (parallel, optional):**

For pre-release alpha snapshots (activated only when pre-release infrastructure
is in progress):

1. **Determine content.** Identify which chapters have reached `alpha` WIP status.
2. **Create alpha snapshot.** Copy the current `wip/guide/guide-v*.tex` and
   integrate **all** alpha-approved chapters (**cumulative** — alpha.N includes
   all previously alpha-approved content; see §0.2 D1). Save as:
   `wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]-YYYYMMDD.tex`
3. **Compile and check.** Generate PDF from the alpha snapshot. Verify no errors.
4. **Create Git tag.** Tag format: `vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]`
5. **Create GitHub pre-release.** Mark explicitly as **pre-release**. Attach compiled PDF.
6. **Do NOT** move alpha snapshot to `archive/GUIDE/`. It stays in `wip/` until the
   official release.

Note: The official snapshot in `wip/guide/` is NOT updated during the alpha workflow.
```

### 6.5 Section §6.3 — Archival Strategy

Add a note after the existing text:

```markdown
**Alpha snapshots exception:** Alpha pre-release snapshots (`wip/guide-v*-alpha.*.tex`
in `wip/` root) are NOT archived until the corresponding official release is created.
At that point, they may be moved to `archive/GUIDE/` alongside the regular snapshots.
The single-active-snapshot rule applies only to `wip/guide/` — it does not restrict
the number of alpha snapshots in `wip/` root.
```

### 6.6 Section §6.5.1 — Tags

Add:

```markdown
**Alpha (pre-release) tags:**
- Format: `vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N[.M]`
- Examples: `v0.4.2.0-alpha.1` · `v0.4.2.0-alpha.1.1` · `v0.4.2.0-alpha.2`
- Alpha tags are created **before** the official `vMAJOR.MINOR.PATCH.SUBPATCH` tag
- Multiple alpha tags may exist for the same target version (one per pre-release)

**Alpha version increment rules** (parallel to the canonical version-system):

| Change in snapshot | Canonical equivalent | Alpha counter |
|--------------------|---------------------|--------------|
| New chapter added to snapshot | MINOR | N++ — M disappears (`alpha.2`) |
| Any correction below chapter level (structural or minor) | PATCH or SUBPATCH | M++ (`alpha.1.1`, `alpha.1.2`) |

Notes:
- When N increments, M disappears: the clean state is `alpha.N`, not `alpha.N.0`
- PATCH and SUBPATCH are collapsed into M — no third level needed
- Decision authority: human author only (same as all version decisions)
```

### 6.7 Section §6.5.2 — Releases

Add:

```markdown
**Pre-releases (alpha):**
- Must be marked explicitly as **pre-release** in GitHub (not as a full release)
- Title: `v0.4.2.0-alpha.1 — Chapter 5 Style Revision` (include content summary)
- Description: list which chapters are included and which are pending
  (for a recommended optional template, see §0.2 D4)
- Assets: compiled PDF generated from the alpha snapshot (not from `guide.tex`)
- Pre-releases do NOT replace the current official release
- If the corresponding WIP is later deprecated, the pre-release tag stays as a
  historical record — no GitHub cleanup needed (see §0.2 D3)
```

### 6.8 Section §6.5.4 — Workflow Integration

Replace the current diagram:
```
Issues (in Milestone) → WIP files → Integration → Snapshot → guide.tex → Tag → Release
```

With:
```
Issues (in Milestone) → WIP files → Integration → Snapshot → guide.tex → Tag → Release
                                                                                ↓
                                                                      Close Milestone

ALPHA PATH (parallel, optional):
WIP files (final) → [human decides alpha] → alpha status → Alpha Snapshot (wip/) → Alpha Tag → Pre-Release
                                                                                                    ↓
                                                                              (awaits official integration)
                                                                                         ↓
                                                                          Official flow resumes from Integration
```

### 6.9 Section §7.3 — Key Notes

Add:

```markdown
- Alpha pre-releases (`vX.X.X.X-alpha.N`) are intermediate publications for approved
  chapters that are awaiting the next official version bump. They are marked as
  pre-releases on GitHub and are distinct from official releases.
```

---

## 7. Step 5 — `docs/briefing.md`

**Priority:** 🟠 High

### 7.1 Section §11.1 — Directory Structure

In the directory tree, under `wip/`:

```text
# Current:
├── wip/
│   ├── guide/
│   │   └── guide-vX.X.X.X-YYYYMMDD.tex  # Active snapshot
│   ├── chapter-C#-...tex            # Chapter WIP files
│   └── section-C#-S#-...tex         # Section WIP files

# Add line:
├── wip/
│   ├── guide-v*-alpha.*-*.tex       # Alpha snapshots (when pre-release active)
│   ├── guide/
│   │   └── guide-vX.X.X.X-YYYYMMDD.tex  # Active snapshot
│   ├── chapter-C#-...tex            # Chapter WIP files
│   └── section-C#-S#-...tex         # Section WIP files
```

### 7.2 Section §12.4 — Metadata Block Format

In the mandatory fields note:
```
# Current:
**Status:** dev → review → final → approved → deprecated

# Replace with:
**Status:** dev → review → final → approved → deprecated
(Parallel alpha flow: final → alpha → approved — active only when pre-release infrastructure
is in progress)
```

### 7.3 Section §13 — How to Create and Integrate WIP Files, Step 5

```
# Current (Step 5 Workflow):
- **dev**: Author working
- **review**: Human review
- **final**: Ready for integration
- **approved**: Integrated into guide, moved to ARCHIVE

# Add (after deprecated line if present, or after approved):
- **alpha**: Integrated into pre-release alpha snapshot (parallel flow only);
  WIP file remains in wip/ until official integration
```

### 7.4 Section §14 — Quick Reference: File Naming Convention, Status codes

```
# Current:
- `dev` — Draft
- `review` — Under review
- `final` — Ready for integration
- `approved` — Integrated and archived
- `deprecated` — Intentionally retired

# Add (between final and approved):
- `alpha` — Integrated into pre-release snapshot (parallel flow only)
```

### 7.5 Section §15 — Pre-Integration Checklist

Briefing.md §15 contains a checklist with "Status: final" as a pre-requisite item
for integration into `guide.tex`. For alpha integration the pre-requisite is different.

Add a note after the `final` pre-requisite item:

```markdown
**Alpha integration pre-requisite (parallel flow only):** WIP file status is `alpha`
(not `final`). The `final` status applies to standard integration only.
```

### 7.6 Secondary Impacts

- `briefing.md` is rendered by Jekyll as `docs/contributing.html` — updates automatically.

---

## 8. Step 6 — `README.md`

**Priority:** 🟠 High

### 8.1 Documentation & Governance Table (line ~152)

```
# Current:
| [**WIP-FILE-NAMING**] | ... | Rules for WIP file naming, status lifecycle (dev → review → final → approved) |

# Replace description with:
Rules for WIP file naming, status lifecycle (dev → review → final → approved; alpha parallel flow also supported)
```

### 8.2 WIP File Lifecycle Section (lines ~161–178)

Step 4 "Finalize" and Step 5 "Integrate" — add a new Step 4.A:

```markdown
4. **Finalize** — Approved content, status `final`
4A. **Alpha** *(optional, parallel)* — Integrated into pre-release snapshot, status `alpha`;
    WIP stays in `wip/` pending official integration
5. **Integrate** — Merge into guide, move to `archive/`, status `approved`
```

### 8.3 Status Codes Table (lines ~170–178)

Add row between `final` and `approved`:

```markdown
| `alpha` | Integrated into pre-release snapshot (parallel flow only) |
```

---

## 9. Step 7 — `.github/copilot-instructions.md`

**Priority:** 🟡 Important

### 9.1 WIP File Lifecycle Section (line ~56)

```
# Current:
**Status codes:** `dev` (draft) → `review` (under review) → `final` (approved) →
`approved` (integrated & archived) → `deprecated` (retired)

# Replace with:
**Status codes (standard flow):** `dev` (draft) → `review` (under review) →
`final` (ready to integrate) → `approved` (integrated & archived) → `deprecated` (retired)

**Alpha status (parallel, optional):** `alpha` — approved by the author; integrated
into the alpha pre-release snapshot; WIP file remains in `wip/` until official
integration into `guide.tex`. Active only when pre-release infrastructure is in progress.
```

### 9.2 Workflow Section (lines ~58–66)

After Step 5 "Finalize (status: final)", add:

```markdown
5A. **Alpha** *(parallel, optional)* — Human renames to `alpha` status after creating
    the alpha pre-release snapshot. Only used when pre-release infrastructure is active.
```

---

## 10. Step 8 — `docs/WIP-Snapshot-Generator-v3.1.html`

**Priority:** 🟡 Important

### 10.1 Changes Required

Locate the status dropdown (contains: `dev`, `review`, `final`, `approved`, `deprecated`).

Add option `alpha` between `final` and `approved`:
```html
<option value="alpha">alpha</option>
```

Add a tooltip or hint text explaining the parallel flow:
```html
<!-- near the alpha option or as a hint below the dropdown -->
Note: 'alpha' is the parallel pre-release flow status.
Use only when pre-release infrastructure is active.
```

Update the `pathHint` for `alpha` status to show `wip/` (same as `final`):
- Alpha WIP files stay in `wip/` — same directory as `dev`, `review`, `final`
- Only `approved` and `deprecated` go to `archive/WIP/`

---

## 11. Step 9 — `template/template-wip.tex`

**Priority:** 🟡 Important

### 11.1 Line 21 (IMPORTANTE block)

```latex
% Current:
% Status: dev | review | final | approved | deprecated

% Replace with:
% Status: dev | review | final | alpha | approved | deprecated
% Note: 'alpha' is the parallel pre-release flow (optional) — see wip-naming.md §0.5
```

### 11.2 Line 392 (Metadata Block)

```latex
% Current:
% WIP Status: dev | review | final | approved | deprecated

% Replace with:
% WIP Status: dev | review | final | alpha | approved | deprecated
% (alpha = parallel pre-release flow only — see wip-naming.md §3.1)
```

---

## 12. Steps 10–14 — SVG Diagrams

**Priority:** 🔵 Deferred — post-alpha

**Decision:** New files will likely be created rather than patching the existing ones.

**TODO (after alpha infrastructure is live):**

| File | What to add |
|------|-------------|
| `docs/wip-naming-diagram.svg` | `alpha` card + node in flowchart; forbidden transitions; shift downstream elements |
| `docs/wip-life-cycle.svg` | `alpha` node between `final` and `approved`; parallel dashed branch |
| `docs/wip-creation-workflow.svg` | `alpha` in Status Progression panel; note in Step 5 |
| `docs/wip-integration-flow.svg` | Parallel alpha path branch after Step 1 decision fork |
| `docs/version-system-diagram.svg` | (1) Snapshot filename pattern: add alpha variant `guide-v0.M.P.S-alpha.N-YYYYMMDD.tex`; (2) Version history timeline: add `v0.4.2.0-alpha.1` as projected pre-release entry between v0.4.1.1 and v0.5.0.0; (3) Step 8 "GitHub Tag + Release" in Version Bump Workflow: add note that alpha tags are pre-release |

### 12.1 `docs/wip-naming-diagram.svg` — MOST COMPLEX

**Current structure:** Status definition cards (left), lifecycle flowchart (right), forbidden box, success path callout. viewBox="0 0 1000 1370".

**Changes needed:**

**A. Add alpha status card** (in left column, between `final` y=802 and `approved` y=864):
- New card at y=864 (shift `approved` to y=928 and `deprecated` to y=992)
- Card fill: a distinct color, e.g., `#1565C0` (dark blue)
- Text: `alpha` (17px bold, white)
- Subtext: `wip/ · Parallel flow only`
- Sub-subtext: `Human decides — AI cannot`
- Shift `approved` and `deprecated` cards down by 64px
- Adjust viewBox height from 1370 to ~1430

**B. Add alpha node in flowchart** (right side, between `final` y=822 and `approved` y=894):
- New pill node between them (shift `approved` and its archive label down)
- Node fill: `#1565C0`
- Arrow from `final` to `alpha`: label "create alpha snapshot"
- Arrow from `alpha` to `approved` (green): label "integrate (official)"
- Dashed red arrow from `alpha` to `deprecated`
- Shift `approved` node, archive label, and deprecated node down by 64px

**C. Update FORBIDDEN transitions box** (currently at y=678):
Add two lines:
```
✗  alpha → final   (cannot revert)
✗  alpha → review  (cannot revert)
```

**D. Update SUCCESS PATH EXAMPLE callout** (currently at y=888):
Shift down by 64px to account for new node.

**E. Shift RESPONSIBILITY MATRIX section** (currently starts at y=1000):
Shift entire section down by ~60px. Adjust viewBox height accordingly.

**F. Update footer** (currently at y=1358): shift to y=1418.

### 12.2 `docs/wip-life-cycle.svg`

**Current structure:** Status Flow panel with 5 nodes (dev, review, final, approved, deprecated). viewBox="0 0 900 750".

**Changes needed:**

**A. Add alpha node** between `final` (y=225) and `approved` (y=310):
- Shift `approved` to y=395, `deprecated` to y=470
- New node at y=310: fill `#1565C0`, text "alpha", subtext "wip/ — Parallel flow only"
- Arrow `final → alpha`: label "create alpha snapshot"
- Arrow `alpha → approved`: label "official integration"
- Dashed arrow from left side to `alpha → deprecated` (similar to dev/review/final lines)

**B. Increase viewBox height** from 750 to ~830.

**C. Update footer** text position.

### 12.3 `docs/wip-creation-workflow.svg`

**Current structure:** Creation workflow steps (left), Status Progression panel (right at x=450). viewBox="0 0 800 900".

**Changes needed:**

**A. In Status Progression panel** (right side, currently ends at `approved` y=285):
Add alpha node between `final` (y=205) and `approved` (y=285):
- Shift `approved` down by 70px to y=355
- New node at y=285: fill `#1565C0`, text "alpha", subtext "Integrated into pre-release"
- Arrow `final → alpha`
- Arrow `alpha → approved`

**B. Update Step 5 text** (left side, green box):
```
# Current:
dev → review → final

# Add note:
dev → review → final
(alpha → approved for parallel pre-release flow)
```

**C. Update footer** y position.

### 12.4 `docs/wip-integration-flow.svg`

**Current structure:** Linear flow: Start → Step 1 (WIP "final") → Steps 2–6 → End. viewBox="0 0 850 950".

**Changes needed:**

This is the integration flow — it currently shows only the standard flow. The alpha flow is a DIFFERENT integration path. Add it as a parallel branch.

**A. At Step 1 (y=170 "WIP file has status 'final'")**, add a decision fork:
- After Step 1, add a diamond/decision: "Pre-release active?"
- YES branch (right side): Alpha Integration Path
- NO branch (main): continues to existing Steps 2–6

**B. Alpha Integration Path** (right side panel or branch):
```
Alpha Path:
Step 1-A: Rename WIP to alpha status
Step 1-B: Create alpha snapshot (wip/guide-v*-alpha.N-*.tex)
Step 1-C: Compile + verify
Step 1-D: Create tag v*.*.*.*-alpha.N
Step 1-E: Create GitHub pre-release
Step 1-F: WIP stays in wip/ (NOT moved to archive yet)
→ "Awaiting official integration" (loop back to Start for future cycle)
```

**C. Increase viewBox** height to accommodate the parallel path (estimated +200px).

---

## 13. Steps 16–17 — Issue Templates

**Priority:** 🔵

### 13.1 Step 16 — Create `.github/ISSUE_TEMPLATE/wip-alpha-template.yml`

```yaml
name: WIP — ALPHA (Pre-release Integration)
description: "Track the optional ALPHA step: integrating approved WIP content into a pre-release alpha snapshot."
title: "[ALPHA] C{N}: {Brief description}"
labels: []
body:
  - type: markdown
    attributes:
      value: |
        ## Alpha Integration Issue

        This is the **optional 5th step** in the WIP lifecycle, between FINAL and APPROVED.
        It applies only when pre-release infrastructure is active.

        **Prerequisite:** The corresponding FINAL issue must be closed before this issue is opened.

        **Standard flow for reference:** DEV → REVIEW → FINAL → _(ALPHA)_ → APPROVED

  - type: input
    id: chapter
    attributes:
      label: Chapter
      placeholder: "e.g., C5 — CMS"
    validations:
      required: true

  - type: input
    id: final_issue
    attributes:
      label: FINAL Issue (prerequisite)
      placeholder: "#XX — must be closed"
    validations:
      required: true

  - type: input
    id: alpha_snapshot
    attributes:
      label: Target alpha snapshot filename
      placeholder: "guide-v0.4.2.0-alpha.1-YYYYMMDD.tex"
    validations:
      required: true

  - type: input
    id: alpha_tag
    attributes:
      label: Target pre-release tag
      placeholder: "v0.4.2.0-alpha.1"
    validations:
      required: true

  - type: textarea
    id: deliverables
    attributes:
      label: Deliverables
      value: |
        - [ ] WIP file renamed from `final` to `alpha` status
        - [ ] Alpha snapshot created: `wip/guide-v*-alpha.N-*.tex`
        - [ ] Alpha snapshot compiled without errors
        - [ ] Alpha PDF generated and verified
        - [ ] Git tag created: `v*.*.*.*-alpha.N`
        - [ ] GitHub pre-release published (marked as pre-release, not full release)
        - [ ] Pre-release description lists included and pending chapters
    validations:
      required: false

  - type: textarea
    id: acceptance_criteria
    attributes:
      label: Acceptance Criteria (for transition to APPROVED)
      value: |
        APPROVED status (and archival to archive/WIP/) occurs only after:
        - [ ] Official integration into guide.tex (standard workflow)
        - [ ] Official version bump (e.g., v0.4.2.0)
        - [ ] Official GitHub release published
    validations:
      required: false

  - type: markdown
    attributes:
      value: |
        ---
        **Note:** This issue stays open until official integration (APPROVED).
        The WIP file stays in `wip/` until that point.
```

### 13.2 Step 17 — Update `.github/ISSUE_TEMPLATE/wip-final-template.yml`

Locate the "Next Steps" section in the existing template. Add a note:

```yaml
# In the Next Steps or bottom notes area, add:
- type: markdown
  attributes:
    value: |
      **Optional alpha flow:** When pre-release infrastructure is active, an ALPHA issue
      may be opened between FINAL and APPROVED. See `wip-alpha-template` for details.
```

---

## 14. Step 15 — `scripts/generate-integrated-files.py`

**Priority:** 🟢 Low (no breakage — minor cosmetic improvement)

**Decision required:** See §11.A before implementing.

### Option A (default — no code change)

Alpha snapshots (`guide-v*-alpha.*.tex`) in `wip/` will automatically appear in the
`wip/` section of the INTEGRATED-FILES report alongside WIP content files. No change needed.

### Option B (enhanced — separate section)

Add filter in `get_tracked_files()` to route files matching
`guide-v*-alpha.*-*.tex` to a separate "Alpha Snapshots" section.

Implementation:
```python
# In TRACKED_PATHS, add a new entry:
"wip/": {
    "ext": ".tex",
    "subfolders": ["wip/"],
    "exclude_pattern": r"^guide-v\d+\.\d+\.\d+\.\d+-alpha\.\d+-\d{8}\.tex$"
},
# And add:
"wip/ (alpha snapshots)": {
    "ext": ".tex",
    "subfolders": ["wip/"],
    "include_pattern": r"^guide-v\d+\.\d+\.\d+\.\d+-alpha\.\d+-\d{8}\.tex$",
    "label": "Alpha Snapshots"
},
```

This requires modifying `get_tracked_files()` to support `include_pattern` and `exclude_pattern` filters.

---

## 15. PNG Diagrams

**Priority:** 🖼️ Deferred — post-alpha

**Decision:** New files will likely be created using a design tool (draw.io, Figma, etc.) rather than modifying existing ones.

**TODO (after alpha infrastructure is live):**

| File | What to add |
|------|-------------|
| `docs/WIP-status-chart.png` | `alpha` node between `final` and `approved` |
| `docs/charts-and-diagrams/WIP Life Cycle.png` | Alpha bifurcation after `final` |
| `docs/charts-and-diagrams/WIP-integration-steps.png` | Note: alpha pre-integration status is `alpha`, not `final` |

---

## 16. Decisions (Resolved 2026-02-26)

### 16.A `generate-integrated-files.py` — Alpha Snapshots section

**Decision: Option B** — Separate "Alpha Snapshots" section in INTEGRATED-FILES report.
Alpha snapshots (`guide-v*-alpha.*.tex`) are routed to a dedicated section, not mixed
with WIP content files. Requires code change in Step 15 (use Option B implementation).

Code changes: both `exclude_pattern` in the `wip/` entry and a new `wip/ (alpha snapshots)`
entry — see Step 15.

Note: these script changes are implemented in `feat/alpha-release` but only execute
(produce output) after the branch is merged to `main`.

### 16.B Milestones

**Decision: Option A** — Use existing `v0.4.2.0` milestone. Standard practice
(GitHub, SemVer, npm, PyPI): pre-releases belong to the target version's milestone.
Alpha integration issues will be associated with `v0.4.2.0` and appear in its
milestone history when the official release is made.

### 16.C `validate-wip-naming.yml` test strategy

**Decision: Option B** — No validation on `feat/alpha-release`. Test via
`workflow_dispatch` after merging to `main`, or validate by pushing a test commit
to `main` in a controlled way.

### 16.D `generate-integrated-files.py` — Pre-release Tags section

**Decision: Option B** — Add a "Pre-release Tags" section to the INTEGRATED-FILES
report that captures alpha tags specifically.

Regex to add: `^v\d+\.\d+\.\d+\.\d+-alpha\.\d+(\.\d+)?$` — captures `v*-alpha.N`
and `v*-alpha.N.M` tags, excludes official version tags.

Note: same as §16.A — implemented in `feat/alpha-release`, executes after merge.

---

## 17. Validation Checklist

After implementing each step, verify:

### Critical (Steps 1–2)
- [ ] `validate-wip-naming.yml`: Push a test file `chapter-C5-test-alpha-2026-02-26.tex` to branch — workflow passes
- [ ] `validate-wip-naming.yml`: Push a test file `guide-v0.4.2.0-alpha.1-20260226.tex` to `wip/` — workflow passes
- [ ] `generate-wip-snapshot.py`: Run locally with a test `alpha` WIP file in `wip/` — emoji 🟢 appears in README table
- [ ] `generate-wip-snapshot.py`: Run locally with alpha snapshot in `wip/` — snapshot does NOT appear in WIP table

### Alpha Badge (Step 2B)

- [ ] `update-alpha-badge.py`: Run with alpha snapshot in `wip/guide/` — alpha badge appears in README.md and docs/index.html
- [ ] `update-alpha-badge.py`: Run without alpha snapshot — delimiter blocks are empty (badge absent)
- [ ] `README.md`: section heading renamed to `## 📊 Current Version — Official Guide`
- [ ] `README.md`: cell `| **Guide Version** | v... |` unchanged (script still matches)

### Governance (Steps 3–6)
- [ ] `wip-naming.md`: Standard flow (§0.5 Step 3) matches Consistency Glossary §0.3 verbatim
- [ ] `version-system.md`: Alpha snapshot naming (§2.1) matches Consistency Glossary §0.3 verbatim
- [ ] `briefing.md`: Status codes (§14) match wip-naming.md §7.2 exactly
- [ ] `README.md`: Status Codes table includes `alpha` with correct description
- [ ] All Cluster A files: verify `alpha` definition is identical

### Tools (Steps 7–9)
- [ ] `copilot-instructions.md`: Standard flow description includes alpha note
- [ ] `WIP-Snapshot-Generator HTML`: `alpha` option in dropdown; path hint shows `wip/`
- [ ] `template-wip.tex`: Both status comment lines include `alpha`

### SVGs (Steps 10–14)
- [ ] Each SVG: `alpha` node added between `final` and `approved`
- [ ] `wip-naming-diagram.svg`: FORBIDDEN box includes `alpha → final` and `alpha → review`
- [ ] `wip-integration-flow.svg`: parallel alpha path added

### Issue Templates (Steps 16–17)
- [ ] `wip-alpha-template.yml`: visible in GitHub issue creation UI
- [ ] `wip-final-template.yml`: "Next Steps" mentions alpha option

---

## 18. PR Strategy

### Commit Convention

Every commit made on `feat/alpha-release` during this implementation **must** reference issue #49 in the message:

```
<type>(<scope>): <description>

Refs #49
```

Examples:

```
feat(workflow): add alpha status to validate-wip-naming regex

Refs #49
```

```
docs(wip-naming): add alpha status definitions and two-flow block

Refs #49
```

This applies to all commits — including documentation, scripts, and minor fixes.

---

Before creating the PR:

1. **Sync with main:** `git merge origin/main` — resolve any `README.md` divergence (daily badge commits)
2. **Test validate-wip-naming.yml** (if Option A chosen in §16.C)
3. **Verify no automated workflows were accidentally modified** to trigger on `feat/alpha-release`
4. **Review consistency clusters** — spot-check all Cluster A files for identical wording

PR title: `feat: alpha release infrastructure (parallel pre-release flow)`

PR description must mention:
- 19 files modified, 3 created
- Branch was isolated from all automated workflows during development
- No changes to `wip/guide/` workflow, `guide.tex`, or any existing official release behavior

---

## 19. Impact Workflow Diagram

```
ALPHA RELEASE INFRASTRUCTURE — COMPLETE IMPACT MAP
====================================================

[DECISIONS] ──────────────────────────────────────────────────────────────────────
  §16.A: generate-integrated-files.py option?   (blocks Step 15)
  §16.B: milestones strategy?                   (informational)
  §16.C: validate-wip-naming.yml test strategy? (blocks validation)

[BRANCH] feat/alpha-release ─────────────────────────────────────────────────────
  All work here. Zero automatic workflow interference.

[CI/CRITICAL] ────────────────────────────────────────────────────────────────────

  Step 1: validate-wip-naming.yml
    ├── +alpha to 4 regex patterns (lines 89, 95, 101, 113)
    ├── +ALPHA_SNAPSHOT elif pattern in WIP/ARCHIVE/WIP block (before "Unknown WIP file" else)
    ├── +alpha snapshot elif pattern in GUIDE/ARCHIVE/GUIDE block (gap found during impl)
    └── +alpha to PR comment body (line 168)

  Step 2: generate-wip-snapshot.py
    ├── +STATUS_EMOJI['alpha'] = '🟢'
    ├── +alpha in parse_status() regex
    ├── +exclude any guide-*.tex from get_wip_files() (fname.startswith('guide'))
    └── +🟢 alpha in legend string
         └── [SECONDARY] README.md WIP legend auto-updates on next run

  Step 2B: update-alpha-badge workflow (NEW)
    ├── NEW: .github/workflows/update-alpha-badge.yml (push main + workflow_dispatch)
    ├── NEW: scripts/update-alpha-badge.py
    │         ├── scans wip/guide/ for guide-v*-alpha*.tex
    │         ├── if found: fills ALPHA-BADGE + ALPHA-FOOTER delimiter blocks
    │         └── if not found: clears delimiter blocks
    ├── README.md: +<!-- ALPHA-BADGE-START/END --> below official badge (line ~29)
    ├── README.md: +<!-- ALPHA-FOOTER-START/END --> below footer line (line ~289)
    ├── README.md: rename section heading → `## 📊 Current Version — Official Guide` (line ~47)
    └── docs/index.html: +<!-- ALPHA-BADGE-START/END --> below version badge (line ~305)

[GOVERNANCE — source of truth] ───────────────────────────────────────────────────

  Step 3: wip-naming.md  ◄── CANONICAL WORDING SOURCE
    ├── §0.3 +note on alpha snapshots not covered by WIP naming convention
    ├── §0.4 +guide-v*-alpha.*-*.tex to directory tree
    ├── §0.5 Step 3 +two-flow block (Standard + Alpha)
    ├── §3.1 +alpha row in Status Definitions table
    ├── §3.2 +Alpha Flow diagram (ASCII, separate block)
    ├── §3.3 +Alpha Flow Transitions block
    ├── §3.4 +Alpha Flow Success Path example
    ├── §4.2→§4.3 Alpha Integration Workflow (new subsection)
    ├── §4.3→§4.4 Archival +note on alpha WIP files
    ├── §5.3 +Alpha Flow workflow diagram
    ├── §6 Responsibility Matrix +3 rows
    ├── §7.2 +alpha quick reference row
    ├── §7.3 +folder structure note
    └── §7.4 Checklist for AI +alpha to valid status list
         └── [SECONDARY] SVG diagrams (Steps 10-14) must reflect §3.1-§3.4

  Step 4: version-system.md
    ├── §1.5 +alpha snapshot note in repo structure
    ├── §2.1 +alpha snapshot naming pattern
    ├── §2.3 +alpha snapshot examples
    ├── §6.2 +Alpha Snapshot Workflow section
    ├── §6.3 +alpha snapshots exception to single-file rule
    ├── §6.5.1 +alpha tag format
    ├── §6.5.2 +pre-release rules
    ├── §6.5.4 +alpha path in workflow diagram
    └── §7.3 +pre-release note

  Step 5: briefing.md
    ├── §11.1 +alpha snapshots in directory tree
    ├── §12.4 +alpha in status lifecycle note
    ├── §13 Step 5 +alpha status description
    └── §14 +alpha in status codes quick reference
         └── [SECONDARY] docs/contributing.html auto-updates (Jekyll)

  Step 6: README.md
    ├── Documentation table: WIP-FILE-NAMING description +alpha mention
    ├── WIP Lifecycle: +Step 4A (optional alpha)
    └── Status Codes table: +alpha row

[AI CONTEXT + TOOLS] ─────────────────────────────────────────────────────────────

  Step 7: copilot-instructions.md
    ├── Status codes line +alpha (parallel flow)
    └── Workflow section +Step 5A (alpha)

  Step 8: WIP-Snapshot-Generator HTML
    ├── +alpha option in status dropdown
    ├── +path hint: alpha → wip/ (same as final)
    └── +note: parallel pre-release flow

  Step 9: template-wip.tex
    ├── Line 21: +alpha to status list
    └── Line 392: +alpha to WIP Status line

[SVG DIAGRAMS] ────────────────────────────────────────────────────────────────────

  Step 10: wip-naming-diagram.svg (most complex)
    ├── +alpha status card (left column, between final and approved)
    ├── +alpha node in lifecycle flowchart
    ├── +final→alpha, alpha→approved, alpha→deprecated arrows
    ├── +FORBIDDEN: alpha→final, alpha→review
    └── +viewBox height increase + element position shifts

  Step 11: wip-life-cycle.svg
    ├── +alpha node between final and approved
    ├── +arrows for alpha flow
    └── +viewBox height increase

  Step 12: wip-creation-workflow.svg
    ├── +alpha node in Status Progression panel
    └── +Step 5 text update

  Step 13: wip-integration-flow.svg
    ├── +decision fork after Step 1
    └── +parallel Alpha Integration Path

  Step 14: version-system-diagram.svg
    ├── +alpha snapshot filename pattern
    ├── +v0.4.2.0-alpha.1 in version history timeline
    └── +pre-release note in Step 8 "GitHub Tag + Release"

[ISSUE TEMPLATES] ─────────────────────────────────────────────────────────────────

  Step 16: wip-alpha-template.yml (NEW FILE)
    └── Complete template for ALPHA step in issue workflow

  Step 17: wip-final-template.yml
    └── +note in Next Steps about optional alpha

[LOW PRIORITY] ────────────────────────────────────────────────────────────────────

  Step 15: generate-integrated-files.py (Decision §16.A)
    └── Option A: no change
        Option B: +alpha snapshots section

  Manual/deferred: PNG recreation (post-alpha), milestones, test strategy (decisions)

[CONSISTENCY CLUSTERS — spot-check before PR] ─────────────────────────────────────

  Cluster A (alpha definition, 7 files):
    wip-naming.md §3.1 = briefing.md §14 = copilot-instructions.md = template-wip.tex
    = WIP-Generator HTML = README.md Status Codes

  Cluster B (two-flow block, 3 files):
    wip-naming.md §0.5 = version-system.md §6.5.4 = copilot-instructions.md

  Cluster C (directory trees, 4 files):
    wip-naming.md §0.4 = version-system.md §1.5 = briefing.md §11.1 = README.md

  Cluster D (alpha snapshot naming, 3 files):
    version-system.md §2.1 = version-system.md §2.3 = wip-naming.md §0.3

  Cluster E (alpha tag format, 3 sections):
    version-system.md §6.5.1 = §6.5.2 = §6.5.4

====================================================
TOTAL: 17 files to modify + 3 to create
====================================================
```

---

*Documento gerado após varredura completa de todos os arquivos do repositório.*
*Baseado em: alpha-release-handoff.md (spec) + alpha-release-impact.md (pesquisa) + leitura direta de wip-naming.md, version-system.md, briefing.md, README.md, todos os SVGs, scripts e workflows.*
