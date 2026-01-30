Preamble Completo (Pronto para Colar)

```latex
% ============================================================================
% PREAMBLE COMPLETO — TMS/DMS/CMS Usage Guide for Falcon BMS 4.38.1
% Gerado: 29 January 2026
% Status: Novo preâmbulo (report + twoside + titlesec + fancyhdr melhorado + new hotastable ambient)
% ============================================================================

\documentclass[11pt, a4paper, twoside]{report}

% --------------------------------------------------------------------------
% BASIC ENCODING AND LANGUAGE
% --------------------------------------------------------------------------

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}

% --------------------------------------------------------------------------
% FONTS AND MICROTYPOGRAPHY
% --------------------------------------------------------------------------

\usepackage{lmodern}
\usepackage{microtype}

% --------------------------------------------------------------------------
% PAGE GEOMETRY AND LAYOUT
% --------------------------------------------------------------------------

\usepackage{geometry}
\geometry{a4paper, left=2.0cm, right=2.0cm, top=2.5cm, bottom=2.5cm}
\usepackage{setspace}
\onehalfspacing

% --------------------------------------------------------------------------
% COLORS AND LINKS
% --------------------------------------------------------------------------

\usepackage[table]{xcolor}
\definecolor{linkblue}{HTML}{004488}
\definecolor{linkred}{HTML}{882222}
\definecolor{headerblue}{HTML}{003366}
\definecolor{rowgray}{HTML}{F5F5F5}
\definecolor{subheadgray}{HTML}{E0E0E0}

\usepackage{soul}
\usepackage[pdfencoding=auto, psdextra, colorlinks=true, linkcolor=linkblue, citecolor=linkred, urlcolor=linkblue, breaklinks=true]{hyperref}
\usepackage{bookmark}

% ============================================================================
% CAPTION SETUP BY TYPE
% ============================================================================

\usepackage{caption}

% GLOBAL PATTERN
\captionsetup{font=small, labelfont=bf, justification=centering, singlelinecheck=true}
% FIGURES
\captionsetup[figure]{font=footnotesize, labelfont=bf, justification=centering, singlelinecheck=true}
% % TABLE/LONGTABLE/hotastable:
\captionsetup[table]{font=small, labelfont=bf, justification=centering, singlelinecheck=true}

% --------------------------------------------------------------------------
% HEADERS AND FOOTERS (IMPROVED for report + twoside)
% --------------------------------------------------------------------------

\usepackage{fancyhdr}
\setlength{\headheight}{25pt}                    % Increased (was 15pt) for long names
\pagestyle{fancy}
\fancyhf{}                                        % Clear all
\fancyhead[LO,RE]{\small\textit{\leftmark}}     % Outer edge (odd left, even right): chapter name
\fancyhead[RO,LE]{\small\thepage}               % Inner edge (odd right, even left): page number
\fancyfoot{}                                      % No footer (page number in header)
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% --------------------------------------------------------------------------
% CHAPTER FORMATTING AND SPACING (via titlesec)
% --------------------------------------------------------------------------

\usepackage{titlesec}

% --------------------------------------------------------------------------
% CHAPTER - Nível 0 (Destaque Máximo)
% --------------------------------------------------------------------------
% Shape: display → standalone em nova linha
% Font: \Large\bfseries --- label e título ambos em bold para destaque máximo
% Numeração: SIM
% Espaçamento: 15pt antes, 28pt depois
% --------------------------------------------------------------------------

\titleformat{\chapter}[display]
{\normalfont\Large\bfseries}           % Formato: LARGE + bold (label)
{\chaptertitlename~\thechapter}        % Rótulo: "Chapter 1" (bold também)
{20pt}                                 % Espaço vertical antes do corpo
{\Large\bfseries}                      % Corpo do título: LARGE + bold

\titlespacing{\chapter}
{0pt}       % Margem esquerda (sem indent)
{15pt}      % Espaço ANTES do título do capítulo
{28pt}      % Espaço DEPOIS do título do capítulo (AUMENTADO)
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% SECTION - Nível 1
% --------------------------------------------------------------------------
% Shape: hang → label à esquerda, corpo indentado (compacto)
% Font: \large\bfseries (mesmo destaque que chapter para coerência)
% Numeração: SIM
% Espaçamento: 15pt antes, 8pt depois (REDUZIDO de 15pt/10pt anteriores)
% --------------------------------------------------------------------------

\titleformat{\section}[hang]
{\normalfont\large\bfseries}           % Formato: large + bold
{\thesection}                          % Rótulo: "1", "2", etc
{1em}                                  % Espaço entre rótulo e corpo
{}                                     % Corpo do título (herda do format)

\titlespacing{\section}
{0pt}       % Margem esquerda (sem indent)
{15pt}      % Espaço ANTES do título da seção (REDUZIDO)
{8pt}       % Espaço DEPOIS do título da seção (REDUZIDO)
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% SUBSECTION - Nível 2
% --------------------------------------------------------------------------
% Shape: hang → label esquerda, corpo indentado
% Font: \normalsize\bfseries (redução visual, ainda robusto)
% Numeração: SIM
% Espaçamento: 12pt antes, 6pt depois (compacto)
% --------------------------------------------------------------------------

\titleformat{\subsection}[hang]
{\normalfont\normalsize\bfseries}      % Formato: tamanho normal + bold
{\thesubsection}                       % Rótulo: "1.1", "1.2", etc
{1em}                                  % Espaço entre rótulo e corpo
{}                                     % Corpo do título

\titlespacing{\subsection}
{0pt}       % Margem esquerda (sem indent)
{12pt}      % Espaço ANTES do título da subseção
{6pt}       % Espaço DEPOIS do título da subseção
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% SUBSUBSECTION - Nível 3
% --------------------------------------------------------------------------
% Shape: hang → label esquerda, máximo recuo (bem compacto)
% Font: \normalsize\bfseries (mesmo tamanho que subsection, padrão)
% Numeração: SIM (configurable com secnumdepth)
% Espaçamento: 10pt antes, 4pt depois (bem comprimido)
% --------------------------------------------------------------------------

\titleformat{\subsubsection}[hang]
{\normalfont\normalsize\bfseries}      % Formato: tamanho normal + bold
{\thesubsubsection}                    % Rótulo: "1.1.1", "1.1.2", etc
{1em}                                  % Espaço entre rótulo e corpo
{}                                     % Corpo do título

\titlespacing{\subsubsection}
{0pt}       % Margem esquerda (sem indent)
{10pt}       % Espaço ANTES do título
{4pt}       % Espaço DEPOIS do título (bem comprimido)
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% PARAGRAPH - Nível 4 (CRÍTICO: Ilusão Óptica Resolvida)
% --------------------------------------------------------------------------
% Shape: runin → inline, integrado ao texto (seu requisito)
% Font: \small\bfseries (SOLUÇÃO PARA ILUSÃO ÓPTICA DO NEGRITO)%       
% Numeração: NÃO (padrão para \paragraph)
% Espaçamento: runin (sem espaço vertical antes, integrado ao texto)
% --------------------------------------------------------------------------

\titleformat{\paragraph}[runin]
{\normalfont\small\bfseries}           % Formato: SMALL + bold (compensa ilusão)
{}                                     % Rótulo: vazio (sem numeração)
{0em}                                  % Espaço entre rótulo e corpo (zero, runin)
{}                                     % Corpo do título

\titlespacing{\paragraph}
{0pt}       % Margem esquerda (sem indent)
{8pt}       % Espaço ANTES do título do parágrafo (ADICIONADO - cria separação)
{1em}       % Espaço DEPOIS do título (ADICIONADO - espaço após ":")
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% SUBPARAGRAPH - Nível 5 (Preparação Futura)
% --------------------------------------------------------------------------
% Shape: runin → inline, integrado ao texto
% Font: \small (MENOS destaque que \paragraph, sem bold)
% Numeração: NÃO (padrão para \subparagraph)
% Espaçamento: runin (integrado)
% Uso: Se usado, aparecerá com destaque menor que \paragraph
% --------------------------------------------------------------------------

\titleformat{\subparagraph}[runin]
{\normalfont\small}                    % Formato: small, SEM bold (menos destaque)
{}                                     % Rótulo: vazio (sem numeração)
{0em}                                  % Espaço entre rótulo e corpo (zero, runin)
{}                                     % Corpo do título

\titlespacing{\subparagraph}
{0pt}       % Margem esquerda (sem indent)
{8pt}       % Espaço ANTES do título (ADICIONADO)
{1em}       % Espaço DEPOIS do título (ADICIONADO)
[0pt]       % Margem direita

% --------------------------------------------------------------------------
% TABLES AND MACROS
% --------------------------------------------------------------------------

\usepackage{booktabs}
\usepackage{array}
\usepackage{longtable}
\usepackage{tabularx}

% Custom Columns
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}

% Macro for Visual Reference Links
\newcommand{\imglink}[1]{\hspace{2pt}\hyperref[#1]{\scriptsize\textbf{[Fig]}}}

% ============================================================================
% HOTAS table environment (per Briefing v0.2.0.1)
% ============================================================================

\newenvironment{hotastable}[1]{%
  \small
  \setlength{\tabcolsep}{2pt}
  \renewcommand{\arraystretch}{1.25}
  \begin{longtable}{L{1.00cm} L{0.90cm} L{0.90cm} L{3.30cm} L{6.40cm} L{1.40cm} L{2.10cm}}
  \caption{#1}\\
  \rowcolor{headerblue}
  \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{2.10cm}}{\textbf{\color{white}Train.}} \\
  \endfirsthead
  \rowcolor{headerblue}
  \multicolumn{1}{>{\centering\arraybackslash}p{1.00cm}}{\textbf{\color{white}Mode}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Dir.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{0.90cm}}{\textbf{\color{white}Act.}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{3.30cm}}{\textbf{\color{white}Function}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{6.40cm}}{\textbf{\color{white}Effect / Nuance}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{1.40cm}}{\textbf{\color{white}Dash34}} &
  \multicolumn{1}{>{\centering\arraybackslash}p{2.10cm}}{\textbf{\color{white}Train.}} \\
  \endhead
  \multicolumn{7}{r}{\small\emph{Continued on next page}}\\
  \endfoot
  \endlastfoot
}{%
  \end{longtable}
}

% --------------------------------------------------------------------------
% SIMPLE REFERENCE MACROS FOR BMS DOCS
% --------------------------------------------------------------------------

\providecommand{\dashref}[1]{Dash-34~\S~#1}
\providecommand{\dashone}[1]{Dash-1~\S~#1}
\providecommand{\trnref}[1]{TRN~#1}
\providecommand{\trnman}{BMS Training Manual 4.38.1}
\providecommand{\bmsver}{Falcon BMS~4.38.1}
\providecommand{\dashrefs}[1]{\textit{TO 1F-16CMAM-34-1-1}, Dash-34, sections \texttt{#1}}

% --------------------------------------------------------------------------
% VERSION CONTROL MACROS
% --------------------------------------------------------------------------

\newcommand{\docversion}{0.3.0.1}
\newcommand{\docbuild}{20260117}
\newcommand{\docstartdate}{05 January 2026}
\newcommand{\docenddate}{17 January 2026}
\newcommand{\chapterscompletedof}{3/7}
\newcommand{\tablesfilledpct}{Chapter 5 and Chapter 4 - 4.2}
\newcommand{\fulldocversion}{\docversion+\docbuild}

% --------------------------------------------------------------------------
% GRAPHICS
% --------------------------------------------------------------------------

\usepackage{graphicx}
\graphicspath{{fig/}}
\usepackage{float}

% --------------------------------------------------------------------------
% TITLE
% --------------------------------------------------------------------------

\title{TMS, DMS and CMS Usage Guide for \bmsver}
\author{Carlos ``Metal'' Nader}
\date{Version \fulldocversion{} | Progress: Chapters \chapterscompletedof{} | Tables \tablesfilledpct{} | January 2026}

% ============================================================================
% DOCUMENT BEGIN
% ============================================================================

\begin{document}

\maketitle

\pagenumbering{roman}

% ============================================================================
% TOC DEPTH CONFIGURATION (CRITICAL for report)
% ============================================================================
\setcounter{tocdepth}{3}       % Show up to \subsubsection in TOC
\setcounter{secnumdepth}{3}    % Number up to \subsubsection

\newpage

\tableofcontents

\newpage

\pagenumbering{arabic}

% ============================================================================
% CONTENT BEGINS HERE (use \chapter{}, \section{}, \subsection{}, etc.)
% ============================================================================
```

---

