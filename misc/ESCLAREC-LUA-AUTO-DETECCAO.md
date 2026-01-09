# Clarificação: Lua Filters, Auto-Detecção e Integração

**Documento de Referência para entender exatamente como funciona a v3.1.0**

---

## 1. ❓ Lua Filters - Já Estão Integrados Automaticamente?

### Resposta: **PARCIALMENTE SIM, mas depende do que você quer dizer**

#### O que acontece na v3.1.0:

```
md-to-docx-v3-1-0.bat EXECUTA:

1. Detecta se docx-enhancements.lua existe ✅
2. Detecta se template-variables.lua existe ✅
3. Se AMBOS existem → Adiciona ao comando Pandoc:
   pandoc input.md -t docx \
     --lua-filter="template-variables.lua" \
     --lua-filter="docx-enhancements.lua" \
     -o output.docx
4. Se NÃO existem → Mostra [INFO] e continua SEM os filtros
```

#### Visualmente:

```
Cenário A: Você TEM os .lua files no projeto root
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
project-root/
├── md-to-docx-v3-1-0.bat ✅ SCRIPT
├── docx-enhancements.lua ✅ PRESENTE
├── template-variables.lua ✅ PRESENTE
├── docs/
│   └── GITHUB-DESKTOP-GUIDE.md
└── guide.tex

Resultado: ✅ Lua filters AUTOMATICAMENTE integrados
           Conversão usa: --lua-filter=template-variables.lua
                         --lua-filter=docx-enhancements.lua

Cenário B: Você NÃO tem os .lua files
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
project-root/
├── md-to-docx-v3-1-0.bat ✅ SCRIPT
├── docs/
│   └── GITHUB-DESKTOP-GUIDE.md
└── guide.tex

Resultado: ⚠️  [INFO] Lua filter nao encontrado
           Conversão continua NORMALMENTE mas SEM filtros
           (Markdown → DOCX funciona, só sem enhancements)
```

### O que significa "Já integrado"?

**NÃO quer dizer:** Os filters estão dentro do `.bat` script

**QUER dizer:** O `.bat` script verifica, detecta e aplica automaticamente se os `.lua` files existem

```batch
REM Dentro do md-to-docx-v3-1-0.bat:

set LUA_ENHANCEMENTS=!LUA_FILTER_DIR!\docx-enhancements.lua
set LUA_VARIABLES=!LUA_FILTER_DIR!\template-variables.lua

if exist "!LUA_ENHANCEMENTS!" (
    set HAS_LUA_FILTERS=Y
    echo [OK] Lua filter detectado
)

REM Depois, ao converter:
if /i "!HAS_LUA_FILTERS!"=="Y" (
    set PANDOC_FILTERS=!PANDOC_FILTERS! --lua-filter="!LUA_VARIABLES!"
    set PANDOC_FILTERS=!PANDOC_FILTERS! --lua-filter="!LUA_ENHANCEMENTS!"
)

REM Então executa:
pandoc input.md -t docx !PANDOC_FILTERS! -o output.docx
```

### ✅ O que você faz:

1. **Coloca os 3 arquivos na raiz do projeto:**
   ```
   md-to-docx-v3-1-0.bat
   docx-enhancements.lua
   template-variables.lua
   ```

2. **Double-click no .bat**

3. **Pronto!** O script já detecta e usa os filters automaticamente

---

## 2. ❓ Auto-Detecta Versão de `version-system-v4-2.md` - Como?

### Resposta: O **template-variables.lua** lê o arquivo

#### O mecanismo:

```lua
-- Em template-variables.lua:

local function load_variables_from_env()
    -- Try to read version from file if env var not set
    if not os.getenv('FALCON_VERSION') then
        local version_file = io.open('docs/version-system-v4-2.md', 'r')
        
        if version_file then
            for line in version_file:lines() do
                -- Procura por linhas que contenham versões tipo "v0.2.2.0"
                if line:match('v[0-9]+%.[0-9]+%.[0-9]+%.[0-9]+') then
                    local version = line:match('v[0-9]+%.[0-9]+%.[0-9]+%.[0-9]+')
                    if version then
                        variables.VERSION = version
                        break  -- Para na primeira versão encontrada
                    end
                end
            end
            version_file:close()
        end
    end
end
```

#### Passo a passo do que acontece:

```
1. Pandoc começa a converter seu .md
2. Encontra ${VERSION} no seu markdown
3. Executa template-variables.lua
4. Lua abre: docs/version-system-v4-2.md
5. Lê linha por linha procurando por "v0.2.2.0" (formato)
6. Encontra a primeira match: "v0.2.2.0"
7. Substitui ${VERSION} por "0.2.2.0"
8. Continua a conversão com valor real
```

#### Exemplo concreto:

**Seu arquivo `docs/version-system-v4-2.md` contém:**

```markdown
# Version System v4.2

Current Active Version: v0.2.2.0
Latest Release: v0.2.2.0 (2026-01-08)
```

**Seu arquivo `docs/GITHUB-DESKTOP-GUIDE.md` contém:**

```markdown
# Guide
Version: ${VERSION}
```

**Pandoc executa:**

```
pandoc GITHUB-DESKTOP-GUIDE.md \
  --lua-filter=template-variables.lua \
  -o GITHUB-DESKTOP-GUIDE.docx
```

**Resultado no DOCX:**

```
# Guide
Version: 0.2.2.0
```

### ⚠️ Importante: A ORDEM e PRECEDÊNCIA

```lua
if not os.getenv('FALCON_VERSION') then
    -- Lê do arquivo
end
```

**Precedência (do maior para menor):**

1. **Variável de ambiente FALCON_VERSION** (se você setou)
   ```batch
   set FALCON_VERSION=0.3.0.0
   md-to-docx-v3-1-0.bat
   ```
   → Usa `0.3.0.0` (ignora o arquivo)

2. **Lê de `version-system-v4-2.md`** se env var não existir
   → Usa versão do arquivo

3. **Valor padrão em código** se arquivo não existir
   ```lua
   VERSION = os.getenv('FALCON_VERSION') or '0.2.2.0'
   ```
   → Usa `0.2.2.0` (fallback)

---

## 3. ❓ Auto-Detecta `.lua` Files no Projeto - Não Entendi

### Resposta: O **BAT script procura pelos arquivos antes de converter**

#### O mecanismo no `md-to-docx-v3-1-0.bat`:

```batch
REM ========================================================================
REM STEP 1.5: Check for Lua Filters
REM ========================================================================

set HAS_LUA_FILTERS=N

REM Procura por docx-enhancements.lua
if exist "!LUA_ENHANCEMENTS!" (
    color 0A
    echo [OK] Lua filter detectado / Lua filter found: docx-enhancements.lua
    color 0F
    set HAS_LUA_FILTERS=Y
) else (
    color 0E
    echo [INFO] Lua filter nao encontrado / Lua filter not found
    echo        Conversao continuara sem filtros avancados
    color 0F
)

REM Procura por template-variables.lua
if exist "!LUA_VARIABLES!" (
    color 0A
    echo [OK] Filtro de variaveis detectado / Variables filter found
    color 0F
    set HAS_LUA_FILTERS=Y
) else (
    color 0E
    echo [INFO] Filtro de variaveis nao encontrado / Variables filter not found
    color 0F
)
```

#### O que significa "auto-detecta"?

```
Auto-detecta = Script verifica automaticamente ANTES de converter

NÃO quer dizer: Procura em pastas estranhas ou internet
SIM quer dizer: Procura no project-root (pasta onde o .bat está)
```

#### Visualmente, o fluxo é:

```
┌─────────────────────────────────────────────────────────────┐
│  INICIO: Você duplo-clica em md-to-docx-v3-1-0.bat        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Script detecta Project Root (pasta do .bat)               │
│  PROJECT_ROOT = C:\Meu Projeto                            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│  Script verifica se existem:                               │
│  - PROJECT_ROOT\docx-enhancements.lua ❓                  │
│  - PROJECT_ROOT\template-variables.lua ❓                 │
│  - PROJECT_ROOT\docs\ (pasta) ❓                           │
└─────────────────────────────────────────────────────────────┘
                              ↓
            ┌─────────────────┴─────────────────┐
            ↓                                   ↓
    ✅ AMBOS existem           ❌ Pelo menos um falta
    HAS_LUA_FILTERS=Y          HAS_LUA_FILTERS=N
            ↓                                   ↓
    [OK] Lua filters detected  [INFO] Filters not found
    Será usar os filtros       Continuará sem filtros
```

#### Código técnico:

```batch
REM Isso define onde procurar:
cd /d "%~dp0" >nul 2>&1              REM Muda para pasta do .bat
set PROJECT_ROOT=%CD%               REM PROJECT_ROOT = pasta atual
set LUA_FILTER_DIR=!PROJECT_ROOT!   REM Procura na raiz do projeto

REM Isso verifica:
set LUA_ENHANCEMENTS=!LUA_FILTER_DIR!\docx-enhancements.lua
set LUA_VARIABLES=!LUA_FILTER_DIR!\template-variables.lua

if exist "!LUA_ENHANCEMENTS!" (     REM Se docx-enhancements.lua existe
    set HAS_LUA_FILTERS=Y
)
```

#### Exemplo real:

```
Seu projeto estrutura:

C:\Users\carlos\Projects\falcon-bms-guide\
├── md-to-docx-v3-1-0.bat ✅ SCRIPT (aqui)
├── docx-enhancements.lua ✅ DETECTADO
├── template-variables.lua ✅ DETECTADO
└── docs/

Quando você duplo-clica em md-to-docx-v3-1-0.bat:

1. Script detecta: PROJECT_ROOT = C:\Users\carlos\Projects\falcon-bms-guide
2. Script procura em PROJECT_ROOT:
   - C:\Users\carlos\Projects\falcon-bms-guide\docx-enhancements.lua ✅ ENCONTRADO
   - C:\Users\carlos\Projects\falcon-bms-guide\template-variables.lua ✅ ENCONTRADO
3. Script seta: HAS_LUA_FILTERS=Y
4. Script mostra: [OK] Lua filter detectado
5. Script prepara: PANDOC_FILTERS=--lua-filter="docx-enhancements.lua" ...
6. Script executa: pandoc ... !PANDOC_FILTERS! ...
```

---

## 4. RESUMO: Os 3 Conceitos Juntos

```
┌─────────────────────────────────────────────────────────────┐
│  CONCEITO 1: Integração Automática                          │
│  "Lua Filters já estão integrados ao .bat"                 │
│  ✅ SIM: O .bat script automaticamente:                     │
│     - Detecta se .lua files existem                         │
│     - Se sim: adiciona --lua-filter ao Pandoc              │
│     - Se não: continua sem filters                          │
│  ❌ NÃO quer dizer: Estão DENTRO do arquivo .bat            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  CONCEITO 2: Leitura de version-system-v4-2.md            │
│  "Auto-detecta versão"                                      │
│  ✅ SIM: template-variables.lua:                            │
│     - Abre docs/version-system-v4-2.md                     │
│     - Lê linha por linha                                    │
│     - Procura por "v0.2.2.0" (formato)                     │
│     - Substitui ${VERSION} por valor encontrado            │
│  ❌ NÃO é "mágica": É Lua file que lê o markdown           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  CONCEITO 3: Auto-Detecção de .lua Files                   │
│  "Auto-detecta .lua files no projeto"                      │
│  ✅ SIM: .bat script:                                       │
│     - Detecta sua própria pasta (PROJECT_ROOT)             │
│     - Verifica se docx-enhancements.lua existe             │
│     - Verifica se template-variables.lua existe            │
│     - Se SIM: prepara PANDOC_FILTERS com --lua-filter      │
│     - Se NÃO: mostra [INFO] e continua                     │
│  ❌ NÃO procura em Internet/outras pastas                   │
└─────────────────────────────────────────────────────────────┘
```

---

## 5. Fluxo Completo de UMA Conversão

```
Você digita: C:\Project> md-to-docx-v3-1-0.bat
             E escolhe Opção 2: Converter docs/
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ Script verifica PROJECT_ROOT (C:\Project)                    │
│ - Encontra: docx-enhancements.lua ✅                         │
│ - Encontra: template-variables.lua ✅                        │
│ - Set HAS_LUA_FILTERS=Y                                      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ Script prepara PANDOC_FILTERS:                               │
│ PANDOC_FILTERS = --lua-filter="template-variables.lua" \    │
│                  --lua-filter="docx-enhancements.lua"        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ Script encontra GITHUB-DESKTOP-GUIDE.md em docs/             │
│ Arquivo contém: Version: ${VERSION}                          │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ Script executa:                                              │
│                                                              │
│ pandoc GITHUB-DESKTOP-GUIDE.md \                            │
│   -t docx \                                                  │
│   --lua-filter="template-variables.lua" \                   │
│   --lua-filter="docx-enhancements.lua" \                    │
│   --citeproc -f markdown-smart \                            │
│   -o GITHUB-DESKTOP-GUIDE.docx                              │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ PANDOC EXECUTA:                                              │
│                                                              │
│ 1. Carrega template-variables.lua                            │
│    → Abre docs/version-system-v4-2.md                       │
│    → Encontra "v0.2.2.0"                                    │
│    → Substitui ${VERSION} por "0.2.2.0"                     │
│                                                              │
│ 2. Carrega docx-enhancements.lua                             │
│    → Melhora renderização de tabelas                        │
│    → Preserva código, links, citations                      │
│                                                              │
│ 3. Renderiza Markdown para DOCX                              │
│    → Usa template.docx se existir                           │
│    → Aplica estilos                                         │
│                                                              │
│ 4. Salva GITHUB-DESKTOP-GUIDE.docx                           │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│ RESULTADO:                                                   │
│                                                              │
│ GITHUB-DESKTOP-GUIDE.docx ✅                                 │
│ Contém: Version: 0.2.2.0 (automaticamente substituído)      │
│ Com: Tabelas melhoradas, código formatado, etc.             │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. O Que Você Precisa Fazer

### Passo 1: Baixar 3 Arquivos

- `md-to-docx-v3-1-0.bat` [44]
- `docx-enhancements.lua` [42]
- `template-variables.lua` [43]

### Passo 2: Colocar na Raiz do Projeto

```
C:\Projects\falcon-bms-guide\
├── md-to-docx-v3-1-0.bat ← Coloca aqui
├── docx-enhancements.lua ← Coloca aqui
├── template-variables.lua ← Coloca aqui
├── guide.tex
├── docs/
│   ├── GITHUB-DESKTOP-GUIDE.md
│   ├── version-system-v4-2.md
│   └── ...
```

### Passo 3: Duplo-Clique e Escolha Opção 2

```
Double-click: md-to-docx-v3-1-0.bat
              ↓
Menu apareça:
  1. Convert single file
  2. Convert docs/ folder ← ESCOLHE AQUI
  3. ...
```

### Passo 4: Pronto!

O script:
- ✅ Detecta os .lua files
- ✅ Executa Pandoc com os filters
- ✅ Substitui ${VERSION}, ${DATE}, etc.
- ✅ Salva DOCX em docs/

---

## 7. Testando Tudo

Crie um arquivo de teste em `docs/TEST.md`:

```markdown
# Teste de Variáveis

Projeto: ${PROJECT}
Versão: ${VERSION}
Data: ${DATE}
Autor: ${AUTHOR}
Fase: ${PHASE}
Tempo: ${DATETIME}

## Tabela de Teste

| Coluna 1 | Coluna 2 |
|----------|----------|
| Valor A  | Valor B  |

## Código de Teste

\`\`\`python
def hello():
    print("World")
\`\`\`
```

Então:

1. Duplo-clique `md-to-docx-v3-1-0.bat`
2. Escolha Opção 2
3. Abra `docs/TEST.docx`

Resultado esperado:

```
Projeto: Falcon BMS TMS/DMS/CMS Guide ✅ (auto-substituído)
Versão: 0.2.2.0 ✅ (auto-lido de version-system)
Data: 2026-01-09 ✅ (auto-data do sistema)
Autor: Carlos Nader ✅ (padrão no .lua)
Fase: Pre-Publication (0.x.x.x) ✅ (auto-detectado)
Tempo: 2026-01-09 11:43:00 ✅ (data/hora do sistema)

Tabela: Formatada, bem-alinhada ✅
Código: Monospace, destaque de sintaxe ✅
```

---

**Ficou claro agora?** 😊 Qual parte você quer que eu expanda mais?

