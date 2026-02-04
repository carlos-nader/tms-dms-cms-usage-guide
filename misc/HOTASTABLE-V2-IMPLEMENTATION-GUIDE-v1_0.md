# Guia de Implementação — Atualização do Ambiente hotastable v2.0

**Data:** 2026-02-04  
**Autor:** Claude (Co-Editor) com aprovação de Carlos Nader (Metal)  
**Versão do Guia:** 1.0  
**Status:** Pendente de implementação

---

## 1. Visão Geral da Mudança

### 1.1 Motivação

A versão atual do ambiente `hotastable` apresentava overflow de conteúdo na coluna **Train.** quando múltiplas missões de treinamento eram referenciadas (ex: "TRN 18 (BARCAP), TRN 28 (SEAD-EW)").

**Problemas identificados:**
- Coluna Train. (2.10 cm) insuficiente para conteúdo longo (~4.5–5.0 cm necessários)
- `\tabcolsep{2pt}` causava células visualmente "coladas" sem respiro
- Texto transbordando horizontalmente para células adjacentes

### 1.2 Solução Implementada

**Estratégia em duas frentes:**
1. **Simplificação de conteúdo:** Coluna Train. passa a conter apenas números de missões (ex: "18, 28")
2. **Ajuste estrutural do ambiente:** Redução de fonte, aumento de espaçamento, redistribuição de larguras

**Resultado esperado:**
- ✅ Overflow eliminado
- ✅ Melhor respiro visual entre células
- ✅ Maior densidade de informação (fonte menor permite mais texto por célula)
- ✅ Largura total mantida dentro de 17.0 cm

---

## 2. Especificação Técnica — hotastable v2.0

### 2.1 Parâmetros do Ambiente

| Parâmetro | v1.0 (Atual) | v2.0 (Proposto) | Justificativa |
|-----------|--------------|-----------------|---------------|
| Font size | `\small` (9pt) | `\footnotesize` (8pt) | Maior densidade, mais texto por célula |
| `\tabcolsep` | 2pt | 3pt | Melhor espaçamento visual entre células |
| `\arraystretch` | 1.25 | 1.30 | Compensa fonte menor, mantém legibilidade vertical |
| Mode | 1.00 cm | 1.00 cm | — |
| Dir. | 0.90 cm | 0.90 cm | — |
| Act. | 0.90 cm | 0.90 cm | — |
| Function | 3.30 cm | 3.30 cm | — |
| Effect/Nuance | 6.40 cm | 6.40 cm | — |
| Dash34 | 1.40 cm | 1.40 cm | — |
| Train. | 2.10 cm | 1.60 cm | Conteúdo simplificado (apenas números) |

### 2.2 Cálculo de Largura Total

**Largura das colunas:**
```
1.00 + 0.90 + 0.90 + 3.30 + 6.40 + 1.40 + 1.60 = 15.50 cm
```

**Padding lateral (7 colunas × 2 lados × 3pt):**
```
7 × 2 × 3pt = 42pt ≈ 1.48 cm
```

**Largura total:**
```
15.50 + 1.48 = 16.98 cm ✅ (dentro do limite de 17.0 cm)
```

---

## 3. Código LaTeX — Ambiente Atualizado

### 3.1 Código Completo do Ambiente hotastable v2.0

**Localização no repositório:** `guide.tex` (preâmbulo) ou arquivo de preâmbulo separado (ex: `preamble.tex`)

```latex
% ============================================================================
% HOTAS table environment
% Version: 2.0 (2026-02-04)
% Changes from v1.0:
%   - Font reduced from \small to \footnotesize for better density
%   - \tabcolsep increased from 2pt to 3pt for better visual spacing
%   - Train. column reduced from 2.10cm to 1.60cm (content simplified to numbers only)
%   - \arraystretch increased from 1.25 to 1.30 to compensate for smaller font
% Total width: 15.50cm (columns) + 1.48cm (padding) = 16.98cm
% ============================================================================

\newenvironment{hotastable}[1]{%
  \footnotesize  % 8pt base font (down from \small 9pt)
  \setlength{\tabcolsep}{3pt}  % cell padding (up from 2pt)
  \renewcommand{\arraystretch}{1.30}  % row height factor (up from 1.25)
  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{1.60cm}}
  	\caption{#1}\\
  	\rowcolor{headerblue}
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
  	\endfirsthead
  	\rowcolor{headerblue}
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  	\multicolumn{1}{>{\centering\arraybackslash}p{1.60cm}}{\textbf{\color{white}Train.}} \\
  	\endhead
  	\multicolumn{7}{r}{\small\emph{Continued on next page}}\\
  	\endfoot
  	\endlastfoot
  }{%
  \end{longtable}
}
```

### 3.2 Localização da Definição Atual (Para Substituir)

**Arquivo:** `guide.tex` (ou arquivo de preâmbulo se existir)

**Buscar por:**
```latex
\newenvironment{hotastable}
```

**Ação:** Substituir toda a definição pela versão v2.0 acima.

---

## 4. Mudanças no Conteúdo das Tabelas

### 4.1 Simplificação da Coluna Train.

**Regra:** Coluna Train. deve conter apenas números de missões, separados por vírgula.

**Antes (v1.0):**
```latex
& \dashref{2.7.2.2} & \trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)} \\
```

**Depois (v2.0):**
```latex
& \dashref{2.7.2.2} & 18, 28 \\
```

**OU** (se preferir manter o macro `\trnref` mas simplificado):
```latex
& \dashref{2.7.2.2} & \trnref{18}, \trnref{28} \\
```

### 4.2 Busca e Substituição (Regex)

**Ferramenta:** Editor de texto com suporte a regex (VSCode, Sublime, TeXstudio)

**Padrão de busca (regex):**
```regex
\\trnref\{(\d+)\s*\([^)]+\)\}
```

**Substituição:**
```regex
\1
```

**Exemplo de resultado:**
- `\trnref{18 (BARCAP)}` → `18`
- `\trnref{28 (SEAD-EW)}` → `28`

**Nota:** Se houver múltiplas referências na mesma célula, o padrão acima captura uma de cada vez. Execute múltiplas vezes ou ajuste o regex.

### 4.3 Padrão Alternativo (Mais Conservador)

Se a busca automática for arriscada, fazer busca simples e substituir manualmente:

**Buscar:** `\trnref{`

**Ação:** Revisar cada ocorrência e simplificar manualmente.

---

## 5. Texto de Apresentação das Tabelas

### 5.1 Objetivo

Informar ao leitor que a coluna Train. contém apenas códigos numéricos e que descrições das missões devem ser consultadas no BMS Training Manual 4.38.1.

### 5.2 Localização Sugerida

- **Opção A:** Início de cada capítulo com tabelas (antes da primeira `hotastable`)
- **Opção B:** Seção dedicada no Capítulo 1 (Introduction)
- **Opção C:** Nota de rodapé na primeira tabela de cada capítulo

### 5.3 Texto Proposto (Opção A — Recomendado)

Inserir antes da primeira tabela de cada capítulo (ex: Cap. 4, 5):

```latex
\subsection*{How to Read the Tables}

The tables in this chapter use the following column structure:

\begin{itemize}[leftmargin=*, nosep]
  \item \textbf{Mode:} The operational context (master mode, CMDS mode, sensor state).
  \item \textbf{Dir.:} The physical direction for pressing the switch (Up, Down, Left, Right).
  \item \textbf{Act.:} The press type (Short, Medium, Long, or Long Hold).
  \item \textbf{Function:} What the switch command activates or controls.
  \item \textbf{Effect / Nuance:} The resulting system behavior, including tactical considerations and constraints.
  \item \textbf{Dash34:} Reference section in the Dash-34 manual (TO 1F-16CMAM-34-1-1 BMS).
  \item \textbf{Train.:} Recommended BMS training mission codes for hands-on practice. 
        \emph{For mission descriptions and learning objectives, refer to the BMS Training Manual 4.38.1.}
\end{itemize}
```

### 5.4 Texto Proposto (Opção C — Nota de Rodapé)

Inserir na primeira tabela de cada capítulo:

```latex
\begin{hotastable}{CMS Actuation with CMDS Automatic Mode\footnotemark}
...
\end{hotastable}

\footnotetext{Training mission codes refer to BMS Training Manual 4.38.1. 
For example, mission 18 is ``BARCAP'' (Barrier Combat Air Patrol). 
Consult the manual for detailed learning objectives and mission flows.}
```

---

## 6. Impactos em Documentos de Governança

### 6.1 BRIEFING-v0.2.0.1

**Arquivo:** `docs/BRIEFING-v0.2.0.1.md`

**Seção a atualizar:** 6.3 Formatação de Tabelas (hotastable)

**Mudanças Necessárias:**

**Substituir:**
```markdown
### 6.3 Formatação de Tabelas (hotastable)

- Font size: `\small` (10pt)
- Row height: `\arraystretch = 1.25`
- Colunas: Mode (1.00cm), Dir. (0.90cm), Act. (0.90cm), Sensor/Mode (3.30cm), Effect/Nuance (6.40cm), Dash-34 (1.40cm), Training (2.10cm)
```

**Por:**
```markdown
### 6.3 Formatação de Tabelas (hotastable)

**Environment:** `hotastable`  
**Version:** 2.0 (updated 2026-02-04)

**Formatting parameters:**
- Font size: `\footnotesize` (8pt base)
- Row height: `\arraystretch = 1.30`
- Cell padding: `\tabcolsep = 3pt`

**Column widths:**

| Column | Width | Alignment | Content |
|--------|-------|-----------|---------|
| Mode | 1.00 cm | Left | Master mode, CMDS mode, sensor state |
| Dir. | 0.90 cm | Center | UP, DN, LT, RT |
| Act. | 0.90 cm | Center | S, M, L, LH |
| Function | 3.30 cm | Left | System function or control activated |
| Effect / Nuance | 6.40 cm | Left | Behavior, tactics, constraints (primary narrative column) |
| Dash34 | 1.40 cm | Center | Section references (e.g., 3-60, 2.7.2.2) |
| Train. | 1.60 cm | Center | Training mission codes only (e.g., 18, 28) |

**Total width:**
- Columns: 15.50 cm
- Padding (3pt × 7 cols × 2): 1.48 cm
- **Total: 16.98 cm** (within 17.0 cm text width)

**Training column content:**
The Train. column contains only mission codes (e.g., "18, 28"). 
Mission names and descriptions are referenced in the BMS Training Manual 4.38.1, 
as noted in the table introduction text within each chapter.

**Changelog:**
- v2.0 (2026-02-04): Font reduced to \footnotesize, \tabcolsep increased to 3pt, 
  Train. width reduced to 1.60 cm, arraystretch increased to 1.30
- v1.0 (2026-01-XX): Initial implementation with \small, 2pt padding, 2.10 cm Train.
```

### 6.2 Bump de Versão do BRIEFING

**Decisão necessária:** A mudança na seção 6.3 justifica bump de versão do BRIEFING?

**Opções:**
- `v0.2.0.1 → v0.2.1.0` (PATCH bump, mudanças estruturais significativas em templates)
- `v0.2.0.1 → v0.2.0.2` (SUBPATCH bump, correções e melhorias menores)

**Recomendação:** `v0.2.1.0` (PATCH bump), pois altera especificação de template usado em todo o projeto.

### 6.3 WIP-FILE-NAMING-v1.4

**Arquivo:** `docs/WIP-FILE-NAMING-v1.4.md`

**Ação:** Nenhuma mudança necessária (nomenclatura de arquivos não afetada).

### 6.4 VERSION-SYSTEM-v4.2.1

**Arquivo:** `docs/VERSION-SYSTEM-v4.2.1.md`

**Ação:** Nenhuma mudança necessária (versionamento do guide não afetado diretamente).

### 6.5 PROJECT-TRACKING-v5.0.0

**Arquivo:** `docs/PROJECT-TRACKING-v5.0.0.md`

**Ação:** Adicionar entrada na próxima sessão de trabalho:

```markdown
### Session XX (2026-02-04)
**Focus:** Atualização estrutural do ambiente `hotastable` v2.0

**Changes:**
- Updated `hotastable` environment: font size reduced, padding increased, Train. column simplified
- Updated BRIEFING v0.2.0.1 → v0.2.1.0 with new table specifications
- Simplified Train. column content across all existing tables (numbers only)
- Added table introduction text explaining training mission codes

**Files modified:**
- `guide.tex` (environment definition)
- `template-wip-V1.0.tex` (environment definition)
- `docs/BRIEFING-v0.2.0.1.md` → `docs/BRIEFING-v0.2.1.0.md`
- All WIP files with `hotastable` instances (Train. column simplified)

**Status:** [dev/review/final/approved]
```

### 6.6 template-wip-V1.0.tex

**Arquivo:** `TEMPLATES/template-wip-V1.0.tex`

**Ação:** Atualizar definição do ambiente `hotastable` com versão v2.0 (mesmo código da seção 3.1).

**Nota:** Se o template tiver o ambiente embutido (não via `\input`), substituir. Se usar `\input{preamble.tex}`, não há mudança necessária no template.

---

## 7. Passo-a-Passo de Implementação

### 7.1 Preparação (Backup e Organização)

#### Passo 1.1: Criar Branch Git (Recomendado)

```bash
git checkout -b feature/hotastable-v2
```

**Justificativa:** Permite reverter facilmente se houver problemas.

#### Passo 1.2: Backup do guide.tex Atual

```bash
cp guide.tex guide-backup-$(date +%Y%m%d).tex
```

#### Passo 1.3: Identificar Arquivos Afetados

**Arquivos a modificar:**
- `guide.tex` (definição do ambiente)
- `TEMPLATES/template-wip-V1.0.tex` (definição do ambiente)
- `docs/BRIEFING-v0.2.0.1.md` (renomear e atualizar)
- Todos os WIP files com tabelas `hotastable` (simplificar Train.)

**Lista de WIP files com hotastable (verificar):**
```bash
grep -r "\\begin{hotastable}" wip/
```

### 7.2 Atualização do Ambiente LaTeX

#### Passo 2.1: Atualizar guide.tex

**Localização:** Preâmbulo do `guide.tex` (antes de `\begin{document}`)

**Ação:**
1. Buscar por `\newenvironment{hotastable}`
2. Substituir toda a definição pelo código da seção 3.1 deste guia
3. Adicionar comentário de versionamento no topo da definição

**Verificação:**
```bash
# Buscar pela definição antiga
grep -A 5 "\\newenvironment{hotastable}" guide.tex

# Verificar se \tabcolsep{3pt} está presente
grep "tabcolsep{3pt}" guide.tex
```

#### Passo 2.2: Atualizar template-wip-V1.0.tex

**Ação:** Mesma substituição do Passo 2.1, mas no arquivo de template.

**Nota:** Se o template usar `\input{preamble.tex}` para carregar o ambiente, verificar se `preamble.tex` existe e atualizá-lo em vez do template.

### 7.3 Simplificação do Conteúdo das Tabelas

#### Passo 3.1: Listar Todas as Tabelas Afetadas

```bash
# Buscar por \trnref com nomes de missões entre parênteses
grep -r "\\trnref{[0-9]* ([^)]*)" wip/ guide.tex
```

**Resultado esperado:** Lista de arquivos e linhas com padrão antigo.

#### Passo 3.2: Substituir Conteúdo (Opção Automática — Cuidado!)

**Ferramenta:** VSCode, Sublime Text, ou `sed`

**Regex de busca:**
```regex
\\trnref\{(\d+)\s*\([^)]+\)\}
```

**Substituição:**
```regex
\1
```

**Comando sed (Linux/Mac — usar com cautela!):**
```bash
# Teste primeiro (dry-run)
sed -E 's/\\trnref\{([0-9]+)\s*\([^)]+\)\}/\1/g' guide.tex

# Se o resultado parecer correto, aplicar
sed -i.bak -E 's/\\trnref\{([0-9]+)\s*\([^)]+\)\}/\1/g' guide.tex
```

⚠️ **ATENÇÃO:** Sempre fazer backup antes de usar `sed -i`.

#### Passo 3.3: Substituir Conteúdo (Opção Manual — Mais Seguro)

**Ferramenta:** Editor de texto com busca/substituição

**Buscar:** `\trnref{18 (BARCAP)}`  
**Substituir:** `18`

Repetir para cada missão (18, 19, 28, etc.) em todos os arquivos.

#### Passo 3.4: Casos Especiais — Múltiplas Missões na Mesma Célula

**Antes:**
```latex
\trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)}
```

**Depois:**
```latex
18, 28
```

**OU** (se houver line breaks internos):
```latex
18, \newline 28
```

**Recomendação:** Usar formato compacto `18, 28` sempre que possível.

### 7.4 Adicionar Texto de Apresentação das Tabelas

#### Passo 4.1: Localizar Primeira Tabela de Cada Capítulo

**Capítulos com tabelas hotastable:**
- Capítulo 4 (DMS)
- Capítulo 5 (CMS)
- (Futuros: Cap. 3 TMS quando criado)

#### Passo 4.2: Inserir Texto Introdutório

**Posição:** Imediatamente antes da primeira `\begin{hotastable}` do capítulo.

**Código a inserir:** (da seção 5.3)

```latex
\subsection*{How to Read the Tables}

The tables in this chapter use the following column structure:

\begin{itemize}[leftmargin=*, nosep]
  \item \textbf{Mode:} The operational context (master mode, CMDS mode, sensor state).
  \item \textbf{Dir.:} The physical direction for pressing the switch (Up, Down, Left, Right).
  \item \textbf{Act.:} The press type (Short, Medium, Long, or Long Hold).
  \item \textbf{Function:} What the switch command activates or controls.
  \item \textbf{Effect / Nuance:} The resulting system behavior, including tactical considerations and constraints.
  \item \textbf{Dash34:} Reference section in the Dash-34 manual (TO 1F-16CMAM-34-1-1 BMS).
  \item \textbf{Train.:} Recommended BMS training mission codes for hands-on practice. 
        \emph{For mission descriptions and learning objectives, refer to the BMS Training Manual 4.38.1.}
\end{itemize}
```

**Exemplo de integração:**
```latex
\section{CMS Switch Actuation}

\subsection*{How to Read the Tables}
[texto introdutório aqui]

\begin{hotastable}{CMS Actuation with CMDS Manual Mode}
...
```

### 7.5 Atualização do BRIEFING

#### Passo 5.1: Renomear Arquivo

```bash
cd docs/
mv BRIEFING-v0.2.0.1.md BRIEFING-v0.2.1.0.md
```

#### Passo 5.2: Atualizar Metadados do Arquivo

No topo do `BRIEFING-v0.2.1.0.md`:

```markdown
# Falcon BMS TMS/DMS/CMS HOTAS Guide — Project Briefing

**Version:** 0.2.1.0  
**Date:** 2026-02-04  
**Author:** Carlos Nader (Metal)  
**Status:** Active

**Changelog:**
- v0.2.1.0 (2026-02-04): Updated hotastable environment specification (v2.0)
- v0.2.0.1 (2026-01-XX): [previous changes]
```

#### Passo 5.3: Atualizar Seção 6.3

Substituir seção **6.3 Formatação de Tabelas (hotastable)** pelo texto da seção 6.1 deste guia.

### 7.6 Compilação e Teste

#### Passo 6.1: Compilar guide.tex

```bash
# No terminal (assumindo MiKTeX ou TeX Live instalado)
pdflatex guide.tex
pdflatex guide.tex  # Segunda passagem para resolver referências
```

**OU** usar TeXstudio/VSCode com LaTeX Workshop.

#### Passo 6.2: Verificar Warnings

**Buscar no log de compilação:**
```
Overfull \hbox
Underfull \hbox
```

Se houver overfull: Revisar conteúdo da célula problemática.

#### Passo 6.3: Inspeção Visual do PDF

**Checklist:**
- [ ] Tabelas renderizam sem overflow
- [ ] Espaçamento entre células visualmente confortável (não "coladas")
- [ ] Fonte `\footnotesize` legível em tela
- [ ] Fonte `\footnotesize` legível em impressão (teste crítico!)
- [ ] Coluna Train. mostra apenas números (ex: "18, 28")
- [ ] Texto de apresentação aparece antes da primeira tabela de cada capítulo
- [ ] Headers das tabelas renderizam corretamente (fundo azul, texto branco)

#### Passo 6.4: Teste de Impressão (Crítico!)

**Ação:** Imprimir 1–2 páginas contendo tabelas.

**Verificar:**
- Legibilidade da fonte `\footnotesize` (8pt) no papel
- Se fonte parecer pequena demais, considerar:
  - Retornar para `\small` (9pt), OU
  - Usar fonte customizada 8.5pt (ver seção 8.2 deste guia)

### 7.7 Atualização de PROJECT-TRACKING

#### Passo 7.1: Adicionar Nova Entrada de Sessão

**Arquivo:** `docs/PROJECT-TRACKING-v5.0.0.md`

Inserir no final da seção de sessões:

```markdown
### Session XX (2026-02-04)
**Focus:** Structural update of hotastable environment to v2.0

**Objectives:**
- Resolve Train. column overflow issue
- Improve visual spacing of table cells
- Simplify training mission references

**Changes Implemented:**
- Updated `hotastable` environment definition (v1.0 → v2.0)
  - Font: \small → \footnotesize (9pt → 8pt)
  - \tabcolsep: 2pt → 3pt
  - Train. width: 2.10cm → 1.60cm
  - \arraystretch: 1.25 → 1.30
- Simplified Train. column content across all tables (numbers only)
- Added "How to Read the Tables" introduction text in chapters with tables
- Updated BRIEFING v0.2.0.1 → v0.2.1.0 with new specifications
- Updated template-wip-V1.0.tex with new environment

**Files Modified:**
- `guide.tex` (environment definition + table content)
- `TEMPLATES/template-wip-V1.0.tex` (environment definition)
- `docs/BRIEFING-v0.2.0.1.md` → `docs/BRIEFING-v0.2.1.0.md`
- [List specific WIP files modified, if any]

**Compilation Status:** ✅ Success / ⚠️ Warnings / ❌ Errors  
**Visual Inspection:** ✅ Pass / ⚠️ Minor issues / ❌ Major issues  
**Print Test:** ✅ Legible / ⚠️ Borderline / ❌ Too small

**Next Steps:**
- [If print test fails: Adjust font size to 8.5pt custom]
- [If successful: Proceed with normal development]

**Notes:**
- [Any observations during implementation]
```

### 7.8 Commit Git e Versionamento

#### Passo 8.1: Adicionar Arquivos Modificados

```bash
git add guide.tex
git add TEMPLATES/template-wip-V1.0.tex
git add docs/BRIEFING-v0.2.1.0.md
git add docs/PROJECT-TRACKING-v5.0.0.md
# Adicionar outros arquivos modificados (WIP files, etc.)
```

#### Passo 8.2: Commit com Mensagem Descritiva

```bash
git commit -m "Update hotastable environment to v2.0

- Font reduced to \footnotesize (8pt) for better density
- \tabcolsep increased to 3pt for improved cell spacing
- Train. column reduced to 1.60cm (content simplified to numbers only)
- \arraystretch increased to 1.30 to compensate for smaller font
- Updated BRIEFING v0.2.0.1 -> v0.2.1.0
- Added table introduction text explaining training mission codes
- Total table width: 16.98cm (within 17.0cm text width)

Refs: Issue #XX (if applicable)"
```

#### Passo 8.3: Merge para Main (Se Tudo OK)

```bash
# Se compilação e testes passaram
git checkout main
git merge feature/hotastable-v2
git push origin main
```

#### Passo 8.4: Tag de Versão (Opcional)

Se o BRIEFING foi atualizado para v0.2.1.0, considerar tag:

```bash
git tag -a briefing-v0.2.1.0 -m "BRIEFING v0.2.1.0 - hotastable v2.0 specifications"
git push origin briefing-v0.2.1.0
```

---

## 8. Troubleshooting e Ajustes Finos

### 8.1 Problema: Overfull Hbox Ainda Presente

**Diagnóstico:**
```bash
# Verificar log de compilação
grep "Overfull" guide.log
```

**Possíveis causas:**
- Conteúdo de Train. não foi simplificado em alguma célula
- Conteúdo de outra coluna (Function, Effect/Nuance) excede largura

**Solução:**
- Verificar célula específica apontada no log
- Simplificar conteúdo ou adicionar `\newline` interno

### 8.2 Problema: Fonte \footnotesize Pequena Demais

**Sintoma:** Teste de impressão mostra fonte ilegível ou muito cansativa.

**Solução:** Usar fonte customizada 8.5pt (meio-termo entre `\small` e `\footnotesize`)

**Código ajustado:**
```latex
\newenvironment{hotastable}[1]{%
  \fontsize{8.5pt}{10.2pt}\selectfont  % custom 8.5pt font
  \setlength{\tabcolsep}{3pt}
  \renewcommand{\arraystretch}{1.28}  % ajustar se necessário
  ...
```

### 8.3 Problema: Espaçamento Vertical Excessivo

**Sintoma:** Linhas da tabela ficam muito "altas" (muito espaço branco vertical).

**Solução:** Reduzir `\arraystretch`

**Teste:**
```latex
\renewcommand{\arraystretch}{1.20}  % down from 1.30
```

### 8.4 Problema: Células Ainda "Coladas"

**Sintoma:** `\tabcolsep{3pt}` ainda parece apertado visualmente.

**Solução:** Aumentar para 4pt, mas **ATENÇÃO:** isso pode causar overfull!

**Cálculo necessário:**
```
Padding com 4pt: 7 × 2 × 4pt = 56pt ≈ 1.98 cm
Largura total: 15.50 + 1.98 = 17.48 cm ⚠️ OVERFULL!
```

**Solução alternativa:**
- Reduzir largura de colunas (ex: Function 3.30 → 3.10) para compensar

---

## 9. Documentação Adicional e Referências

### 9.1 Tabela de Referência de Missões de Treinamento

Pendente de criação (sugestão para Capítulo 6 ou Apêndice).

**Formato sugerido:**
```latex
\section{BMS Training Mission Reference}

\begin{table}[h]
\centering
\caption{Training Mission Codes and Descriptions}
\begin{tabular}{clp{8cm}}
\toprule
\textbf{Code} & \textbf{Abbrev.} & \textbf{Description} \\
\midrule
18 & BARCAP & Barrier Combat Air Patrol — defensive CAP mission \\
19 & GUN AIM & Gun Aiming Practice — air-to-air gunnery training \\
28 & SEAD-EW & Suppression of Enemy Air Defenses with Electronic Warfare \\
... & ... & ... \\
\bottomrule
\end{tabular}
\end{table}
```

### 9.2 Referência Rápida — Comandos LaTeX

| Comando | Efeito |
|---------|--------|
| `\footnotesize` | Font 8pt (2 pontos menor que `\normalsize`) |
| `\small` | Font 9pt (1 ponto menor que `\normalsize`) |
| `\setlength{\tabcolsep}{3pt}` | Padding horizontal de células = 3pt |
| `\renewcommand{\arraystretch}{1.30}` | Altura de linha = 1.30× baseline |
| `L{X.XXcm}` | Coluna alinhada à esquerda com largura fixa |

### 9.3 Links Úteis

- LaTeX Table Generator: https://www.tablesgenerator.com/
- Overleaf Documentation — Tables: https://www.overleaf.com/learn/latex/Tables
- CTAN longtable package: https://ctan.org/pkg/longtable

---

## 10. Checklist Final de Implementação

### Pré-Implementação
- [ ] Backup de `guide.tex` criado
- [ ] Branch Git `feature/hotastable-v2` criado (opcional)
- [ ] Lista de arquivos afetados identificada

### Implementação — Código LaTeX
- [ ] Ambiente `hotastable` atualizado em `guide.tex`
- [ ] Ambiente `hotastable` atualizado em `template-wip-V1.0.tex`
- [ ] Verificação: `\tabcolsep{3pt}` presente
- [ ] Verificação: `\footnotesize` presente
- [ ] Verificação: Train. width = 1.60cm

### Implementação — Conteúdo
- [ ] Coluna Train. simplificada em todas as tabelas (apenas números)
- [ ] Texto "How to Read the Tables" adicionado em cada capítulo com tabelas
- [ ] Verificação: Nenhum `\trnref{XX (NAME)}` restante

### Implementação — Documentação
- [ ] BRIEFING renomeado para v0.2.1.0
- [ ] BRIEFING seção 6.3 atualizada com specs v2.0
- [ ] PROJECT-TRACKING atualizado com entrada de sessão
- [ ] Changelog adicionado ao topo do BRIEFING

### Compilação e Teste
- [ ] `pdflatex guide.tex` executa sem erros
- [ ] Nenhum warning "Overfull \hbox" relacionado a tabelas
- [ ] Inspeção visual do PDF: tabelas renderizam corretamente
- [ ] Teste de impressão: fonte legível no papel

### Versionamento Git
- [ ] Arquivos modificados adicionados ao staging (`git add`)
- [ ] Commit criado com mensagem descritiva
- [ ] Merge para main (se branch foi usada)
- [ ] Tag `briefing-v0.2.1.0` criada (opcional)
- [ ] Push para repositório remoto

### Pós-Implementação
- [ ] Arquivos de backup antigos arquivados ou deletados
- [ ] Documentação deste guia arquivada para referência futura
- [ ] Issue relacionada (se existir) fechada no GitHub

---

## 11. Notas Finais

### 11.1 Reversão (Se Necessário)

Se a implementação causar problemas graves:

**Opção A — Via Git:**
```bash
git checkout main
git revert HEAD  # reverte último commit
```

**Opção B — Via Backup:**
```bash
cp guide-backup-YYYYMMDD.tex guide.tex
```

### 11.2 Iterações Futuras

Possíveis melhorias para v3.0 (pós-v1.0.0.0 do guide):
- Migração para `booktabs` package (linhas horizontais mais elegantes)
- Uso de `tabularx` para auto-ajuste de colunas
- Cores alternadas de linhas (zebra striping) para melhor legibilidade
- Ícones visuais na coluna Dir. (setas Unicode ou gráficos)

### 11.3 Feedback e Ajustes

Após implementação:
- Solicitar feedback de beta readers (se aplicável)
- Verificar legibilidade em diferentes dispositivos (monitor, tablet, impressão)
- Ajustar font size se necessário (8.5pt customizado pode ser melhor compromisso)

---

## 12. Contato e Suporte

Dúvidas durante implementação?
- Retomar conversa com Claude (co-editor) para esclarecimentos
- Consultar documentação LaTeX oficial (links na seção 9.3)
- Revisar este guia (seções de troubleshooting)

---

**Fim do Guia de Implementação — hotastable v2.0**

**Data de criação:** 2026-02-04  
**Preparado por:** Claude (Co-Editor AI)  
**Aprovado por:** Carlos Nader (Metal) — Pendente  
**Versão deste guia:** 1.0  
**Status:** Pronto para uso

---

## Apêndice A — Diff Visual (Antes × Depois)

### Ambiente hotastable

```diff
\newenvironment{hotastable}[1]{%
-  \small
-  \setlength{\tabcolsep}{2pt}
-  \renewcommand{\arraystretch}{1.25}
-  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{2.10cm}}
+  \footnotesize
+  \setlength{\tabcolsep}{3pt}
+  \renewcommand{\arraystretch}{1.30}
+  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{1.60cm}}
```

### Conteúdo de Tabela (Exemplo)

```diff
CMDS AUTO & Up & Short & Execute Program 1--4 &
Manual override... &
-\dashref{2.7.2.2} & \trnref{18 (BARCAP)}, \trnref{28 (SEAD-EW)} \\
+\dashref{2.7.2.2} & 18, 28 \\
```

---

Este guia deve ser suficiente para implementação completa. Qualquer dúvida durante o processo, retome a conversa! 🎯
