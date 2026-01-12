# DMS (Display Management Switch) - Funções Completas
## Extraído de: TO 1F-16CMAM-34-1-1 BMS (DASH-34-1)

---

## 📌 SEÇÃO DO MANUAL
**Capítulo:** 2.1.6.3 e 2.3.1.2.1.7
**Título:** Sensor of Interest SOI / Display Management Switch DMS
**Página:** ~66-67 e ~181

---

## 🎮 DMS - Características Básicas

- **Localização:** Stick (Manche) / Controles portáteis
- **Posição de repouso:** Spring-loaded para centro (CENTRO)
- **Acionamento:** 3 posições
  - **UP** (Para cima)
  - **CENTER** (Centro / Repouso)
  - **DOWN** (Para baixo)
- **Nota importante:** DMS **não tem LEFT/RIGHT** como funções primárias na descrição oficial
  - LEFT e RIGHT são para **Master Mode específico** ou **cycling through formatos**
  - A documentação DASH-34-1 menciona DMS LEFT/RIGHT para **seleção de formato MFD**, mas são secundários

---

## 🔴 DMS UP - Funções Possíveis

### Função Principal:
**Designa HUD como Sensor of Interest (SOI)**

#### Descrição completa (do manual):
> Moving the Display Management Switch DMS upward, which transitions the SOI designation to the HUD if allowed.

#### Contexto de aplicação:
- **Master Modes permitidos:** NAV (Navegação) e A-G (Ar-para-Solo)
- **Master Mode NOT permitido:** A-A (Ar-para-Ar) - o HUD SÓ pode ser SOI com HMCS habilitado
- **Condição:** O HUD deve estar em modo que permite SOI
- **Restrições:** Não funciona em MARK OFLY submode ou snowplow (SP) ground radar mode em PRE state

#### Resultado visual:
- Asterisco (*) aparece no canto superior esquerdo do HUD (acima da escala de velocidade)
- MFD(s) perdem o box de SOI (linha ao redor da borda)
- Controles HOTAS agora afetam o HUD primariamente

#### Tabela de contexto:
| Master Mode | DMS UP Resultado | HUD pode ser SOI? |
|---|---|---|
| **NAV** | HUD ← SOI | ✅ SIM |
| **A-G** | HUD ← SOI | ✅ SIM |
| **A-A** | HUD ← SOI | ❌ NÃO (exceto com TGP/HSD/FCR formatos limitados) |
| **DGFT** | Sem efeito | ❌ NÃO |
| **MSL OVRD** | Sem efeito | ❌ NÃO |

---

## 🔵 DMS DOWN - Funções Possíveis

### Função Principal:
**Cicla SOI entre MFD(s) OU retorna de HUD para MFD**

#### Descrição completa (do manual):
> When the HUD is the SOI and the DMS is moved downward, the SOI designation shifts to the MFDs. If the DMS is moved downward and the SOI is on the MFDs, the SOI transitions to the other MFD if allowed.

#### Fluxo de operação (em sequência):

**Estado 1: HUD é SOI**
```
DMS DOWN → MFD esquerdo (LEFT) torna-se SOI
```
- Asterisco desaparece do HUD
- Box de SOI aparece ao redor da borda do MFD esquerdo

**Estado 2: MFD Esquerdo é SOI**
```
DMS DOWN → MFD direito (RIGHT) torna-se SOI
```
- Box de SOI sai do MFD esquerdo
- Box de SOI aparece ao redor do MFD direito

**Estado 3: MFD Direito é SOI**
```
DMS DOWN → MFD esquerdo (LEFT) torna-se SOI novamente
```
- Cicla de volta (comportamento toggle entre MFDs)

#### Restrições:
- "**If allowed**" = alguns formatos MFD não podem ser SOI
- **Formatos que NÃO podem ser SOI:** Qualquer formato que exiba "NOT SOI" no centro
- **Formatos que PODEM ser SOI:** FCR, TGP, WPN, HAD, HSD (em A-A: apenas FCR, HSD, TGP)

#### Tabela de contexto:
| Situação Atual | DMS DOWN Ação |
|---|---|
| HUD = SOI | Vai para LEFT MFD (se permitido) |
| LEFT MFD = SOI | Vai para RIGHT MFD (se permitido) |
| RIGHT MFD = SOI | Volta para LEFT MFD |
| Nenhum formato compatível | Sem mudança ou mantém estado anterior |

---

## 🟢 DMS LEFT - Função

### Função Principal:
**Muda formato primário no MFD ESQUERDO**

#### Descrição do manual:
> The primary format can also be changed by using the DMS left for the left MFD or right for the right MFD switch.

#### Mecanismo de seleção:
```
Formato selecionado (PRIMARY) → DMS LEFT → próximo formato disponível
```

#### Sequência de ciclo:
1. Formato primário atual é destacado
2. DMS LEFT pressiona OSB adjacente a **formato secundário** (esq ou dir)
3. Novo formato torna-se primário
4. Formatos em branco ("BLANK") são **PULADOS** automaticamente

#### Ordem de seleção:
- **De dentro para fora:** Primário → Secundário 1 → Secundário 2 → Volta
- Exato ordem depende de configuração de ramp start ou DTC

#### Nota sobre formatos:
- **Máximo 6 formatos total:** 3 per MFD
- **Nenhum duplicado permitido:** A menos que sejam BLANK ou TEST (durante BIT)
- **Formatos disponíveis:** FCR, TGP, HSD, SMS, WPN, HAD, FLIR, TFR, FLCS, DTE, TCN, TEST, BLANK

#### Restrição importante:
> If a format is selected from the master menu page that already exists as one of the five other formats, the blank format is used instead of the old format.

---

## 🟡 DMS RIGHT - Função

### Função Principal:
**Muda formato primário no MFD DIREITO**

#### Descrição do manual:
> The primary format can also be changed by using the DMS left for the left MFD or right for the right MFD switch.

#### Mecanismo de seleção:
```
Formato selecionado (PRIMARY) no MFD DIREITO → DMS RIGHT → próximo formato
```

#### Comportamento:
- **Idêntico ao DMS LEFT**, mas afeta **MFD direito** apenas
- Cicla através dos 3 formatos disponíveis no MFD direito
- Pula formatos BLANK automaticamente

#### Nota sobre master modes:
- Disponível em **todos os master modes** (A-A, A-G, NAV, DGFT, MSL OVRD)
- Útil para rápida alternância de displays operacionais

---

## ⚠️ FUNÇÕES SECUNDÁRIAS / CONTEXTUAIS

### A. EXPANDFOV (não é DMS, mas relacionado)
- **Controle:** Botão separado (não mencionado como DMS)
- **Função:** Cicla entre FOVs expandidas para SOI

### B. SWAP OSB (Troca de Displays)
```
Pressionando SWAP OSB em qualquer MFD:
- Conteúdo do MFD LEFT ↔ Conteúdo do MFD RIGHT
- Inclui vídeo e texto
- SOI segue o display (se era LEFT MFD = SOI, passa a ser RIGHT MFD = SOI)
```

### C. DCLT (Declutter)
- **Não é função DMS**, mas frequentemente usado com DMS
- **Botão:** OSB específico
- **Função:** Remove labels OSB da tela (deixa dados principais visíveis)

---

## 📋 RESUMO TABULAR DE FUNÇÕES DMS

| Posição DMS | Função | Resultado | Master Mode Restrictions |
|---|---|---|---|
| **UP** | Designa HUD como SOI | Asterisco no HUD, MFD perde SOI box | NAV, A-G apenas |
| **DOWN (HUD→MFD)** | Move SOI de HUD para LEFT MFD | Asterisco sai HUD, box vai para LEFT MFD | Todos, se HUD era SOI |
| **DOWN (MFD→MFD)** | Cicla SOI entre MFDs | Box move: LEFT↔RIGHT | Todos |
| **LEFT** | Muda formato primário LEFT MFD | Novo formato exibido no LEFT MFD | Todos |
| **RIGHT** | Muda formato primário RIGHT MFD | Novo formato exibido no RIGHT MFD | Todos |

---

## 🔍 CASOS DE USO OPERACIONAIS (do DASH-34-1)

### Caso 1: NAV Mode - Mudar de HSD para FCR
```
Situação: HSD é SOI em NAV mode
Ação: DMS DOWN
Resultado: MFD esquerdo (com FCR) torna-se SOI
Efeito: Cursor control agora afeta radar, não HUD
```

### Caso 2: A-A Mode - Ciclar entre Radar Modes
```
Situação: MFD esquerdo mostra FCR, MFD direito mostra SMS
Ação: DMS LEFT (repetido)
Resultado: Formatos alternam dentro do MFD esquerdo
Efeito: Sem mudança de SOI, apenas display muda
```

### Caso 3: Air-to-Ground Data Link
```
Situação: Precisa transferir SOI para HSD (para fazer data link)
Ação: DMS UP (se em A-G mode) → depois DMS DOWN para selecionar MFD com HSD
Resultado: HSD torna-se SOI (com box ao redor)
Efeito: Pode usar cursor para selecionar steerpoint e data link
```

### Caso 4: Trocar entre MFDs sem mudar formato
```
Situação: LEFT MFD = FCR (SOI), RIGHT MFD = TGP
Ação: DMS DOWN
Resultado: RIGHT MFD torna-se SOI (TGP ativo)
Efeito: Cursor control muda para TGP automaticamente
```

---

## 🎯 LIMITAÇÕES IMPORTANTES

1. **HUD não pode ser SOI em A-A mode** (exceto em certain TGP/HSD/FCR sub-modes específicos)
2. **DMS UP funciona APENAS se HUD está em modo permitido** (NAV ou A-G)
3. **Alguns formatos MFD não permitem SOI** (exibem "NOT SOI")
4. **LEFT/RIGHT cycling só funciona com formatos válidos** - BLANK é pulo
5. **Spring-loaded ao centro** = sempre retorna para posição neutra
6. **DMS não afeta FCR operação diretamente** (use TMS para isso)
7. **DMS não afeta Radar modes** (use OSBs ou menu para isso)

---

## ✅ RESUMO FINAL

**DMS tem 5 funções principais:**

1. **UP** → HUD como SOI (NAV/A-G apenas)
2. **DOWN (HUD)** → Retorna para MFD como SOI
3. **DOWN (MFD)** → Cicla entre MFDs
4. **LEFT** → Próximo formato no MFD LEFT
5. **RIGHT** → Próximo formato no MFD RIGHT

**Master-mode dependent behavior:**
- A-A: DOWN apenas (cicla MFDs), LEFT/RIGHT (cicla formatos)
- A-G/NAV: UP (HUD), DOWN (alterna HUD↔MFD), LEFT/RIGHT (formatos)
- DGFT/MSL OVRD: LEFT/RIGHT (formatos) apenas

---

**Fonte:** TO 1F-16CMAM-34-1-1 BMS, Capítulos 2.1.6.3, 2.3.1.2.1.7
**Data do Manual:** Change 4.38 (BMS 4.38)
**Data de Extração:** 12 JAN 2026