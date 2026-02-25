# 🛠️ Setup Guide — TMS/DMS/CMS Usage Guide for Falcon BMS

**Version:** 1.0.0
**Last Updated:** 2026-02-25
**Target Audience:** Contributors, editors, and technical writers

---

## 📋 Table of Contents

1. [Prerequisites](#-prerequisites)
2. [Installing Git](#-installing-git)
3. [Installing LaTeX Distribution (MiKTeX)](#-installing-latex-distribution-miktex)
4. [Setting Up TeXstudio IDE](#-setting-up-texstudio-ide)
5. [Setting Up Visual Studio Code](#-setting-up-visual-studio-code)
6. [Cloning the Repository](#-cloning-the-repository)
7. [Building the PDF Locally](#-building-the-pdf-locally)
8. [Creating WIP Files](#-creating-wip-files)
9. [Git Workflow for Editing](#-git-workflow-for-editing)
10. [Running Automation Scripts](#-running-automation-scripts)
11. [Troubleshooting](#-troubleshooting)

---

## 🎯 Prerequisites

Before setting up the project, ensure you have:

| Requirement | Minimum Version | Purpose |
|------------|----------------|---------|
| **Windows 10/11** or **macOS/Linux** | Latest stable | Operating system |
| **Git** | 2.30+ | Version control |
| **Python** | 3.8+ | Automation scripts (optional) |
| **MiKTeX** (Windows) or **TeX Live** (Linux/macOS) | Latest | LaTeX distribution |
| **4 GB RAM** | — | LaTeX compilation |
| **500 MB free disk space** | — | MiKTeX packages + repo |

> **Note:** Python is only required if you want to run automation scripts in `/scripts/`. The main workflow (editing LaTeX, building PDFs, Git operations) works perfectly without Python.

### Optional (Recommended)
- **GitHub Desktop** — GUI for Git operations
- **GitHub account** — For contributing via pull requests
- **VS Code** or **TeXstudio** — IDEs for editing

---

## 🔧 Installing Git

Git is essential for version control and contributing to the project.

### Windows Installation

1. **Download Git for Windows**
   - Visit: https://git-scm.com/download/win
   - Download **64-bit Git for Windows Setup**

2. **Run the Installer**
   - Use recommended settings for most options
   - **Important selections:**
     - **Editor:** Choose your preferred editor (VS Code recommended)
     - **PATH environment:** Select **"Git from the command line and also from 3rd-party software"**
     - **HTTPS transport backend:** Use **OpenSSL library**
     - **Line ending conversions:** Choose **"Checkout Windows-style, commit Unix-style"**

3. **Verify Installation**
   ```powershell
   # Open PowerShell and run:
   git --version
   ```
   Expected output:
   ```
   git version 2.x.x
   ```

4. **Configure Git Identity** (Required for commits)
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

### macOS Installation

**Option 1: Using Homebrew (Recommended)**
```bash
brew install git
```

**Option 2: Xcode Command Line Tools**
```bash
xcode-select --install
```

**Verify:**
```bash
git --version
```

### Linux Installation

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install git

# Fedora
sudo dnf install git

# Arch Linux
sudo pacman -S git
```

### Post-Installation Configuration

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# Enable credential caching (optional, saves passwords)
git config --global credential.helper cache

# Verify configuration
git config --list
```

### Optional: GitHub Desktop (GUI Alternative)

If you prefer a graphical interface:

1. **Download GitHub Desktop**
   - https://desktop.github.com/
   - Available for Windows and macOS

2. **Sign in with GitHub account**
   - Automatically configures Git credentials

3. **Benefits:**
   - Visual diff viewer
   - Simplified branching and merging
   - Integrated pull request creation

---

## 📦 Installing LaTeX Distribution (MiKTeX)

### Windows Installation

1. **Download MiKTeX**
   - Visit: https://miktex.org/download
   - Download **MiKTeX Installer (64-bit)**

2. **Run the Installer**
   - Launch the downloaded `.exe` file
   - Choose **"Install MiKTeX for all users"** (recommended)
   - Install location: `C:\Program Files\MiKTeX` (default)

3. **Configuration During Setup**
   - **Package Installation:** Choose **"Always install packages on-the-fly"**
     - This auto-downloads missing LaTeX packages during compilation
   - **Paper Size:** Select **A4** (matches guide settings)

4. **Verify Installation**
   ```powershell
   # Open PowerShell and run:
   pdflatex --version
   ```
   Expected output:
   ```
   MiKTeX-pdfTeX 4.x (MiKTeX xx.xx)
   ```

5. **Update MiKTeX Packages** (Important!)
   - Open **MiKTeX Console** (search in Start Menu)
   - Click **"Check for updates"**
   - Install all available updates
   - Restart your computer

### macOS Installation

1. **Install MacTeX** (macOS equivalent of MiKTeX)
   ```bash
   # Using Homebrew
   brew install --cask mactex-no-gui

   # Or download from: https://www.tug.org/mactex/
   ```

2. **Update TeX Live**
   ```bash
   sudo tlmgr update --self
   sudo tlmgr update --all
   ```

### Linux Installation

1. **Install TeX Live**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install texlive-full

   # Fedora
   sudo dnf install texlive-scheme-full

   # Arch Linux
   sudo pacman -S texlive-most
   ```

---

## 🖊️ Setting Up TeXstudio IDE

**TeXstudio** is the recommended IDE for editing `guide.tex` and WIP LaTeX files.

### Installation

1. **Download TeXstudio**
   - Windows: https://www.texstudio.org/
   - macOS: `brew install --cask texstudio`
   - Linux: `sudo apt-get install texstudio`

2. **Launch TeXstudio**

### Configuration

#### 1. Set MiKTeX as LaTeX Distribution

1. Go to **Options → Configure TeXstudio**
2. Navigate to **"Commands"**
3. Verify paths:
   ```
   PdfLaTeX: pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex
   ```

#### 2. Configure Build Settings

1. Go to **Options → Configure TeXstudio → Build**
2. Set **Default Compiler:** `PdfLaTeX`
3. Set **Default Bibliography Tool:** `BibTeX` (if using references)
4. Enable **"Automatic Build & View"** (optional)

#### 3. Enable SyncTeX (Recommended)

SyncTeX allows you to **click in the PDF to jump to the corresponding LaTeX source**.

1. Go to **Options → Configure TeXstudio → Commands**
2. Ensure `-synctex=1` flag is present in PdfLaTeX command
3. In **Internal PDF Viewer**, enable **"Show line numbers"**

#### 4. Set Editor Preferences

1. Go to **Options → Configure TeXstudio → Editor**
2. Enable:
   - ✅ **Line numbers**
   - ✅ **Auto-save** (every 5 minutes)
   - ✅ **Replace tabs by spaces** (4 spaces)

### Building the Guide in TeXstudio

1. **Open the guide:**
   - `File → Open → guide.tex`

2. **Build PDF:**
   - Press **F5** (Build & View)
   - Or click the **green arrow** ▶️ button

3. **View Output:**
   - PDF appears in right panel
   - Build log appears in bottom panel
   - Errors/warnings highlighted in red/yellow

---

## 💻 Setting Up Visual Studio Code

**VS Code** is ideal for multi-file editing, Git integration, and Python scripting.

### Installation

1. **Download VS Code**
   - https://code.visualstudio.com/
   - Install with default settings

### Required Extensions

Install these extensions via **Extensions panel (Ctrl+Shift+X)**:

| Extension | ID | Purpose |
|-----------|----|---------|
| **LaTeX Workshop** | `James-Yu.latex-workshop` | LaTeX editing, compilation, PDF preview |
| **Python** | `ms-python.python` | Python scripting support (optional) |
| **Markdown All in One** | `yzhang.markdown-all-in-one` | Markdown editing in `/docs/` |

> **Note:** VS Code has excellent built-in Git integration (Source Control panel, `Ctrl+Shift+G`). No additional Git extensions are required. The native integration handles commits, diffs, branches, and sync operations.

### Configuration

#### 1. Configure LaTeX Workshop

Create/edit `.vscode/settings.json`:

```json
{
  "latex-workshop.latex.autoBuild.run": "never",
  "latex-workshop.latex.tools": [
    {
      "name": "pdflatex",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "-file-line-error",
        "%DOC%"
      ]
    }
  ],
  "latex-workshop.latex.recipes": [
    {
      "name": "pdflatex",
      "tools": [
        "pdflatex"
      ]
    }
  ],
  "latex-workshop.view.pdf.viewer": "tab",
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 5000
}
```

#### 2. Add Build Tasks (Recommended)

Create/edit `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Build PDF (guide.tex)",
      "type": "shell",
      "command": "pdflatex",
      "args": [
        "-synctex=1",
        "-interaction=nonstopmode",
        "guide.tex"
      ],
      "group": {
        "kind": "build",
        "isDefault": true
      },
      "presentation": {
        "reveal": "always",
        "panel": "new"
      },
      "problemMatcher": []
    },
    {
      "label": "Run Integrity Check",
      "type": "shell",
      "command": "pwsh",
      "args": [
        "-File",
        "./check-guide-integrity.ps1"
      ],
      "group": "test",
      "presentation": {
        "reveal": "always"
      }
    },
    {
      "label": "Generate Integrated Files Report",
      "type": "shell",
      "command": "python",
      "args": [
        "scripts/generate-integrated-files.py"
      ],
      "group": "none",
      "presentation": {
        "reveal": "always"
      }
    }
  ]
}
```

#### 3. Keyboard Shortcuts

- **Build PDF:** `Ctrl+Shift+B` (runs default build task)
- **View PDF:** `Ctrl+Alt+V` (LaTeX Workshop)
- **SyncTeX Forward:** `Ctrl+Alt+J` (source → PDF)
- **SyncTeX Backward:** `Ctrl+Click` in PDF (PDF → source)

### Building the Guide in VS Code

1. **Open workspace:**
   - `File → Open Folder → projeto-bms/`

2. **Open guide.tex**

3. **Build PDF:**
   - Press `Ctrl+Shift+B`
   - Or: `Terminal → Run Build Task`
   - Or: Click **"Build LaTeX project"** in status bar

4. **View PDF:**
   - Press `Ctrl+Alt+V`
   - PDF opens in side panel with SyncTeX enabled

---

## 📥 Cloning the Repository

### Using Git (Command Line)

```bash
# Clone via HTTPS
git clone https://github.com/carlos-nader/tms-dms-cms-usage-guide.git

# Navigate to project directory
cd tms-dms-cms-usage-guide

# Verify remote
git remote -v
```

### Using GitHub Desktop

1. **Open GitHub Desktop**
2. **File → Clone Repository**
3. Select **URL** tab
4. Paste: `https://github.com/carlos-nader/tms-dms-cms-usage-guide.git`
5. Choose local path: `C:\Users\[YourName]\Documents\projeto-bms`
6. Click **Clone**

### Post-Clone Setup

```bash
# Ensure you're on the main branch
git checkout main

# Pull latest changes
git pull origin main

# Check repository status
git status
```

---

## 🏗️ Building the PDF Locally

### Quick Build (Command Line)

```bash
# Navigate to project root
cd /path/to/tms-dms-cms-usage-guide

# Compile guide.tex with pdflatex
pdflatex -synctex=1 -interaction=nonstopmode guide.tex

# Output: guide.pdf
```

### Full Build (With References/TOC)

For documents with table of contents, cross-references, or bibliographies, run **twice**:

```bash
# First pass (generates references)
pdflatex guide.tex

# Second pass (resolves references)
pdflatex guide.tex
```

### Build with TeXstudio

1. Open `guide.tex` in TeXstudio
2. Press **F5** (Build & View)
3. PDF opens automatically

### Build with VS Code

1. Open `guide.tex`
2. Press `Ctrl+Shift+B`
3. View PDF with `Ctrl+Alt+V`

### Verify Build Success

**Expected output files:**
```
guide.pdf         ← Main output (PDF)
guide.aux         ← Auxiliary data
guide.log         ← Compilation log
guide.out         ← Hyperref output
guide.synctex.gz  ← SyncTeX data
guide.toc         ← Table of contents
guide.lot         ← List of tables
```

**Check for errors:**
```bash
# Search for errors in log
grep -i error guide.log
```

---

## 📝 Creating WIP Files

All work-in-progress content follows a **standardized naming convention** defined in [docs/wip-naming-v1.4.md](docs/wip-naming-v1.4.md).

### WIP File Naming Format

```
{type}-C{N}[-S{M}[-S{K}]]-{title}-{status}-{YYYY-MM-DD}.{ext}
```

**Components:**
- `{type}` → File type: `chapter`, `section`, `table`, `notes`, `visual`
- `C{N}` → Chapter number (e.g., `C4` for Chapter 4)
- `S{M}` → Section number (optional, e.g., `S2`)
- `S{K}` → Subsection number (optional, e.g., `S3`)
- `{title}` → Descriptive kebab-case title (e.g., `tms-structure`)
- `{status}` → Lifecycle stage: `dev`, `review`, `final`, `approved`, `deprecated`
- `{YYYY-MM-DD}` → Creation date (e.g., `2026-02-12`)
- `{ext}` → File extension: `.tex`, `.md`, `.svg`, `.png`

### Examples

```bash
# Chapter 4 (TMS) in development
chapter-C4-tms-structure-dev-2026-02-12.tex

# Section 2 of Chapter 3 under review
section-C3-S2-dms-up-review-2026-02-10.tex

# HOTAS table ready for integration
table-C5-CMDS-HOTAS-final-2026-02-11.tex

# Research notes
notes-C4-GEN-research-snippet-2026-02-08.md

# Conceptual diagram
visual-C2-soi-concept-diagram-dev-2026-02-09.svg
```

### WIP File Lifecycle

| Status | Description | Next Step |
|--------|-------------|-----------|
| **dev** | Draft, not ready for review | Complete content → `review` |
| **review** | Under human review | Address feedback → `final` |
| **final** | Approved, ready for integration | Integrate into `guide.tex` → `approved` |
| **approved** | Integrated into guide, archived | Move to `archive/WIP/` |
| **deprecated** | Retired or superseded | Move to `archive/WIP/` |

### Creating a WIP File

#### Step 1: Use the Template

```bash
# Copy the official WIP template
cp template/template-wip-V1.0.tex wip/chapter-C6-training-dev-2026-02-12.tex
```

#### Step 2: Edit Metadata

Open the WIP file and update the header:

```latex
% ============================================================================
% WIP FILE METADATA
% ============================================================================
% Type:             chapter
% Chapter:          C6 — Training References and Practical Flows
% Title:            Training References
% Status:           dev
% Created:          2026-02-12
% Author:           Carlos "Metal" Nader
% Description:      Practical training flows for HOTAS switch usage
% ============================================================================
```

#### Step 3: Add Content

Write your chapter/section content using LaTeX markup.

#### Step 4: Compile & Test

```bash
# Build WIP file to verify LaTeX syntax
pdflatex chapter-C6-training-dev-2026-02-12.tex
```

#### Step 5: Change Status When Ready

```bash
# Move to review stage
git mv wip/chapter-C6-training-dev-2026-02-12.tex wip/chapter-C6-training-review-2026-02-12.tex
```

---

## 🔄 Git Workflow for Editing

### Basic Workflow

```bash
# 1. Create a feature branch
git checkout -b feature/chapter-6-training

# 2. Make changes to WIP files or documentation
# ... edit files ...

# 3. Stage changes
git add wip/chapter-C6-training-dev-2026-02-12.tex

# 4. Commit with descriptive message
git commit -m "feat(C6): add training flows for TMS employment

- Add A-A training progression
- Add A-G target sequencing exercises
- Include practice scenarios"

# 5. Push to remote
git push origin feature/chapter-6-training

# 6. Create Pull Request on GitHub
gh pr create --title "Add Chapter 6: Training References" --body "..."
```

### Commit Message Format

Follow **conventional commits** format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat` — New content (new chapter, section)
- `fix` — Corrections (typos, errors)
- `docs` — Documentation changes
- `style` — Formatting, spacing (no content change)
- `refactor` — Restructuring content
- `chore` — Maintenance (scripts, workflows)

**Example:**
```bash
git commit -m "fix(C4): correct TMS-Up behavior in NAV mode

Previously described as cycling radar cursors, but actually
commands A-A radar scan azimuth reset in NAV mode.

Ref: TO 1F-16CMAM-34-1-1 BMS, p. 237"
```

### Branching Strategy

```
main                  ← Stable, always buildable
  ├── develop         ← Integration branch (if needed)
  ├── feature/*       ← New content (e.g., feature/chapter-6)
  ├── fix/*           ← Bug fixes (e.g., fix/c4-tms-typo)
  └── docs/*          ← Documentation updates (e.g., docs/setup-guide)
```

### Before Committing (Checklist)

- [ ] LaTeX compiles without errors (`pdflatex guide.tex`)
- [ ] WIP file follows naming convention
- [ ] No `TODO` or `TBD` placeholders in final content
- [ ] Cross-references work (`\secref`, `\chapref`, `\tabref`)
- [ ] Commit message follows conventional format
- [ ] Changes tested locally

---

## 🐍 Running Automation Scripts

The repository includes Python scripts in `/scripts/` for automation.

### Prerequisites

Ensure Python 3.8+ is installed:

```bash
python --version
# Output: Python 3.x.x
```

### Script 1: Generate Integrated Files Report

**Purpose:** Creates `INTEGRATED-FILES.md` tracking all repository content.

```bash
# Run from project root
python scripts/generate-integrated-files.py

# Output files:
# - INTEGRATED-FILES.md
# - INTEGRATED-FILES.json
# - docs/integrated-files.html
```

### Script 2: Validate LaTeX Preamble

**Purpose:** Checks all `.tex` files for preamble consistency.

```bash
python scripts/validate-tex-preamble.py

# Output: Console report showing:
# - Missing packages
# - Forbidden placeholders (TBD, TODO)
# - Compliance per file
```

### Script 3: Update README Version

**Purpose:** Updates version badges in `README.md`.

```bash
python scripts/update-readme-version.py

# Automatically updates:
# - Version badge (e.g., v0.4.1.0)
# - Date in README
# - docs/index.html version
```

### Script 4: Scrape Forum Views

**Purpose:** Tracks community engagement metrics.

```bash
python scripts/scrape-forum-views-debug.py

# Outputs: Forum view count
```

### Running Scripts on Windows (PowerShell)

If Python is not in PATH:

```powershell
# Use full Python path
C:\Users\[YourName]\AppData\Local\Programs\Python\Python3xx\python.exe scripts/generate-integrated-files.py
```

---

## 🔧 Troubleshooting

### Issue 1: `pdflatex: command not found`

**Cause:** LaTeX distribution not in system PATH.

**Solution (Windows):**
```powershell
# Add MiKTeX to PATH (PowerShell as Administrator)
$env:Path += ";C:\Program Files\MiKTeX\miktex\bin\x64"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::Machine)

# Restart PowerShell and verify
pdflatex --version
```

**Solution (macOS/Linux):**
```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="/usr/local/texlive/2024/bin/x86_64-linux:$PATH"

# Reload shell
source ~/.bashrc
```

---

### Issue 2: Missing LaTeX Package Errors

**Error Example:**
```
! LaTeX Error: File `geometry.sty' not found.
```

**Solution:**

**Windows (MiKTeX):**
1. Open **MiKTeX Console**
2. Go to **Packages** tab
3. Search for missing package (e.g., `geometry`)
4. Click **Install**

**macOS/Linux (TeX Live):**
```bash
sudo tlmgr install geometry
```

**Auto-install (recommended):**
- Enable **"Always install packages on-the-fly"** in MiKTeX settings
- Missing packages will download automatically during compilation

---

### Issue 3: SyncTeX Not Working

**Cause:** `-synctex=1` flag missing from build command.

**Solution (TeXstudio):**
1. Options → Configure TeXstudio → Commands
2. Update PdfLaTeX command:
   ```
   pdflatex.exe -synctex=1 -interaction=nonstopmode %.tex
   ```

**Solution (VS Code):**
- Ensure `.vscode/settings.json` includes `-synctex=1` in `latex-workshop.latex.tools`

---

### Issue 4: Git Push Rejected

**Error:**
```
! [rejected]        main -> main (fetch first)
```

**Cause:** Remote has commits you don't have locally.

**Solution:**
```bash
# Pull remote changes first
git pull origin main --rebase

# Then push
git push origin main
```

---

### Issue 5: Workflow Validation Fails

**Error:** GitHub Actions workflow `validate-wip-naming.yml` fails.

**Cause:** WIP file doesn't follow naming convention.

**Solution:**
1. Check [docs/wip-naming-v1.4.md](docs/wip-naming-v1.4.md)
2. Rename file to match format:
   ```bash
   git mv wip/wrong-name.tex wip/chapter-C6-training-dev-2026-02-12.tex
   ```
3. Commit and push:
   ```bash
   git add wip/
   git commit -m "fix: rename WIP file to match naming convention"
   git push
   ```

---

### Issue 6: Python Script Fails

**Error:**
```
ModuleNotFoundError: No module named 'requests'
```

**Solution:**
```bash
# Install missing Python packages
pip install requests

# Or install all dependencies (if requirements.txt exists)
pip install -r requirements.txt
```

---

### Issue 7: PDF Not Updating

**Cause:** Old auxiliary files (`.aux`, `.toc`) cached.

**Solution:**
```bash
# Clean auxiliary files
rm guide.aux guide.log guide.out guide.toc guide.lot guide.synctex.gz

# Rebuild
pdflatex guide.tex
pdflatex guide.tex  # Second pass for references
```

**Windows (PowerShell):**
```powershell
Remove-Item guide.aux, guide.log, guide.out, guide.toc, guide.lot, guide.synctex.gz -ErrorAction SilentlyContinue
pdflatex guide.tex
```

---

### Issue 8: Permission Denied on Git Push

**Cause:** GitHub credentials not configured.

**Solution (HTTPS):**
```bash
# Configure Git credentials
git config --global credential.helper store

# Next push will prompt for username/token
git push origin main
```

**Solution (SSH - Recommended):**
1. Generate SSH key:
   ```bash
   ssh-keygen -t ed25519 -C "your_email@example.com"
   ```
2. Add to GitHub: Settings → SSH and GPG keys → New SSH key
3. Update remote:
   ```bash
   git remote set-url origin git@github.com:carlos-nader/tms-dms-cms-usage-guide.git
   ```

---

## 📚 Additional Resources

### Documentation

- [BRIEFING](docs/briefing.md) — Scope, style, layout standards
- [WIP File Naming (v1.4)](docs/wip-naming-v1.4.md) — WIP naming conventions
- [Version System](docs/version-system.md) — Versioning rules
- [Project Tracking](docs/project-tracking.md) — Session logs, milestones
- [CONTRIBUTING.md](.github/CONTRIBUTING.md) — Contribution guidelines

### External Resources

- [MiKTeX Documentation](https://miktex.org/howto)
- [TeXstudio Manual](https://www.texstudio.org/)
- [LaTeX Workshop (VS Code)](https://github.com/James-Yu/LaTeX-Workshop/wiki)
- [Git Documentation](https://git-scm.com/doc)
- [Conventional Commits](https://www.conventionalcommits.org/)

### Community

- **GitHub Discussions:** https://github.com/carlos-nader/tms-dms-cms-usage-guide/discussions
- **Falcon BMS Forum Thread:** https://forum.falcon-bms.com/topic/32541
- **Issue Tracker:** https://github.com/carlos-nader/tms-dms-cms-usage-guide/issues

---

## 🎯 Quick Start Checklist

Copy this checklist to verify your setup:

```markdown
- [ ] Install MiKTeX (Windows) or TeX Live (macOS/Linux)
- [ ] Update all LaTeX packages
- [ ] Install TeXstudio or configure VS Code with LaTeX Workshop
- [ ] Clone repository via Git or GitHub Desktop
- [ ] Verify `pdflatex --version` works
- [ ] Build guide.pdf successfully
- [ ] Open guide.pdf and verify formatting
- [ ] Create test WIP file with correct naming
- [ ] Run Python script: generate-integrated-files.py
- [ ] Configure Git username/email
- [ ] Test Git commit and push to feature branch
```

---

## 📧 Getting Help

If you encounter issues not covered in this guide:

1. **Check existing issues:** https://github.com/carlos-nader/tms-dms-cms-usage-guide/issues
2. **Open a new issue** with:
   - Detailed description of the problem
   - Steps to reproduce
   - Your environment (OS, LaTeX version, IDE)
   - Error messages or logs
3. **Contact maintainer:** Carlos "Metal" Nader

---

**Document Version:** 1.0.0
**Last Updated:** 2026-02-25
**Maintained By:** Carlos "Metal" Nader
**License:** CC BY-NC 4.0
