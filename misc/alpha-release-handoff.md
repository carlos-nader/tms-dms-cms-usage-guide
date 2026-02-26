# Handoff Briefing — Alpha Release Infrastructure
## Para: Claude Code (VSCode)
## De: Claude (claude.ai) — sessão 2026-02-26
## Projeto: Falcon BMS TMS/DMS/CMS HOTAS Usage Guide

---

## 1. Contexto e Problema

O projeto está em v0.4.1.1. O bump para v0.4.2.0 só ocorrerá quando **todos os capítulos**
(C1, C2, C3, C5) passarem por revisão de estilo completa (issue #44). Isso vai demorar meses.

Enquanto isso, o `guide.tex` fica estático em v0.4.1.1 e o trabalho aprovado fica preso
em WIPs com status `final` — invisível para a comunidade.

**A solução decidida:** criar uma infraestrutura de **alpha releases** que permita publicar
capítulos aprovados progressivamente, sem integração oficial ao `guide.tex` e sem bump de
versão oficial.

---

## 2. Decisões Tomadas (sujeitas a revisões e propostas de melhoria)

Todas as decisões abaixo foram tomadas pelo autor humano (Carlos) em sessão de 2026-02-26.

### 2.1 Mecanismo de publicação: pre-release tags GitHub

A cada capítulo aprovado no style review:
- Cria-se uma tag `v0.4.2.0-alpha.N` (ex: `v0.4.2.0-alpha.1` para C5)
- A tag gera um GitHub Release marcado explicitamente como **pre-release**
- O PDF publicado na release é gerado a partir do **snapshot alpha** (não do `guide.tex`)

### 2.2 Novo status no ciclo WIP

- Aplicável apenas quanddo houver necessidade de versões ALPHA intermediárias;
- Sistema novo existirá em PARALELO ao sistema atual.

O ciclo atual é: `dev → review → final → approved`

O novo ciclo será: `dev → review → final → alpha → approved`

**Definição de `alpha`:**
- Conteúdo aprovado pelo autor no style review
- Integrado no snapshot alpha
- Aguardando integração oficial no `guide.tex` e bump de versão
- WIP permanece em `wip/` (NÃO vai para `archive/WIP/`)
- `approved` continua reservado para integração oficial em `guide.tex`

### 2.3 Localização do snapshot alpha

**Problema técnico crítico:** `wip/guide/` só pode conter UM arquivo — os GitHub Actions
workflows assumem arquivo único nessa pasta. Colocar o snapshot alpha lá quebraria os workflows.

**Solução:** o snapshot alpha fica em `wip/` (raiz dos WIPs), NÃO em `wip/guide/`.

```
wip/
  guide/
    guide-v0.4.1.1-20260218.tex        ← snapshot oficial (único, INTOCADO)
  guide-v0.4.2.0-alpha.1-YYYYMMDD.tex  ← snapshot alpha (AQUI, não em guide/)
  chapter-C5-style-rev-alpha-...tex    ← WIP com status alpha
  ...
```

Nomenclatura do snapshot alpha:
```
wip/guide-v0.4.2.0-alpha.{N}-{YYYYMMDD}.tex
```

### 2.4 Escopo das alterações: OFICIAL

Esta infraestrutura deve ser implementada como política **oficial** do projeto —
atualizada em todos os documentos de governança. Não é solução casuística.
A razão: C1, C2, C3 passarão pelo mesmo ciclo. O padrão se repetirá. Futuras versões poderão ser submetidas ao mesmo processo.

---

## 3. Arquivos a Modificar (necessária revisão para verificação de outros arquivos, links, estrutura etc.)

Os seguintes arquivos de governança precisam ser atualizados.
(sem número de versão no nome — policy 2026-02-25).

**Princípio orientador para todas as alterações:** o fluxo alpha é uma **estrutura paralela
e opcional** ao fluxo padrão — não uma etapa obrigatória inserida no ciclo existente.
O fluxo padrão (`dev → review → final → approved`) permanece intacto e inalterado.
O fluxo alpha (`final → alpha → approved`) é uma bifurcação ativada apenas quando há
infraestrutura de pre-release em curso. Toda documentação deve deixar isso explícito.

### 3.1 `docs/wip-naming.md` — Alterações necessárias

1. **Seção 0.4 (File Organization Structure):** adicionar `guide-v0.4.2.0-alpha.N-YYYYMMDD.tex`
   como entrada em `wip/` (não em `wip/guide/`). Anotar que snapshots alpha coexistem
   com WIP files de capítulo/seção na mesma pasta.

2. **Seção 0.5 Step 3 (status list):** NÃO inserir `alpha` no fluxo padrão. Em vez disso,
   adicionar bloco separado após a descrição do fluxo padrão:
   ```
   FLUXO PADRÃO (sempre aplicável):
   dev → review → final → approved

   FLUXO ALPHA (paralelo, opcional — ativo apenas quando pre-release em curso):
   final → alpha → approved
   ```
   Com definição de `alpha`: "conteúdo aprovado pelo autor e integrado no snapshot alpha;
   WIP permanece em `wip/` aguardando integração oficial em `guide.tex`; `approved`
   só ocorre após integração oficial."

3. **Seção 3.1 (Status Codes):** adicionar linha para `alpha` com nota explícita de que
   é status do fluxo paralelo, não do fluxo padrão:
   | `alpha` | `wip/` | Fluxo paralelo: integrado no snapshot alpha; aguarda integração oficial |

4. **Seção 3.2 (Status Flow Diagram):** NÃO modificar o diagrama principal. Adicionar
   diagrama separado para o fluxo alpha, após o diagrama existente, com cabeçalho
   "Alpha Flow (parallel, optional)".

5. **Seção 3.3 (Transition Rules):** adicionar bloco separado "Alpha Flow Transitions"
   após as regras existentes:
   - Permitidas: `final → alpha`, `alpha → approved`, `alpha → deprecated`
   - Proibidas: `alpha → final`, `alpha → review`, `alpha → dev`
   - Nota: as transições do fluxo padrão não são alteradas.

6. **Seção 3.4 (Success Path Example):** manter o exemplo existente (fluxo padrão)
   intacto. Adicionar exemplo separado "Success Path — Alpha Flow" após o existente.

7. **Seção 4.2 (Integration into Main Document):** manter o workflow existente intacto.
   Adicionar subseção separada "4.3 Alpha Integration Workflow" descrevendo o fluxo
   paralelo: integração no snapshot alpha, geração do PDF, criação da pre-release tag.

8. **Seção 5.3 (GitHub Workflow):** manter o diagrama existente intacto. Adicionar
   diagrama paralelo para o fluxo alpha:
   ```
   final → alpha snapshot → tag v0.4.2.0-alpha.N → pre-release → (aguarda)
                                                                        ↓
                                                              approved (quando guide.tex integrado)
   ```

9. **Seção 7.2 (Status Codes quick reference):** adicionar linha `alpha` com nota
   "(parallel flow only)".

10. **Seção 7.3 (Folder Structure):** documentar que `wip/` pode conter snapshots alpha,
    distinguindo-os dos WIP files de capítulo/seção.

### 3.2 `docs/version-system.md` — Alterações necessárias

1. **Seção 1.5 (Repository Structure):** clarificar que `wip/` pode conter snapshots alpha
   (`guide-v*.alpha.*.tex`) além dos WIP files de capítulo/seção.

2. **Seção 2.1 (Snapshot File Name Rule):** adicionar padrão de nomenclatura para snapshots alpha:
   ```
   wip/guide-vMAJOR.MINOR.PATCH.SUBPATCH-alpha.N-YYYYMMDD.tex
   ```
   Distinguir claramente de snapshots oficiais em `wip/guide/`.

3. **Seção 2.3 (Examples):** adicionar exemplo de snapshot alpha.

4. **Seção 6.2 (File Naming and Snapshot Workflow):** adicionar workflow paralelo para
   alpha snapshots (geração, localização, relação com snapshot oficial).

5. **Seção 6.3 (Archival Strategy):** clarificar que snapshots alpha em `wip/` NÃO seguem
   a regra de arquivo único de `wip/guide/`. Podem coexistir múltiplos snapshots alpha em `wip/`.

6. **Seção 6.5.1 (Tags):** adicionar formato de tag alpha:
   ```
   v{MAJOR}.{MINOR}.{PATCH}.{SUBPATCH}-alpha.{N}
   ```
   Ex: `v0.4.2.0-alpha.1`

7. **Seção 6.5.2 (Releases):** adicionar regra para pre-releases:
   - Marcados como **pre-release** no GitHub (não como release oficial)
   - PDF gerado a partir do snapshot alpha (não do `guide.tex`)
   - Description deve indicar claramente quais capítulos estão incluídos e quais estão pendentes

8. **Seção 6.5.4 (Workflow Integration):** adicionar fluxo alpha ao diagrama existente.

9. **Seção 7.3 (Key Notes):** adicionar nota sobre pre-releases e sua relação com
   versões oficiais.

### 3.3 `README.md` — Alterações necessárias

Verificar se há menção ao ciclo de versões ou ao status de releases. Se houver:
- Adicionar nota sobre pre-releases alpha e o que significam
- Indicar que pre-releases contêm trabalho aprovado mas não integrado oficialmente

### 3.4 GitHub Pages — Verificar

Verificar se há páginas que listam releases ou descrevem o processo de versionamento.
Se houver, atualizar para mencionar pre-releases alpha.

### 3.5 `docs/briefing.md` — Verificar

Verificar seção 11 (WIP files) e qualquer menção ao ciclo de status. Atualizar se necessário.

### 3.6 Outros arquivos de governança — Verificar

Fazer varredura profunda no Repo para verificar se há outros arquivos que necessitem de atualização.
Atualizar conforme necessário para garantir consistência.

---

## 4. O que NÃO alterar

- `wip/guide/` e seu comportamento: continua com arquivo único, workflows intactos.
- `guide.tex`: não é tocado por nada relacionado ao alpha.
- O snapshot oficial atual: `wip/guide/guide-v0.4.1.1-20260218.tex` — intocado.
- A semântica de `approved`: continua significando integração oficial em `guide.tex`.
- Qualquer GitHub Action que processa `wip/guide/`: não tocar.

---

## 5. Estado Atual do Projeto (contexto para o trabalho)

- **Versão oficial:** v0.4.1.1 (lançada 2026-02-18)
- **Issue #44:** revisão de estilo AI-speak (C1, C2, C3, C5) — bloqueia v0.4.2.0
- **C5 status:** §5.1–§5.2.1.3 aprovados na sessão de hoje; §5.2.2–§5.3 pendentes
- **WIP ativo de C5:** `chapter-C5-style-rev-review-2026-02-26.tex` (status: review)
- **Quando C5 estiver completo:** o WIP avança para `final`, depois para `alpha`,
  e o snapshot alpha `wip/guide-v0.4.2.0-alpha.1-YYYYMMDD.tex` é criado com C5 integrado.

---

## 6. Ordem de Execução Recomendada (sujeita a revisão e adaptação conforme necessidade)

1. Ler os arquivos de governança atuais antes de alterar qualquer coisa:
   - `docs/wip-naming.md`
   - `docs/version-system.md`
   - `docs/briefing.md`
   - `README.md`
   - GitHub Pages (se acessível)

2. Verificar os GitHub Actions workflows que tocam `wip/guide/` para confirmar
   que as alterações propostas não os afetam.

3. Implementar alterações em `docs/wip-naming.md` primeiro (é o documento mais
   diretamente afetado pelo novo status `alpha`).

4. Implementar alterações em `docs/version-system.md`.

5. Verificar e atualizar `README.md` e GitHub Pages conforme necessário.

6. Verificar `docs/briefing.md`.

7. Propor commit message ao autor antes de fazer qualquer commit.

---

## 7. Princípios do Projeto (para manter consistência de tom e decisão)

- Políticas concretas e defensáveis, não diretrizes subjetivas.
- O autor humano é o tomador de decisão final — nunca avançar sem autorização explícita.
- Nunca fazer commit ou push sem aprovação do autor.
- Nunca mover arquivos para `archive/` sem instrução explícita.
- Documentação de governança em inglês; conversa com o autor em português.

---

*Gerado em: 2026-02-26 — sessão claude.ai*
*Alterado em: 2026-02-26 — autor humano*
*Referência: issue #44, decisões de sessão 2026-02-26*
