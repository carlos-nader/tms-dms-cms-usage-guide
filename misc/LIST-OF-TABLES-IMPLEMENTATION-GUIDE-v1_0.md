# Guide: Implementação do List of HOTAS Tables

**Versão:** 1.0  
**Data:** 2026-02-04  
**Autor:** Metal (Carlos Nader) + Claude (co-editor)  
**Status:** Guia de Implementação (não implementado)

---

## 1. Visão Geral

Este documento descreve como implementar o **List of HOTAS Tables** no guide, um índice automático de todas as tabelas `hotastable` que aparecerá logo após o Table of Contents.

**Objetivo:** Facilitar navegação rápida para tabelas HOTAS específicas (ex: "TMS em A-A mode está na página X").

**Escopo:** Apenas tabelas `hotastable` são indexadas. Outras tabelas (abreviações, comparações, etc.) NÃO aparecem no índice.

---

## 2. Código LaTeX — Preâmbulo

### 2.1 No `guide.tex` (Preâmbulo)

**Localização:** Após pacotes `\usepackage{...}`, antes de `\begin{document}`

```latex
% ============================================================================
% LIST OF HOTAS TABLES
% ============================================================================
% Customiza o título do índice de tabelas para "List of HOTAS Tables"
\renewcommand{\listtablename}{List of HOTAS Tables}
```

**Explicação:**
- `\listtablename` é o comando LaTeX padrão que define o título do `\listoftables`
- Por padrão, seria "List of Tables"
- Renomeamos para "List of HOTAS Tables" para deixar claro o escopo restrito

---

### 2.2 No `guide.tex` (Corpo do Documento)

**Localização:** Logo após `\tableofcontents`, antes do primeiro `\chapter{...}`

```latex
\tableofcontents

% List of HOTAS Tables - índice automático de todas as tabelas com \caption
\listoftables

\chapter{Introduction}
...
```

**Explicação:**
- `\listoftables` gera automaticamente o índice
- LaTeX coleta todas as tabelas com `\caption{...}` e lista título + número de página
- A ordem é a mesma que as tabelas aparecem no documento

**Opcional:** Adicionar `\clearpage` ou `\newpage` se quiser que o índice comece em página nova:

```latex
\tableofcontents
\clearpage  % Força quebra de página
\listoftables
```

---

## 3. Código LaTeX — Template WIP

### 3.1 No `template-wip-V1.0.tex`

**Localização:** Onde está o exemplo de `\begin{table}...\end{table}`

**Substituir o bloco de exemplo atual por:**

```latex
% ============================================================================
% HOTAS TABLE ENVIRONMENT
% ============================================================================
% IMPORTANTE: TODAS as tabelas hotastable DEVEM ter \caption para aparecer
% no "List of HOTAS Tables" que é gerado automaticamente após o Table of Contents.
%
% FORMATO DE CAPTION OBRIGATÓRIO:
% \caption{[Switch] Actions in [Mode/Context]}
%
% EXEMPLOS:
% \caption{TMS Actions in Air-to-Air Master Mode}
% \caption{DMS Actions with FCR as SOI}
% \caption{CMS Switch Actuation Summary}
%
% TABELAS NÃO-HOTAS (ex: abreviações): NÃO usar \caption para evitar indexação
% ============================================================================

\begin{table}[H]
\caption{[Switch] Actions in [Mode/Context]} % SUBSTITUIR pelo título correto
\centering
\small
\setlength{\arrayrulewidth}{0.5pt}
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{|>{\centering\arraybackslash}p{1.00cm}|>{\centering\arraybackslash}p{0.90cm}|>{\centering\arraybackslash}p{0.90cm}|p{3.30cm}|p{6.40cm}|>{\centering\arraybackslash}p{1.40cm}|>{\centering\arraybackslash}p{2.10cm}|}
\hline
\textbf{Mode} & \textbf{Dir.} & \textbf{Act.} & \textbf{Sensor/Mode} & \textbf{Effect/Nuance} & \textbf{Dash-34} & \textbf{Training} \\
\hline
% PREENCHER LINHAS AQUI
\hline
\end{tabular}
\end{table}
```

---

## 4. Regras de Caption

### 4.1 Formato Obrigatório

**Padrão:**
```
[Switch] Actions in [Mode/Context]
```

**Componentes:**
- `[Switch]`: TMS, DMS ou CMS
- `Actions`: sempre plural
- `in`: preposição
- `[Mode/Context]`: modo, sensor, ou contexto específico

### 4.2 Exemplos Corretos

```latex
\caption{TMS Actions in Air-to-Air Master Mode}
\caption{TMS Actions in FCR STT/SAM Submode}
\caption{TMS Actions in NAV Master Mode}
\caption{TMS Actions in Air-to-Ground Weapon Employment}

\caption{DMS Actions with MFD as SOI}
\caption{DMS Actions with FCR as SOI}
\caption{DMS Actions with HUD as SOI}

\caption{CMS Switch Actuation Summary}
\caption{CMS Forward/Aft Actions}
\caption{CMS Left/Right Actions}
```

**Regra para contextos longos:**

Quando o contexto for muito verboso, use abreviações padronizadas:

✅ **Correto:** `\caption{TMS Actions in FCR STT/SAM Mode}`  
❌ **Evitar:** `\caption{TMS Actions in FCR Single Target Track Search-and-Track Mode with Situational Awareness Mode Active}`

**Abreviações aceitas:** FCR, STT, SAM, CRM, RWS, TWS, ACM, DGFT, A-A, A-G, NAV

### 4.3 Exemplos Incorretos

❌ `\caption{TMS Table}` — muito genérico  
❌ `\caption{Air-to-Air TMS}` — ordem invertida  
❌ `\caption{TMS up/down/left/right}` — minúsculas, sem contexto  
❌ `\caption{Table 3.1}` — apenas número, sem descrição  

---

## 5. Tratamento de Tabelas Não-HOTAS

### 5.1 Regra Geral

**Tabelas que NÃO devem aparecer no List of HOTAS Tables:**
- Tabelas de abreviações (ex: training missions)
- Tabelas comparativas (ex: blocos/variantes)
- Tabelas de glossário
- Qualquer tabela que não seja uma `hotastable` de ações de switch

**Solução:** NÃO usar `\caption{...}` nessas tabelas.

### 5.2 Exemplo de Tabela Não-HOTAS

```latex
% Tabela de abreviações - SEM \caption, não aparece no índice
\begin{table}[H]
\centering
{\small
\begin{tabular}{ll}
\toprule
\textbf{Abbreviation} & \textbf{Meaning} \\
\midrule
BVR & Beyond Visual Range \\
WVR & Within Visual Range \\
FCR & Fire Control Radar \\
\bottomrule
\end{tabular}
}
% Note: não há \label{} nem \caption{} - tabela não é referenciável
\end{table}
```

**Observação:** Se futuramente você quiser referenciar a tabela no texto (ex: "see Table X.Y"), terá que adicionar `\caption`. Nesse caso, considere criar um segundo índice "List of General Tables" ou aceitar que ela aparecerá no List of HOTAS Tables.

---

## 6. Impacto nos Documentos de Governança

### 6.1 BRIEFING (versão atual: v0.2.0.1)

**Arquivo:** `docs/BRIEFING-v0.2.0.1.md`

**Localização da alteração:** Seção 6 (Layout and LaTeX Formatting), após "6.4 Macros de Referência"

**Adicionar nova seção 6.5:**

```markdown
### 6.5 List of HOTAS Tables

The guide includes a **List of HOTAS Tables** immediately after the Table of Contents. This index is automatically generated by LaTeX based on table captions.

#### Rules for HOTAS Tables

1. **Caption is mandatory:**
   - Every `hotastable` environment MUST include a `\caption{...}`
   - Without caption, the table will NOT appear in the index

2. **Caption format:**
   - Standard: `[Switch] Actions in [Mode/Context]`
   - Examples:
     - `TMS Actions in Air-to-Air Master Mode`
     - `DMS Actions with FCR as SOI`
     - `CMS Switch Actuation Summary`

3. **Caption placement:**
   - Place `\caption{...}` immediately after `\begin{table}[H]`, before `\centering`

4. **Descriptive captions:**
   - Captions must be self-explanatory when listed in the index
   - Avoid generic terms like "TMS Table" or "Table 1"

#### Rules for Non-HOTAS Tables

Tables that are **not** HOTAS action tables (e.g., abbreviation tables, comparison tables) should **NOT** use `\caption{...}` to avoid appearing in the List of HOTAS Tables.

If you need to reference a non-HOTAS table in the text, you will need to either:
- (A) Accept that it will appear in the List of HOTAS Tables, or
- (B) Create a second index for general tables (future consideration)

#### Compilation Notes

The List of HOTAS Tables requires **two passes** of `pdflatex` to generate correctly:
1. First pass: collects captions and page numbers
2. Second pass: typesets the index

Most LaTeX editors (TeXstudio, VSCode with LaTeX Workshop) handle this automatically.
```

**Nota sobre versionamento:** Esta adição ao BRIEFING pode:
- **(A)** Ser feita diretamente no BRIEFING-v0.2.0.1 (sem bump de versão, já que é adição de detalhe técnico, não mudança de escopo)
- **(B)** Gerar BRIEFING-v0.2.1.0 (se você considerar que é alteração estrutural significativa)

**Recomendação:** Opção A — não justifica bump de versão, é apenas documentação de funcionalidade LaTeX.

---

### 6.2 WIP-FILE-NAMING (versão atual: v1.4)

**Arquivo:** `docs/WIP-FILE-NAMING-v1.4.md`

**Impacto:** **Nenhum.**

Este documento trata apenas de nomenclatura de arquivos WIP. A adição do List of Tables não altera padrões de naming.

---

### 6.3 VERSION-SYSTEM (versão atual: v4.2.1)

**Arquivo:** `docs/VERSION-SYSTEM-v4.2.1.md`

**Impacto:** **Nenhum.**

Adição do List of Tables **não** dispara bump de versão do guide, pois:
- Não é novo conteúdo técnico (capítulo/seção)
- É apenas funcionalidade de navegação (índice)
- Análogo a adicionar Table of Contents — não muda versão

**Exceção:** Se você considerar que é feature significativa o suficiente, pode argumentar para SUBPATCH bump (ex: v0.3.3.0 → v0.3.3.1), mas não é necessário.

---

### 6.4 PROJECT-TRACKING (versão atual: v5.0.0)

**Arquivo:** `docs/PROJECT-TRACKING-v5.0.0.md`

**Impacto:** Adicionar entrada na sessão de trabalho onde a implementação ocorrer.

**Exemplo de entrada:**

```markdown
## Session YYYY-MM-DD — Implementação do List of HOTAS Tables

**Objetivos:**
- Adicionar List of HOTAS Tables ao guide
- Atualizar template WIP com instruções de caption
- Documentar regras no BRIEFING

**Trabalho Realizado:**
- [x] Atualizado `guide.tex`: preâmbulo + `\listoftables`
- [x] Atualizado `template-wip-V1.0.tex`: comentários + exemplo de caption
- [x] Atualizado `BRIEFING-v0.2.0.1.md`: nova seção 6.5
- [x] Revisados captions em C4 (DMS) e C5 (CMS)
- [x] Testada compilação: List of HOTAS Tables gerado corretamente

**Versão após sessão:** v0.3.3.0 (sem bump — apenas feature de navegação)

**Próximos Passos:**
- Garantir que todas as futuras tabelas HOTAS incluam caption formatado
- Revisar periodicamente se captions estão descritivos
```

---

## 7. Passo-a-Passo de Implementação

### Fase 1: Backup

```bash
# Fazer commit de tudo que estiver pendente
git add .
git commit -m "Pre-implementation backup before List of HOTAS Tables"
git push
```

---

### Fase 2: Atualizar `guide.tex`

1. Abrir `guide.tex` no TeXstudio ou VSCode

2. **Preâmbulo:** Adicionar após os `\usepackage{...}`:
   ```latex
   % LIST OF HOTAS TABLES
   \renewcommand{\listtablename}{List of HOTAS Tables}
   ```

3. **Corpo:** Adicionar após `\tableofcontents`:
   ```latex
   \tableofcontents
   \listoftables  % Novo: índice de tabelas HOTAS
   ```

4. Salvar

---

### Fase 3: Atualizar `template-wip-V1.0.tex`

1. Abrir `templates/template-wip-V1.0.tex`

2. Localizar o exemplo de `\begin{table}...\end{table}`

3. Substituir pelo código fornecido na **Seção 3.1** deste guia (com comentários explicativos + exemplo de caption)

4. Salvar

---

### Fase 4: Revisar Captions Existentes

**Objetivo:** Garantir que todas as tabelas HOTAS já integradas no guide tenham captions corretos.

**Arquivos a revisar:**

| Capítulo | Arquivo | Seções |
|----------|---------|--------|
| C4 (DMS) | `guide.tex` (já integrado) | 4.1, 4.2, 4.3 |
| C5 (CMS) | `guide.tex` (já integrado) | 5.1, 5.2, 5.3 |

**Checklist para cada tabela:**

- [ ] Tem `\caption{...}`?
- [ ] Caption segue formato `[Switch] Actions in [Mode/Context]`?
- [ ] Caption é descritivo o suficiente para ser útil no índice?

**Exemplo de revisão:**

Se encontrar:
```latex
\begin{table}[H]
\centering
\small
...
\end{table}
```

Corrigir para:
```latex
\begin{table}[H]
\caption{DMS Actions with MFD as SOI}  % ADICIONAR
\centering
\small
...
\end{table}
```

---

### Fase 5: Atualizar BRIEFING

1. Abrir `docs/BRIEFING-v0.2.0.1.md`

2. Localizar **Seção 6.4** (Macros de Referência)

3. Adicionar **Seção 6.5** com o texto fornecido na **Seção 6.1** deste guia

4. Salvar

---

### Fase 6: Compilar e Testar

1. **Primeira compilação:**
   ```bash
   pdflatex guide.tex
   ```
   - LaTeX coleta informações de captions (gera `guide.lot`)

2. **Segunda compilação:**
   ```bash
   pdflatex guide.tex
   ```
   - LaTeX gera o List of HOTAS Tables com base em `guide.lot`

3. **Abrir `guide.pdf` e verificar:**
   - [ ] Table of Contents aparece normalmente
   - [ ] List of HOTAS Tables aparece logo depois do ToC
   - [ ] Título é "List of HOTAS Tables" (não "List of Tables")
   - [ ] Todas as tabelas HOTAS esperadas estão listadas
   - [ ] Números de página estão corretos
   - [ ] Nenhuma tabela não-HOTAS aparece (se houver alguma no guide)

---

### Fase 7: Commit e Push

```bash
git add guide.tex templates/template-wip-V1.0.tex docs/BRIEFING-v0.2.0.1.md
git commit -m "feat: Add List of HOTAS Tables

- Added \listoftables to guide.tex with custom title
- Updated template-wip with caption instructions
- Documented rules in BRIEFING section 6.5
- Reviewed and corrected captions in C4 and C5"
git push
```

---

### Fase 8: Atualizar PROJECT-TRACKING

1. Abrir `docs/PROJECT-TRACKING-v5.0.0.md`

2. Adicionar entrada de sessão (ver exemplo na **Seção 6.4** deste guia)

3. Salvar e commitar:
   ```bash
   git add docs/PROJECT-TRACKING-v5.0.0.md
   git commit -m "docs: Update PROJECT-TRACKING with List of HOTAS Tables implementation"
   git push
   ```

---

## 8. Resolução de Problemas (Troubleshooting)

### Problema 1: List of HOTAS Tables não aparece

**Sintomas:**
- Após `\listoftables`, o índice está vazio ou não aparece

**Causas possíveis:**
1. Nenhuma tabela tem `\caption{...}`
2. Compilação foi feita apenas 1 vez (precisa de 2 passes)
3. Arquivo `.lot` está corrompido

**Soluções:**
```bash
# Deletar arquivos auxiliares e recompilar
rm guide.lot guide.aux
pdflatex guide.tex
pdflatex guide.tex
```

---

### Problema 2: Tabelas não-HOTAS aparecem no índice

**Sintomas:**
- Tabela de abreviações ou outra tabela genérica aparece no List of HOTAS Tables

**Causa:**
- Tabela tem `\caption{...}` quando não deveria

**Solução:**
- Remover `\caption{...}` da tabela não-HOTAS
- Recompilar

---

### Problema 3: Título do índice está "List of Tables" ao invés de "List of HOTAS Tables"

**Causa:**
- `\renewcommand{\listtablename}{...}` não está no preâmbulo
- Ou está **depois** de `\begin{document}`

**Solução:**
- Mover `\renewcommand{\listtablename}{List of HOTAS Tables}` para **antes** de `\begin{document}`

---

### Problema 4: Números de página incorretos

**Causa:**
- Compilação incompleta (precisa de 2 passes)

**Solução:**
```bash
pdflatex guide.tex
pdflatex guide.tex  # Segunda passagem resolve referências
```

---

### Problema 5: Caption aparece no topo da tabela no PDF

**Sintomas:**
- Texto do caption é renderizado acima da tabela

**Causa:**
- Comportamento **esperado** do LaTeX — `\caption` sempre aparece no PDF

**Solução:**
- Isso é **correto**. Captions devem aparecer visualmente acima das tabelas.
- Se você **não** quer que o caption apareça visualmente, você **não pode** ter List of HOTAS Tables (sem caption, sem índice).

---

## 9. Considerações Futuras

### 9.1 Quando Criar um Segundo Índice (List of General Tables)?

**Cenário:** Se você começar a ter muitas tabelas não-HOTAS (comparações, glossários, etc.) e quiser indexá-las separadamente.

**Solução:**
```latex
% Preâmbulo
\usepackage{tocloft}  % Permite múltiplos índices customizados

% Após \listoftables (HOTAS)
\listof{generaltable}{List of General Tables}
```

Mas isso exigiria criar um novo ambiente `generaltable` separado de `table`. **Complexidade alta**, só vale se realmente necessário.

---

### 9.2 Formatação Customizada do Índice

**Se quiser mudar a aparência do List of HOTAS Tables** (fonte, espaçamento, etc.):

```latex
\usepackage{tocloft}

% Customizar fonte dos títulos das tabelas no índice
\renewcommand{\cfttabfont}{\small\itshape}

% Customizar espaçamento entre entradas
\setlength{\cfttabindent}{0em}
```

**Recomendação:** Deixar padrão inicialmente. Só customizar se realmente necessário.

---

### 9.3 Automação da Compilação

**Script Bash (Linux/Mac):**
```bash
#!/bin/bash
# build.sh - Compila o guide com 2 passes

pdflatex -interaction=nonstopmode guide.tex
pdflatex -interaction=nonstopmode guide.tex

echo "Build completo. Verifique guide.pdf"
```

**Script Batch (Windows):**
```batch
@echo off
REM build.bat - Compila o guide com 2 passes

pdflatex -interaction=nonstopmode guide.tex
pdflatex -interaction=nonstopmode guide.tex

echo Build completo. Verifique guide.pdf
pause
```

---

## 10. Referências

**Documentação LaTeX:**
- `\listoftables`: https://www.overleaf.com/learn/latex/Lists_of_tables_and_figures
- `\caption`: https://www.overleaf.com/learn/latex/Captions
- `tocloft` package: https://ctan.org/pkg/tocloft

**Documentos do Projeto:**
- `docs/BRIEFING-v0.2.0.1.md` — Seção 6 (Layout)
- `templates/template-wip-V1.0.tex` — Template de arquivos WIP

---

## 11. Checklist Final de Implementação

Antes de considerar a implementação completa, verificar:

- [ ] `guide.tex` atualizado (preâmbulo + `\listoftables`)
- [ ] `template-wip-V1.0.tex` atualizado (comentários + exemplo)
- [ ] `BRIEFING-v0.2.0.1.md` atualizado (nova seção 6.5)
- [ ] Captions revisados em C4 e C5
- [ ] Compilação testada (2 passes)
- [ ] List of HOTAS Tables aparece corretamente no PDF
- [ ] Título correto ("List of HOTAS Tables")
- [ ] Números de página corretos
- [ ] Commits feitos com mensagens descritivas
- [ ] `PROJECT-TRACKING-v5.0.0.md` atualizado

---

**Fim do Guia de Implementação**
