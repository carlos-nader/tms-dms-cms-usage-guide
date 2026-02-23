# TMS/DMS/CMS Usage Guide for Falcon BMS and other F-16 Flight Simulators

[![Generate Integrated Files Report](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/generate-integrated-files.yml/badge.svg?branch=main)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/generate-integrated-files.yml) [![pages-build-deployment](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/pages/pages-build-deployment) [![Sync PDF to docs](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/sync-pdf-to-docs.yml/badge.svg?branch=main)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/sync-pdf-to-docs.yml)[![Validate LaTeX Preamble](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/validate-tex-preamble.yml/badge.svg)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/actions/workflows/validate-tex-preamble.yml)

[![GitHub stars](https://img.shields.io/github/stars/carlos-nader/tms-dms-cms-usage-guide?style=social)](https://github.com/carlos-nader/tms-dms-cms-usage-guide)
[![GitHub forks](https://img.shields.io/github/forks/carlos-nader/tms-dms-cms-usage-guide?style=social)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/fork)

[**Changelog**](CHANGELOG.md) | [**Setup Guide**](SETUP.md)

A comprehensive guide documenting F-16 HOTAS switch systems (Target Management Switch, Display Management Switch, and Countermeasures Management Switch) for Falcon BMS and other F-16 flight simulators.

The author is not affiliated with or endorsed by Falcon BMS or any other flight sim developers. This is not an official guide or manual. It aims to help the flight sim community by consolidating information that is otherwise scattered across multiple manuals, training materials, and community resources into a single, structured reference.

---

## 🚀 Quick Start

1. **📕 Read the Guide:** See **Main Guide Files** Section below
2. **🌐 Explore the Website:** [Project documentation site](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)
3. **💬 Join Discussion:** [BMS Forum Thread](https://forum.falcon-bms.com/topic/32541)
4. **⭐ Star this repo** if you find it useful!

---

<div align="center">

## 📄 Main Guide Files

[![Version](https://img.shields.io/badge/LATEST%20version-v0.4.1.1-yellow?style=for-the-badge&logo=tag&logoColor=black)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/releases)

| Format | Link | Description |
|:------:|:----:|:------------|
| 📄 **LaTeX Source** | [`guide.tex`](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/guide.tex) | Editable source file |
| 📕 **Compiled PDF** | [`guide.pdf`](https://carlos-nader.github.io/tms-dms-cms-usage-guide/guide-web.pdf) | Ready-to-read document |

**👆 Click the links above to access the guide! 👆**

</div>

> ⚠️ **Style Revision in Progress (v0.4.2.0)**  
> A dedicated style revision pass is currently underway to improve clarity and
> directness across all chapters. The guide, in its current version is fully accessible and technically
> accurate. Expected completion: 2026-03-20.

---

## 📊 Current Status

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.4.1.1 |
| **Phase** | Pre-publication (0.x.x.x) |
| **Chapters Planned** | 7 |
| **Chapters with Content** | 4 (C1, C2, C3, C5) |
| **Chapters with Style Revision Complete** | 0 (in progress: C5) |
| **Next Target** | v0.4.2.0 — Style Full Revision |

---

<!-- WIP-SNAPSHOT-START -->

## 🗄️ WIP Snapshot — Active Work-in-Progress Files

| Status | File Name | Last Modified |
|:------:|-----------|:-------------|
| 🟠 dev | chapter-C4-tms-structure-dev-2026-02-13.tex | 2026-02-23 |
| 🟡 review | chapter-C5-style-rev-review-2026-02-22.tex | 2026-02-23 |
| ⚪ final | section-C2-S1-S3-soi-context-dependency-final-2026-02-15.tex | 2026-02-23 |
| 🟡 review | section-C4-S3-tms-aa-review-2026-02-17.tex | 2026-02-23 |

**Legend:**  🟠 dev	🟡 review	⚪ final

> For integrated files, see the `archive/WIP/` folder.
<!-- WIP-SNAPSHOT-END -->

---

## 📈 Development Activity (last 7 days)

[![wakatime](https://wakatime.com/badge/user/a7867e5c-aed5-4764-9e32-54ff6e08eaa8/project/22723c4f-b262-4526-a7ed-bff46e9902ff.svg)](https://wakatime.com/projects/projeto-bms)

Transparent time tracking via WakaTime specifically for this repository.

---

## 📖 About This Project

[![GitHub Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)
[![Perplexity](https://img.shields.io/badge/perplexity-000000?style=for-the-badge&logo=perplexity&logoColor=088F8F)](https://perplexity.ai)
[![Claude](https://img.shields.io/badge/Claude-cc785c?style=for-the-badge&logo=anthropic&logoColor=white)](https://claude.ai)
[![GitHub Copilot](https://img.shields.io/badge/GitHub%20Copilot-0969da?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/copilot)
[![Falcon BMS](https://img.shields.io/badge/Falcon%20BMS-4.38.1-blue?style=for-the-badge)](https://www.falcon-bms.com/)

This project develops a structured guide explaining the F-16 HOTAS TMS, DMS and CMS switch functionality, grounded in Falcon BMS manuals (Dash-34, Dash-1) and training materials.

---

## 📁 Project Structure
```
tms-dms-cms-usage-guide/
│
├── guide.tex                         # Current production version (.tex)
├── guide.pdf                         # Compiled PDF
├── INTEGRATED-FILES.md               # Auto-generated tracking report
├── CHANGELOG.md                      # Releases changelog tracking
├── SETUP.md                          # Infrastructure setup
│
├── docs/                             # Governance & tracking
│   ├── guide-web.pdf                 # guide.pdf copy for online visualization
│   ├── briefing-v0.2.0.1.md
│   ├── wip-file-naming-v1.4.md
│   ├── version-system-v4.2.1.md
│   ├── project-tracking-v5.0.0.md
│   ├── WIP-Snapshot-Generator-v3.1.html       
│   └── tex-preamble-consolidated.md
│
├── wip/                              # Active work-in-progress files
│   ├── chapter-*.tex                 # Chapter drafts
│   ├── section-*.tex                 # Section drafts
│   └── guide/                        # Active guide snapshots
│
├── archive/                          # Historical & approved files
│   ├── WIP/                          # Integrated/deprecated WIP files
│   ├── GUIDE/                        # Older guide versions
│   └── GUIDE-STRUCTURE/              # Older structure-only files
│
├── template/                         # Templates & blueprints
│   └── template-wip-V1.0.tex         # Canonical WIP template
│
├── fig/                              # Images used in the guide
├── misc/                             # Miscellaneous resources
│   ├── STYLE-GUIDE-v0.2.0.md
│   └── fontes/                       # Source PDFs (Dash-34, etc.)
├── scripts/                          # Automation scripts
├── .github/                          # Issues, Actions, PR templates, community files
├── .vscode/                          # VSCode workspace settings
│
├── LICENSE                           # CC BY-NC 4.0
└── README.md                         # This file
```

---

## 📋 Documentation & Governance

The project uses **five governance documents** and an **auto-generated tracking report**:

| Document | Location | Purpose |
|----------|----------|---------|
| [**BRIEFING**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/docs/briefing-v0.2.0.1.md) | `/docs/` | Project scope, content outline, layout standards |
| [**STYLE-GUIDE**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/misc/STYLE-GUIDE-v0.2.0.md) | `/misc/` | Prose style, voice, formatting policies, and prohibited patterns |
| [**WIP-FILE-NAMING**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/docs/wip-file-naming-v1.4.md) | `/docs/` | Rules for WIP file naming, status lifecycle (dev → review → final → approved) |
| [**VERSION-SYSTEM**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/docs/version-system-v4.2.1.md) | `/docs/` | Guide version numbering (0.x.x.x pre-publication, x.y.z post-publication) |
| [**PROJECT-TRACKING**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/docs/project-tracking-v5.0.0.md) | `/docs/` | Session log, WIP status snapshot, milestones, current priorities |
| [**INTEGRATED-FILES**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/INTEGRATED-FILES.md) | `/` (root) | Auto-generated report: tracked files, commits, issues, milestones *(updated by GitHub Action)* |

---

## 🔄 Workflow

### WIP File Lifecycle

1. **Create** — Copy template from `template/` to `wip/`
2. **Develop** — Edit with status `dev`
3. **Review** — Human review, status `review`
4. **Finalize** — Approved content, status `final`
5. **Integrate** — Merge into guide, move to `archive/`, status `approved`

### Status Codes

| Status | Meaning |
|--------|---------|
| `dev` | Draft stage, not ready for review |
| `review` | Under human review |
| `final` | Approved, ready for integration |
| `approved` | Integrated and archived |
| `deprecated` | Retired or superseded |

---

## 🛠️ Tools & Utilities

### Development Environment

* **TeXstudio + MiKTeX** — Primary LaTeX IDE for guide compilation and PDF generation
* **Visual Studio Code** — Multi-purpose editor for LaTeX, Markdown, scripts, and Copilot/Claude AI integration
* **Git / GitHub Desktop** — Version control and repository management

### AI Collaboration

* **Perplexity Pro (Perplexity AI)** — Research organization, project structuring, governance framework design, initial draft content generation, and review
* **Claude Pro (Anthropic)** — Research, initial draft content generation, review, and governance framework; used via web interface and VSCode (Claude Code)
* **GitHub Copilot Pro (GitHub / Microsoft)** — Documentation, repository management, issue and pull request coordination, and collaborative development; used via GitHub web interface and VSCode

### Project Utilities

* **WIP Snapshot Generator** — Interactive HTML tool ([WIP Generator v3.1](https://carlos-nader.github.io/tms-dms-cms-usage-guide/WIP-Snapshot-Generator-v3.1.html)) for generating compliant WIP file names

---

## 📚 Sources & References

This guide is grounded in official [**Falcon BMS**](https://www.falcon-bms.com/) documentation:

* [**TO 1F-16CMAM-34-1-1**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/misc/fontes/TO%201F-16CMAM-34-1-1%20BMS.pdf) — Falcon BMS Simulator F-16 Avionics & Weapons Manual (Dash-34)
* **TO 1F-16CMAM-1** — Falcon BMS Simulator F-16C/D Flight Manual (Dash-1)
* **Falcon BMS 4.38.1 Training Manual** — Training missions guide
* **F-16 Combat Aircraft Fundamentals Handbook (MCH 11-F16 Vol 5)** — USAF Multi-Command guidelines

All technical claims are cross-referenced to these sources.

✈️ **New to Falcon BMS?** Visit the [official website](https://www.falcon-bms.com/downloads/) to download the simulator (free with Falcon 4.0 ownership).

---

## 🗺️ Roadmap

| Resource | Description |
|----------|-------------|
| [**Milestones**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/milestones) | Planned releases |
| [**Issues**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/issues) | Current tasks |
| [**Tags**](https://github.com/carlos-nader/tms-dms-cms-usage-guide/tags) | Version history |

**Next milestones:**
* **v0.4.2.0** — Style Full Revision
* **v0.5.0.0** — Chapter 4 (TMS) integration

---

## 🤝 Contributing & Community

[![Forum Views](https://img.shields.io/badge/Forum%20Views-1277%20views-brightgreen)](https://forum.falcon-bms.com/topic/32541)

Contributions are welcome! See [CONTRIBUTING.md](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/CONTRIBUTING.md) for guidelines.

**Ways to contribute:**
* Content corrections and accuracy improvements
* Structural and clarity suggestions
* New sections or expanded coverage
* LaTeX compilation or PDF rendering feedback

**Community:**
* 💬 [Join the discussion on Falcon BMS Forum](https://forum.falcon-bms.com/topic/32541)
* ⭐ Star this repo if you find it useful
* 👍 Drop a vote or comment on the forum thread

---

## 📜 License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

This project is released under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

**You are free to:** share, translate, adapt, and enhance this guide with attribution.

**Restrictions:** No commercial use. Attribution required.

For full legal details, see the [LICENSE](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/LICENSE) file.

---

## 👥 Credits & Acknowledgments

**Project Development:**
* Carlos "Metal" Nader — Project lead, content author
* AI Assistants for structural guidance, governance framework, Dash-34 research, and initial content drafting — Perplexity Pro and Claude Pro
* AI Assistant for GitHub coding and repository maintenance — Copilot Pro

**Technical References:**
* Falcon BMS (official manuals & training materials)
* F-16 community knowledge & subject-matter experts

---

## 📞 Contact

For questions, suggestions, or feedback:

* 🕹️ Discord user name: @carlosnader
* 📧 [carlos.snm@gmail.com](mailto:carlos.snm@gmail.com)
* 💬 [Falcon BMS Forum Thread](https://forum.falcon-bms.com/topic/32541)
* 🐛 [Open an Issue](https://github.com/carlos-nader/tms-dms-cms-usage-guide/issues)

---

**License:** CC BY-NC 4.0 | **Guide Status:** Pre-publication v0.4.1.1
