DMS (DISPLAY MANAGEMENT SWITCH) - FUNÇÕES COMPLETAS
F-16C/D BLOCO 50/52 (BMS 4.38)
Extraído de: TO 1F-16CMAM-34-1-1 (DASH-34-1)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

POSIÇÃO DMS │ NOME TÉCNICO        │ DESCRIÇÃO TÉCNICA                                     │ RESULTADO VISÍVEL                                  │ MASTER MODES VÁLIDOS │ RESTRIÇÕES/NOTAS                      
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

UP          │ HUD SOI Designate   │ Designa HUD como Sensor of Interest (SOI)            │ • Asterisco (*) aparece no HUD (canto sup-esq)    │ NAV, A-G             │ • NAV: Sempre OK                      
            │                     │                                                       │ • MFD perde box de SOI                             │                      │ • A-G: Sempre OK                      
            │                     │                                                       │ • Controles HOTAS agora afetam HUD                 │                      │ • A-A: NÃO permite (exceto TGP/HSD)   
            │                     │                                                       │                                                    │                      │ • DGFT/MSL OVRD: Sem efeito           
            │                     │                                                       │                                                    │                      │ • HUD deve estar em modo compatível   
            │                     │                                                       │                                                    │                      │ • Rejeita MARK OFLY e SP ground mode  

DOWN        │ SOI Toggle (HUD→MFD)│ Move SOI de HUD para MFD Esquerdo                    │ • Asterisco sai do HUD                             │ NAV, A-G (qdo HUD)   │ • Só funciona se HUD era SOI          
            │ ou (MFD→MFD)        │ OU cicla entre MFD LEFT e RIGHT                      │ • Box de SOI aparece no LEFT MFD                   │ A-A, DGFT, MSL OVRD  │ • Alterna: LEFT ↔ RIGHT ↔ LEFT...     
            │                     │                                                       │ • Se em LEFT MFD: vai para RIGHT MFD               │ (cicla entre MFDs)   │ • Formatos incompatíveis: ignorados    
            │                     │                                                       │                                                    │                      │ • Pula formatos BLANK automaticamente  
            │                     │                                                       │                                                    │                      │ • Alguns formatos não permitem SOI    

LEFT        │ Format Select (L)   │ Cicla para próximo formato primário no MFD ESQUERDO  │ • Novo formato aparece no MFD esquerdo            │ TODOS                │ • Afeta APENAS MFD esquerdo           
            │ (MFD Left Primary)  │                                                       │ • Outros displays não mudam                        │                      │ • Pula formatos BLANK                 
            │                     │                                                       │                                                    │                      │ • Nenhum formato duplicado permitido   
            │                     │                                                       │                                                    │                      │ • Se SOI estava neste MFD: permanece  
            │                     │                                                       │                                                    │                      │ • Ordem: PRIMARY → SEC1 → SEC2 → ...  

RIGHT       │ Format Select (R)   │ Cicla para próximo formato primário no MFD DIREITO   │ • Novo formato aparece no MFD direito              │ TODOS                │ • Afeta APENAS MFD direito            
            │ (MFD Right Primary) │                                                       │ • MFD esquerdo não muda                            │                      │ • Pula formatos BLANK                 
            │                     │                                                       │                                                    │                      │ • Nenhum formato duplicado permitido   
            │                     │                                                       │                                                    │                      │ • Se SOI estava neste MFD: permanece  
            │                     │                                                       │                                                    │                      │ • Ordem: PRIMARY → SEC1 → SEC2 → ...  

CENTER      │ Neutral/Detent      │ Posição de repouso (spring-loaded retorna aqui)      │ • Sem mudanças (estado anterior mantido)           │ TODOS                │ • Sempre volta automaticamente ao centro
(REPOUSO)   │ (Neutral)           │                                                       │                                                    │                      │ • Posição de inicialização             

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

SEQUÊNCIA OPERACIONAL - DMS DOWN (Ciclo Completo):

   Estado 1: HUD é SOI          →  [DMS DOWN]  →  Estado 2: MFD LEFT é SOI       →  [DMS DOWN]  →  Estado 3: MFD RIGHT é SOI     →  [DMS DOWN]  →  Estado 1: MFD LEFT...
   (asterisco no HUD)                                (box ao redor MFD L)                          (box ao redor MFD R)                        
   Indicador: * no HUD                             Indicador: Linha ao redor MFD L              Indicador: Linha ao redor MFD R         

   NOTA: Alguns formatos MFD não permitem SOI - neste caso, o DMS DOWN pode pular ou manter estado anterior!

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

FORMATOS DISPONÍVEIS NOS MFDs (para DMS LEFT/RIGHT):

   FORMATO                       │ SIGLA │ TIPO     │ Pode ser SOI? │ Master Modes Disponível         
   ────────────────────────────────────────────────────────────────────────────────────────────────────
   Fire Control Radar            │ FCR   │ Video    │ SIM (todos)   │ A-A, A-G, NAV, DGFT, MSL OVRD 
   Targeting Pod                 │ TGP   │ Video    │ SIM (todos)   │ A-A, A-G, NAV                 
   Horizontal Situation Display  │ HSD   │ Text     │ SIM (todos)   │ A-A, A-G, NAV, DGFT, MSL OVRD 
   Weapon Display                │ WPN   │ Video    │ SIM (A-G,NAV) │ A-A, A-G, NAV                 
   HARM Attack Display           │ HAD   │ Text     │ SIM (A-G,NAV) │ A-G, NAV                      
   Stores Mgmt System            │ SMS   │ Text     │ NÃO           │ TODOS                         
   Data Transfer Equipment       │ DTE   │ Text     │ NÃO           │ TODOS                         
   FLIR (Nav Pod)                │ FLIR  │ Video    │ NÃO           │ NAV, A-G                      
   Terrain Following Radar       │ TFR   │ Video    │ NÃO           │ NAV, A-G                      
   FLCS Digital Flight Ctrl      │ FLCS  │ Text     │ NÃO           │ NAV, A-G                      
   TACAN                         │ TCN   │ Text     │ NÃO           │ NAV, A-G                      
   Test (MFD BIT)                │ TEST  │ Text     │ NÃO (BIT)     │ Teste apenas                  
   Blank                         │ BLANK │ Nenhum   │ NÃO           │ TODOS (pulado por DMS L/R)    

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

MASTER MODE X DMS BEHAVIOR:

   MASTER MODE │ DMS UP        │ DMS DOWN                      │ DMS LEFT/RIGHT  │ Restrições Especiais           
   ────────────────────────────────────────────────────────────────────────────────────────────────────
   A-A         │ ❌ Bloqueado  │ ✅ MFD cycle (LEFT ↔ RIGHT)  │ ✅ Format cycle │ FCR, HSD, TGP (não SMS/HAD)   
   A-G         │ ✅ Allowed    │ ✅ HUD↔MFD toggle + MFD cycle│ ✅ Format cycle │ Todos formatos ok             
   NAV         │ ✅ Allowed    │ ✅ HUD↔MFD toggle + MFD cycle│ ✅ Format cycle │ Todos formatos ok             
   DGFT        │ ❌ Bloqueado  │ ✅ MFD cycle (LEFT ↔ RIGHT)  │ ✅ Format cycle │ Apenas air-to-air formatos    
   MSL OVRD    │ ❌ Bloqueado  │ ✅ MFD cycle (LEFT ↔ RIGHT)  │ ✅ Format cycle │ Apenas air-to-air formatos    
   JETTISON    │ ❌ Bloqueado  │ ✅ MFD cycle (LEFT ↔ RIGHT)  │ ✅ Format cycle │ Limitado (emergency)          

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

FUNÇÕES RELACIONADAS (NÃO são DMS, mas frequentemente usadas conjuntamente):

   FUNÇÃO            │ CONTROLE        │ EFEITO                                                  
   ──────────────────────────────────────────────────────────────────────────────────────────────
   SWAP Displays     │ OSB 15 (MFD)    │ Troca conteúdo LEFT MFD ↔ RIGHT MFD (inclui SOI)    
   DCLT (Declutter)  │ OSB specific    │ Remove labels OSB deixando dados principais visíveis 
   EXPANDFOV         │ Botão separado  │ Cicla entre FOVs expandidas do SOI                  
   Format Menu       │ Pressionar Prim │ Acessa menu de todos formatos (12+ opções)          

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

CASOS DE USO COMUNS:

1️⃣  AIR-TO-AIR (A-A Mode):
    • Usar DMS LEFT/RIGHT para alternar entre FCR, TGP, HSD formatos
    • DMS DOWN cicla entre MFDs (ex: LEFT FCR ↔ RIGHT SMS)
    • DMS UP bloqueado (HUD não pode ser SOI em A-A)
    
2️⃣  AIR-TO-GROUND CAS/CLOSE AIR SUPPORT:
    • Inicial: DMS UP para colocar HUD como SOI (para navegação visual)
    • Depois: DMS DOWN para MFD com TGP (para targeting)
    • Alternar: DMS LEFT/RIGHT para TGP ↔ HSD formatos
    
3️⃣  NAVIGATION + TARGETING (A-G Mode):
    • Começa em HSD (SOI) para navegação
    • DMS DOWN para HUD se necessário (navegação visual)
    • DMS LEFT para FCR A-G (ground mapping)
    • DMS RIGHT para TGP (targeting pod video)
    
4️⃣  DATA LINK OPERATIONS:
    • DMS UP (se A-G) para designar HUD
    • DMS DOWN para MFD com HSD
    • HSD como SOI permite cursor control para data link steerpoints
    
5️⃣  RAPID FORMAT SWITCHING:
    • Mantenha DMS LEFT/RIGHT pressionado rapidamente
    • Cicla através de 3 formatos por MFD
    • Permite acesso rápido a FCR, TGP, HSD, SMS

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

AVISOS / LIMITAÇÕES CRÍTICAS:

   ⚠️  DMS UP só funciona em NAV ou A-G master mode
   ⚠️  DMS UP rejeitado se HUD está em MARK OFLY ou SP (snowplow) ground mode PRE state
   ⚠️  Alguns formatos MFD NÃO permitem SOI (exibem "NOT SOI" no centro) - DMS DOWN pode não mudar nada!
   ⚠️  DMS LEFT/RIGHT NÃO mudam SOI, apenas formato primário do MFD
   ⚠️  DMS é "spring-loaded to center" - sempre retorna ao repouso automaticamente
   ⚠️  Formatos BLANK são pulados automaticamente (DMS LEFT/RIGHT e DOWN cycle)
   ⚠️  Nenhum formato pode ser duplicado entre os 6 slots (LEFT 3 + RIGHT 3)
   ⚠️  DMS NÃO controla radar modes diretamente - use TMS ou OSBs para isso
   ⚠️  DMS NÃO controla weapon selection - use weapon select menus ou OSBs

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

RESUMO RÁPIDO - AS 5 FUNÇÕES:

   DMS UP      → Designa HUD como SOI (NAV/A-G)
   DMS DOWN    → Alterna HUD↔MFD ou LEFT↔RIGHT MFD
   DMS LEFT    → Próximo formato no MFD ESQUERDO
   DMS RIGHT   → Próximo formato no MFD DIREITO
   CENTER      → Posição neutra (spring-loaded)

═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════

FONTE:  TO 1F-16CMAM-34-1-1 BMS (DASH-34-1)
SEÇÕES: 2.1.6.3 (Sensor of Interest SOI)
        2.3.1.2.1.7 (Display Management Switch DMS)
MANUAL DATE: Change 4.38 (BMS 4.38.1)
EXTRACTION DATE: 12 JAN 2026
═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════