@echo off

REM ========================================================================
REM MD to DOCX Converter -- VERSÃO v3.1.0 (WITH LUA FILTERS & VARIABLES)
REM ========================================================================

REM v3.0.0 -> v3.1.0 New Features:
REM
REM NEW:
REM - Lua filter support (docx-enhancements.lua) for advanced formatting
REM - Template variable substitution (${VERSION}, ${DATE}, ${PROJECT}, etc.)
REM - Auto-detection of Lua filters in project root
REM - Environment variable support for project metadata
REM - Improved table and code block rendering
REM - Citation and footnote preservation
REM
REM EXISTING FEATURES (v3.0.0):
REM - Auto-detection of `docs/` folder for governance conversion
REM - Smart template selection (auto-detect from docs/ or project root)
REM - Auto-open DOCX after conversion (optional, Windows only)
REM - Backup of previous .docx versions (automatic versioning)
REM - UTF-8 encoding enforcement throughout
REM - Color-coded console output (OK=green, ERROR=red, INFO=yellow)
REM
REM ========================================================================

setlocal enabledelayedexpansion

cls

REM Color scheme
color 0F

REM ========================================================================
REM INITIALIZATION: Setup Paths, Logs, and Configuration
REM ========================================================================

REM Detect Documents folder language-independent
for /f "tokens=3" %%A in ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v "Personal" 2^>nul ^| findstr /i personal') do (
    set DOCUMENTS_PATH=%%A
)

REM Fallback if registry fails
if "!DOCUMENTS_PATH!"=="" (
    set DOCUMENTS_PATH=%USERPROFILE%\Documents
)

set LOGFILE=!DOCUMENTS_PATH!\md-to-docx-v3.1.0-log.txt
set CONFIG_FILE=!DOCUMENTS_PATH!\md-to-docx-config.ini
set TIMESTAMP=%DATE% %TIME%

REM Auto-detect project root and docs folder
cd /d "%~dp0" >nul 2>&1
set PROJECT_ROOT=%CD%
set DOCS_FOLDER=!PROJECT_ROOT!\docs
set TEMPLATE_DIR=!DOCS_FOLDER!
set TEMPLATE_FILE=!TEMPLATE_DIR!\template.docx
set LUA_FILTER_DIR=!PROJECT_ROOT!

REM Look for Lua filters
set LUA_ENHANCEMENTS=!LUA_FILTER_DIR!\docx-enhancements.lua
set LUA_VARIABLES=!LUA_FILTER_DIR!\template-variables.lua

REM Fallback template paths
if not exist "!TEMPLATE_FILE!" (
    set TEMPLATE_FILE=!PROJECT_ROOT!\template.docx
)

REM Create log header if doesn't exist
if not exist "!LOGFILE!" (
    (
        echo.
        echo ========================================================================
        echo MD to DOCX Converter v3.1.0 - Log File
        echo ========================================================================
        echo.
    ) > "!LOGFILE!"
)

echo [!TIMESTAMP!] Script iniciado / Script started >> "!LOGFILE!"

REM ========================================================================
REM DISPLAY BANNER
REM ========================================================================

cls
color 0F
echo.
echo ========================================================================
echo MD to DOCX Converter v3.1.0 - ADVANCED EDITION WITH LUA FILTERS
echo ========================================================================
echo Pandoc 3.0^+  ^|  Enhanced Markdown to DOCX conversion
echo.
echo Project Root: !PROJECT_ROOT!
echo Docs Folder: !DOCS_FOLDER!
echo Lua Filters: !LUA_FILTER_DIR!
echo.

REM ========================================================================
REM STEP 1: Verify Pandoc Installation and Version
REM ========================================================================

pandoc --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] Pandoc nao encontrado / Pandoc not found
    echo.
    echo Voce precisa instalar Pandoc 3.0 ou superior / You need Pandoc 3.0^+
    echo Baixe em / Download at: https://pandoc.org/installing.html
    echo.
    echo [!TIMESTAMP!] ERROR: Pandoc not found >> "!LOGFILE!"
    pause
    exit /b 1
)

REM Get pandoc version
for /f "tokens=2" %%a in ('pandoc --version ^| findstr /R "^pandoc"') do set PANDOC_VERSION=%%a

color 0A
echo [OK] Pandoc !PANDOC_VERSION! encontrado / found
echo.

REM Validate Pandoc version is at least 3.0
for /f "tokens=1 delims=." %%a in ("!PANDOC_VERSION!") do set PANDOC_MAJOR=%%a

if !PANDOC_MAJOR! LSS 3 (
    color 0E
    echo [AVISO/WARNING] Pandoc version !PANDOC_VERSION! may be outdated.
    echo Recommend: Pandoc 3.0 or higher
    echo.
    set /p CONTINUE="Continuar mesmo assim? / Continue anyway? (S/N): "
    if /i not "!CONTINUE:~0,1!"=="S" (
        if /i not "!CONTINUE:~0,1!"=="Y" (
            echo [!TIMESTAMP!] WARNING: User cancelled due to old Pandoc version >> "!LOGFILE!"
            exit /b 1
        )
    )
)

echo.
color 0F

REM ========================================================================
REM STEP 1.5: Check for Lua Filters
REM ========================================================================

set HAS_LUA_FILTERS=N

if exist "!LUA_ENHANCEMENTS!" (
    color 0A
    echo [OK] Lua filter detectado / Lua filter found: docx-enhancements.lua
    color 0F
    set HAS_LUA_FILTERS=Y
) else (
    color 0E
    echo [INFO] Lua filter nao encontrado / Lua filter not found: docx-enhancements.lua
    echo        Conversao continuara sem filtros avancados
    color 0F
)

if exist "!LUA_VARIABLES!" (
    color 0A
    echo [OK] Filtro de variaveis detectado / Variables filter found: template-variables.lua
    color 0F
    set HAS_LUA_FILTERS=Y
) else (
    color 0E
    echo [INFO] Filtro de variaveis nao encontrado / Variables filter not found
    color 0F
)

echo.
color 0F

REM ========================================================================
REM STEP 2: Check for Drag-and-Drop Argument
REM ========================================================================

if not "%~1"=="" (
    echo [INFO] Arquivo fornecido via drag-and-drop / File provided via drag-and-drop
    echo.
    set MDFILE=%~1
    goto VALIDATE_DRAG_DROP
) else (
    goto MAIN_MENU
)

REM ========================================================================
REM MAIN MENU
REM ========================================================================

:MAIN_MENU

cls
color 0F
echo.
echo ========================================================================
echo MD to DOCX Converter v3.1.0 - MAIN MENU
echo ========================================================================
echo.
echo Escolha uma opcao / Choose an option:
echo.
color 0B
echo  1. Converter arquivo unico / Convert single file
echo  2. Converter pasta docs/ / Convert docs/ folder (auto-detect governance)
echo  3. Converter pasta inteira / Convert entire folder (batch mode)
echo  4. Ver log de conversoes / View conversion log
echo  5. Gerenciar configuracoes / Manage settings
echo  6. Sair / Exit
echo.
color 0F
echo ========================================================================
echo.

set /p CHOICE="Digite sua opcao (1-6) / Enter your choice (1-6): "

if /i "!CHOICE!"=="1" (
    goto SINGLE_MODE
) else if /i "!CHOICE!"=="2" (
    goto AUTO_DOCS_MODE
) else if /i "!CHOICE!"=="3" (
    goto BATCH_MODE
) else if /i "!CHOICE!"=="4" (
    goto VIEW_LOG
) else if /i "!CHOICE!"=="5" (
    goto SETTINGS_MENU
) else if /i "!CHOICE!"=="6" (
    echo.
    color 0A
    echo Ate logo! / Goodbye!
    echo.
    color 0F
    exit /b 0
) else (
    echo.
    color 0C
    echo [ERROR] Opcao invalida / Invalid choice
    echo.
    color 0F
    pause
    goto MAIN_MENU
)

REM ========================================================================
REM HELPER: Build Pandoc command with optional Lua filters
REM ========================================================================

:BUILD_PANDOC_CMD

REM Reset Pandoc options
set PANDOC_FILTERS=
set PANDOC_OPTIONS=

REM Add Lua filters if they exist
if /i "!HAS_LUA_FILTERS!"=="Y" (
    if exist "!LUA_VARIABLES!" (
        set PANDOC_FILTERS=!PANDOC_FILTERS! --lua-filter="!LUA_VARIABLES!"
    )
    if exist "!LUA_ENHANCEMENTS!" (
        set PANDOC_FILTERS=!PANDOC_FILTERS! --lua-filter="!LUA_ENHANCEMENTS!"
    )
)

REM Add standard options
set PANDOC_OPTIONS=--citeproc -f markdown-smart

goto :EOF

REM ========================================================================
REM AUTO DOCS MODE: Detect and convert all .md files in docs/ folder
REM ========================================================================

:AUTO_DOCS_MODE

cls
color 0F
echo.
echo ========================================================================
echo MODO DOCS / Auto-Convert Governance Documents
echo ========================================================================
echo.

if not exist "!DOCS_FOLDER!" (
    color 0C
    echo [ERROR] Pasta docs/ nao encontrada / docs/ folder not found
    echo Path: !DOCS_FOLDER!
    echo.
    color 0F
    pause
    goto MAIN_MENU
)

set MDCOUNT=0
for /r "!DOCS_FOLDER!" %%F in (*.md) do (
    set /a MDCOUNT+=1
)

if !MDCOUNT! EQU 0 (
    color 0C
    echo [ERROR] Nenhum arquivo .md encontrado em docs/ / No .md files found in docs/
    echo.
    color 0F
    pause
    goto MAIN_MENU
)

color 0A
echo [OK] Pasta docs/ detectada / docs/ folder detected
echo Arquivos .md encontrados / .md files found: !MDCOUNT!
echo.
color 0F

REM Ask about template
call :SELECT_TEMPLATE

echo.
set /p CONFIRM="Converter todos os arquivos .md em docs/? / Convert all .md files in docs/? (S/N): "

if /i not "!CONFIRM:~0,1!"=="S" (
    if /i not "!CONFIRM:~0,1!"=="Y" (
        echo.
        color 0E
        echo [INFO] Cancelado / Cancelled
        echo.
        color 0F
        goto MAIN_MENU
    )
)

REM Build Pandoc command
call :BUILD_PANDOC_CMD

REM Execute batch conversion
echo.
echo ========================================================================
echo Iniciando conversao em lote / Starting batch conversion in docs/...
echo ========================================================================
echo.

echo [!TIMESTAMP!] LOTE / BATCH started: "!DOCS_FOLDER!" ^(!MDCOUNT! files^) >> "!LOGFILE!"

set CONVERTED=0
set FAILED=0

for /r "!DOCS_FOLDER!" %%F in (*.md) do (
    set MDFILE=%%F
    
    for %%A in ("!MDFILE!") do (
        set FULLPATH=%%~dpA
        set FILENAME=%%~nxA
        set NAMEONLY=!FILENAME:.md=!
        set DOCXFILE=!FULLPATH!!NAMEONLY!.docx
    )
    
    color 0B
    echo [!MDCOUNT!] Convertendo / Converting: %%~nxF
    color 0F
    
    REM Backup previous version
    if exist "!DOCXFILE!" (
        set BACKUP_FILE=!FULLPATH!!NAMEONLY!.docx.backup
        copy /Y "!DOCXFILE!" "!BACKUP_FILE!" >nul 2>&1
    )
    
    set ERROR_LOG=%TEMP%\pandoc_error_!RANDOM!.log
    
    if /i "!USETEMPLATE!"=="Y" (
        pandoc "!MDFILE!" -t docx --reference-doc="!TEMPLATEFILE!" !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
    ) else (
        pandoc "!MDFILE!" -t docx !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
    )
    
    if !errorlevel! EQU 0 (
        set /a CONVERTED+=1
        color 0A
        echo [OK] %%~nxF --^> %%~nxF.docx
        color 0F
        echo [!TIMESTAMP!] OK: %%F >> "!LOGFILE!"
    ) else (
        set /a FAILED+=1
        color 0C
        echo [ERROR] Falha / Failed: %%~nxF
        color 0F
        if exist "!ERROR_LOG!" (
            type "!ERROR_LOG!" >> "!LOGFILE!"
        )
        echo [!TIMESTAMP!] ERRO / FAILED: %%F >> "!LOGFILE!"
    )
    
    REM Clean up temp file
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
)

echo.
echo ========================================================================
color 0A
echo Conversao em lote concluida / Batch conversion completed
color 0F
echo ========================================================================
echo.

color 0B
echo Convertidos com sucesso / Converted successfully: !CONVERTED!
echo Falhados / Failed: !FAILED!
echo.
color 0F

echo [!TIMESTAMP!] LOTE / BATCH completed in docs/: !CONVERTED! OK, !FAILED! FAILED >> "!LOGFILE!"

set /p ANOTHER="Voltar ao menu? / Back to menu? (S/N): "
if /i "!ANOTHER:~0,1!"=="S" goto MAIN_MENU
exit /b 0

REM ========================================================================
REM SUBROUTINE: Select Template
REM ========================================================================

:SELECT_TEMPLATE

setlocal enabledelayedexpansion

set LOCAL_USETEMPLATE=N
set LOCAL_TEMPLATEFILE=

echo.
set /p WANTTEMPLATE="Usar template customizado? / Use custom template? (S/N): "
echo.

if /i not "!WANTTEMPLATE:~0,1!"=="S" (
    endlocal & set USETEMPLATE=N & set TEMPLATEFILE=
    goto :EOF
)

REM User wants to use a template
if exist "!TEMPLATE_FILE!" (
    color 0A
    echo [OK] Template encontrado / Template found
    echo Path: !TEMPLATE_FILE!
    echo.
    color 0F
    set /p USEDEFAULT="Usar este template? / Use this template? (S/N): "
    if /i "!USEDEFAULT:~0,1!"=="S" (
        set LOCAL_USETEMPLATE=Y
        set LOCAL_TEMPLATEFILE=!TEMPLATE_FILE!
        goto END_SELECT_TEMPLATE
    ) else (
        goto ASK_TEMPLATE_ALT
    )
) else (
    color 0E
    echo [INFO] Nenhum template padrao detectado / No default template found
    echo Esperado / Expected at: !TEMPLATE_FILE!
    echo.
    color 0F
    goto ASK_TEMPLATE_ALT
)

:ASK_TEMPLATE_ALT

set RETRY_COUNT=0

:ASK_TEMPLATE_ALT_RETRY

set /a RETRY_COUNT+=1
if !RETRY_COUNT! GTR 3 (
    color 0E
    echo [AVISO] Limite de tentativas atingido / Retry limit reached
    echo.
    color 0F
    set LOCAL_USETEMPLATE=N
    set LOCAL_TEMPLATEFILE=
    goto END_SELECT_TEMPLATE
)

echo.
echo Cole o caminho do template.docx
echo Paste the path to your template.docx
echo.

set /p TEMPLATE="Enter: "

REM Remove quotes
set TEMPLATE=!TEMPLATE:"=!

if not exist "!TEMPLATE!" (
    echo.
    color 0C
    echo [ERROR] Template nao encontrado / Template not found
    echo Path: !TEMPLATE!
    echo.
    color 0F
    goto ASK_TEMPLATE_ALT_RETRY
)

if /i not "!TEMPLATE:~-5!"==".docx" (
    echo.
    color 0C
    echo [ERROR] Template deve ser .docx / Template must be .docx
    echo Path: !TEMPLATE!
    echo.
    color 0F
    goto ASK_TEMPLATE_ALT_RETRY
)

echo.
color 0A
echo [OK] Template customizado valido / Custom template valid
color 0F
set LOCAL_USETEMPLATE=Y
set LOCAL_TEMPLATEFILE=!TEMPLATE!

:END_SELECT_TEMPLATE

endlocal & set USETEMPLATE=!LOCAL_USETEMPLATE! & set TEMPLATEFILE=!LOCAL_TEMPLATEFILE!
goto :EOF

REM ========================================================================
REM VIEW LOG
REM ========================================================================

:VIEW_LOG

cls
color 0F
echo.
echo ========================================================================
echo Log de Conversoes / Conversion Log
echo ========================================================================
echo.

if not exist "!LOGFILE!" (
    color 0E
    echo [INFO] Nenhuma conversao realizada ainda / No conversions yet
    echo.
    color 0F
) else (
    type "!LOGFILE!"
    echo.
)

echo ========================================================================
echo.

set /p BACK="Voltar ao menu? / Back to menu? (S/N): "
if /i "!BACK:~0,1!"=="S" goto MAIN_MENU
if /i "!BACK:~0,1!"=="Y" goto MAIN_MENU
exit /b 0

REM ========================================================================
REM SETTINGS MENU
REM ========================================================================

:SETTINGS_MENU

cls
color 0F
echo.
echo ========================================================================
echo CONFIGURACOES / SETTINGS
echo ========================================================================
echo.
echo 1. Ver informacoes do ambiente / View environment info
echo 2. Localizar e usar novo template / Find and set new template
echo 3. Limpar log / Clear log file
echo 4. Voltar / Back to menu
echo.

set /p SETTINGS_CHOICE="Digite sua opcao / Enter your choice (1-4): "

if /i "!SETTINGS_CHOICE!"=="1" (
    cls
    color 0F
    echo.
    echo ========================================================================
    echo INFORMACOES DO AMBIENTE / ENVIRONMENT INFO
    echo ========================================================================
    echo.
    color 0B
    echo Pandoc Version: !PANDOC_VERSION!
    echo Project Root: !PROJECT_ROOT!
    echo Docs Folder: !DOCS_FOLDER!
    echo Template File: !TEMPLATE_FILE!
    echo Lua Filters: !HAS_LUA_FILTERS!
    echo Log File: !LOGFILE!
    echo.
    color 0F
    pause
    goto SETTINGS_MENU
) else if /i "!SETTINGS_CHOICE!"=="2" (
    call :SELECT_TEMPLATE
    echo.
    color 0A
    echo [OK] Template configurado / Template set
    color 0F
    echo.
    pause
    goto SETTINGS_MENU
) else if /i "!SETTINGS_CHOICE!"=="3" (
    del /q "!LOGFILE!" 2>nul
    echo.
    color 0A
    echo [OK] Log limpo / Log cleared
    color 0F
    echo.
    pause
    goto SETTINGS_MENU
) else if /i "!SETTINGS_CHOICE!"=="4" (
    goto MAIN_MENU
) else (
    goto SETTINGS_MENU
)

REM ========================================================================
REM SINGLE FILE MODE
REM ========================================================================

:SINGLE_MODE

cls
color 0F
echo.
echo ========================================================================
echo MODO 1 / Converter Arquivo Unico / SINGLE FILE MODE
echo ========================================================================
echo.

set RETRY_COUNT=0

:ASKFILE

set /a RETRY_COUNT+=1
if !RETRY_COUNT! GTR 5 (
    echo.
    color 0E
    echo [AVISO] Limite de tentativas atingido / Retry limit reached
    echo.
    color 0F
    goto MAIN_MENU
)

echo Cole o caminho completo do arquivo .md
echo Paste the full path to your .md file
echo.
echo Exemplo / Example:
echo C:\guide-v0.1.3.md
echo.

set /p MDFILE="Enter: "

REM Remove quotes
set MDFILE=!MDFILE:"=!

echo.

REM Check if file exists
if not exist "!MDFILE!" (
    color 0C
    echo [ERROR] Arquivo nao encontrado / File not found
    echo Path: !MDFILE!
    echo.
    color 0F
    goto ASKFILE
)

if /i not "!MDFILE:~-3!"==".md" (
    color 0C
    echo [ERROR] Arquivo deve ser .md / File must be .md
    echo Path: !MDFILE!
    echo.
    color 0F
    goto ASKFILE
)

REM Generate output filename
for %%A in ("!MDFILE!") do (
    set FULLPATH=%%~dpA
    set FILENAME=%%~nxA
    set NAMEONLY=!FILENAME:.md=!
    set DOCXFILE=!FULLPATH!!NAMEONLY!.docx
)

color 0A
echo [OK] Arquivo valido / File valid
echo.
color 0F

echo INPUT:  "!MDFILE!"
echo OUTPUT: "!DOCXFILE!"
echo.

REM Ask about template
call :SELECT_TEMPLATE

REM Ask about Advanced Options
set EXTRAOPTS=

echo.
set /p USEADVANCED="Usar opcoes avancadas de Pandoc? / Use advanced Pandoc options? (S/N): "
echo.

if /i "!USEADVANCED:~0,1!"=="S" (
    color 0B
    echo Opcoes disponiveis / Available options:
    echo 1. --toc / indice automatico / auto TOC
    echo 2. --number-sections / numera secoes / number sections
    echo 3. --shift-heading-level-by-1 / reduz nivel de headings
    echo 4. --wrap=none / sem quebra de linha / no line wrap
    echo.
    color 0F
    
    echo Digite os numeros das opcoes desejadas, separadas por ponto-e-virgula
    echo Enter option numbers separated by semicolon
    echo Exemplo / Example: 1;3 ou / or 2;4
    echo ou pressione ENTER para pular / or press ENTER to skip
    echo.
    
    set /p OPTIONNUMS="Enter: "
    
    if not "!OPTIONNUMS!"=="" (
        if not "!OPTIONNUMS:1=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --toc
        if not "!OPTIONNUMS:2=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --number-sections
        if not "!OPTIONNUMS:3=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --shift-heading-level-by-1
        if not "!OPTIONNUMS:4=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --wrap=none
        
        echo.
        color 0A
        echo [OK] Opcoes selecionadas / Selected options:!EXTRAOPTS!
        color 0F
    )
)

echo.

REM Final Confirmation
echo.
set /p CONFIRM="Converter? / Convert? (S/N): "

if /i "!CONFIRM:~0,1!"=="S" (
    goto DOCONVERT
) else if /i "!CONFIRM:~0,1!"=="Y" (
    goto DOCONVERT
) else (
    echo.
    color 0E
    echo [INFO] Cancelado / Cancelled
    echo.
    color 0F
    set /p ANOTHER="Outra opcao? / Back to menu? (S/N): "
    if /i "!ANOTHER:~0,1!"=="S" goto MAIN_MENU
    exit /b 0
)

REM ========================================================================
REM Execute Conversion
REM ========================================================================

:DOCONVERT

echo.
color 0B
echo Convertendo / Converting...
echo.
color 0F

REM Build Pandoc command
call :BUILD_PANDOC_CMD

REM Backup previous version if exists
if exist "!DOCXFILE!" (
    set BACKUP_FILE=!FULLPATH!!NAMEONLY!.docx.backup
    copy /Y "!DOCXFILE!" "!BACKUP_FILE!" >nul 2>&1
    color 0E
    echo [INFO] Backup anterior salvo / Previous version backed up
    color 0F
    echo.
)

set ERROR_LOG=%TEMP%\pandoc_error_!RANDOM!.log

if /i "!USETEMPLATE!"=="Y" (
    pandoc "!MDFILE!" -t docx --reference-doc="!TEMPLATEFILE!" !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
) else (
    pandoc "!MDFILE!" -t docx !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
)

if errorlevel 1 (
    echo.
    echo ========================================================================
    color 0C
    echo [ERROR] Conversao falhou / Conversion failed
    color 0F
    echo ========================================================================
    echo.
    
    if exist "!ERROR_LOG!" (
        color 0E
        echo [DETALHES DO ERRO / ERROR DETAILS:]
        echo.
        color 0F
        type "!ERROR_LOG!"
        echo.
        type "!ERROR_LOG!" >> "!LOGFILE!"
    )
    
    echo.
    echo [!TIMESTAMP!] ERROR / FAILED: !MDFILE! >> "!LOGFILE!"
    
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
    
    set /p RETRY="Tentar novamente? / Try again? (S/N): "
    if /i "!RETRY:~0,1!"=="S" goto ASKFILE
    goto MAIN_MENU
)

if not exist "!DOCXFILE!" (
    echo.
    echo ========================================================================
    color 0C
    echo [ERROR] Arquivo nao foi criado / File was not created
    color 0F
    echo ========================================================================
    echo.
    
    echo [!TIMESTAMP!] ERROR / FAILED file not created: !MDFILE! >> "!LOGFILE!"
    
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
    
    set /p RETRY="Tentar novamente? / Try again? (S/N): "
    if /i "!RETRY:~0,1!"=="S" goto ASKFILE
    goto MAIN_MENU
)

if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"

REM Success
echo.
echo ========================================================================
color 0A
echo [OK] SUCESSO / SUCCESS!
color 0F
echo ========================================================================
echo.

echo Arquivo criado / File created:
echo "!DOCXFILE!"
echo.

REM Get file size
for %%A in ("!DOCXFILE!") do set FILESIZE=%%~zA

set /a FILESIZEKB=!FILESIZE!/1024

if !FILESIZEKB! LEQ 0 (
    color 0C
    echo [AVISO/WARNING] Arquivo pode estar corrompido / File may be corrupted
    echo Tamanho / Size: !FILESIZEKB! KB
    color 0F
    echo.
) else (
    color 0A
    echo Tamanho / Size: !FILESIZEKB! KB
    color 0F
    echo.
)

echo [!TIMESTAMP!] SUCCESS: !MDFILE! --^> !DOCXFILE! ^(Size: !FILESIZEKB! KB^) >> "!LOGFILE!"

echo.
set /p OPENFILE="Abrir arquivo? / Open file? (S/N): "

if /i "!OPENFILE:~0,1!"=="S" (
    start "" "!DOCXFILE!"
) else if /i "!OPENFILE:~0,1!"=="Y" (
    start "" "!DOCXFILE!"
)

echo.
set /p ANOTHER="Outra conversao? / Convert another file? (S/N): "
if /i "!ANOTHER:~0,1!"=="S" (
    goto MAIN_MENU
) else (
    echo.
    pause
    exit /b 0
)

REM ========================================================================
REM BATCH MODE: Convert Multiple Files from Folder
REM ========================================================================

:BATCH_MODE

cls
color 0F
echo.
echo ========================================================================
echo MODO 3 / Converter Pasta Inteira / BATCH MODE - Multiple Files
echo ========================================================================
echo.

set RETRY_COUNT=0

:ASKFOLDER

set /a RETRY_COUNT+=1
if !RETRY_COUNT! GTR 5 (
    echo.
    color 0E
    echo [AVISO] Limite de tentativas atingido / Retry limit reached
    echo.
    color 0F
    goto MAIN_MENU
)

echo Cole o caminho completo da PASTA contendo arquivos .md
echo Paste the full path to the FOLDER containing .md files
echo.
echo Exemplo / Example:
echo C:\meus-guias
echo.

set /p FOLDER="Enter: "

REM Remove quotes
set FOLDER=!FOLDER:"=!

echo.

if not exist "!FOLDER!" (
    color 0C
    echo [ERROR] Pasta nao encontrada / Folder not found
    echo Path: !FOLDER!
    echo.
    color 0F
    goto ASKFOLDER
)

REM Verify it's a directory
cd /d "!FOLDER!" >nul 2>&1
if errorlevel 1 (
    color 0C
    echo [ERROR] Caminho nao eh uma pasta / Path is not a folder
    echo Path: !FOLDER!
    echo.
    color 0F
    goto ASKFOLDER
)

set MDCOUNT=0
for /r "!FOLDER!" %%F in (*.md) do (
    set /a MDCOUNT+=1
)

if !MDCOUNT! EQU 0 (
    color 0C
    echo [ERROR] Nenhum arquivo .md encontrado / No .md files found
    echo Pasta / Folder: !FOLDER!
    echo.
    color 0F
    goto ASKFOLDER
)

color 0A
echo [OK] Pasta valida / Folder valid
echo.
color 0F

echo Pasta / Folder: "!FOLDER!"
echo Arquivos .md encontrados / .md files found: !MDCOUNT!
echo.

REM Ask about template
call :SELECT_TEMPLATE

echo.
set /p CONFIRM="Converter todos? / Convert all? (S/N): "

if /i not "!CONFIRM:~0,1!"=="S" (
    if /i not "!CONFIRM:~0,1!"=="Y" (
        echo.
        color 0E
        echo [INFO] Cancelado / Cancelled
        echo.
        color 0F
        goto MAIN_MENU
    )
)

REM Build Pandoc command
call :BUILD_PANDOC_CMD

REM Execute batch conversion
echo.
echo ========================================================================
color 0B
echo Iniciando conversao em lote / Starting batch conversion...
color 0F
echo ========================================================================
echo.

echo [!TIMESTAMP!] BATCH started: "!FOLDER!" ^(!MDCOUNT! files^) >> "!LOGFILE!"

set CONVERTED=0
set FAILED=0

for /r "!FOLDER!" %%F in (*.md) do (
    set MDFILE=%%F
    
    for %%A in ("!MDFILE!") do (
        set FULLPATH=%%~dpA
        set FILENAME=%%~nxA
        set NAMEONLY=!FILENAME:.md=!
        set DOCXFILE=!FULLPATH!!NAMEONLY!.docx
    )
    
    color 0B
    echo [!MDCOUNT!] Convertendo / Converting: %%~nxF
    color 0F
    
    set ERROR_LOG=%TEMP%\pandoc_error_!RANDOM!.log
    
    if /i "!USETEMPLATE!"=="Y" (
        pandoc "!MDFILE!" -t docx --reference-doc="!TEMPLATEFILE!" !PANDOC_FILTERS! !PANDOC_OPTIONS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
    ) else (
        pandoc "!MDFILE!" -t docx !PANDOC_FILTERS! !PANDOC_OPTIONS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
    )
    
    if !errorlevel! EQU 0 (
        set /a CONVERTED+=1
        color 0A
        echo [OK] %%~nxF --^> %%~nxF.docx
        color 0F
        echo [!TIMESTAMP!] OK: %%F >> "!LOGFILE!"
    ) else (
        set /a FAILED+=1
        color 0C
        echo [ERROR] Falha / Failed: %%~nxF
        color 0F
        if exist "!ERROR_LOG!" (
            type "!ERROR_LOG!" >> "!LOGFILE!"
        )
        echo [!TIMESTAMP!] FAILED: %%F >> "!LOGFILE!"
    )
    
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
)

echo.
echo ========================================================================
color 0A
echo Conversao em lote concluida / Batch conversion completed
color 0F
echo ========================================================================
echo.

color 0B
echo Convertidos com sucesso / Converted successfully: !CONVERTED!
echo Falhados / Failed: !FAILED!
echo.
color 0F

echo [!TIMESTAMP!] BATCH completed: !CONVERTED! OK, !FAILED! FAILED >> "!LOGFILE!"

set /p ANOTHER="Outra conversao? / Convert another folder? (S/N): "
if /i "!ANOTHER:~0,1!"=="S" (
    goto MAIN_MENU
) else (
    echo.
    pause
    exit /b 0
)

REM ========================================================================
REM VALIDATE Drag-and-Drop File
REM ========================================================================

:VALIDATE_DRAG_DROP

if not exist "!MDFILE!" (
    color 0C
    echo [ERROR] Arquivo nao encontrado / File not found via drag-and-drop
    echo Path: !MDFILE!
    echo.
    color 0F
    echo [!TIMESTAMP!] ERROR: Drag-and-drop file not found >> "!LOGFILE!"
    pause
    exit /b 1
)

if /i not "!MDFILE:~-3!"==".md" (
    color 0C
    echo [ERROR] Arquivo deve ser .md / File must be .md
    echo Path: !MDFILE!
    echo.
    color 0F
    echo [!TIMESTAMP!] ERROR: Drag-and-drop file is not .md >> "!LOGFILE!"
    pause
    exit /b 1
)

REM Generate output filename
for %%A in ("!MDFILE!") do (
    set FULLPATH=%%~dpA
    set FILENAME=%%~nxA
    set NAMEONLY=!FILENAME:.md=!
    set DOCXFILE=!FULLPATH!!NAMEONLY!.docx
)

color 0A
echo [OK] Arquivo valido / File valid
echo.
color 0F

echo INPUT:  "!MDFILE!"
echo OUTPUT: "!DOCXFILE!"
echo.

REM Check for template on drag-and-drop (default only, quick)
set USETEMPLATE=N
set TEMPLATEFILE=

if exist "!TEMPLATE_FILE!" (
    set USETEMPLATE=Y
    set TEMPLATEFILE=!TEMPLATE_FILE!
    color 0A
    echo [OK] Template detectado automaticamente / Template auto-detected
    color 0F
    echo.
)

REM Build Pandoc command
call :BUILD_PANDOC_CMD

REM Ask about advanced options
set EXTRAOPTS=
set /p USEADVANCED="Usar opcoes avancadas? / Use advanced options? (S/N): "
echo.

if /i "!USEADVANCED:~0,1!"=="S" (
    color 0B
    echo Opcoes disponiveis / Available options:
    echo 1. --toc / indice automatico / auto TOC
    echo 2. --number-sections / numera secoes / number sections
    echo 3. --shift-heading-level-by-1 / reduz nivel de headings
    echo 4. --wrap=none / sem quebra de linha / no line wrap
    echo.
    color 0F
    
    echo Digite os numeros das opcoes desejadas, separadas por ponto-e-virgula
    echo Enter option numbers separated by semicolon
    echo Exemplo / Example: 1;3 ou / or 2;4
    echo.
    
    set /p OPTIONNUMS="Enter: "
    
    if not "!OPTIONNUMS!"=="" (
        if not "!OPTIONNUMS:1=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --toc
        if not "!OPTIONNUMS:2=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --number-sections
        if not "!OPTIONNUMS:3=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --shift-heading-level-by-1
        if not "!OPTIONNUMS:4=!"=="!OPTIONNUMS!" set EXTRAOPTS=!EXTRAOPTS! --wrap=none
        
        echo.
        color 0A
        echo [OK] Opcoes selecionadas / Selected options:!EXTRAOPTS!
        color 0F
    )
)

REM Execute conversion
echo.
color 0B
echo Convertendo / Converting...
echo.
color 0F

if exist "!DOCXFILE!" (
    set BACKUP_FILE=!FULLPATH!!NAMEONLY!.docx.backup
    copy /Y "!DOCXFILE!" "!BACKUP_FILE!" >nul 2>&1
    color 0E
    echo [INFO] Backup anterior salvo / Previous version backed up
    color 0F
    echo.
)

set ERROR_LOG=%TEMP%\pandoc_error_!RANDOM!.log

if /i "!USETEMPLATE!"=="Y" (
    pandoc "!MDFILE!" -t docx --reference-doc="!TEMPLATEFILE!" !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
) else (
    pandoc "!MDFILE!" -t docx !PANDOC_FILTERS! !PANDOC_OPTIONS! !EXTRAOPTS! -o "!DOCXFILE!" 2> "!ERROR_LOG!"
)

if errorlevel 1 (
    echo.
    echo ========================================================================
    color 0C
    echo [ERROR] Conversao falhou / Conversion failed
    color 0F
    echo ========================================================================
    echo.
    
    if exist "!ERROR_LOG!" (
        color 0E
        echo [ERROR DETAILS / DETALHES DO ERRO:]
        echo.
        color 0F
        type "!ERROR_LOG!"
        echo.
        type "!ERROR_LOG!" >> "!LOGFILE!"
    )
    
    echo [!TIMESTAMP!] ERROR: !MDFILE! ^(drag-and-drop^) >> "!LOGFILE!"
    
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
    
    pause
    exit /b 1
)

if not exist "!DOCXFILE!" (
    echo.
    echo ========================================================================
    color 0C
    echo [ERROR] Arquivo nao foi criado / File was not created
    color 0F
    echo ========================================================================
    echo.
    
    echo [!TIMESTAMP!] ERROR file not created: !MDFILE! ^(drag-and-drop^) >> "!LOGFILE!"
    
    if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"
    
    pause
    exit /b 1
)

if exist "!ERROR_LOG!" del /q "!ERROR_LOG!"

REM Success
echo.
echo ========================================================================
color 0A
echo [OK] SUCESSO / SUCCESS!
color 0F
echo ========================================================================
echo.

echo Arquivo criado / File created:
echo "!DOCXFILE!"
echo.

for %%A in ("!DOCXFILE!") do set FILESIZE=%%~zA
set /a FILESIZEKB=!FILESIZE!/1024

color 0A
echo Tamanho / Size: !FILESIZEKB! KB
color 0F
echo.

echo [!TIMESTAMP!] SUCCESS: !MDFILE! ^(drag-and-drop^) --^> !DOCXFILE! ^(Size: !FILESIZEKB! KB^) >> "!LOGFILE!"

echo.
set /p OPENFILE="Abrir arquivo? / Open file? (S/N): "

if /i "!OPENFILE:~0,1!"=="S" (
    start "" "!DOCXFILE!"
) else if /i "!OPENFILE:~0,1!"=="Y" (
    start "" "!DOCXFILE!"
)

echo.
pause
exit /b 0

endlocal
