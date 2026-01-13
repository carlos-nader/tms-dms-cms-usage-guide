# HUD SOI em A-G PRE - PONTOS CRÍTICOS PARA REVISÃO

**Data:** 13 JAN 2026
**Status:** ⚠️ PENDENTE APROFUNDAMENTO
**Marcado para:** Revisão Técnica Completa

---

## QUESTÃO CENTRAL

**Quando HUD é SOI em A-G PRE (CCRP, Maverick PRE, Harpoon PRE):**
- O designator box (TD-box) pode ser ajustado/movido?
- Se sim, é via **HUD cursor control** ou via **FCR/TGP cursor?**

---

## EVIDÊNCIAS ENCONTRADAS

### 1. HUD SOI EM A-G MASTER MODE - PERMITIDO

**Seção 2.1.1.2.3 - SENSOR-OF-INTEREST SOI**
```
"The HUD can only be the designated SOI in navigation and air-to-ground master modes."
```
✅ **CONFIRMADO:** HUD pode ser SOI em A-G

---

### 2. HUD SOI TEM "CURSOR" PARA AJUSTAR POSIÇÃO

**Seção 2.1.7.5.4 - HUD SENSOR OF INTEREST SOI**
```
"When the HUD is selected as SOI, a movable cursor or target designator box is displayed on the HUD. 
The position of this cursor or designator box can be adjusted using the cursor switch on the throttle, 
and the designated target can be stabilized or designated for ground-based operations using the TMS up command on the sidestick."
```
✅ **MAS:** Esta seção menciona "two MAIN purposes":
1. Creating HUD mark points
2. Employing air-to-ground missiles in Visual VIS mode

❓ **QUESTÃO:** Isto também aplica-se a A-G PRE modes (CCRP, Maverick PRE)?

---

### 3. TD-BOX AJUSTÁVEL - MAS POR QUEM?

**Seção 4.2.2.2.1.4 - AIR TO GROUND TARGET DESIGNATOR BOX**
```
"The TD box represents the LOS to the target and is positioned over the INS representation of the steer point."
```

**Seção 4.2.2.2.1.2.1 - DIRECT AIMPOINT SIGHTING STPT/TGT**
```
"Slewing the cursor via the cursor control may be required to place the steerpoint position over a desired aim point more precisely."
```

**Seção 4.2.1.5 - A-G RADAR AND SPI**
```
"When slewing the radar cursor, the SPI position will update as well on the HUD—the TD box will move"
```

⚠️ **CRÍTICO:** Estes textos referem-se a **FCR/TGP cursor slewing**, NÃO a HUD cursor!

---

### 4. RESTRIÇÃO EXPLÍCITA - SNOWPLOW E MARK OFLY

**Seção 2.1.1.2.3 - SENSOR-OF-INTEREST SOI**
```
"It is important to note that the SOI cannot be designated in the MARK OFLY submode 
or the snowplow SP ground radar mode within the pre-designate PRE state."
```

❓ **QUESTÃO:** Isto restringe TODA A DESIGNAÇÃO em PRE, ou apenas em submodes específicos?

---

## PONTOS DE AMBIGUIDADE

### A. Diferença entre "Movable Cursor" em VIS vs PRE

| Aspecto | VIS Mode | PRE Mode |
|---------|----------|----------|
| HUD é SOI? | ✅ Sim | ✅ Permitido |
| TD-box movível? | ✅ Sim (DTOS) | ❓ Não está claro |
| Via HUD cursor? | ✅ Sim | ❓ Não mencionado |
| Via FCR/TGP? | Não aplicável | ✅ Sim (confirma) |

### B. "Main Purposes" vs "Only Purposes"

Manual cita: **"two MAIN purposes"** para HUD SOI
- Creating HUD mark points
- Employing missiles in VIS mode

❓ Isto **exclui** A-G PRE, ou apenas lista os principais?

---

## CITAÇÕES-CHAVE PARA INVESTIGAÇÃO ADICIONAL

1. **Seção 4.2.2.2.1.2.3 - VIP (Visual Initial Point)**
   - Menciona "Slew corrections may be zeroed via cursor zero"
   - Mas é para VIP, não PRE genérico

2. **Seção 4.2.4.1.7.1 - Maverick PRE**
   - "AGM-65 LOS slaved to the FCR or TGP LOS"
   - Não menciona HUD como opção de slew

3. **Training Manual - Mission 10 (CCRP)**
   - Descreve CCRP com FCR/TGP como SOI
   - Não há procedimento com HUD como SOI em CCRP

---

## QUESTÕES PARA APROFUNDAMENTO

1. ❓ A seção 2.1.7.5.4 (HUD cursor ajustável) aplica-se APENAS a VIS ou também a PRE?

2. ❓ Quando manual diz "The SOI cannot be designated in MARK OFLY...within PRE state", isto significa:
   - (a) Você não pode ter HUD como SOI em nenhum PRE mode?
   - (b) Você não pode designar EM MARK OFLY ou SP, mas PODE em CCRP/LADD?

3. ❓ A "restrição explícita" em 2.1.1.2.3 refere-se a **designação do SOI** ou **movimento do SOI**?

4. ❓ Se HUD SOI está permitido em A-G PRE, por que o Training Manual (Mission 10) NÃO demonstra isto?

5. ❓ Qual é a diferença funcional entre:
   - HUD como SOI com HUD cursor control (proposto)
   - FCR/TGP como SOI com MFD cursor control (confirmado)

---

## RECOMENDAÇÃO PARA REVISÃO

### Necessário:
1. ✅ Procurar por **"HUD cursor"** explicitamente em contexto A-G PRE
2. ✅ Investigar **todo o capítulo 4.2.2.2.1** (CCRP) para menção a HUD
3. ✅ Verificar **Training Manual Mission 10** (CCRP bombs) procedimentos
4. ✅ Procurar por **"HUD slew"** ou **"HUD designate"** em contexto PRE
5. ✅ Investigar comportamento de **MARK OFLY** vs outros PRE submodes

### Secundário:
- Comparar com **DTOS procedures** (VIS) para entender diferença
- Verificar **Maverick/Harpoon specific procedures** no capítulo 4.2.4
- Consultar **SPI Management (4.2.1)** sobre quem pode mover SPI

---

## CONCLUSÃO PROVISÓRIA

**Permitido:** ✅ HUD pode ser SOI em A-G PRE (legalmente)

**Funcional:** ❓ Não está claramente estabelecido se o TD-box pode ser ajustado via HUD cursor em A-G PRE

**Mais Provável:** ⚠️ TD-box em A-G PRE é ajustável via **FCR/TGP cursor** (MFD), NÃO via HUD cursor (embora HUD seja SOI)

---

## NOTAS IMPORTANTES

- Usar **cursor control** (CURSOR ENABLE switch) não é o mesmo que "HUD cursor control"
- **SOI (Sensor of Interest)** é um conceito diferente de "quem pode mover o cursor"
- **MFD pages (FCR/TGP)** podem ser SOI para fins de **cursor slew** mesmo que HUD seja SOI para **display purposes**

---

**Marcado para:** Revisão técnica completa com foco em:
- Capítulo 4.2.2.2.1 (CCRP) - relação entre HUD SOI e TD-box
- Training Manual Missions 10-15 - procedimentos reais
- Seção 4.2.4.1.7 (Maverick PRE) - comportamento específico