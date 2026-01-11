# C5‑S3 – CMS Block and Variant Notes  
Guia de revisão estruturada (WIP Review 5.3)

## 1. Objetivo da seção 5.3

- 5.2 define o **comportamento base** do CMS (switch actuation e lógica geral).  
- 5.3 existe **apenas** para:
  - Indicar **variações por bloco/variante** em relação a esse baseline.  
  - Deixar claro **quando o CMS é usado com ECM externo** vs **IDIAS interno**, e como isso muda os gestos no hat.  
- Regra de ouro: 5.3 **não reexplica 5.1/5.2**; só aponta onde cada variante “desvia” do padrão.

---

## 2. Estrutura proposta para 5.3 (árvore de seções)

Usar a seguinte hierarquia-alvo ao revisar o arquivo:

- 5.3 **CMS Block and Variant Notes**  
  Pequeno parágrafo introdutório:
  - Reforça que 5.2 é o baseline.  
  - Diz que 5.3 só trata de diferenças por variante, especialmente ECM externo vs IDIAS.

  - 5.3.1 **ECM Configurations in BMS**  
    - Descrever, em 2–3 parágrafos curtos:
      - Grupo 1: **External ECM pods (ALQ‑131 / ALQ‑184)**.  
      - Grupo 2: **Internal ECM (IDIAS)**.  
    - Focar em:
      - Como o CMS conversa com cada tipo de sistema (sem entrar em tática geral).  
      - Referências Dash‑34, sem listar operador por operador.

  - 5.3.2 **Variants and Applicable Procedures**  
    - Explicar quais variantes BMS caem em cada grupo:  
      - Variantes que seguem “perfil ECM externo” → usam procedimentos de 5.2 “external pod”.  
      - Variantes que seguem “perfil IDIAS” → usam procedimentos de 5.2 “IDIAS + diferenças de 5.3.3”.  
    - Deixar claro que o foco é **BMS 4.38.1**, não catálogo real‑world completo.

  - 5.3.3 **Critical Operational Differences**  
    - Conter apenas diferenças que impactam diretamente o uso do CMS:
      - 5.3.3.1 **CMS Aft vs CMS Left**  
        - ECM externo: CMS Aft concede/gera transmissão; CMS Left não é usado para ECM.  
        - IDIAS: CMS Left cicla modos; CMS Aft não controla transmissão.  
        - Fechar com aviso explícito de “habits transfer” (quem vem de pod e entra em IDIAS precisa trocar o reflexo).
      - 5.3.3.2 **XMIT knob vs XMTR switch**  
        - ECM externo: XMIT knob 3 posições (1/2/3) com implicações claras.  
        - IDIAS: XMTR STBY/OPER; seleção de modo vem do CMS Left.  
        - Ressaltar que não há “Continuous Jam” equivalente em IDIAS (no contexto BMS).

  - 5.3.4 **Variant Summary Cross‑Reference**  
    - Introdução bem curta explicando a tabela:
      - Como ler as colunas.  
      - Como usar para saber se a variante segue “procedimentos pod” ou “procedimentos IDIAS”.
    - Tabela enxuta, com:
      - Colunas do tipo “Variant”, “ECM Type”, “CMS Transmit”, “CMS Mode Select”, “Mode Selector”, “Section Ref / Baseline”.

  - 5.3.5 **Operational Notes and Safety Reminders**  
    - Manter só o que é **diretamente ligado a confundir ECM externo vs IDIAS no uso do CMS**:
      - Perigo de apertar CMS Aft em IDIAS (não liga ECM).  
      - Perigo de apertar CMS Left esperando algo em ECM externo (não faz nada).  
      - Necessidade de confirmar tipo de ECM antes de aplicar os procedimentos de 5.2.  
    - Itens de missão/tática mais amplos (ameaças, geometria, drag, interoperabilidade) devem:
      - Ser **removidos** daqui, ou  
      - Migrar no futuro para Capítulo 6 (Training / flows), se ainda forem relevantes.

---

## 3. O que reduzir ou remover

Durante a review, aplicar estes filtros:

- **Listas longas de variantes e operadores (por país)**  
  - Problema:
    - Fica parecendo inventário de frota, não apêndice prático de 5.2.  
  - Ação:
    - Reduzir para **2–4 linhas por grupo**, focadas em:
      - “Grupo X de variantes BMS usa ECM externo → seguir comportamento de 5.2 (external pod).”  
      - “Grupo Y de variantes BMS usa IDIAS interno → seguir comportamento de 5.2 (IDIAS) + diferenças de 5.3.3.”  
    - Manter referências Dash‑34 por grupo, não por operador específico, sempre que possível.

- **Notas de planejamento de missão genéricas**  
  - Exemplos a podar ou mover:
    - Discussão sobre ameaça/terreno/drag/interoperabilidade que não impacta **diretamente** o gesto no CMS.  
  - Ação:
    - Manter só avisos cujo impacto seja “apertar o botão errado / usar a sequência errada de CMS”.  
    - Resto: cortar, ou planejar reaproveitamento no Cap. 6.

- **Repetição de explicações de 5.1/5.2**  
  - Ação:
    - Quando algo já está explicado em 5.1 ou 5.2, usar remissão curta:
      - “Baseline CMS actuation is described in Section 5.2. This subsection only notes how IDIAS differs from that baseline.”  

---

## 4. Ajustes técnicos de LaTeX para integração futura

Quando este WIP estiver maduro para integração:

- **Remover preâmbulo e estrutura standalone**  
  - Apagar tudo de `\documentclass` até `\pagenumbering{arabic}`.  
  - No guia, a seção começa diretamente com:
    - `\section{CMS Block and Variant Notes}`  
    - Seguido das subseções planejadas.

- **Não redefinir infraestrutura global (hotastable, cores, macros)**  
  - O arquivo atual redefine:
    - Ambiente `hotastable`.  
    - Cores (`headerblue`, etc.).  
    - Macros de referência (`\dashref`, `\dashone`, `\trnref`, etc.).  
  - Para evitar divergência com o template congelado na Seção 11 do Briefing:
    - Remover essas redefinições locais em 5.3.  
    - Confiar totalmente nas definições globais de `guide.tex` / template.

- **Simplificar labels**  
  - Hoje aparecem labels do tipo `sec:C5-S3-S3-S1-cms-aft-left`.  
  - Recomendar:
    - `\label{sec:C5-S3}` para a seção principal.  
    - `\label{sec:C5-S3-config}`, `\label{sec:C5-S3-variants}`, `\label{sec:C5-S3-critical}`, `\label{sec:C5-S3-summary}`, `\label{sec:C5-S3-safety}` para as subseções.  
    - Em subsubseções críticas (Aft vs Left, XMIT vs XMTR):
      - `\label{sec:C5-S3-cms-aft-left}`  
      - `\label{sec:C5-S3-xmit-xmtr}`  
    - Mantém coerência e evita hierarquia excessivamente profunda nos labels.

---

## 5. Checklist rápido de revisão de conteúdo (C5‑S3)

Usar este checklist quando for revisar/fechar o WIP:

- [ ] A introdução de 5.3 deixa claro que:
  - 5.2 é o baseline.  
  - 5.3 só trata de variações por bloco/variante.

- [ ] 5.3.1 restringe‑se a descrever **tipos de ECM em BMS** (pod vs IDIAS), em poucas linhas.  
- [ ] 5.3.2 mapeia variantes para:
  - Grupo “procedimentos pod” vs “procedimentos IDIAS”.  
  - Sem virar catálogo de operadores.

- [ ] 5.3.3 contém apenas diferenças que mudam o uso do CMS (direção/gesto/botão) e remete a 5.2 para o resto.  
- [ ] 5.3.4 tem tabela enxuta, com colunas úteis para “qual procedimento aplicar” e refs de seção claras.  
- [ ] 5.3.5 mantém apenas:
  - Avisos de hábito cruzado (Aft vs Left, XMIT vs XMTR).  
  - Checklist mínimo para confirmar tipo de ECM antes de aplicar procedimentos.

- [ ] Não há redefinição local de `hotastable`, cores ou macros de referência na versão a ser integrada.  
- [ ] Labels seguem padrão raso e coerente com o restante do Capítulo 5.  
- [ ] Qualquer afirmação sensível (modo de transmissão, persistência, comportamento de knobs/switches) está alinhada com Dash‑34 / BMS Training Manual.
