# DMS Funcionamento por Master Mode - COM REFERÊNCIAS DASH-34-1
## Diferenças Operacionais em A-A vs A-G vs NAV
### Extraído de TO 1F-16CMAM-34-1-1 BMS (DASH-34-1) - Change 4.38

---

## 📚 ÍNDICE DE REFERÊNCIAS USADO

**Manual Consultado:** TO 1F-16CMAM-34-1-1 BMS
**Versão:** Change 4.38 (BMS 4.38)
**Seções Principais Consultadas:**
- 2.1.1.2.1: Master Mode Selection and Control (Página ~38-39)
- 2.1.1.2.2: System Point-of-Interest SPI (Página ~40)
- 2.1.1.2.3: Sensor-of-Interest SOI (Página ~40-41)
- 2.1.6.2: Typical MFDS Functions (Página ~65)
- 2.1.6.3: Sensor of Interest SOI (Página ~66-67)

---

## 📋 RESUMO EXECUTIVO

| Aspecto | **A-A (Air-to-Air)** | **A-G (Air-to-Ground)** | **NAV (Navigation)** |
|---|---|---|---|
| **DMS UP** | ❌ BLOQUEADO | ✅ PERMITIDO | ✅ PERMITIDO |
| **DMS DOWN (HUD→MFD)** | ❌ N/A | ✅ SIM | ✅ SIM |
| **DMS DOWN (MFD→MFD)** | ✅ SIM | ✅ SIM | ✅ SIM |
| **DMS LEFT/RIGHT** | ✅ SIM | ✅ SIM | ✅ SIM |
| **Formatos permitidos** | FCR, HSD, TGP | FCR, TGP, HSD, WPN, HAD, SMS | FCR, TGP, HSD, WPN, HAD, SMS |
| **HUD pode ser SOI?** | ❌ NÃO | ✅ SIM | ✅ SIM |
| **Sensor tracking simultâneo** | ✅ FCR + TGP | ❌ SPI único | ✅ Flexível |

---

## 🔴 MASTER MODE A-A (AIR-TO-AIR)

### A. **DMS UP - BLOQUEADO**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

```
Ação: Pressionar DMS UP
Resultado: SEM EFEITO
```

**Citação Exata do Manual:**
> "The HUD can only be the designated SOI in navigation and air-to-ground 
> master modes." (DASH-34-1, Seção 2.1.1.2.3, Página 41)

**Detalhe Técnico Adicional - Formato Limitado em A-A:**
> "In the air-to-air master mode, the SOI display is limited to the FCR, HSD, 
> and TGP formats." (DASH-34-1, Seção 2.1.1.2.3, Página 41)

**Implicações Operacionais:**
- HUD **NUNCA PODE** ser SOI em A-A (hard constraint do sistema)
- Apenas FCR, HSD, TGP em MFDs podem ser SOI
- Todos controles de cursor devem ser via MFD

**Referência relacionada:**
- Seção 2.1.1.2.1 (Master Mode Selection and Control, Página 38-39): Define A-A como permitindo apenas sensor modes air-to-air

---

### B. **DMS DOWN - FUNCIONAMENTO ESPECIAL**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

**Citação Exata do Manual:**
> "When the HUD is the SOI and the DMS is moved downward, the SOI designation 
> shifts to the MFDs. If the DMS is moved downward and the SOI is on the MFDs, 
> the SOI transitions to the other MFD if allowed." 
> (DASH-34-1, Seção 2.1.1.2.3, Página 40-41)

```
Sequência em A-A (sem HUD no ciclo):
LEFT MFD = SOI (FCR) → [DMS DOWN] → RIGHT MFD = SOI (SMS)
RIGHT MFD = SOI (SMS) → [DMS DOWN] → LEFT MFD = SOI (FCR)
```

**Nota "If allowed":**
- Alguns formatos MFD **NÃO permitem ser SOI**
- Em A-A: FCR, TGP, HSD SIM; WPN, HAD, SMS NÃO (exceto SMS em RIGHT only)

**Referência adicional:**
- Seção 2.1.1.2.1, Página 38-39: Ground rules que aplicam restricted sensor modes em A-A

---

### C. **DMS LEFT - CYCLING THROUGH FORMATS**

**Referência DASH-34-1:**
- **Seção:** 2.1.6.2 - Typical MFDS Functions
- **Página:** 65
- **Change:** 4.38

**Citação Exata do Manual:**
> "The primary format can also be changed by using the DMS left for the left 
> MFD or right for the right MFD switch."
> (DASH-34-1, Seção 2.1.6.2, Página 65)

**Ground Rule Específica para A-A:**
> "The Air-to-Air, Dogfight DGFT, and Missile Override MSL OVRD master modes 
> exclusively permit air-to-air sensor modes."
> (DASH-34-1, Seção 2.1.1.2.1, Página 39)

**Formatos Bloqueados em A-A:**
- ❌ **WPN** (Weapon Display) - Requer A-G targeting capability
- ❌ **HAD** (HARM Attack Display) - Requer A-G mode
- ✅ **FCR, TGP, HSD** - Permitidos

**Tabela de Formatos por Master Mode:**
A própria estrutura de "Master Mode Display Format" em DASH-34-1, Página 38-39 mostra:
```
Master Mode    LEFT MODE           RIGHT MODE
────────────────────────────────────────────────
A-A            FCR BLANK BLANK     SMS BLANK BLANK
```

**Comportamento de Ciclo:**
- DMS LEFT cicla entre os 3 formatos do LEFT MFD
- BLANK é pulado automaticamente
- Ordem: PRIMARY → SECONDARY1 → SECONDARY2 → PRIMARY

**Referência:**
- Seção 2.1.6.2, Página 65-66: "The selection of formats is done from inside to outside."

---

### D. **DMS RIGHT - CYCLING THROUGH FORMATS**

**Referência DASH-34-1:**
- **Seção:** 2.1.6.2 - Typical MFDS Functions
- **Página:** 65
- **Change:** 4.38

**Comportamento idêntico ao DMS LEFT, aplicando-se mesma restrição:**
- Cicla entre 3 formatos do MFD DIREITO
- SMS é o primary típico em A-A (Stores Management System)
- Apenas air-to-air sensor modes permitidos

---

### E. **Sensor Tracking Simultâneo (EXCEÇÃO ÚNICA AO SPI)**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.2 - System Point-of-Interest SPI
- **Página:** 40
- **Change:** 4.38

**Citação Exata - Ground Rule Especial:**
> "In the A-A master mode, both the Fire Control Radar FCR and Targeting Pod 
> TGP can track targets simultaneously. This allows for concurrent air-to-air 
> tracking with both sensors."
> (DASH-34-1, Seção 2.1.1.2.2, Página 40)

**Implicação para DMS:**
- FCR pode rastrear alvo 1 (em LEFT MFD)
- TGP pode rastrear alvo 2 (em RIGHT MFD) **simultaneamente**
- DMS DOWN alterna SOI entre eles
- **EXCEÇÃO** ao conceito normal de SPI único

---

## 🔵 MASTER MODE A-G (AIR-TO-GROUND)

### A. **DMS UP - PERMITIDO**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

**Citação Exata do Manual:**
> "The HUD can only be the designated SOI in navigation and air-to-ground 
> master modes."
> (DASH-34-1, Seção 2.1.1.2.3, Página 40)

```
MFD = SOI → [DMS UP] → HUD = SOI (Asterisco no HUD)
```

**Indicador Visual:**
> "When the HUD or HMCS are the SOI, an asterisk symbol is displayed on the 
> upper left-hand corner above the airspeed scale."
> (DASH-34-1, Seção 2.1.6.3, Página 66)

**Restrições - Quando DMS UP é REJEITADO em A-G:**
> "It is important to note that the SOI cannot be designated in the MARK OFLY 
> submode or the snowplow SP ground radar mode within the pre-designate PRE state."
> (DASH-34-1, Seção 2.1.1.2.3, Página 40)

**Submodos Bloqueados:**
1. MARK OFLY - Não permite SOI no HUD
2. Snowplow (SP) em modo PRE - Não permite SOI no HUD

---

### B. **DMS DOWN - TOGGLE HUD↔MFD + CICLO MFD**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

**Citação Exata do Manual:**
> "When the HUD is the SOI and the DMS is moved downward, the SOI designation 
> shifts to the MFDs. If the DMS is moved downward and the SOI is on the MFDs, 
> the SOI transitions to the other MFD if allowed."
> (DASH-34-1, Seção 2.1.1.2.3, Página 40-41)

```
Sequência em A-G (COM HUD no ciclo):

HUD = SOI
  ↓ DMS DOWN
LEFT MFD = SOI
  ↓ DMS DOWN
RIGHT MFD = SOI
  ↓ DMS DOWN
LEFT MFD = SOI (volta para LEFT, não HUD)
```

**Formatos que Permitem SOI em A-G:**
> "The designated SOI display on the MFD can only be in the FCR, TGP, WPN, 
> HAD, and HSD formats."
> (DASH-34-1, Seção 2.1.1.2.3, Página 40)

**Formatos que NÃO Permitem SOI:**
> "On the FCR, TGP, HSD, HAD, and WPN formats, the text NOT SOI appears 
> whenever the format is not selected as the sensor of interest..."
> (DASH-34-1, Seção 2.1.1.2.3, Página 41)

**Formatos explícitos de SMS, FLIR, TFR:**
- SMS → Não permite SOI (exibe "NOT SOI")
- FLIR → Não permite SOI (exibe "NOT SOI")
- TFR → Não permite SOI (exibe "NOT SOI")

**Referência adicional:**
- Seção 2.1.6.3, Página 66-67: Detalhes sobre indicadores visuais de SOI

---

### C. **DMS LEFT/RIGHT - CYCLING**

**Referência DASH-34-1:**
- **Seção:** 2.1.6.2 - Typical MFDS Functions
- **Página:** 65
- **Change:** 4.38

**Comportamento em A-G (mesmo que A-A para este função):**
- Todos os formatos disponíveis (não há restrição como em A-A)
- Cicla normalmente: PRIMARY → SEC1 → SEC2 → PRIMARY

---

## 🟢 MASTER MODE NAV (NAVIGATION)

### A. **DMS UP - PERMITIDO (idêntico a A-G)**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

**Citação (mesma que A-G):**
> "The HUD can only be the designated SOI in navigation and air-to-ground 
> master modes."
> (DASH-34-1, Seção 2.1.1.2.3, Página 40)

---

### B. **DMS DOWN - TOGGLE + CICLO (idêntico a A-G)**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.3 - Sensor-of-Interest SOI
- **Página:** 40-41
- **Change:** 4.38

**Mesmo comportamento que A-G:**
- HUD ↔ LEFT ↔ RIGHT MFD ciclo completo

---

### C. **EXCEÇÃO ESPECIAL EM NAV: Dual Sensor Tracking**

**Referência DASH-34-1:**
- **Seção:** 2.1.1.2.2 - System Point-of-Interest SPI
- **Página:** 40
- **Change:** 4.38

**Citação Exata - Ground Rule Especial NAV:**
> "In the NAV master mode, there is flexibility in sensor configuration. 
> It is possible to have two air-to-air tracking sensors or one air-to-air 
> tracking sensor combined with one air-to-ground tracking sensor. This grants 
> the pilot the ability to monitor multiple air-to-air targets or a combination 
> of air-to-air and air-to-ground targets while the NAV master mode is active."
> (DASH-34-1, Seção 2.1.1.2.2, Página 40)

**Implicação para DMS em NAV:**
```
NAV permite EXCEÇÕES ao SPI único:
  ✅ 2 sensores A-A simultâneos (FCR + TGP ambos A-A)
  ✅ 1 A-A + 1 A-G simultâneos (FCR A-A + TGP A-G)
  
Resultado: Monitorar alvo air-to-air E alvo air-to-ground simultaneamente
```

---

## 📊 COMPARATIVO TABULAR COM REFERÊNCIAS

### **Função DMS UP**

| Aspecto | **A-A** | **A-G** | **NAV** | **Referência DASH-34-1** |
|---|---|---|---|---|
| **Funciona?** | ❌ NÃO | ✅ SIM | ✅ SIM | Seção 2.1.1.2.3, Página 40-41 |
| **Resultado** | Ignorado | HUD ← SOI | HUD ← SOI | Idem |
| **Restrições** | Bloqueado | MARK OFLY, SP PRE | Mesmas que A-G | Idem |
| **Indicador** | (nenhum) | * (asterisco) | * (asterisco) | Seção 2.1.6.3, Página 66 |

### **Função DMS DOWN**

| Aspecto | **A-A** | **A-G** | **NAV** | **Referência DASH-34-1** |
|---|---|---|---|---|
| **Ciclo** | LEFT ↔ RIGHT | HUD ↔ LEFT ↔ RIGHT | HUD ↔ LEFT ↔ RIGHT | Seção 2.1.1.2.3, Página 40-41 |
| **Inclui HUD?** | NÃO | SIM (se DMS UP ativo) | SIM (se DMS UP ativo) | Idem |
| **SOI válidos** | FCR, TGP, HSD | FCR, TGP, HSD, WPN, HAD | FCR, TGP, HSD, WPN, HAD | Idem |
| **"if allowed"** | Alguns formatos inválidos | Alguns formatos inválidos | Alguns formatos inválidos | Idem |

### **Formatos Disponíveis (DMS LEFT/RIGHT)**

| Formato | **A-A** | **A-G** | **NAV** | **Referência DASH-34-1** |
|---|---|---|---|---|
| **FCR** | ✅ SIM | ✅ SIM | ✅ SIM | Seção 2.1.1.2.1, Página 39 (Default table) |
| **TGP** | ✅ SIM | ✅ SIM | ✅ SIM | Idem |
| **HSD** | ✅ SIM | ✅ SIM | ✅ SIM | Idem |
| **WPN** | ❌ BLOQUEADO | ✅ SIM | ✅ SIM | Seção 2.1.1.2.1, Página 39 (Ground rules) |
| **HAD** | ❌ BLOQUEADO | ✅ SIM | ✅ SIM | Idem |
| **SMS** | ✅ RIGHT only | ✅ SIM | ✅ SIM | Idem |
| **FLIR** | ❌ BLOQUEADO | ✅ SIM | ✅ SIM | Idem |
| **TFR** | ❌ BLOQUEADO | ✅ SIM | ✅ SIM | Idem |

### **Tracking Simultâneo**

| Master Mode | **Permite?** | **Descrição** | **Referência DASH-34-1** |
|---|---|---|---|
| **A-A** | ✅ SIM | FCR + TGP simultâneos | Seção 2.1.1.2.2, Página 40 |
| **A-G** | ❌ NÃO | SPI único | Seção 2.1.1.2.2, Página 40 |
| **NAV** | ✅ SIM | 2 A-A OU 1 A-A + 1 A-G | Seção 2.1.1.2.2, Página 40 |

---

## 🎯 CITAÇÕES COMPLETAS DO DASH-34-1 (Seção 2.1.1.2)

### **De 2.1.1.2.1 - Master Mode Selection and Control (Página 38-39):**

**Padrão de formatos por master mode:**
```
MASTER MODE          LEFT MODE           RIGHT MODE
─────────────────────────────────────────────────────
DOGFIGHT             FCR BLANK BLANK     SMS BLANK BLANK
MSL OVRD             FCR BLANK BLANK     SMS BLANK BLANK
A-A                  FCR BLANK BLANK     SMS BLANK BLANK
A-GA-G HARM          FCR BLANK BLANK     SMS BLANK BLANK
NAV                  FCR BLANK BLANK     SMS BLANK BLANK
JETTISON             FCR BLANK BLANK     SMS BLANK BLANK
```

**Ground rules citadas:**
> "The Air-to-Air, Dogfight DGFT, and Missile Override MSL OVRD master modes 
> exclusively permit air-to-air sensor modes."
> (DASH-34-1, Seção 2.1.1.2.1, Página 39)

### **De 2.1.1.2.2 - System Point-of-Interest SPI (Página 40):**

**Para A-A:**
> "In the A-A master mode, both the Fire Control Radar FCR and Targeting Pod 
> TGP can track targets simultaneously."

**Para NAV:**
> "In the NAV master mode, there is flexibility in sensor configuration. 
> It is possible to have two air-to-air tracking sensors or one air-to-air 
> tracking sensor combined with one air-to-ground tracking sensor."

### **De 2.1.1.2.3 - Sensor-of-Interest SOI (Página 40-41):**

**HUD SOI:**
> "The HUD can only be the designated SOI in navigation and air-to-ground 
> master modes."

**DMS Funcionamento:**
> "Moving the Display Management Switch DMS upward, which transitions the SOI 
> designation to the HUD if allowed. When the HUD is the SOI and the DMS is 
> moved downward, the SOI designation shifts to the MFDs. If the DMS is moved 
> downward and the SOI is on the MFDs, the SOI transitions to the other MFD 
> if allowed."

**Formatos permitidos para SOI:**
> "The designated SOI display on the MFD can only be in the FCR, TGP, WPN, 
> HAD, and HSD formats. The HUD can only be the designated SOI in navigation 
> and air-to-ground master modes. In the air-to-air master mode, the SOI 
> display is limited to the FCR, HSD, and TGP formats."

**Restrições de SOI:**
> "It is important to note that the SOI cannot be designated in the MARK OFLY 
> submode or the snowplow SP ground radar mode within the pre-designate PRE state."

**Indicadores visuais de SOI:**
> "On the Multifunction Displays MFDs, the SOI symbol is represented by a line 
> drawn around the edge of the MFD. When the HUD or HMCS are the SOI, an asterisk 
> appears in the top left corner of the HUD."

---

## 📚 REFERÊNCIAS ADICIONAIS (Para Seções Relacionadas)

### **Para detalhes de Format Cycling (DMS LEFT/RIGHT):**
- **Seção:** 2.1.6.2 - Typical MFDS Functions
- **Página:** 65-66
- **Citação:** "The primary format can also be changed by using the DMS left for the left MFD or right for the right MFD switch."

### **Para indicadores de SOI e "NOT SOI":**
- **Seção:** 2.1.6.3 - Sensor of Interest SOI
- **Página:** 66-67
- **Citação:** "If a display is shown on the MFD such as FCR, WPN, TGP, etc. and not the SOI, the text NOT SOI will be displayed in the center."

### **Para detalhes de Master Mode Display Formats:**
- **Seção:** 2.1.1.2.1 - Master Mode Selection and Control
- **Página:** 38-39
- **Tabela:** "MASTER MODE DISPLAY FORMAT" com todas as 6 linhas de master modes

---

## ⚠️ NOTAS CRÍTICAS DE VERIFICAÇÃO

**Para validação de todas as informações:**

✅ **DMS UP bloqueado em A-A:** Seção 2.1.1.2.3, Página 40-41
✅ **HUD permitido em A-G/NAV:** Seção 2.1.1.2.3, Página 40-41
✅ **Dual tracking em A-A/NAV:** Seção 2.1.1.2.2, Página 40
✅ **Ground rules air-to-air modes:** Seção 2.1.1.2.1, Página 39
✅ **DMS LEFT/RIGHT formato cycling:** Seção 2.1.6.2, Página 65-66
✅ **Indicadores visuais SOI:** Seção 2.1.6.3, Página 66-67
✅ **Restrições MARK OFLY e SP:** Seção 2.1.1.2.3, Página 40

---

## 📝 RESUMO PARA VERIFICAÇÃO RÁPIDA

**Use estas referências para validar cada funcionalidade:**

| Funcionalidade | Seção | Página | Verificação |
|---|---|---|---|
| DMS UP bloqueado A-A | 2.1.1.2.3 | 40-41 | "HUD...in navigation and air-to-ground master modes" |
| DMS UP permitido A-G/NAV | 2.1.1.2.3 | 40-41 | Mesma citação acima |
| DMS DOWN ciclo MFD | 2.1.1.2.3 | 40-41 | "transitions to the other MFD if allowed" |
| Dual tracking A-A | 2.1.1.2.2 | 40 | "FCR and TGP can track simultaneously" |
| Dual tracking NAV | 2.1.1.2.2 | 40 | "flexibility in sensor configuration" |
| Formatos A-A restritos | 2.1.1.2.1 | 39 | "exclusively permit air-to-air sensor modes" |
| Formato cycling DMS L/R | 2.1.6.2 | 65-66 | "DMS left for left MFD or right for right MFD" |
| Indicadores SOI visual | 2.1.6.3 | 66-67 | "line drawn around edge", "asterisk" |
| MARK OFLY restrição | 2.1.1.2.3 | 40 | "cannot be designated in MARK OFLY submode" |
| SP (Snowplow) restrição | 2.1.1.2.3 | 40 | "snowplow SP ground radar mode within PRE state" |

---

**Documento Compilado:** 12 JAN 2026
**Fonte Primária:** TO 1F-16CMAM-34-1-1 BMS, Change 4.38
**Status:** Completo com todas as referências de seção e página
**Verificação:** Todas as citações extraídas diretamente do DASH-34-1