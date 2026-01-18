Preamble Completo (Pronto para Colar)

```latex
% ============================================================================
% PREAMBLE COMPLETO — TMS/DMS/CMS Usage Guide for Falcon BMS 4.38.1
% Gerado: 17 January 2026
% Status: Novo preâmbulo (report + twoside + titlesec + fancyhdr melhorado)
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

\usepackage[pdfencoding=auto, psdextra, colorlinks=true, linkcolor=linkblue, citecolor=linkred, urlcolor=linkblue, breaklinks=true]{hyperref}
\usepackage{bookmark}

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

% Chapter format: display style with custom spacing
\titleformat{\chapter}[display]
  {\normalfont\Large\bfseries}
  {\chaptertitlename~\thechapter}
  {20pt}
  {\Large}

% Chapter spacing: before=10pt (was 50pt), after=20pt (was 40pt)
\titlespacing{\chapter}
  {0pt}
  {10pt}      % Space BEFORE chapter title
  {20pt}      % Space AFTER chapter title
  [0pt]

% Section spacing (optional, for consistency)
\titlespacing{\section}
  {0pt}
  {15pt}
  {10pt}
  [0pt]

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
  \renewcommand{\arraystretch}{1.25}
  \begin{longtable}{L{1.6cm} L{1.0cm} L{1.0cm} L{3.4cm} L{5.8cm} L{1.4cm} L{1.4cm}}
  \caption{#1}\\
  \rowcolor{headerblue}
  \textbf{\color{white}State} &
  \textbf{\color{white}Dir} &
  \textbf{\color{white}Act} &
  \textbf{\color{white}Function} &
  \textbf{\color{white}Effect / Nuance} &
  \textbf{\color{white}Dash34} &
  \textbf{\color{white}Train} \\
  \endfirsthead
  \rowcolor{headerblue}
  \textbf{\color{white}State} &
  \textbf{\color{white}Dir} &
  \textbf{\color{white}Act} &
  \textbf{\color{white}Function} &
  \textbf{\color{white}Effect / Nuance} &
  \textbf{\color{white}Dash34} &
  \textbf{\color{white}Train} \\
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

