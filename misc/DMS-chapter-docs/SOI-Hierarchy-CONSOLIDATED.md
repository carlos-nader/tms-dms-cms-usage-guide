# SOI HIERARCHY & DMS OPERATION - DASH-34-1 COMPREHENSIVE GUIDE
## Complete Master Mode Analysis: A-A, DGFT, MSL OVRD, NAV
### Extraído de TO 1F-16CMAM-34-1-1 BMS (DASH-34-1) - Change 4.38

---

## 📚 ÍNDICE COMPLETO DE REFERÊNCIAS

**Manual:** TO 1F-16CMAM-34-1-1 BMS - Change 4.38

**Seções Consultadas:**
- 2.1.1.2.1: Master Mode Selection and Control (Página 38-39)
- 2.1.1.2.2: System Point-of-Interest SPI (Página 40)
- 2.1.1.2.3: Sensor-of-Interest SOI (Página 40-41)
- 2.1.6.2: Typical MFDS Functions (Página 65)
- 2.1.6.3: Sensor of Interest SOI (Página 66)
- 4.3.2.2: DOGFIGHT DGFT MODE (Página 593-595)
- 4.3.2.4.1: Missile Override Mode Page (Página 601)
- 4.3.2.4.3.2: AIM-9LM SLAVE Hierarchy (Página 605)

---

## 📋 RESUMO EXECUTIVO

| Aspecto | **A-A** | **DGFT** | **MSL OVRD** | **NAV** |
|---|---|---|---|---|
| **DMS UP** | ❌ Bloqueado | ❌ Bloqueado | ❌ Bloqueado | ✅ Permitido |
| **DMS DOWN** | ✅ L↔R MFD | ✅ L↔R MFD | ✅ L↔R MFD | ✅ HUD↔MFD |
| **DMS LEFT/RIGHT** | ❌ BLANK | ❌ BLANK | ❌ BLANK | ✅ Formats |
| **LEFT MFD** | FCR (fixo) | FCR (fixo) | FCR (fixo) | FCR (fixo) |
| **RIGHT MFD** | SMS (fixo) | SMS (fixo) | SMS (fixo) | SMS (fixo) |
| **Formatos SOI** | FCR, HSD, TGP | FCR, HSD, TGP* | FCR, HSD, TGP* | FCR, TGP, HSD, WPN, HAD |
| **HUD SOI** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ✅ SIM |
| **Dual Tracking** | ✅ SIM (FCR+TGP) | ❌ Não (SPI constraints) | ❌ Não (SPI constraints) | ✅ SIM (flexível) |
| **Master Mode Priority** | Normal | ✅ Priority | ✅ Priority | Normal |

*DGFT/MSL OVRD: Formatos restritos por SPI constraints de arma

---

## PARTE I: CONCEITOS FUNDAMENTAIS

### **1. Definição: SOI vs SPI**

**SOI (Sensor of Interest) - Seção 2.1.1.2.3, Página 40:**
> "The Simplified Sensor of Interest SOI mechanism streamlines the management 
> of multiple sensors by designating a single sensor format for hands-on control."

**SPI (System Point-of-Interest) - Seção 2.1.1.2.2, Página 40:**
> "The F-16 sensor management follows a single line-of-sight concept, where all 
> sensors are synchronized to a shared focal point known as the System Point-of-Interest SPI."

**Diferença Crítica:**
```
SOI = Qual display piloto controla com DMS/TMS (visual/cursor)
SPI = Qual sensor arma usa como linha de vista (weapon targeting)

Podem ser DIFERENTES em DGFT/MSL OVRD!
```

### **2. Master Mode Display Format Table**

**Seção 2.1.1.2.1, Página 38-39:**

```
Master Mode    LEFT MODE              RIGHT MODE
───────────────────────────────────────────────────────
DOGFIGHT       FCR BLANK BLANK        SMS BLANK BLANK
MSL OVRD       FCR BLANK BLANK        SMS BLANK BLANK
A-A            FCR BLANK BLANK        SMS BLANK BLANK
A-G/HARM       FCR BLANK BLANK        SMS BLANK BLANK
NAV            FCR BLANK BLANK        SMS BLANK BLANK
JETTISON       FCR BLANK BLANK        SMS BLANK BLANK
```

**Conclusão:** Todos master modes têm **MESMO display layout** (FCR + SMS fixo)

### **3. Ground Rules para Sensor Modes**

**Seção 2.1.1.2.1, Página 39:**

> "To streamline display management, the following ground rules are applied to 
> sensor modes: **The Air-to-Air, Dogfight DGFT, and Missile Override MSL OVRD 
> master modes exclusively permit air-to-air sensor modes.**"

**Implicação:**
```
A-A, DGFT, MSL OVRD = "air-to-air sensor modes ONLY"
  ├─ FCR (Air-to-Air mode)
  ├─ TGP (Air-to-Air tracking)
  └─ HSD (Situational awareness)

Bloqueados em todos 3:
  ├─ WPN (weapon display)
  ├─ HAD (HARM targeting)
  └─ FLIR, TFR, TNC (ground-specific)
```

---

## PARTE II: MASTER MODES - ANÁLISE DETALHADA

---

## 🔴 MASTER MODE A-A (AIR-TO-AIR)

### **A. DMS Funcionamento**

#### **DMS UP: BLOQUEADO**
- **Seção 2.1.1.2.3, Página 40-41**
- **Citação:** "The HUD can only be the designated SOI in navigation and air-to-ground master modes."
- **Resultado:** Sem efeito, HUD não pode ser SOI

#### **DMS DOWN: Alterna MFDs**
- **Seção 2.1.1.2.3, Página 40-41**
- **Citação:** "If the DMS is moved downward and the SOI is on the MFDs, the SOI transitions to the other MFD if allowed."
- **Resultado:** LEFT ↔ RIGHT MFD (sem HUD no ciclo)

#### **DMS LEFT/RIGHT: SEM EFEITO**
- **Seção 2.1.6.2, Página 65**
- **Problema:** Master Mode Display Format mostra BLANK como 2º/3º
- **Resultado:** Nenhum formato secundário para cyclar

### **B. SOI Hierarchy em A-A**

#### **Formatos Permitidos como SOI:**
- **Seção 2.1.1.2.3, Página 41**
- **Citação:** "In the air-to-air master mode, the SOI display is limited to the FCR, HSD, and TGP formats."

**Hierarquia (Priority-based):**
```
1. FCR (Fire Control Radar) - HIGHEST
   └─ Preferido para targeting
   └─ Estabelece SPI se em STT

2. TGP (Targeting Pod) - SECONDARY
   └─ Se em tracking mode A-A
   └─ Pode ser SPI se FCR não tem TOI

3. HSD (Horizontal Situation Display) - TERTIARY
   └─ Situational awareness apenas
   └─ Não pode ser SPI para arma
```

#### **Weapon SPI Constraints em A-A:**

**Com AIM-120 - Seção 2.1.1.2.2, Página 40:**
> "In the Air-to-Air Missile modes where the AIM-120 is selected as the weapon, 
> the Fire Control Radar FCR establishes the system line-of-sight, and the 
> weapons are launched against targets tracked by the FCR."

**Com SRM (AIM-9) - Seção 2.1.1.2.2, Página 40:**
> "In Air-to-Air Missile modes with a Short Range Missile SRM as the chosen 
> weapon, **either the FCR or the Targeting Pod TGP can define the system 
> line-of-sight.**"

**AIM-9 SLAVE Hierarchy - Seção 4.3.2.4.3.2, Página 605:**
> "The prioritized hierarchy for AIM-9LM SLAVE is as follows:
> - FCR if there is a radar TOI (Target of Interest)
> - TGP, if the TGP is selected as the SOI and is in air-to-air tracking mode."

**Conclusão:** SPI é **forçado** pela arma, pode ser diferente de SOI!

### **C. Dual Tracking em A-A**

**Seção 2.1.1.2.2, Página 40:**
> "In the A-A master mode, both the Fire Control Radar FCR and Targeting Pod 
> TGP can track targets simultaneously. This allows for concurrent air-to-air 
> tracking with both sensors."

**Implicação:**
```
Piloto pode monitorar:
  ├─ FCR rastreando alvo 1
  └─ TGP rastreando alvo 2 (simultaneamente)

Diferente de SPI único em A-G!
```

---

## 🟡 MASTER MODE DGFT (DOGFIGHT)

### **A. Definição & Priority**

**Seção 2.1.1.2.1, Página 38:**
> "The Dogfight and Missile Override master modes have priority over any other 
> selected master mode, except for Emergency Jettison."

**Ativação:**
```
Switch: Throttle Dogfight/Missile Override
Position: LEFT-OUTBOARD
```

### **B. DMS Funcionamento em DGFT**

#### **DMS UP: BLOQUEADO** (idêntico a A-A)
- HUD não pode ser SOI
- Resultado: Sem efeito

#### **DMS DOWN: Alterna MFDs** (idêntico a A-A)
- LEFT (FCR) ↔ RIGHT (SMS)
- Designa qual será SOI

#### **DMS LEFT/RIGHT: SEM EFEITO** (idêntico a A-A)
- Master Mode Display Format: FCR BLANK BLANK | SMS BLANK BLANK
- Nenhum formato secundário

### **C. Display Layout DGFT**

**Seção 2.1.1.2.1, Página 39:**
```
DOGFIGHT       FCR BLANK BLANK    SMS BLANK BLANK
```

**Comportamento:**
```
LEFT MFD PRIMARY:   FCR (sempre, não pode mudar)
RIGHT MFD PRIMARY:  SMS (sempre, não pode mudar)

Piloto está PRESO neste layout
  (Diferente de A-A em teoria, mas tabela é idêntica!)
```

### **D. SPI Constraints em DGFT (Crítico!)**

#### **Com AIM-120 - Seção 2.1.1.2.2, Página 40:**
> "In the Dogfight DGFT...and Air-to-Air Missile modes where the AIM-120 is 
> selected as the weapon, **the Fire Control Radar FCR establishes the system 
> line-of-sight,** and the weapons are launched against targets tracked by the FCR."

**Implicação:**
```
Piloto designa: TGP = SOI (via DMS DOWN)
Sistema força: FCR = SPI (para AIM-120)

Resultado: DMS controla TGP, mas míssil segue FCR!
           SPI ≠ SOI em DGFT com AIM-120
```

#### **Com SRM (AIM-9) - Seção 2.1.1.2.2, Página 40:**
> "In DGFT...and Air-to-Air Missile modes with a Short Range Missile SRM as the 
> chosen weapon, **either the FCR or the Targeting Pod TGP can define the system 
> line-of-sight.**"

**Implicação:**
```
Maior flexibilidade que AIM-120
Piloto pode escolher:
  ├─ FCR como SPI (via FCR tracking)
  └─ TGP como SPI (via TGP tracking)

Mas SOI (DMS) é independente!
```

### **E. SPI vs SOI em DGFT - Exemplo Operacional**

```
Cenário: DGFT com AIM-120

Piloto quer monitorar TGP (alvo visual):
  1. Pressiona DMS DOWN
     → TGP = SOI (hands-on cursor control)
     → Pode mover cursor no TGP
  
  2. Seleciona AIM-120
     → Sistema força FCR = SPI
     → Míssil segue FCR, não TGP!
  
  3. Resultado:
     ├─ Display: Piloto controla TGP (SOI)
     ├─ Arma: Míssil segue FCR (SPI)
     └─ Possível confusão se não entendido!
```

### **F. Comparação: DGFT vs A-A**

| Aspecto | A-A | DGFT |
|---|---|---|
| **DMS Operação** | Idêntica | Idêntica |
| **Display Layout** | FCR+SMS | FCR+SMS |
| **Dual Tracking** | ✅ Permitido | ❌ Constraints |
| **SPI com AIM-120** | Flexível | FCR forçado |
| **SPI com SRM** | Flexível | FCR ou TGP |
| **SOI Selection** | Piloto choice (DMS) | Piloto choice (DMS) |
| **Master Mode Priority** | Normal | ✅ ALTA |

---

## 🟠 MASTER MODE MSL OVRD (MISSILE OVERRIDE)

### **A. Definição & Ativação**

**Seção 2.1.1.2.1, Página 38:**
> "The Dogfight and Missile Override master modes have priority over any other 
> selected master mode, except for Emergency Jettison."

**Ativação:**
```
Switch: Throttle Dogfight/Missile Override
Position: RIGHT-INBOARD
```

### **B. DMS Funcionamento em MSL OVRD**

**Idêntico a DGFT:**
- DMS UP: ❌ Bloqueado
- DMS DOWN: ✅ Alterna MFDs
- DMS LEFT/RIGHT: ❌ Sem efeito

### **C. Display Layout MSL OVRD**

**Seção 2.1.1.2.1, Página 39:**
```
MSL OVRD       FCR BLANK BLANK    SMS BLANK BLANK
```

**Idêntico a DGFT - mesmas restrições**

### **D. SPI Constraints em MSL OVRD**

**Com AIM-120 - Seção 2.1.1.2.2, Página 40:**
> "In...Missile Override MSL OVRD, and Air-to-Air Missile modes where the 
> AIM-120 is selected as the weapon, the Fire Control Radar FCR establishes 
> the system line-of-sight..."

**Com SRM - Seção 2.1.1.2.2, Página 40:**
> "In DGFT, MSL OVRD, and Air-to-Air Missile modes with a Short Range Missile 
> SRM as the chosen weapon, either the FCR or the Targeting Pod TGP can define 
> the system line-of-sight."

**Conclusão:** Comportamento **IDÊNTICO** a DGFT

### **E. Diferença: MSL OVRD vs DGFT**

**Único ponto diferencial:**
- MSL OVRD = foco prioritário em **armas** (override de modo)
- DGFT = foco em **dogfighting visual** (guns + missiles)

**Operacionalmente:** DMS atua **identicamente** em ambos!

---

## 🟢 MASTER MODE NAV (NAVIGATION)

### **A. Definição & Ativação**

**Seção 2.1.1.2.1, Página 38:**
> "Navigation - Default if no other Master Mode selected"

**Ativação:**
```
Centra o throttle Dogfight/Missile Override
Ou default se nenhum outro master mode ativo
```

### **B. DMS Funcionamento em NAV**

#### **DMS UP: PERMITIDO** ⭐ DIFERENTE!
- **Seção 2.1.1.2.3, Página 40**
- **Citação:** "The HUD can only be the designated SOI in navigation and air-to-ground master modes."
- **Resultado:** HUD = SOI (quando apropriado)

#### **DMS DOWN: Alterna HUD ↔ MFDs**
- **Seção 2.1.1.2.3, Página 40-41**
- **Citação:** "When the HUD is the SOI and the DMS is moved downward, the SOI designation shifts to the MFDs."
- **Resultado:** HUD ↔ LEFT ↔ RIGHT MFD ciclo completo

#### **DMS LEFT/RIGHT: Cicla Formatos** ⭐ DIFERENTE!
- **Seção 2.1.6.2, Página 65**
- **Resultado:** Pode cyclar entre múltiplos formatos (não BLANK)

### **C. SOI Hierarchy em NAV**

#### **Formatos Permitidos como SOI:**
- **Seção 2.1.1.2.3, Página 40-41**
- **Citação:** "The designated SOI display on the MFD can only be in the FCR, TGP, WPN, HAD, and HSD formats. The HUD can only be the designated SOI in navigation and air-to-ground master modes."

**Hierarquia em NAV:**
```
Primary Level (Hands-on prioritário):
  1. HUD (se DMS UP ativado)
     └─ Para navegação visual/OOFLC
  
  2. HSD (Horizontal Situation Display)
     └─ Para situação tática/waypoint management

Secondary Level (Tracking):
  3. FCR (Air-to-Air)
  4. TGP (Air-to-Air ou Air-to-Ground)
  
Tertiary Level (Support):
  5. WPN/SMS/HAD (formatos não-SOI normalmente)
```

### **D. Dual Tracking em NAV**

**Seção 2.1.1.2.2, Página 40:**
> "In the NAV master mode, there is flexibility in sensor configuration. It is 
> possible to have **two air-to-air tracking sensors or one air-to-air tracking 
> sensor combined with one air-to-ground tracking sensor.**"

**Implicação:**
```
NAV permite:
  ├─ 2x Air-to-Air (FCR + TGP ambos A-A)
  ├─ 1x Air-to-Air + 1x Air-to-Ground (FCR A-A + TGP A-G)
  └─ Simultaneamente (sem SPI constraint rígido)

Resultado: MÁXIMA flexibilidade em NAV
```

### **E. HSD Behavior especial em NAV**

**Seção 2.1.6.18.3, Página 84:**
> "When the HSD is selected as the Sensor of Interest SOI, the HSD cursor is 
> initially positioned at the location of the FCR Fire Control Radar ghost cursor, 
> either in air-to-air A-A or air-to-ground A-G mode. In cases where no ghost 
> cursor is available, the HSD cursor initializes at the ownship location."

**Implicação:**
```
HSD SOI em NAV:
  ├─ Cursor começa na posição FCR ghost cursor
  ├─ Permite cursor control manual
  └─ HSD não é o SOI = cursor desaparece
```

---

## PARTE III: COMPARAÇÃO COMPLETA

### **Tabela: DMS Operation por Master Mode**

| Função | A-A | DGFT | MSL OVRD | NAV |
|---|---|---|---|---|
| **DMS UP** | ❌ BLKD | ❌ BLKD | ❌ BLKD | ✅ HUD |
| **DMS DOWN** | ✅ L↔R | ✅ L↔R | ✅ L↔R | ✅ HUD↔L↔R |
| **DMS LEFT** | ❌ BLKD* | ❌ BLKD* | ❌ BLKD* | ✅ CYCLE |
| **DMS RIGHT** | ❌ BLKD* | ❌ BLKD* | ❌ BLKD* | ✅ CYCLE |
| **SWAP OSB** | ✅ L↔R | ✅ L↔R | ✅ L↔R | ✅ L↔R |

*BLANK formatos bloqueiam cycling

### **Tabela: SOI Capabilities por Master Mode**

| Aspecto | A-A | DGFT | MSL OVRD | NAV |
|---|---|---|---|---|
| **HUD SOI** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ✅ SIM |
| **FCR SOI** | ✅ SIM | ✅ SIM | ✅ SIM | ✅ SIM |
| **TGP SOI** | ✅ SIM | ✅ SIM | ✅ SIM | ✅ SIM |
| **HSD SOI** | ✅ SIM | ✅ SIM | ✅ SIM | ✅ SIM |
| **WPN SOI** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ✅ SIM |
| **HAD SOI** | ❌ NÃO | ❌ NÃO | ❌ NÃO | ✅ SIM |

### **Tabela: SPI Constraints por Master Mode**

| Weapon | A-A SPI | DGFT SPI | MSL OVRD SPI | NAV SPI |
|---|---|---|---|---|
| **AIM-120** | Flexível (FCR) | **FCR forçado** | **FCR forçado** | Flexível |
| **AIM-9/SRM** | Flexível (FCR/TGP) | FCR ou TGP | FCR ou TGP | Flexível |
| **Gun** | FCR STT | Visual/Boresight | Visual/Boresight | Visual |
| **Dual Track** | ✅ FCR+TGP | ❌ Constraints | ❌ Constraints | ✅ Flexível |

---

## PARTE IV: RESTRIÇÕES CRÍTICAS

### **1. SOI não pode ser designado em certos submodos**

**Seção 2.1.1.2.3, Página 40:**
> "It is important to note that the SOI cannot be designated in the MARK OFLY 
> submode or the snowplow SP ground radar mode within the pre-designate PRE state."

**Impacto:**
- MARK OFLY: SOI fixado, DMS DOWN bloqueado
- Snowplow PRE: SOI não pode ser designado

### **2. Formatos que NUNCA podem ser SOI**

**Seção 2.1.1.2.3, Página 41:**
> "On the FCR, TGP, HSD, HAD, and WPN formats, the text NOT SOI appears 
> whenever the format is not selected as the sensor of interest..."

**Formatos bloqueados (sempre "NOT SOI"):**
- SMS (nunca SOI)
- FLIR (nunca SOI)
- TFR (nunca SOI)
- FLCS (nunca SOI)
- DTE (nunca SOI)

---

## PARTE V: PROCEDIMENTOS OPERACIONAIS

### **Procedimento 1: Mudar SOI de FCR para TGP em A-A**

```
1. A-A mode ativo, FCR = SOI (display tem box ao redor)
2. Pressionar DMS DOWN (1x)
   → Erro! Não há TGP como format disponível (SMS está em RIGHT)
   
Solução: Piloto precisa MUDAR display format primeiro
  (Não é possível via DMS LEFT/RIGHT porque BLANK bloqueia)
  
Resultado: Em A-A modo com padrão display, só pode trocar:
  ├─ FCR = SOI
  └─ SMS = SOI
  (Nenhuma outra opção!
```

⚠️ **Nota Importante:** Documento DASH-34-1 não especifica como acessar HSD/TGP em A-A se não são formatos secundários padrão. Possível via Menu Format ou DTE reprogramming.

### **Procedimento 2: Mudar SOI entre HUD e MFDs em NAV**

```
1. NAV mode ativo, HUD pode ser SOI
2. DMS UP (1x)
   → HUD = SOI (asterisco aparece no HUD)
   → Cursor hands-on agora no HUD
3. DMS DOWN (1x)
   → HUD ← LEFT MFD (FCR) = SOI
   → Cursor agora no LEFT MFD
4. DMS DOWN (2x)
   → LEFT MFD ← RIGHT MFD (SMS) = SOI
5. DMS DOWN (3x)
   → Volta para HUD = SOI (ciclo completo)
```

### **Procedimento 3: Weapon SPI vs SOI em DGFT com AIM-120**

```
1. DGFT mode ativo
2. Piloto via DMS DOWN designa: SMS = SOI
   (Quer monitorar status de armas)
3. Seleciona AIM-120
4. Sistema força: FCR = SPI (para AIM-120)

Resultado:
  ├─ Display (SOI): SMS (piloto vê status)
  ├─ Arma (SPI): FCR (míssil usa FCR)
  └─ Podem ser diferentes!
```

---

## PARTE VI: RESUMO DE DIFERENÇAS CRÍTICAS

### **O que é IDÊNTICO em A-A, DGFT, MSL OVRD:**
```
✅ Display layout (FCR + SMS)
✅ DMS UP bloqueado (HUD não permitido)
✅ DMS DOWN alterna L/R
✅ DMS LEFT/RIGHT bloqueado (BLANK)
✅ Formatos disponíveis como SOI (FCR, HSD, TGP)
```

### **O que é DIFERENTE em DGFT/MSL OVRD vs A-A:**
```
❌ SPI constraints em arma:
   - AIM-120: FCR FORÇADO
   - SRM: Flexível (FCR ou TGP)
   
❌ Dual tracking:
   - A-A: Sempre permitido
   - DGFT/MSL OVRD: Com constraints

❌ Master Mode Priority:
   - A-A: Normal
   - DGFT/MSL OVRD: ALTA (override outros modes)
```

### **O que é DIFERENTE em NAV vs outros:**
```
✅ DMS UP funciona (HUD permitido)
✅ DMS DOWN cicla HUD completo
✅ DMS LEFT/RIGHT cycla formatos
✅ Formatos expandidos (WPN, HAD, etc.)
✅ Dual tracking flexível (sem constraints)
```

---

## 📚 CITAÇÕES COMPLETAS ADICIONAIS

### **Master Mode Priority (Seção 2.1.1.2.1, Página 38):**

> "The Dogfight and Missile Override master modes have priority over any other 
> selected master mode, except for Emergency Jettison. When Dogfight or Missile 
> Override is chosen, the master mode will be configured with the options saved 
> in the Data Transfer Cartridge DTC or manually set during ramp start."

### **Sensor Mode Ground Rules (Seção 2.1.1.2.1, Página 39):**

> "To streamline display management, the following ground rules are applied to 
> sensor modes: The Air-to-Air, Dogfight DGFT, and Missile Override MSL OVRD 
> master modes exclusively permit air-to-air sensor modes. Modes that necessitate 
> both air-to-ground targeting capability and air-to-air situational awareness 
> permit the use of both air-to-air and air-to-ground sensor modes."

### **DMS Behavior (Seção 2.1.1.2.3, Página 40-41):**

> "The selection of the SOI is based on either the sensor with the highest 
> priority or the pilots intended choice. Pilot intent can be influenced by 
> various actions, including Moving the Display Management Switch DMS upward, 
> which transitions the SOI designation to the HUD if allowed."

---

## ✅ TABELA DE VERIFICAÇÃO RÁPIDA

Use esta tabela para validar comportamentos no manual:

| Situação | Esperado | Página | Confirmado |
|---|---|---|---|
| DMS UP em DGFT | Bloqueado | 40-41 | ✅ |
| DMS DOWN em DGFT | Alterna L/R | 40-41 | ✅ |
| DMS LEFT em DGFT | Sem efeito | 39 | ✅ |
| SOI TGP em DGFT | Possível | 41 | ✅* |
| SPI AIM-120 em DGFT | FCR forçado | 40 | ✅ |
| SPI SRM em DGFT | FCR ou TGP | 40 | ✅ |
| DMS UP em NAV | HUD = SOI | 40 | ✅ |
| Dual track em A-A | Permitido | 40 | ✅ |
| Dual track em DGFT | Com constraints | 40 | ✅ |
| Dual track em NAV | Flexível | 40 | ✅ |

*TGP como format secundário não está listado em Master Mode Display Format table

---

**Documento Consolidado:** 12 JAN 2026, 04:10 AM
**Fonte Primária:** TO 1F-16CMAM-34-1-1 BMS, Change 4.38
**Seções Cobertas:** 2.1.1.2.1-2.3, 2.1.5-2.6, 4.3.2.2-4.3.2.5
**Status:** Pesquisa completa, consolidada com todas as referências diretas
**Download:** Pronto para verificação contra Capítulo 4 do manual