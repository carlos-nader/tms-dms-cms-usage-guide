# Alpha Release Infrastructure — Impact & Implementation Scope

**Created:** 2026-02-26
**Author:** Research session — Claude Sonnet 4.6
**Source spec:** [`misc/alpha-release-handoff.md`](alpha-release-handoff.md)
**Status:** Awaiting author review before implementation

> **Princípio orientador:** o fluxo alpha é uma estrutura paralela e opcional ao fluxo padrão.
> O fluxo padrão (`dev → review → final → approved`) permanece **intacto e inalterado**.
> O fluxo alpha (`final → alpha → approved`) é ativado apenas quando há infraestrutura de
> pre-release em curso. Toda alteração deve deixar isso explícito.

---

## Metodologia

Varredura completa do repositório realizada em 2026-02-26:
- Todos os arquivos em `docs/`, `scripts/`, `.github/workflows/`, `.github/ISSUE_TEMPLATE/`
- Todos os arquivos `.md`, `.tex`, `.py`, `.yml`, `.html`, `.svg`, `.png` relevantes
- Issues e milestones do GitHub via `gh` CLI
- Contraste com checklist externo fornecido pelo autor

---

## 1. Crítico — quebra o CI/automação se não atualizado

### 1.1 `.github/workflows/validate-wip-naming.yml`

**Problema:** A regex de validação de status é `(dev|review|final|approved|deprecated)`. Dois casos de falha:

1. Um WIP file com status `alpha` (ex: `chapter-C5-style-rev-alpha-2026-02-27.tex`) seria rejeitado na validação de nomes.
2. O snapshot alpha `guide-v0.4.2.0-alpha.1-YYYYMMDD.tex` localizado em `wip/` (raiz) não bate com nenhum padrão WIP existente e também não está em `wip/guide/` — falha em todos os padrões.

**Mudanças necessárias:**
- Adicionar `alpha` à regex de status válidos nos padrões `chapter`, `section`, `table`, `visual`, `notes`
- Adicionar padrão específico para snapshots alpha em `wip/` (arquivos com formato `guide-v*-alpha.*-*.tex`)

**Nota sobre trigger:** o workflow não tem filtro de paths — dispara em **qualquer** push para `main` ou `develop` (confirmado por observação em produção). O branch `feat/alpha-release` **não está** na lista de branches do trigger, portanto as mudanças no workflow **não serão testadas automaticamente** no feature branch. Estratégia de teste: adicionar `feat/alpha-release` temporariamente ao trigger durante desenvolvimento, ou testar manualmente via `workflow_dispatch`.

---

### 1.2 `scripts/generate-wip-snapshot.py`

**Problema:** Dois pontos de falha silenciosa:

1. Dicionário `STATUS_EMOJI` não tem entrada para `alpha` — WIP files com status `alpha` aparecem sem emoji e com status em branco na tabela WIP do README.
2. `parse_status()` não reconhece `alpha` — mesmo resultado.
3. O snapshot alpha `guide-v0.4.2.0-alpha.1-YYYYMMDD.tex` em `wip/` seria incluído na tabela de WIP ativos sem status — confusão visual, pois é um snapshot, não um WIP de conteúdo.

**Mudanças necessárias:**
- Adicionar `'alpha'` ao dicionário `STATUS_EMOJI` (sugestão: emoji distinto, ex: `🔵`)
- Atualizar `parse_status()` para reconhecer `alpha`
- Adicionar filtro para excluir arquivos `guide-v*.tex` da tabela WIP (são snapshots, não WIP de conteúdo)

---

## 2. Alta prioridade — documentação de governança oficial

### 2.1 `docs/wip-naming.md`

Seções que precisam de mudança:

| Seção | Mudança necessária |
|-------|--------------------|
| §0.4 Estrutura de diretórios | Adicionar linha `guide-v*.alpha.*-*.tex` em `wip/` com nota "when pre-release active" |
| §0.5 Step 3 (status progression) | Adicionar bloco separado com Standard Flow e Alpha Flow (parallel, optional) |
| §3.1 Status Codes table | Adicionar linha `alpha` com nota explícita de fluxo paralelo |
| §3.2 Status Flow Diagram | NÃO modificar diagrama principal; adicionar diagrama separado "Alpha Flow (parallel, optional)" |
| §3.3 Transition Rules | Adicionar bloco "Alpha Flow Transitions" após as regras existentes |
| §3.4 Success Path Example | Manter exemplo padrão; adicionar exemplo separado "Success Path — Alpha Flow" |
| §4.2 Integration into Main Document | Manter intacto; adicionar §4.3 "Alpha Integration Workflow" como subseção nova |
| §5.3 GitHub Workflow | Manter diagrama existente; adicionar diagrama paralelo para o fluxo alpha |
| §7.2 Status Codes quick ref | Adicionar linha `alpha` com nota "(parallel flow only)" |
| §7.3 Folder Structure | Documentar que `wip/` pode conter snapshots alpha, distinguindo-os dos WIP files |
| §7.4 Checklist for AI | Adicionar `alpha` à lista de status válidos com nota de que a decisão é exclusivamente humana |

---

### 2.2 `docs/version-system.md`

Seções que precisam de mudança:

| Seção | Mudança necessária |
|-------|--------------------|
| §1.5 Repository Structure | Adicionar snapshots alpha em `wip/` (distinguir de `wip/guide/`) |
| §2.1 Snapshot File Name Rule | Adicionar padrão alpha: `guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N-YYYYMMDD.tex` |
| §2.3 Examples | Adicionar exemplo alpha |
| §6.2 File Naming and Snapshot Workflow | Adicionar fluxo alpha como caminho paralelo |
| §6.3 Archival Strategy | Clarificar que snapshots alpha NÃO vão para `archive/GUIDE/`; ficam em `wip/` até a release oficial |
| §6.5.1 Tags | Adicionar formato de tag alpha: `v0.4.2.0-alpha.N` |
| §6.5.2 Releases | Adicionar regras para pre-releases: marcados como pre-release no GitHub, não substituem a release oficial |
| §6.5.4 Workflow Integration | Adicionar fluxo alpha ao diagrama de integração |
| §7.3 Key Notes | Adicionar nota sobre pre-releases e sua distinção das releases oficiais |

---

### 2.3 `docs/briefing.md`

Seções que precisam de mudança:

| Seção | Mudança necessária |
|-------|--------------------|
| §11.1 Directory Structure | Mostrar `wip/` com snapshots alpha possíveis |
| §14 Quick Reference | Ciclo `final → approved` sem menção ao alpha; adicionar nota sobre fluxo paralelo |
| §15 Checklist | Item "Status: final" como pré-requisito para integração; adicionar que para alpha o pré-requisito é `alpha` |

---

### 2.4 `README.md`

**Mudança necessária:** Seção de status/workflow do projeto menciona releases sem distinção de pre-releases. Adicionar nota sobre o significado de releases alpha e que não substituem a versão oficial.

---

## 3. Importante — ferramentas e contexto de AI

### 3.1 `.github/copilot-instructions.md`

**Problema:** Linha 56 descreve explicitamente o ciclo como `dev (draft) → review → final → approved → deprecated`. Esta é a fonte de verdade para todos os agentes de IA no projeto.

**Mudança necessária:**
- Atualizar a lista de status codes para incluir `alpha`
- Atualizar a seção "WIP File Lifecycle" (step-by-step) para contemplar o fluxo alpha como opcional
- Adicionar nota: "alpha é status do fluxo paralelo, ativado apenas quando pre-release está em curso"

---

### 3.2 `docs/WIP-Snapshot-Generator-v3.1.html`

**Problema:** Dropdown de status contém apenas: `dev / review / final / approved / deprecated`. Ferramenta usada para gerar nomes de arquivos WIP.

**Mudança necessária:**
- Adicionar opção `alpha` ao dropdown de status
- Adicionar nota ou hint explicando que `alpha` é do fluxo paralelo (opcional)
- Atualizar o `pathHint` para mostrar que arquivos `alpha` ficam em `wip/` (como `final`)

---

### 3.3 `template/template-wip.tex`

**Problema:** Linhas 21 e 392 listam explicitamente os status válidos:
```
% Status: dev | review | final | approved | deprecated
```

**Mudança necessária:**
- Atualizar as duas ocorrências para incluir `alpha`:
  `% Status: dev | review | final | alpha | approved | deprecated`
- Adicionar comentário explicativo sobre `alpha` (fluxo paralelo, opcional)

---

## 4. Diagramas SVG — editáveis como texto

Todos os quatro SVGs abaixo descrevem o lifecycle e precisam de atualização.
São arquivos de texto (XML) — editáveis diretamente.

| Arquivo | Conteúdo atual | Mudança necessária |
|---------|---------------|-------------------|
| `docs/wip-naming-diagram.svg` | Diagrama mais completo: dois fluxos de lifecycle + transições proibidas + exemplos | Adicionar node `alpha` e fluxo paralelo; atualizar transições proibidas |
| `docs/wip-life-cycle.svg` | Nodes: dev → review → final → approved → deprecated | Adicionar node `alpha` como ramificação paralela após `final` |
| `docs/wip-creation-workflow.svg` | Fluxo: dev → review → final → approved | Adicionar bifurcação alpha após `final` |
| `docs/wip-integration-flow.svg` | Fluxo de integração a partir de `final` → `approved` | Adicionar caminho alpha: `alpha` → snapshot → tag → pre-release |

**Estes dois NÃO precisam de mudança:**
- `docs/version-system-diagram.svg` — sobre versionamento de releases, não lifecycle de WIP
- `docs/issue-dependency-map.svg` — auto-gerado via `gh issue list`, não descreve lifecycle

---

## 5. Diagramas PNG — precisam ser recriados manualmente

Estes são arquivos binários — **não editáveis via ferramentas de texto**. Precisam ser recriados em ferramenta de design (ex: draw.io, Lucidchart, Figma).

| Arquivo | Conteúdo atual | Mudança necessária |
|---------|---------------|-------------------|
| `docs/WIP-status-chart.png` | Diagrama completo dev→review→final→approved→deprecated com descrições de cada status | Adicionar node `alpha` com descrição; mostrar como fluxo paralelo |
| `docs/charts-and-diagrams/WIP Life Cycle.png` | Flowchart: dev→review→final→approved com decision diamonds | Adicionar bifurcação alpha após `final` |
| `docs/charts-and-diagrams/WIP-integration-steps.png` | Checklist Before/During/Post integration; item (1): "File status is final in WIP/" | Adicionar variante ou nota: para alpha, status pré-integração é `alpha` (não `final`) |

---

## 6. Issue Templates — workflow visível ao usuário

### 6.1 Criar: `.github/ISSUE_TEMPLATE/wip-alpha-template.yml` (NOVO)

Os 4 templates existentes descrevem "4 sequential issues: DEV → REVIEW → FINAL → APPROVED". O fluxo alpha é invisível para quem abre uma issue.

**Criar** um novo template `wip-alpha-template.yml` para o passo opcional ALPHA, análogo aos existentes, descrevendo:
- Que é o 5º passo opcional, entre FINAL e APPROVED
- Pré-requisito: FINAL issue fechada
- Entregáveis: rename para `-alpha-`, criação do snapshot alpha, geração do PDF, tag pre-release
- Critérios de aceite para transição para APPROVED

### 6.2 Atualizar: `.github/ISSUE_TEMPLATE/wip-final-template.yml`

**Mudança mínima:** Adicionar nota em "Next Steps" mencionando que entre FINAL e APPROVED existe a opção do passo ALPHA (quando pre-release infrastructure está ativa).

---

## 7. Scripts sem impacto (verificados e confirmados)

| Script/Workflow | Motivo de não precisar de mudança |
|-----------------|----------------------------------|
| `scripts/update-readme-version.py` | `validate_version()` rejeita `0.4.2.0-alpha.1` com exit 1 — comportamento **correto**, impede que alpha atualize a versão oficial no README/index.html |
| `scripts/validate-tex-preamble.py` | Usa `rglob('*.tex')` — valida qualquer `.tex` incluindo snapshots alpha; preamble correto passa normalmente |
| `scripts/generate-integrated-files.py` | Alpha tags aparecem no campo "Releases" (glob funciona); ausência na seção "VERSION TAGS" (regex exclui) é omissão menor, não falha. Snapshot alpha em `wip/` aparece automaticamente na seção `wip/` do relatório — ver Questão em aberto §8 |
| `.github/workflows/sync-pdf-to-docs.yml` | Só copia `guide.pdf`; alpha PDF vai como release asset, não como `guide.pdf` |
| `.github/workflows/update-readme-on-tag.yml` | Trigger `workflow_dispatch` apenas (manual); alpha tags não o disparam |
| `.github/workflows/validate-tex-preamble.yml` | Trigger `wip/**/*.tex` cobre `wip/file.tex`; snapshot alpha é validado normalmente |
| `.github/workflows/generate-integrated-files.yml` | Trigger adequado; comportamento do script já analisado acima |
| `.github/workflows/greetings.yml` | Saúda novos contribuidores — sem impacto |
| `.github/workflows/update-forum-views.yml` | Atualiza badge de visualizações. Commit com deploy key em `main` dispara chain completo: `validate-wip-naming.yml` (sem path filter — roda em qualquer push para `main`/`develop`), `generate-wip-snapshot.yml` (sem path filter), `pages-build-deployment`. Chain benigno, termina em no máximo 3 runs adicionais. Não afeta `feat/alpha-release`. |
| `pages-build-deployment` (GitHub Pages) | Rebuild automático a cada push para `main`. Ao mergear `feat/alpha-release` → `main`, o site será reconstruído automaticamente com SVGs e docs atualizados. Comportamento esperado e desejado. Não requer ação. |
| `docs/contributing.html` | GitHub Pages renderizado de CONTRIBUTING.md; atualiza automaticamente |
| `docs/integrated-files.html` | Auto-gerado pelo workflow `generate-integrated-files.yml` — atualiza automaticamente |
| `docs/_config.yml` | Configuração Jekyll; sem referências a lifecycle |
| `docs/tex-preamble-consolidated.md` | Documentação de preamble LaTeX; sem lifecycle |
| `misc/STYLE-GUIDE.md` | Prosa e estilo; "final/review" aparecem como inglês comum, não como status codes |
| `CHANGELOG.md` | Registro de eventos; entrada para alpha será adicionada quando o primeiro alpha for criado, não agora |
| `SETUP.md` | Configuração de ambiente; workflow fica nos docs de governança |
| `docs/version-system-diagram.svg` | Sobre versioning system, não WIP lifecycle |
| `docs/issue-dependency-map.svg` | Auto-gerado via `gh issue list` |
| `check-guide-integrity.ps1` | Só escaneia `wip\guide\` (linha `$SnapshotDir = "$RepoRoot\wip\guide"`); alpha snapshots ficam em `wip\` raiz — nenhuma interferência. Também é gitignored (arquivo local, não versionado). |
| `.gitignore` | Alpha snapshots (`guide-v*-alpha.*.tex` em `wip/`) não são afetados por nenhuma regra existente — serão trackeados normalmente. `misc/pessoal/*.*` é inteiramente gitignored (arquivos locais, sem impacto no repo). |
| `misc/Pessoal/` (todos os arquivos) | Gitignored — locais apenas. `claude-project-instructions.md`, `STYLE-PROMPT.md`, `ClaudeCode-Diagnostico.md` não são versionados. Sem ação necessária. |
| GitHub Labels | Sem label `alpha` ou `pre-release`. Problema pré-existente: templates de issue referenciam label `"wip"` que também não existe. Para `wip-alpha-template.yml`, criar label seria ideal mas é baixa prioridade — GitHub ignora silenciosamente labels inexistentes. |

---

## 8. Questões em aberto para decisão do autor

| Questão | Contexto | Opções |
|---------|----------|--------|
| **Milestones** | Alpha releases de C5 cabem no milestone v0.4.2.0 existente, ou precisam de milestone separado? | (A) Usar milestone v0.4.2.0 existente · (B) Criar milestone `v0.4.2.0-alpha` separado |
| **`generate-integrated-files.py` — seção do relatório** | O script já escaneia `wip/*.tex`, então o snapshot alpha aparecerá automaticamente na seção `wip/` do INTEGRATED-FILES junto com WIP de conteúdo (chapters, sections). É uma decisão estrutural: separar ou não? | (A) Aceitar como está — snapshot alpha aparece misturado com WIP de conteúdo · (B) Filtrar `guide-v*-alpha.*.tex` para seção dedicada "Alpha Snapshots" no relatório |
| **`generate-integrated-files.py` — VERSION TAGS** | Alpha tags aparecem em "Releases" (glob captura) mas não na seção "VERSION TAGS" (regex `^v\d+\.\d+\.\d+\.\d+$` exclui). Problema visual? | (A) Aceitar como está · (B) Adicionar seção "Pre-release Tags" no relatório |
| **Ordem de implementação** | O que vai para o branch primeiro — scripts críticos ou documentação? | Sugestão: scripts críticos primeiro (1.1, 1.2) para validar o CI antes de qualquer push com arquivo alpha |

---

## 9. Análise de isolamento do branch `feat/alpha-release`

> **Conclusão da análise (2026-02-26):** a estratégia de branch paralelo é segura. O trabalho em `feat/alpha-release` é completamente isolado dos workflows automáticos de `main`.

### 9.1 Workflows automáticos — impacto sobre o feature branch

| Workflow | Trigger | Afeta `feat/alpha-release`? | Motivo |
| -------- | ------- | -------------------------- | ------ |
| `update-forum-views.yml` | Schedule diário (10h UTC) | ❌ Não | Só roda em `main` via `schedule`; push resultante vai para `main` |
| `generate-wip-snapshot.yml` | Push para `main` (sem path filter) | ❌ Não | Branch não está na lista de triggers |
| `validate-wip-naming.yml` | Push para `main` ou `develop` (sem path filter) | ❌ Não | `feat/alpha-release` não está na lista de branches |
| `pages-build-deployment` | Push para `main` | ❌ Não | GitHub Pages só serve `main` |
| `generate-integrated-files.yml` | Push para `main` (paths específicos) | ❌ Não | Branch não está no trigger |
| `validate-tex-preamble.yml` | Push (paths `wip/**/*.tex`) | ❌ Não | Branch não está no trigger |

### 9.2 Divergência acumulada durante a implementação

O único ponto de atenção é divergência em `README.md`:

- `update-forum-views.yml` atualiza a badge de views diariamente em `main`
- `generate-wip-snapshot.yml` pode atualizar a tabela WIP em `main` se houver push de arquivos WIP
- Nenhum desses commits toca nos arquivos que serão modificados no feature branch (exceto `README.md`)

**Resolução:** executar `git merge origin/main` no `feat/alpha-release` antes de abrir o PR final. Conflitos esperados em `README.md` são triviais (seções distintas).

### 9.3 Limitação de teste no feature branch

`validate-wip-naming.yml` não dispara em `feat/alpha-release`. As mudanças no workflow só serão testadas automaticamente após o merge para `main`.

**Estratégia de contorno (a decidir):**

- (A) Adicionar `feat/alpha-release` temporariamente ao trigger do workflow durante desenvolvimento → remover antes do PR
- (B) Testar manualmente via `workflow_dispatch` na branch após push

---

## 10. Resumo executivo

**Total: 15 arquivos a modificar + 1 a criar**

| Prioridade | Qtd | Arquivos |
|-----------|-----|---------|
| 🔴 Crítico | 2 | `validate-wip-naming.yml`, `generate-wip-snapshot.py` |
| 🟠 Alta | 4 | `wip-naming.md`, `version-system.md`, `briefing.md`, `README.md` |
| 🟡 Importante | 3 | `copilot-instructions.md`, `WIP-Snapshot-Generator-v3.1.html`, `template-wip.tex` |
| 🟢 SVG (texto) | 4 | `wip-naming-diagram.svg`, `wip-life-cycle.svg`, `wip-creation-workflow.svg`, `wip-integration-flow.svg` |
| 🔵 Issue templates | 2 | `wip-alpha-template.yml` (CRIAR), `wip-final-template.yml` (nota) |
| 🖼️ PNG (binário) | 3 | `WIP-status-chart.png`, `WIP Life Cycle.png`, `WIP-integration-steps.png` |

**Branch de implementação:** `feat/alpha-release` → implementar em ordem de prioridade → PR para `main` quando validado.

**Nota sobre workflows automáticos em `main` durante a implementação:**
O workflow `update-forum-views.yml` faz commit diário em `README.md` na `main`. O `generate-wip-snapshot.yml` (sem filtro de paths) dispara em seguida mas sai silenciosamente se não há mudanças WIP. Ambos os commits acumulam divergência em `README.md` entre `main` e `feat/alpha-release`. Resolução padrão: `git merge origin/main` no branch antes do PR final.

---

*Documento gerado por varredura completa do repositório. Sujeito a revisão e aprovação do autor antes de qualquer implementação.*
