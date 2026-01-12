# Análise do Capítulo 5 (CMS) - guide.tex
## Para servir como base de estrutura para Capítulo 4 (DMS)

---

## ESTRUTURA GERAL DO CAPÍTULO CMS

### Seção 5.1: Conceito e Interação com CMDS/ECM/RWR

**Foco Principal**: Definição funcional e propósito operacional
- Explica por que CMS é crítica (G-load, workload, design ergonômico)
- Descreve a integração com RWR como "decision engine"
- Articula os dois níveis defensivos: CMDS e ECM
- Inclui imagem do F-16 stick mostrando localização física do CMS

**Estilo**: Narrativo, profissional, com ênfase em contexto operacional

**Comprimento**: ~500-600 palavras, bem condensado

### Seção 5.2: CMS Switch Actuation (Seção PRINCIPAL - VERY WIP)

**Estrutura de Tabelas HOTAS**:
```
Estado | Direção | Ação | Função | Efeito | Nuance | DASH-34 | Treinamento
```

**Subsecções**:
1. **5.2.1**: CMS com CMDS (3 modos)
   - 5.2.1.1 Manual Mode (hotastable com 2 linhas - UP, LEFT)
   - 5.2.1.2 Automatic Mode (hotastable com 4 linhas - UP, LEFT, AFT, RIGHT)
   - 5.2.1.3 Semi-Automatic Mode (hotastable com 4 linhas - UP, LEFT, AFT, RIGHT)

2. **5.2.2**: CMS com ECM (2 configurações)
   - 5.2.2.1 External ECM Pod (hotastable com 2 linhas - AFT, RIGHT)
   - 5.2.2.2 Internal ECM IDIAS (hotastable com 2 linhas - LEFT, RIGHT)

3. **5.2.3**: CMS Consent and Constraints
   - 1 hotastable mostrando joint consent model (CMDS AUTO/SEMI + ECM Pod)

4. **5.2.4**: Important Operational Notes
   - Bullet points explicando: Consent State Tracking, Bingo Behavior, RF Switch Override, ECM vs CMDS Consent, Ground Safety

### Seção 5.3: CMS Block Variant Notes

**Estrutura**:
- Explicação de ECM configurations no BMS
- 2 tabelas (tabularp) mostrando Block/Variant → External ECM ou Internal IDIAS

---

## CARACTERÍSTICAS ESTRUTURAIS IMPORTANTES

### 1. USO DE REFERENCE LINKS
- **Padrão**: `2.7.2.1` = seção de DASH-34 (ex: 2.7.2.1 = CMDS AUTO mode)
- **Padrão**: `18 BARCAP, 28 SEAD-EW` = missões de treinamento (ex: Training Mission 18, 28)
- Estas referências cruzadas são **críticas para rastreabilidade**

### 2. NEGRITO PARA ÊNFASE
- **Sempre em negrito**: Sistema names (CMDS, ECM, RWR, IDIAS, ALE-47)
- **Sempre em negrito**: Nomes de modos (MAN, AUTO, SEMI, STBY, etc.)
- **Sempre em negrito**: Estados de luz (ECM Enable light)
- **Nunca em negrito**: Direções (up, down, left, right) — são lowercase

### 3. ENVIRONMENT: hotastable
- MacroLaTeX custom para tabelas HOTAS
- Formato: `\begin{hotastable}...\end{hotastable}`
- 7 colunas com headers em headerblue + white text
- Linhas de dados em formato simples com `\` para quebra de linha
- Uma `\end{hotastable}` e correspondente `\hline` de rodapé

**Exemplo de estrutura**:
```latex
\begin{hotastable}
\textbf{State} & \textbf{Dir} & \textbf{Act} & \textbf{Function} & 
\textbf{Effect} & \textbf{Nuance} & \textbf{Dash34} \\
\hline
CMDS MAN & Up & Shrt & Execute Program 1-4 & Runs the program... & 
No threat sensing... & 2.7.2.2 \\
\hline
\end{hotastable}
```

### 4. CROSS-REFERENCING
- **sec5-S1**: Seção 5.1
- **sec5-S2**: Seção 5.2
- **tab5-S3-external-ecm-pods**: Tabela 5.3 subsecção external ECM pods
- Padrão: `\label{sec5-S2-S1}` dentro de subsecções

### 5. TABELAS VARIANTES (tabularp)
- Subsecção 5.3 usa `\begin{tabularp}{3.0cm}{5.8cm}` (tamanhos de coluna fixos)
- Formato: Operator | BlockVariant
- Estrutura de header igual aos hotastables

### 6. NEGRITO EM TEXTO PRINCIPAL
- CMS é sempre em negrito dentro de texto
- Nomes de comandos são em negrito (Up, Down, Left, Right, Aft)
- "CMS Aft grants consent" é padrão
- "CMS Right" é padrão

---

## PADRÕES DE CONTEÚDO

### Para cada Modo/Configuração:
1. **Introdução curta** (1-2 frases) explicando o contexto
2. **Hotastable com 2-4 linhas** mostrando as opções
3. **Notas operacionais adicionais** (em seção separada se muitas)

### Para cada Entrada de Tabela:
- **Function**: Ação em voz passiva ou imperativa ("Execute...", "Give Consent...", "Cycle...")
- **Effect**: Resultado em voz ativa e detalhe técnico ("CMS Aft grants consent for AUTO CMDS. RWR-detected threats trigger...")
- **Nuance**: Contexto, restrições, caveats, tácticas ("This unified control maximizes pilot situational awareness...")
- **Dash34**: Seção de DASH-34 (ex: "2.7.2.2")
- **Train**: Missões de treinamento (ex: "18 BARCAP, 28 SEAD-EW")

---

## DIFERENÇAS CRÍTICAS PARA DMS

Enquanto CMS é sobre **consent authority, modes, and transmit control**, DMS é sobre **navigation, format selection, e SOI cycling**.

### Implicações Estruturais:
1. **Sem "modos" como em CMS** — DMS tem contextos de formato MFD, não modos CMDS
2. **Sem "consent"** — DMS é puramente navegacional
3. **Sem "state persistence"** — DMS alterações de formato são instantâneas, não mantêm estado hidden
4. **Tabelas DMS provavelmente serão MAIS simples** — menos subconfigurações
5. **DMS não tem "variants" como CMS (external vs. internal ECM)**
   - Pode ter variações por radar mode (A-A vs. A-G) ou sensor type
   - Mas não é tão estrutural quanto external/internal ECM

### Seções Esperadas para DMS:
- 4.1: Conceito e papel de SOI
- 4.2: DMS Switch Actuation
  - 4.2.1: SOI Selection (UP/DOWN)
  - 4.2.2: MFD Format Stepping (LEFT/RIGHT)
  - 4.2.3: DCLT (Declutter) mode
  - 4.2.4: Constraints and Notes
- 4.3: DMS Block Variant Notes (provavelmente simples)

---

## FONTE DE VERDADE TÉCNICA

O capítulo CMS refere-se constantemente a:
- **DASH-34**: 2.7.1 (CMDS), 2.7.2 (ECM), 2.7.3 (RWR), 2.7.4 (CMS Operations)
- **BMS Training Manual**: Missões 18 (BARCAP), 28 (SEAD-EW)

Para DMS, será necessário:
- **DASH-34**: 2.1.6 (MFD - Multi-Function Display)
- **DASH-34**: Seções sobre SOI cycling
- **BMS Training Manual**: Referências de missões de treinamento apropriadas

---

## CONCLUSÃO

O Capítulo 5 (CMS) é **bem estruturado, profissional e completo**. 

Para escrever o Capítulo 4 (DMS), devo:
1. Manter a mesma estrutura geral (Conceito → Actuation → Variants)
2. **Simplificar** as subsecções (DMS tem menos "ramificações" que CMS)
3. Manter o mesmo nível de rigor técnico e cross-referencing
4. Usar o mesmo ambiente `hotastable`
5. Enfatizar que DMS é **linear, determinístico e simples** (contraste com CMS)
6. Fornecer referências DASH-34 apropriadas para DMS (seção 2.1.6 ou similar)
7. Incluir missions de treinamento apropriadas que usam heavily DMS
