# Falcon BMS TMS/DMS/CMS Guide Version System v4.1

**Latest Update:** 07 January 2026, 02:40 -03  
**Effective Date:** 07 January 2026  
**Replaces:** v4.0 (adiciona referência explícita ao WIP-FILE-NAMING para arquivos individuais de preparação)

---

## 0. Como usar este documento

### 0.1 Pergunta inicial 🤔

Antes de qualquer mudança de versão, responda:

- O guia **já tem uma edição publicada (≥ 1.0)?**
  - **Não** → aplicar o **Regime de pré-publicação (0.x.x.x)** 📝
  - **Sim** → aplicar o **Regime de pós-publicação (x.x.x)** 🎯

### 0.2 Passos de decisão ⚙️

1. **Identifique o tipo de mudança feita na sessão de trabalho:**
   - Um **novo capítulo** entrou no arquivo principal do guia?
   - Houve **reestruturação forte** de seções ou de como as tabelas organizam o conteúdo?
   - Foram apenas **ajustes pequenos** de texto, formatação ou células de tabela?

2. **Vá para a tabela "When to Increment"** correspondente:
   - Se ainda estiver em 0.x.x.x → use **Quick Reference (0.x.x.x -- pré-publicação)** 📋
   - Se já estiver em ≥ 1.0 → use **Quick Reference (x.x.x -- pós-publicação)** 📊

3. **Aplique o File Naming Workflow:**
   - Atualize as **macros de versão e data** no preâmbulo LaTeX do guia.
   - Atualize o **nome do arquivo** `.tex` com o novo número e data.
   - Atualize o **PROJECT-TRACKING** com a nova entrada.
   - Arquive a versão anterior na pasta correta.

### 0.3 Exemplos orientados por cenário 🎬

- **"Terminei a narrativa de um novo capítulo, ainda sem tabelas completas."**
  - Regime: 0.x.x.x
  - Tendência: **MINOR** sobe (novo capítulo em desenvolvimento), PATCH/SUBPATCH em 0 ✍️

- **"Preenchi parte de uma tabela importante em capítulo já existente, mudando a forma como o leitor usa aquele capítulo."**
  - Regime: 0.x.x.x
  - Tendência: **PATCH** (mudança estrutural dentro do capítulo) 🔄

- **"Corrigi apenas typos em dois capítulos, sem mudar estrutura nem lógica das tabelas."**
  - Regime: 0.x.x.x ou x.x.x, conforme o caso
  - Tendência: **SUBPATCH** (em 0.x.x.x) ou **PATCH** (em x.x.x) ✏️

---

## 1. Cabeçalho e escopo

### 1.1 Metadados 📌

- **Título:** Falcon BMS TMS/DMS/CMS Guide Version System v4.1

- **Função:** define como nomear, numerar, atualizar e arquivar versões do guia TMS/DMS/CMS

- **Regime atual do projeto:**
  - Enquanto nenhuma edição ≥ 1.0 for declarada, o projeto está em **regime 0.x.x.x (pré-publicação)** 🔴
  - Após a primeira edição publicada, o projeto passa a combinar:
    - Histórico em 0.x.x.x (congelado) 🗂️
    - Versões ativas em **x.x.x (≥ 1.0, pós-publicação)** 🟢

### 1.2 Objetivo 🎯

- Estabelecer um sistema de versionamento que:
  - ✅ Distingue claramente **trabalho interno (0.x.x.x)** de **edições publicadas (≥ 1.0)**
  - ✅ Alinha **MAJOR** com "edição" do guia, em vez de fases internas (scaffold/tabelas/revisão)
  - ✅ Trata **tabelas como parte de capítulos**, não como versões independentes

### 1.3 Escopo 📑

- Aplica-se ao:
  - Arquivo principal do guia: `guide-v*.tex`
  - Artefatos derivados: PDFs versionados, arquivos de seção (`section-*.tex`), documentos de tracking (`PROJECT-TRACKING-*.md`), briefings  
  - **Nomes de arquivos individuais de preparação seguem regras próprias definidas em arquivo separado `WIP-FILE-NAMING v*` (`section-`, `table-`, `visual-`, `notes-`).**

- Não se aplica a outros projetos fora do TMS/DMS/CMS Guide, salvo referência explícita

### 1.4 Campos de versão no LaTeX do guia 🏷️

O arquivo principal do guia contém macros de versão e data no preâmbulo, por exemplo:

```latex
\newcommand{\docversion}{0.1.4.0}     % Número da versão
\newcommand{\docbuild}{20260106}      % Data de build YYYYMMDD
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{DD MMM 2026}
\newcommand{\chapterscompletedof}{1/7}
\newcommand{\tablesfilledpct}{0\%}
\newcommand{\fulldocversion}{\docversion+\docbuild}
```

Essas macros são a **fonte interna de verdade** da versão do documento.

Em toda mudança de versão:

- ✏️ `\docversion` e `\docbuild` **devem** ser atualizadas para refletir o novo número e a nova data
- ✏️ `\fulldocversion` e campos derivados (capa, seção de status, etc.) passam a exibir o novo valor

O número de versão registrado nessas macros **deve sempre coincidir** com:

- O número presente no **nome do arquivo** `.tex`
- O número registrado no **PROJECT-TRACKING**

---

## 2. Naming convention global

### 2.1 Regra única de nome de arquivo 📝

Todo arquivo principal do guia deve seguir o padrão:

```
guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex
```

- `MAJOR`, `MINOR`, `PATCH`, `SUBPATCH` são inteiros ≥ 0
- `YYYYMMDD` é a **data de build** (ano, mês, dia)

### 2.2 Formato da data 📅

- A data **sempre** usa o formato `YYYYMMDD` (por exemplo, `20260106` para 06 janeiro 2026)
- A build date é atualizada sempre que:
  - Uma nova versão é gerada (bump em qualquer dígito)
  - Um snapshot relevante é compilado, mesmo sem mudança de conteúdo, quando se deseja arquivar o artefato

### 2.3 Exemplos 📚

- Pré-publicação (regime 0.x.x.x):
  - `guide-v0.1.0.0-20260105.tex`
  - `guide-v0.1.4.0-20260106.tex`

- Primeira edição publicada (regime ≥ 1.0, após promoção):
  - `guide-v1.0.0-2026XXXX.tex`

- Revisão maior em nova edição:
  - `guide-v2.0.0-2026XXXX.tex`

---

## 3. Regime de pré-publicação (0.x.x.x)

### 3.1 Semântica dos dígitos em 0.x.x.x

Durante a pré-publicação, o número de versão tem quatro dígitos:

```
0.MINOR.PATCH.SUBPATCH
```

- **MAJOR = 0** 🔴
  - Indica que o guia está em **linha de desenvolvimento interno**, ainda **não publicado**
  - A estrutura pode mudar de forma significativa (capítulos entrando, saindo, sendo reordenados) sem compromisso de estabilidade com o leitor

- **MINOR (2º dígito)** 📖
  - Representa **qual enésimo capítulo você está trabalhando no guia** (ordem de entrada no arquivo principal, não o número do capítulo)
  - Exemplos:
    - `0.1.x.x` → 1º capítulo em desenvolvimento (pode ser o Capítulo 1, 3, 5 etc.)
    - `0.2.x.x` → 2º capítulo em desenvolvimento (independente de ser "Capítulo 2")
    - ... até `0.7.x.x`, quando os 7 capítulos planejados tiverem entrado

- **PATCH (3º dígito)** 🔧
  - Marca **mudanças estruturais relevantes** dentro do(s) capítulo(s) ativo(s) naquele MINOR:
    - Inclusão de novas seções importantes
    - Reorganização de seções/subseções
    - Introdução ou reformulação de tabelas de modo que alterem a forma como o capítulo é usado

- **SUBPATCH (4º dígito)** ✍️
  - Registra **refinamentos menores**, sem mudança estrutural significativa:
    - Correção de typos e ortografia
    - Pequenas melhorias de wording
    - Ajustes localizados em células de tabela, notas de rodapé ou formatação

### 3.2 Regras de incremento em 0.x.x.x ⬆️

Apenas o MAJOR é fixo (0); os demais dígitos variam conforme o tipo de alteração.

#### 3.2.1 Regra central 🎯

- **Somente conteúdo que entra no arquivo principal do guia (`guide-v*.tex`) pode disparar bump de MINOR/PATCH/SUBPATCH.**  
  - Trabalhos em WIP externo (`section-...tex`, `table-...tex`, `visual-...{svg,pdf,png,tex}`, `notes-...md`, rascunhos) **não** mudam o número de versão até serem integrados.

#### 3.2.2 Tabela "When to Increment (pré-publicação)" 📊

| Situação | Incremento | Observação |
|----------|------------|------------|
| ✨ Começar a trabalhar em um novo capítulo no arquivo principal | **MINOR** | Ex.: `0.1.x.x → 0.2.0.0` |
| 📄 Adicionar uma nova seção relevante em capítulo já ativo | **PATCH** | Ex.: `0.1.1.0 → 0.1.2.0` |
| 🔄 Reestruturar seções/subseções de um capítulo | **PATCH** | Mantém MINOR; altera arquitetura interna |
| 📋 Preencher/alterar tabelas de forma que mude o fluxo de uso do capítulo | **PATCH** | Ex.: nova tabela de HOTAS que reorganiza a leitura |
| ⚠️ Corrigir erros de sintaxe LaTeX que impediam compilação | **PATCH** | "Major bugfix" estrutural |
| ✏️ Corrigir typos, pontuação, pequenos ajustes de wording | **SUBPATCH** | Ex.: `0.1.4.0 → 0.1.4.1` |
| 🎨 Ajustar poucas células em tabelas, sem mudar lógica/estrutura | **SUBPATCH** | Refinamento local |
| 💾 Apenas compilar/salvar, sem mudança de conteúdo | **Data** | Atualizar `YYYYMMDD`, não o número |
| 📁 Trabalho em WIP externo não integrado (`section-...tex`, `table-...tex`, `visual-...{svg,pdf,png,tex}`, `notes-...md`) | **Nenhum** | Versão só sobe quando o conteúdo entra no guia |

#### 3.2.3 Fases internas como metadado 📌

- Fases como **"scaffolding de capítulo"**, **"preenchimento de tabelas"**, **"revisão"** são tratadas como **metadados de progresso**, não como gatilhos diretos para mudar MAJOR em 0.x.x.x
- Essas fases podem aparecer:
  - No PROJECT-TRACKING
  - Na seção de status do próprio guia

### 3.3 Papel das tabelas em 0.x.x.x 📋

#### 3.3.1 Tabelas como parte de capítulos

- O ambiente `hotastable` é definido como **meio de apresentação de conteúdo**, não como unidade estrutural independente
- As tabelas de TMS, DMS e CMS:
  - ✅ São sempre **parte de seções/capítulos** (Cap. 3, 4, 5 etc.)
  - ✅ São indexadas no apêndice de tabelas, reforçando que pertencem aos capítulos principais

#### 3.3.2 Tabelas e incrementos de versão 🔢

- **PATCH por causa de tabela** quando:
  - A inclusão, remoção ou grande reformulação de uma tabela:
    - Muda a forma como o leitor navega ou entende o capítulo
    - Reorganiza o conteúdo (por exemplo, substituir explicação livre por tabela central de referência)

- **SUBPATCH por causa de tabela** quando:
  - Os ajustes:
    - Corrigem descrições de células, typos ou referências
    - Adicionam/removem poucas linhas sem mudar a lógica geral
    - Ajustam formatação, cores, notas de referência

### 3.4 Exemplos práticos (0.x.x.x) 🎬

#### 3.4.1 Linha evolutiva de pré-publicação 📈

- `v0.1.0.0` -- Introdução estruturada e incluída no guia (1º capítulo em desenvolvimento) ✍️
- `v0.1.3.0` -- Capítulo TMS estruturado, com seções principais definidas 📖
- `v0.1.4.0` -- Capítulo DMS reestruturado; correções de geometria, adoção de novo layout de tabelas 🔧
- `v0.2.0.0` -- 2º capítulo em desenvolvimento entra no guia (por exemplo, HOTAS fundamentals) ✨
- `v0.3.0.0` -- 3º capítulo em desenvolvimento entra (por exemplo, CMS), e assim por diante, até:
- `v0.7.0.0` -- Todos os 7 capítulos planejados entraram no guia (scaffolding concluído) 🎉

#### 3.4.2 Mini-casos por cenário 🔍

- **Caso A -- Novo capítulo (Cap. 2) entra no guia:**
  - Situação: até então, apenas Introdução estava no guia como capítulo desenvolvido
  - Ação: integrar a estrutura do Cap. 2 no arquivo principal
  - Versão: `0.1.4.0 → 0.2.0.0` ⬆️

- **Caso B -- Reestruturação de DMS em Cap. 4:**
  - Situação: seções reordenadas, subseções agrupadas, narrativa ajustada
  - Versão: `0.1.3.0 → 0.1.4.0` (PATCH) 🔄

- **Caso C -- Preenchimento parcial de TMS hotastable em Cap. 3:**
  - Situação: primeira versão de tabela que reorganiza o entendimento do capítulo
  - Versão: PATCH no MINOR correspondente, ex.: `0.1.4.0 → 0.1.5.0` 📋

- **Caso D -- Correção de typos em Introdução e TMS:**
  - Situação: apenas typos e microajustes de wording
  - Versão: `0.2.3.0 → 0.2.3.1` (SUBPATCH) ✏️

---

## 4. Ponte para publicação (0.x.x.x → 1.0)

### 4.1 Critérios para declarar 1.0 ✅

Uma versão `0.a.b.c` pode ser promovida a `1.0.0` quando todos os critérios abaixo forem atendidos:

- **Estrutura geral de capítulos estável** 📖
  - Todos os capítulos previstos no escopo da 1ª edição existem e têm narrativa básica completa
  - O índice de capítulos reflete a estrutura que se deseja "congelar" para os leitores

- **Guia usável na prática** 🛠️
  - Um leitor consegue seguir o fluxo e usar TMS/DMS/CMS com base no texto existente
  - Tabelas podem estar parciais, **desde que isso esteja claramente indicado** (por exemplo, rótulos "Em desenvolvimento" ou notas explicativas)

- **Revisão mínima de consistência e clareza** 🔍
  - Terminologia unificada (nomes de modos, comandos, telas, etc.)
  - Referências críticas (Dash-1, Dash-34, Training Manual) checadas em pontos importantes

### 4.2 Procedimento de transição 🔄

1. **Escolher a base 0.a.b.c** 🎯
   - Selecionar, entre as versões 0.x.x.x existentes, aquela que melhor representa o estado "pronto para 1.0"
   - Confirmar que ela atende aos critérios da Seção 4.1

2. **Criar a versão 1.0.0** 🎉
   - Atualizar as macros no LaTeX do guia principal:
   ```latex
   \newcommand{\docversion}{1.0.0}
   \newcommand{\docbuild}{YYYYMMDD}  % Data do "congelamento" da 1ª edição
   ```
   - Salvar o arquivo com o novo nome:
   ```
   guide-v1.0.0-YYYYMMDD.tex
   ```

3. **Congelar a linha 0.x.x.x** ❄️
   - Mover todos os arquivos `guide-v0.*.tex` para uma pasta de histórico, por exemplo:
   ```
   /prepub/guide-v0.*.tex
   ```
   - **Não criar novas versões 0.\*** após o nascimento de 1.0.0
   - A linha 0.x.x.x passa a ser apenas histórico de pré-publicação

4. **Atualizar tracking** 📝
   - No PROJECT-TRACKING, registrar:
     - Qual versão `0.a.b.c` foi promovida a `1.0.0`
     - Uma breve **justificativa editorial** para a promoção (por que esta é a 1ª edição)
     - O caminho/identificador do PDF `guide-v1.0.0-YYYYMMDD.pdf` arquivado

### 4.3 Ponto de corte entre regimes 🔀

- A partir da data de build registrada em `\docbuild` na versão `1.0.0`:
  - **Todas as novas alterações** no guia devem seguir o **regime x.x.x** descrito no Capítulo 5
  - Ou seja, qualquer nova versão passa a ter forma `1.MINOR.PATCH`, depois `2.MINOR.PATCH`, e assim por diante

### 4.4 Checklist antes de promover para 1.0.0 ✔️

Antes de executar a transição, validar:

- ✅ `\chapterscompletedof` e o índice de capítulos refletem corretamente o estado da 1ª edição (por exemplo, não indicam capítulos planejados que ainda não existem)
- ✅ Não há marcas internas evidentes ao leitor (como "TODO", "FIXME", comentários temporários) nas seções principais
- ✅ Tabelas parciais estão claramente identificadas como tal e não dão impressão de "erro"
- ✅ O PROJECT-TRACKING está consistente com o estado que será congelado como 1.0.0 (datas, versões, descrições das mudanças)

---

## 5. Regime de pós-publicação (≥ 1.0, esquema x.x.x)

> 🚀 A partir de `1.0.0`, o foco deixa de ser desenvolvimento interno e passa a ser **gestão de edições e revisões** para leitores.

### 5.1 Semântica dos dígitos em x.x.x

Após a primeira edição publicada, o guia passa a usar:

```
MAJOR.MINOR.PATCH
```

- **MAJOR (1º dígito) -- Edição do guia** 📕
  - Representa **edições principais** (1ª, 2ª, 3ª...)
  - Deve mudar apenas quando houver alterações suficientemente amplas para justificar falar em "nova edição"
  - Exemplos típicos:
    - Reorganização grande de capítulos (fusões, divisões, mudança forte de ordem)
    - Inclusão/remoção de blocos grandes de conteúdo que alterem o escopo global
    - Adaptação a uma nova versão principal do BMS que exija reescrita relevante de vários capítulos

- **MINOR (2º dígito) -- Mudanças compatíveis, mas substantivas** 🔄
  - Marca **revisões importantes**, porém ainda dentro da **mesma edição**
  - O leitor da edição atual não "se perde" ao migrar de uma MINOR para outra:
    - Índice e estrutura geral seguem reconhecíveis
  - Exemplos:
    - Adição de um novo capítulo relevante
    - Grande expansão de capítulos existentes (novas seções e tabelas importantes)
    - Reorganização interna relevante de um subconjunto de capítulos, mantendo a arquitetura global

- **PATCH (3º dígito) -- Correções e ajustes menores** 🔧
  - Registra **ajustes finos** dentro da mesma MINOR:
    - Correções de typos, gramática, formatação
    - Melhoria de clareza em parágrafos, legendas, notas
    - Pequenos ajustes em tabelas, notas, referências
    - Correção de erros pontuais sem reestruturação grande

### 5.2 Regras gerais de incremento em x.x.x ⬆️

#### 5.2.1 Princípios gerais

1. **Compatibilidade editorial** ✅
   - Se o leitor pode usar a nova versão **como substituta direta** da anterior, sem reaprender a estrutura global → em geral **não é MAJOR**
   - Se a nova versão exige rever seriamente referências estáveis (número de capítulo, ordem global) → **candidata a MAJOR**

2. **Frequência** 📊
   - **MAJOR** é raro (edições)
   - **MINOR** é menos raro, mas ainda sinaliza revisões importantes
   - **PATCH** pode ocorrer com mais frequência (errata, polimento)

3. **Continuidade com 0.x.x.x** 🔗
   - 0.x.x.x vira histórico de pré-publicação; em ≥ 1.0, evita-se derrubar a arquitetura editorial sem necessidade

#### 5.2.2 Tabela "When to Increment (pós-publicação)" 📋

| Situação | Inc. | Comentário |
|----------|------|-----------|
| 🔄 Reorganizar estrutura de capítulos (fusões, divisões, grande mudança de ordem) | **MAJOR** | Leitor enxerga como "nova edição do guia" |
| 📚 Introduzir/remover blocos grandes de conteúdo que alteram o escopo global | **MAJOR** | Ex.: nova parte inteira do documento, ou remoção de parte dominante |
| 🆕 Adaptar o guia a uma nova versão principal do BMS, com reescrita relevante de vários capítulos | **MAJOR** | Conteúdo anterior deixa de ser plenamente atual |
| ✨ Adicionar um **novo capítulo importante** dentro da mesma edição | **MINOR** | Escopo ampliado, mas edição ainda é a mesma |
| 📖 Expandir substancialmente um ou mais capítulos (novas seções, tabelas-chave) | **MINOR** | Melhorias significativas, sem quebrar organização global |
| 🔧 Reorganizar internamente um subconjunto de capítulos, mantendo índice global reconhecível | **MINOR** | "Edição revisada" dentro do mesmo MAJOR |
| ✏️ Corrigir vários erros pontuais de conteúdo (mas localizados) em texto/tabelas | **PATCH** | Foco em correção, não em aumento de escopo |
| 📝 Corrigir typos, gramática, melhorar clareza, atualizar referências | **PATCH** | Versões típicas de errata e polimento |
| 🎨 Ajustar poucas células em tabelas, mudar rótulos sem alterar lógica | **PATCH** | Não requer renumeração de capítulos nem mudança de fluxos de leitura |

### 5.3 Papel das tabelas no regime ≥ 1.0 📊

- **Tabelas são parte de capítulos**, não artefatos MAJOR:
  - Uma nova **tabela grande e central** em capítulo importante:
    - Pode justificar **MINOR**, se a expansão for substancial
    - Ou **PATCH**, se for mero refinamento de algo já descrito

- **Correções localizadas em tabelas** (células, siglas, notas):
  - Tendem a ser **PATCH**, salvo se a mudança for tão ampla que modifique a lógica de uma parte chave (nesse caso, avaliar MINOR)

### 5.4 Exemplo de progressão em x.x.x 📈

#### 5.4.1 Da 1ª edição em diante

- `1.0.0` -- **1ª edição publicada** 🎉
  - Estrutura de capítulos estável, narrativa utilizável, tabelas marcadas mesmo se parciais

- `1.0.1` -- **Errata inicial** 🔍
  - Correções de typos, pequenos erros em descrições de TMS/DMS/CMS, ajustes pontuais de formatação

- `1.1.0` -- **Revisão ampliada dentro da 1ª edição** 📚
  - Adição de 1 novo capítulo relevante (por exemplo, fluxos avançados de treinamento)
  - Algumas tabelas originadas em 0.x.x.x foram completadas

- `1.1.3` -- **Terceiro conjunto de correções menores sobre 1.1.0** ✅
  - `1.1.1`, `1.1.2`, `1.1.3` acumulam errata e clarificações

- `2.0.0` -- **2ª edição revisada** 🚀
  - Vários capítulos reagrupados, ordem revisada, atualizações amplas para acompanhar nova versão principal do BMS

#### 5.4.2 Exemplos de decisão 🤔

- **Caso 1 -- Novo capítulo sobre "TMS/DMS/CMS em aeronaves adicionais" em 1.x**
  - Estrutura global se mantém → `1.0.2 → 1.1.0` (MINOR) ✨

- **Caso 2 -- Correção de comandos errados em tabelas de CMS**
  - Ajustes em células, sem reestruturar capítulos → `1.1.0 → 1.1.1` (PATCH) ✏️

- **Caso 3 -- Reorganizar a parte de treinamento (Cap. 6) em duas partes**
  - Se mexe apenas em parte da estrutura, mantendo índice reconhecível → **MINOR** 🔄
  - Se induz mudança ampla na arquitetura do guia → avaliar **MAJOR** 📕

### 5.5 Interação com o histórico 0.x.x.x 📁

- Versões **0.x.x.x**:
  - Mantidas como **histórico de pré-publicação**, úteis para traçar evolução e decisões didáticas 📚

- Após `1.0.0`:
  - Não se criam novas versões 0.*
  - Toda mudança futura segue o regime x.x.x ✅

### 5.6 Checklist rápido para versões ≥ 1.0 ✔️

1. **Sua mudança altera a edição (leitor deveria ver como "nova edição")?**
   - Sim → **MAJOR** (ex.: `1.3.2 → 2.0.0`) 📕
   - Não → prossiga

2. **Sua mudança aumenta significativamente o escopo ou reorganiza parte importante, mas mantém edição?**
   - Sim → **MINOR** (ex.: `1.0.0 → 1.1.0`) 🔄
   - Não → prossiga

3. **Sua mudança é local (correções, clarificações, pequenos ajustes em tabelas/texto)?**
   - Sim → **PATCH** (ex.: `1.1.0 → 1.1.1`) ✏️

---

## 6. Regras comuns a ambos os regimes 🔗

### 6.1 Build date e compilação 📅

- **Build date (`YYYYMMDD`)** deve ser atualizada sempre que:
  - Uma nova versão de número (0.x.x.x ou x.x.x) é estabelecida ✅
  - Um snapshot relevante é compilado e salvo 💾

- Diferença entre snapshot interno e versão oficial:
  - Apenas versões cujo número foi atualizado em `\docversion` e no nome do arquivo entram no PROJECT-TRACKING como marcos 📌

### 6.2 File naming workflow 📝

Fluxo único, para 0.x.x.x e x.x.x:

1. **Determinar tipo de mudança** 🔍
   - Usar as tabelas "When to Increment" (pré ou pós-publicação)

2. **Atualizar macros de versão/data no LaTeX** ✏️
   - Ajustar `\docversion` para o novo número
   - Ajustar `\docbuild` para a nova data `YYYYMMDD`
   - Garantir que `\fulldocversion` reflita a combinação correta

3. **Compilar e verificar erros** 🔧
   - Gerar o PDF e checar avisos/erros de LaTeX

4. **Renomear o arquivo** `.tex` 📄
   - Aplicar o padrão:
   ```
   guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex
   ```

5. **Atualizar PROJECT-TRACKING** 📊
   - Adicionar linha com versão, data, capítulo(s) afetado(s), descrição sucinta da mudança

6. **Arquivar a versão anterior** 🗂️
   - Mover o `.tex` e, opcionalmente, o `.pdf` para a pasta de histórico adequada (`/prepub/` ou `/published/`)

### 6.3 Archival strategy 📦

- Organização por regime:
  - `/prepub/guide-v0.*.tex` -- histórico de desenvolvimento interno 📚
  - `/published/guide-v1.*.tex`, `/published/guide-v2.*.tex` etc. -- edições e revisões publicadas 🎯

- Git (opcional):
  - Versionar somente fontes `.tex` e arquivos de texto
  - Excluir artefatos com `.gitignore`:
  ```text
  *.pdf
  *.docx
  *.aux
  *.log
  *.synctex.gz
  ```

### 6.4 Relação com naming de arquivos WIP 🧩

- Este documento (`Version System v4.1`) rege **somente** o versionamento e o naming do arquivo principal do guia (`guide-v*.tex`) e seu histórico.  
- Os arquivos de preparação individuais (`section-`, `table-`, `visual-`, `notes-`) seguem regras próprias definidas em arquivo separado **`WIP-FILE-NAMING v*`**.  
- Esses arquivos WIP **só impactam a versão** quando seu conteúdo é efetivamente integrado ao `guide-v*.tex` (isto é, quando altera o conteúdo do arquivo principal).

---

## 7. Quick reference consolidado 🎯

### 7.1 Quick Reference (0.x.x.x -- pré-publicação) 📝

- **MAJOR = 0** sempre
- **MINOR:** novo capítulo entra no guia ✨
- **PATCH:** mudança estrutural em capítulo (seções/tabelas que alteram fluxo) 🔄
- **SUBPATCH:** ajustes finos (typos, wording, pequenos ajustes em tabelas) ✏️

| Situação-chave | Versão pré (ex.) | Versão pós (ex.) |
|---|---|---|
| ✨ Novo capítulo entra no guia | `0.1.4.0 → 0.2.0.0` | --- |
| 🔄 Reestruturar seções de um capítulo | `0.2.1.0 → 0.2.2.0` | --- |
| 📋 Tabela importante altera uso do capítulo | `0.2.2.0 → 0.2.3.0` | --- |
| ✏️ Corrigir typos e microajustes de wording | `0.2.3.0 → 0.2.3.1` | --- |

### 7.2 Quick Reference (x.x.x -- pós-publicação) 🚀

- **MAJOR:** nova edição (mudanças amplas, possível incompatibilidade) 📕
- **MINOR:** expansão compatível, mas substantiva (capítulos novos, blocos grandes) 🔄
- **PATCH:** correções menores, clarificações, ajustes localizados ✏️

| Situação-chave | Versão pré (ex.) | Versão pós (ex.) |
|---|---|---|
| 📕 2ª edição revista (mudança ampla) | --- | `1.3.2 → 2.0.0` |
| ✨ Capítulo novo importante em mesma edição | --- | `1.0.0 → 1.1.0` |
| ✏️ Correções menores e clarificações em 1.1.0 | --- | `1.1.0 → 1.1.1` |

### 7.3 Notas chave 💡

- **Tabelas** são sempre parte de capítulos; **nunca definem MAJOR sozinhas** 📊
- **0.x.x.x** nunca é edição publicada; é sempre regime de desenvolvimento interno 🔴
- **1.0** marca a primeira edição publicada; **2.0**, **3.0** etc. são novas edições sucessivas, em linha com boas práticas de documentação técnica 📚

---

**Fim do documento — Version System v4.1** ✅
