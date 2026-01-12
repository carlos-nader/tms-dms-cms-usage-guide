# DMS & DECLUTTER MODE - DASH-34-1 PESQUISA COMPLETA
## Declutter Feature, Functionality e Relacionamento com DMS
### Extraído de TO 1F-16CMAM-34-1-1 BMS (DASH-34-1) - Change 4.38

---

## 📚 REFERÊNCIAS PRINCIPAIS CONSULTADAS

**Manual:** TO 1F-16CMAM-34-1-1 BMS - Change 4.38
**Seções Principais:**
- 2.1.6.2: Typical MFDS Functions (Página 65)
- 2.1.6.3: Sensor of Interest SOI (Página 66)
- 2.3.1.3.1: FCR DCLT Declutter (Página 183)
- 2.3.1.5.1.5: FCR A-A Declutter Select/Deselect (Página 195)
- 2.1.6.18.8.1: HSD Control Page L16 Declutter (Página 89-90)
- 2.1.6.18.7: HSD Expand Mode (Página 86)

---

## 🎯 DEFINIÇÃO CENTRAL - DECLUTTER (DCLT)

### **Seção Referência:**
- **DASH-34-1, Seção 2.1.6.2, Página 65**

**Citação Exata - Capability Statement:**
> "The capabilities of the MFDS encompass the following abilities Select display 
> formats. Swap display formats. **Declutter certain alphanumeric data.** Select 
> various options via either rotaries or menus. Increment-decrement certain data. 
> Enter numerical data via a keyboard..."
> (DASH-34-1, Seção 2.1.6.2, Página 65)

**Conceito:** Declutter é a capacidade de **remover dados alfanuméricos específicos** do display MFD para reduzir visual clutter (confusão visual).

---

## 🔴 FCR DECLUTTER (DCLT) - DETALHES OPERACIONAIS

### **Seção Referência Principal:**
- **DASH-34-1, Seção 2.3.1.3.1, Página 183**
- **DASH-34-1, Seção 2.3.1.5.1.5, Página 195** (OSB 11 Programmable)

### **Citação Exata - Basic Operation (Seção 2.3.1.3.1, Página 183):**

> "A declutter feature is available to remove most of the OSB labels from the 
> selected display. By briefly pressing the DCLT OSB, the MFD highlights the 
> letters DCLT and eliminates the labels associated with the OSBs located on 
> the left, top, and right edges of the MFDs. However, alphanumeric data 
> unrelated to the OSBs such as range scale mnemonic and the gain gauge and 
> the labels at the bottom of the MFD remain visible. To disable the declutter 
> feature, press the DCLT OSB again within 1 second."
> (DASH-34-1, Seção 2.3.1.3.1, Página 183)

### **A. Botão DCLT - Localização e Ação**

**Comportamento:**
```
Ação: Pressionar DCLT OSB (breve pressão)
Resultado: MFD destaca "DCLT" → Remove OSB labels (esquerda, topo, direita)

Ação: Pressionar DCLT OSB novamente (< 1 segundo)
Resultado: Modo declutter desativado → Labels retornam
```

### **B. O Que é Removido vs Preservado**

**REMOVIDO (Decluttered):**
- ✂️ Labels dos OSBs (lado esquerdo, topo, direita)
- ✂️ Mnemonics dos OSBs associados

**PRESERVADO (Sempre visível):**
- ✅ Range scale mnemonic (ex: "60" para 60 NM)
- ✅ Gain gauge
- ✅ Labels na **BOTTOM** do MFD (OSBs 12-20)

**Citação Exata (Seção 2.3.1.3.1, Página 183):**
> "However, alphanumeric data unrelated to the OSBs such as range scale mnemonic 
> and the gain gauge and the labels at the bottom of the MFD remain visible."

### **C. OSBs Permanecem Funcionais!**

**Nota Crítica (Seção 2.3.1.3.1, Página 183):**
> "NOTE: Even when OSB labels are decluttered, the OSBs themselves remain active 
> and functional."
> (DASH-34-1, Seção 2.3.1.3.1, Página 183)

**Implicação:** 
- Labels desaparecem visualmente
- Botões continuam respondendo a pressões
- Piloto pode operar "blind" com DMS/TMS

### **D. Persistência de Declutter State**

**Citação Exata (Seção 2.3.1.3.1, Página 183):**
> "The declutter state is retained based on the MFD format, except for the radar. 
> For radar, the declutter state is retained based on whether the A-A FCR or A-G 
> FCR mode is active. The declutter setting will persist unless manually deselected 
> by the pilot or because of an MFDS power cycle."
> (DASH-34-1, Seção 2.3.1.3.1, Página 183)

**Regras de Persistência:**

```
MFD Formatos (HSD, SMS, WPN, etc):
  Declutter state → POR FORMATO
  Muda formato? → Estado perdido

FCR/Radar:
  Declutter state → POR MODO (A-A ou A-G)
  Muda modo? → Estado persistido se mesmo tipo

CRM → ACM: Declutter state MANTIDO
GM → GMT: Declutter state MANTIDO

MFDS Power Cycle: Estado PERDIDO
```

### **E. Declutter em Base Pages Only**

**Citação (Seção 2.3.1.3.1, Página 183):**
> "Declutter option is only available on base pages."

**Implicação:**
- Control Pages (CNTL) não têm declutter
- Programmable Declutter Pages não têm declutter
- Only base page display

---

## 🟠 PROGRAMMABLE DECLUTTER - FCR DCLT PAGE

### **Seção Referência:**
- **DASH-34-1, Seção 2.3.1.3.1, Página 183-184**
- **DASH-34-1, Seção 2.3.1.5.1.5, Página 195** (OSB 11 Details)

### **Citação Exata - Access & Function (Seção 2.3.1.3.1, Página 183):**

> "You can program certain FCR display mnemonics and symbology for decluttering. 
> By pressing OSB 11 located next to the DCLT mnemonic for at least 1 second, 
> you can access the programmable declutter page. On this page, the decluttered 
> items are initially highlighted. To declutter a specific mnemonic or symbol, 
> simply press the OSB next to it, which will highlight and select it for 
> decluttering."
> (DASH-34-1, Seção 2.3.1.3.1, Página 183)

### **A. Acessar Programmable Declutter**

```
Ação: Press OSB 11 (≥ 1 segundo)
Resultado: Acessa programmable declutter page (A-A ou A-G específico)

Página mostra: Mnemonics/symbology que podem ser decluttered
Status: Decluttered items = highlighted
```

### **B. Selecionar Itens para Declutter**

```
1. OSB 11 ≥ 1 segundo → Programmable DCLT page
2. Pressionar OSB ao lado do mnemonic desejado
3. Mnemonic fica highlighted (selecionado para declutter)
4. OSB 11 ≥ 1 segundo novamente → Retorna base page
```

### **C. Reset Declutter Items**

**Método 1 (A-A ou A-G MODE page):**
```
1. Acessar Programmable DCLT page
2. OSB 6 (A-A RESET ou A-G RESET)
   → Reseta todos declutter items para defaults
```

**Método 2 (Master Format Menu):**
```
1. Menu page
2. OSB 1 (PROG DCLT RESET)
   → Reseta todos defaults
```

**Nota Importante (Seção 2.3.1.3.1, Página 183):**
> "Please note that the selected declutter items are not retained through power 
> cycles or auto restart. Upon exiting the page, only the default items will be 
> highlighted."

---

## 📋 FCR DECLUTTER ITEMS - LISTA COMPLETA

### **Seção Referência:**
- **DASH-34-1, Seção 2.3.1.3.1, Página 184**
- **Tabela: FCR Declutter Items A-A and A-G Format**

### **A-A FORMAT Declutterable Items:**

| OSB | Mnemonic | Item Decluttered | Função |
|---|---|---|---|
| 1 | A-A MODE | Selected mode mnemonic | Esconde indicador de modo |
| 2 | FCR SUBMODE | Selected submode mnemonic | Esconde submode (STT, SAM, TWS) |
| 3 | FOV | Selected FOV option mnemonic | Esconde field-of-view option |
| 4 | OVRD | Standby override mnemonic | Esconde OVRD indicator |
| 5 | CNRL | Control page mnemonic | Esconde CNTL label |
| 6 | A-A RESET | Reset to defaults | **Special: Reset all defaults** |
| 7 | ALT | Min/max search altitude readouts | Esconde ALT limits |
| 8 | ATTACK STRG | AIM-120 ASEC readout | Esconde ASEC (Allowable Steering) |
| 9 | DLZ | AIM-120 time remaining/TOF | Esconde Dynamic Launch Zone |
| 10 | TGT DATA | Expanded target data | Esconde aspect, KCAS, closure rate |
| 11 | PROG DCLT | Declutter mnemonic | **Access programmable page** |
| 12-15 | FMT3, FMT2, FMT1 | MFD format mnemonics | Esconde format labels |
| 15 | SWAP | SWAP mnemonic | Esconde SWAP label |
| 16 | WPN STAT | Weapon status mnemonic | Esconde status (A-A only) |
| 17 | IFF | Mode label | Esconde IFF mode indicator |
| 18 | AZBAR | Antenna azimuth scan info | Esconde AZ bar |
| 19 | RNG | Selected range scale readout | Esconde range value (ex: "60") |
| 20 | INCDEC | Increment/decrement symbol | Esconde △▽ symbols |

### **A-G FORMAT Declutterable Items:**

| OSB | Mnemonic | Item Decluttered | Função |
|---|---|---|---|
| 1 | A-G MODE | Selected mode mnemonic | Esconde A-G mode indicator |
| 2 | AUTOMAN | Auto/manual range scale option | Esconde AUTO/MAN |
| 3 | FOV | Selected FOV option mnemonic | Esconde FOV |
| 4 | OVRD | Standby override mnemonic | Esconde OVRD |
| 5 | CNRL | Control page mnemonic | Esconde CNTL |
| 6 | A-G RESET | Reset to defaults | **Special: Reset all defaults** |
| 7 | BUP SEN | Backup sensor mnemonic | Esconde backup FCR/TGP |
| 8 | FZSP | Freeze/Snowplow option | Esconde FZ/SP |
| 9 | CZ | Cursor zero option mnemonic | Esconde CZ label |
| 10 | SIGHT POINT | Sighting point option | Esconde sighting mode |
| 11 | PROG DCLT | Declutter mnemonic | **Access programmable page** |
| 12-15 | FMT3, FMT2, FMT1 | MFD format mnemonics | Esconde format labels |
| 15 | SWAP | SWAP mnemonic | Esconde SWAP label |
| 17 | MAP | MAP mnemonic + incdec | Esconde MAP controls |
| 18 | AZ | Antenna azimuth scan info | Esconde AZ |
| 19 | RNG | Selected range scale readout | Esconde range value |
| 20 | INCDEC | Increment/decrement symbol | Esconde △▽ |

### **Default Decluttered Items (Factory Default):**

**Citação (Seção 2.3.1.3.1, Página 184 - Default column):**
> "Default clutter item" - Identificado na tabela

**Itens Default Decluttered em A-A:**
- RNG (OSB 19) - Normalmente escondido por default
- INCDEC (OSB 20) - Normalmente escondido por default

---

## 🟢 HSD DECLUTTER - CONTROL PAGE OPTIONS

### **Seção Referência:**
- **DASH-34-1, Seção 2.1.6.18.8.1, Página 89-90**
- **DASH-34-1, Seção 2.1.6.18.8, Página 88-89** (Base page options)

### **HSD Control Page Declutter Options (Non-L16):**

| OSB | Mnemonic | Função | Efeito |
|---|---|---|---|
| 1 | FCR | Fire Control Radar search volume | Toggle FCR ghost cursor / volume |
| 2 | PRE | Preplanned threat symbols | Toggle threat circles/IDs |
| - | AIFF | IFF friendly/unknown symbols | Toggle IFF markers (L16 only) |
| 3-5 | Various | Threat rings, PRE, AIFF | Declutter específicos |

### **HSD Control Page Declutter L16 Options (Page 2):**

| OSB | Mnemonic | Função | Status |
|---|---|---|---|
| - | ENG | Engagement diamonds (HSD/FCR) | Declutter symbology |
| - | REF PT | L16 reference points | Declutter L16 marks |
| - | T-R | L16 threat rings | Declutter threat rings |
| - | A SURV | L16 air surveillance tracks | Declutter A-A tracks |
| - | G FRND | L16 ground friendly positions | Declutter friendlies |
| - | LAR | JASSM MPPRE LAR displays | Declutter SEAD |
| - | A IDM | Air tracks via IDM | Declutter IDM A-A |
| - | SHIP | L16 ship positions | Declutter naval |
| - | SAM | SAM installations | Declutter SAM threats |
| - | G TGTS | Ground targets (L16/IDM) | Declutter ground tgts |
| - | A TGTS | Air targets via L16 | Declutter L16 A-A |

---

## 🔵 HSD EXPAND MODE - Declutter Automático

### **Seção Referência:**
- **DASH-34-1, Seção 2.1.6.18.7, Página 86**

### **Citação Exata - Declutter During Expansion (Página 86):**

> "While in the expanded mode, the cursor movement is limited to the area within 
> the expanded patch, but the patch itself cannot be moved. During the activation 
> of the expansion mode, the EXP1 or EXP2 label will flash at a rate of 5Hz. 
> Additionally, **certain labels and functions are decluttered while the expansion 
> mode is active:**"
> (DASH-34-1, Seção 2.1.6.18.7, Página 86)

### **O Que É Auto-Decluttered em HSD EXP Mode:**

```
✂️ HSD range scale and increment/decrement switches
✂️ Sensor volume
✂️ HSD A-A ghost cursor
✂️ HSD A-G ghost cursor
✂️ Range rings and Magnetic North pointer
✂️ Centered/Depressed Option
✂️ Coupled/Decoupled Option
✂️ HSD Freeze Option
```

**Implicação:**
- Expansion mode = automatic declutter para zoom visual
- Pilot foca na área expandida sem distração

---

## 📊 RELACIONAMENTO: DMS vs DECLUTTER vs EXPAND

### **A. DMS e Declutter são INDEPENDENTES**

| Função | DMS | Declutter |
|---|---|---|
| **Controla** | SOI selection + Format cycling | OSB label visibility |
| **Relacionado?** | Não | Não |
| **Comportamento** | Muda qual sensor é ativo | Remove visual clutter apenas |
| **Persistência** | Mantém até mudança manual | Perdido em power cycle |

**Citação DASH-34-1, Seção 2.3.1.2.1.7, Página ~190:**
> "The DMS, which is spring-loaded to the center position, controls SOI selection 
> and format MFD page stepping."

**Declutter não mencionado aqui - são FUNÇÕES DISTINTAS**

### **B. Declutter + Expand Mode**

```
HSD EXPAND ativado:
  ↓
Auto-Declutter certos items (ver lista acima)
  ↓
Piloto pode ver área ampliada sem clutter
  ↓
DMS continua funcionando (SOI/format selection)
```

### **C. Declutter + SWAP**

```
SWAP OSB pressiona → Swap LEFT ↔ RIGHT MFD
  ↓
Se LEFT estava decluttered → RIGHT HERDA declutter state?
```

**Comportamento (Seção 2.1.6.9, Página 74):**
> "By depressing the SWAP OSB on either MFD, the information displayed on the 
> left MFD is swapped with that of the right MFD, including both video and text data."

**Não há menção de declutter state + SWAP**
- Presumivelmente: Declutter state é **PER MFD**, não **PER FORMAT**
- Logo, pode trocar com SWAP

---

## 🎯 PROCEDIMENTO: USANDO DECLUTTER EFETIVAMENTE

### **Cenário 1: Quick FCR Declutter (A-A)**

```
1. FCR page ativo
2. Breve pressão em DCLT OSB
   → MFD mostra "DCLT" highlighted
   → OSB labels desaparecem (esquerda/topo/direita)
   → Bottom labels (12-20) permanecem

3. Para desativar: Pressionar DCLT novamente (< 1 sec)
```

### **Cenário 2: Customizar Declutter (Programmable)**

```
1. FCR page ativo (base page)
2. OSB 11 ≥ 1 segundo
   → Programmable declutter page (A-A MODE ou A-G MODE)
   
3. Pressionar OSB ao lado de cada mnemonic para toggle
   Exemplo: OSB 9 (DLZ) → Declutter AIM-120 DLZ display
   
4. OSB 11 ≥ 1 segundo novamente
   → Volta base page com configuração customizada
   
5. Estado persistido até:
   - Power cycle MFDS
   - Mudança de formato (se não FCR)
   - Pressionar A-A/A-G RESET (OSB 6)
```

### **Cenário 3: HSD Expand + Auto Declutter**

```
1. HSD page ativo (SOI)
2. OSB 3 ou EXPAND/FOV button
   → EXP1 (2.1x) ou EXP2 (4.1x)
   
3. Automático:
   → Labels/rings decluttered
   → Cursor expandido em centro
   → Pode mover cursor (limited area)
   
4. DMS/TMS continua funcional
   → Pode cyclar formatos mesmo expandido
```

---

## ⚠️ NOTAS CRÍTICAS SOBRE DECLUTTER

### **1. OSBs Permanecem Ativos**

Nunca se esqueça:
```
Visual: Labels desaparecem
Funcional: Botões continuam respondendo
```

Piloto pode operar **blind** com DMS/TMS mesmo com declutter ativo.

### **2. Nem Tudo é Declutable**

**Sempre visível (não podem ser decluttered):**
- Range scale value (ex: "60 NM")
- Gain gauge
- Bottom OSB labels (12-20)
- Video symbology (não é texto)
- Target symbology

### **3. Base Pages Only**

Declutter não funciona em:
- CNTL pages
- Programmable declutter pages
- Menu pages
- FLIR control pages

### **4. Power Cycle = Reset**

```
Piloto customiza declutter items
MFDS power cycle
↓
Volta aos DEFAULTS (não custom)
```

---

## 📋 TABELA COMPARATIVA: Visibility Modes

### **Estado de Visibilidade no MFD**

| Item | Normal | Declutter | EXPAND |
|---|---|---|---|
| OSB labels (L/T/R) | ✅ Visível | ✂️ Escondido | ✂️ Escondido |
| Range scale value | ✅ Visível | ✅ Visível | ✂️ Escondido |
| Target symbology | ✅ Visível | ✅ Visível | ✅ Visível (ampliado) |
| Radar ghost cursor | ✅ Visível | ✅ Visível | ✂️ Escondido (HSD) |
| Range rings | ✅ Visível | ✅ Visível | ✂️ Escondido (HSD) |
| Threat circles | ✅ Visível | Opt. declarável | ✂️ Escondido (HSD) |
| DMS functional | ✅ Ativo | ✅ Ativo | ✅ Ativo |
| Bottom OSB labels | ✅ Visível | ✅ Visível | ✅ Visível |

---

## 📚 CITAÇÕES COMPLETAS

### **Da Seção 2.1.6.2 (Página 65) - MFDS Capabilities:**

> "The capabilities of the MFDS encompass the following abilities:
> - Select display formats.
> - Swap display formats.
> - **Declutter certain alphanumeric data.**
> - Select various options via either rotaries or menus.
> - Increment-decrement certain data.
> - Enter numerical data via a keyboard..."

### **Da Seção 2.3.1.3.1 (Página 183) - FCR DCLT:**

> "A declutter feature is available to remove most of the OSB labels from the 
> selected display. By briefly pressing the DCLT OSB, the MFD highlights the 
> letters DCLT and eliminates the labels associated with the OSBs located on 
> the left, top, and right edges of the MFDs."

### **Da Seção 2.1.6.18.7 (Página 86) - HSD Expand:**

> "During the activation of the expansion mode, the EXP1 or EXP2 label will 
> flash at a rate of 5Hz. Additionally, certain labels and functions are 
> decluttered while the expansion mode is active."

---

## 🔗 CONEXÃO COM DMS

### **Clarificação: Não há relação direta**

**DMS (Display Management Switch):**
- Controla **qual sensor/format é SOI**
- Controla **cycling entre MFDs e HUD**
- Controla **cycling entre formatos**

**DECLUTTER (DCLT):**
- Controla **visibilidade de labels**
- Não afeta SOI selection
- Não afeta DMS functionality

**Integração:**
```
DMS seleciona MFD como SOI
↓
DECLUTTER ativa no MFD
↓
MFD continua sendo SOI
↓
Labels escondidos, mas DMS/TMS continuam usando MFD
```

**Exemplo Operacional:**
```
1. DMS DOWN → RIGHT MFD = SOI (FCR)
2. Pressionar DCLT → FCR labels desaparecem
3. Pressionar DMS DOWN novamente → LEFT MFD = SOI (HSD)
4. Labels HSD aparecem, labels FCR escondidos

Resultado: DMS funciona INDEPENDENTE de declutter state
```

---

## ✅ VERIFICAÇÃO RÁPIDA

| Pergunta | Resposta | Referência |
|---|---|---|
| **O que é declutter?** | Remove OSB labels para reduzir clutter visual | Seção 2.3.1.3.1, Página 183 |
| **Como ativar?** | Pressionar DCLT OSB brevemente | Idem |
| **Como desativar?** | Pressionar DCLT OSB novamente (< 1 sec) | Idem |
| **Pode customizar?** | Sim, OSB 11 ≥ 1 segundo → programmable page | Idem |
| **OSBs continuam funcionais?** | SIM, labels sumiram mas botões respondem | Idem |
| **Qual formato?** | Base pages apenas | Idem |
| **Persiste após power cycle?** | Não, volta aos defaults | Idem |
| **Relacionado a DMS?** | Não, são independentes | Seção 2.3.1.2.1.7 |
| **HSD expand declutter?** | Sim, auto-declutter certos items | Seção 2.1.6.18.7, Página 86 |
| **Sempre visível?** | Range scale, bottom labels, symbology | Seção 2.3.1.3.1, Página 183 |

---

**Documento Compilado:** 12 JAN 2026
**Fonte:** TO 1F-16CMAM-34-1-1 BMS, Change 4.38
**Seções Consultadas:** 2.1.6.2, 2.3.1.3.1, 2.3.1.5.1.5, 2.1.6.18.7, 2.1.6.18.8.1
**Status:** Pesquisa completa com todas as referências diretas