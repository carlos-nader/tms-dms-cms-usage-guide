# BLUEPRINT CHAPTER 4 — DECISÃO FINAL APROVADA
**Data:** 14 janeiro 2026, 14h40 -03  
**Status:** ✅ APROVADO PELO USUÁRIO  
**Guia para:** Implementação futura de Chapter 4 (DMS)

---

## Ajustes Implementados (User approval, 14 jan 2026)

### 1️⃣ REJEITAR Subsections por Master Mode

**Proposta original:** 
```
4.2.1 DMS Up
  4.2.1.1 DMS Up in NAV
  4.2.1.2 DMS Up in A-G
  4.2.1.3 DMS Up in A-A
```

**Decisão:** ❌ REJEITADO

**Razão:**
- Fragmenta desnecessariamente; C4-S1 (Table 4.1.x) JÁ fornece valid SOI por master mode
- Diferenças são BINÁRIAS (válido/inválido), não multifacetadas
- Replica lógica tipo TMS, que é weapon-specific; DMS é transversal
- Estrutura simples Up/Down/Left/Right é suficiente; master modes referenciados a C4-S1

**Estrutura mantida:**
```
4.2.1 DMS Up: Designate HUD as SOI
4.2.2 DMS Down: Toggle SOI Between Displays
4.2.3 DMS Left/Right: Cycle MFD Formats
4.2.4 Master Mode Summary Table
```

---

### 2️⃣ REMOVER 4.2.4 (DMS + TMS Integration)

**Proposta original:**
- Seção de 400–500 palavras explicando como DMS seleciona SOI e TMS age sobre ele
- 5 contextos críticos (AGM-65 VIS, HARM, Link 16, DTOS, IAM)

**Decisão:** ❌ REMOVIDO

**Razão:**
- **C4-S1** JÁ explica: "DMS selects SOI; TMS acts upon it"
- **DMS Up bullets (AGM-65 VIS, etc.)** JÁ explicam coupling: "Target rejection requires HUD as SOI"
- Adicionar seção 4.2.4 seria **redundância terciária**
- Temas específicos de armas permanecem **inline nos bullets**, não em seção separada

**Resultado:**
- Blueprint reduz de 5 para 4 seções (4.2.1–4.2.4)
- Coupling DMS-TMS fica onde semanticamente pertence: nos bullets de operação
- Uma WIP file a menos para criar

---

### 3️⃣ DEIXAR EXCEPTIONS INLINE (não consolidar em 4.2.5)

**Proposta original:**
- Seção 4.2.5 consolidada com Snowplow (SP) PRE, MARK/OFLY, Operational Notes

**Decisão:** ❌ CONSOLIDAÇÃO REJEITADA; ✅ EXCEPTIONS INLINE

**Razão:**
- Exceptions são **RARAS** (2 casos: Snowplow, MARK/OFLY)
- **Contexto importa:** Leitor em 4.2.1 quer saber imediatamente se exceções afetam DMS Up
- Pular para seção 4.2.5 **interrompe fluxo de leitura**
- Deixa seção 4.2.5 muito magra (~300 palavras)

**Implementação:**
- Snowplow (SP) PRE: subsection "Exception States" inline em 4.2.1 (~100 palavras)
- Snowplow (SP) PRE: subsection "Exception States" inline em 4.2.2 (~100 palavras)
- MARK/OFLY: mencionada em ambas as seções

**Resultado:**
- Exceptions integradas organicamente no contexto onde ocorrem
- Reforço natural (não redundância pura) ao aparecer em múltiplas seções
- Nenhuma seção 4.2.5 vazia

---

## BLUEPRINT FINAL (Estrutura Aprovada)

```
4.1 Concept and Sensor of Interest (SOI)
    [Existente: C4-S1, final, sem alterações]
    └─ Table 4.1.x: Valid SOI Displays by Master Mode

4.2 DMS Switch Actuation

  4.2.1 DMS Up: Designate HUD as SOI
        [~1,200–1,500 words]
        ├─ Subseção: Function and Visual Indication
        ├─ Subseção: DMS Up Effectiveness in All Master Modes
        │   └─ Referências a Table 4.1.x; NAV/A-G/A-A context
        ├─ Subseção: Exception States (inline)
        │   ├─ Snowplow (SP) PRE (unstabilized)
        │   └─ MARK/OFLY Submode
        ├─ Table 4.2.1: DMS Up Usage Across Master Modes
        └─ Operational Examples (CCIP, AGM-65, IAM)

  4.2.2 DMS Down: Toggle SOI Between Displays
        [~1,500–2,000 words]
        ├─ Subseção: Core Logic - Toggle Behavior by Current SOI
        ├─ Subseção: SOI Alternation in Specific Master Modes
        │   └─ Referências a Table 4.1.x; cycling patterns
        ├─ Subseção: Exception States (inline)
        │   ├─ Snowplow (SP) PRE
        │   └─ MARK/OFLY Submode
        ├─ Table 4.2.2: DMS Down Toggle Logic
        └─ Practical Scenarios (NAV rapid toggle, A-A MFD-only, A-G VIS HUD-to-WPN)

  4.2.3 DMS Left/Right: Cycle MFD Formats
        [~1,000–1,300 words]
        ├─ Subseção: Format Cycling Mechanics (blank skipping rules)
        ├─ Subseção: Available Formats by Master Mode
        │   └─ Referências a Table 4.1.x; format availability
        ├─ Subseção: Left/Right Does NOT Affect SOI (critical clarification)
        ├─ Table 4.2.3: DMS Left/Right Behavior by Master Mode
        └─ Practical Scenarios (rapid format access, TGP↔WPN cycling)

  4.2.4 Master Mode Behavior — SOI Selection & DMS Availability Summary
        [~500 words]
        ├─ Brief recap of DMS roles (Up/Down/Left/Right)
        ├─ Table 4.2.4: Consolidated DMS Availability × Master Mode
        └─ Cross-references to 4.2.1–4.2.3; reference back to C4-S1 (Table 4.1.x)
```

**Total word count:** ~5,200–6,300 words (vs ~7,000–8,500 no blueprint original)

**HOTAS tables:** 4 total
- Table 4.2.1 (DMS Up)
- Table 4.2.2 (DMS Down toggle)
- Table 4.2.3 (DMS Left/Right)
- Table 4.2.4 (Master Mode Summary)

---

## Implementação — Próximos Passos

### Fase 1: DMS Up (file:26 trim)
1. Remover ~300–500 palavras de redundância com C4-S1
2. Manter exceptions (Snowplow, MARK/OFLY) inline
3. Manter bullets de operação (CCIP, AGM-65, IAM)
4. Referências a Table 4.1.x em vez de re-explicar master modes
5. Target: 1,200–1,500 words

### Fase 2: DMS Down
1. Extrair de file:26 (já existe, precisa trim)
2. Aplicar same redundancy-removal logic
3. Target: 1,500–2,000 words

### Fase 3: DMS Left/Right
1. Novo WIP file (not in current file:26)
2. ~1,000–1,300 words
3. Foco: Format cycling mechanics, independence from SOI, scenarios

### Fase 4: Master Mode Summary
1. Novo WIP file (short, ~500 words)
2. Table 4.2.4 consolidada
3. Cross-references completas

---

## Referência Rápida: O Que Mudou vs Blueprint Original

| Item | Original | Final | Razão |
|------|----------|-------|-------|
| Subsections por master mode | Sim (4.2.1.1, 4.2.1.2, etc.) | Não | Avoid fragmentação |
| Seção 4.2.4 (DMS+TMS Integration) | Sim (~500 words) | Não | Redundante com C4-S1 + bullets |
| Seção 4.2.5 (Exception States consolidated) | Sim (~600–800 words) | Não | Exceptions inline |
| Total seções em 4.2 | 5 | 4 | Estrutura mais limpa |
| Total word count | ~7,000–8,500 | ~5,200–6,300 | Mais enxuto |
| HOTAS tables | 4–5 | 4 | Uma menos, consolidada |

---

## Status Final

✅ **Blueprint APROVADO e FINAL**  
✅ **Estrutura definida para implementation**  
✅ **Word count targets estabelecidos**  
✅ **Pronto para DMS Up trim (Fase 1)**

**Documento válido para:**
- Guia de desenvolvimento de Chapter 4 DMS
- Referência para decisões de escopo/estrutura
- Validação de completude em cada seção

---

**Data de aprovação:** 14 janeiro 2026, 14h40 -03  
**Aprovado por:** Usuário (Carlos "Metal" Nader)  
**Próximo checkpoint:** DMS Up trim completion + submission
