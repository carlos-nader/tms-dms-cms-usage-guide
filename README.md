=======
# TMS/DMS/CMS Usage Guide for Falcon BMS F-16 Flight Simulator

[![Website](https://img.shields.io/badge/website-online-brightgreen)](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)
[![GitHub stars](https://img.shields.io/github/stars/carlos-nader/tms-dms-cms-usage-guide?style=social)](https://github.com/carlos-nader/tms-dms-cms-usage-guide)
[![GitHub forks](https://img.shields.io/github/forks/carlos-nader/tms-dms-cms-usage-guide?style=social)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/fork)

A comprehensive **LaTeX-based technical guide** documenting F-16 HOTAS switch systems (Throttle Management Switch, Data Management Switch, and Countermeasures Management Switch) for Falcon BMS F-16 Flight Simulator.

The author is by no means affiliated to or endorsed by Falcon BMS or its developers. This guide is not an official Falcon BMS guide or manual. It's intended to help the Falcon BMS Community.

---
<div align="center">

#  🚀 **Main Guide File (Current Content Version)** 🚀

![Version](https://img.shields.io/badge/LATEST%20version-v0.3.2.1-yellow?style=for-the-badge&logo=tag&logoColor=black)

---
[![guide.tex](https://img.shields.io/badge/📄-GUIDE.tex%20(CURRENT%20source)-blue?style=for-the-badge&logo=latex&logoColor=white)](guide.tex) [![PDF Preview](https://img.shields.io/badge/📕-guide.pdf%20(Compiled)-brightgreen?style=for-the-badge&logo=pdf&logoColor=white)](guide.pdf)

**👆 CLICK THE ${\color{lightblue}{BLUE}}$ BADGE ABOVE TO OPEN guide.tex (OR ${\color{lightgreen}{GREEN}}$ ONE FOR THE COMPILED guide.pdf)! 👆**
</div>
<br>

---
## 📖 About This Project

 ![Perplexity](https://img.shields.io/badge/perplexity-000000?style=for-the-badge&logo=perplexity&logoColor=088F8F)

This project develops a structured guide explaining HOTAS functionality across multiple F-16 blocks and international variants. The guide serves both novice and experienced pilots, covering conceptual frameworks, switch actuation, system interactions, and operational nuances grounded in Falcon BMS manuals (Dash-34, Dash-1) and training materials. 

**Current Status:** Pre-publication phase (v0.x.x.x) — Chapter scaffolding and narrative consolidation underway.

---

## 🚀 Quick Start

**New to this guide?** Here's how to get started:

1. **📕 Read the Guide:** [Download PDF](guide.pdf) or [view online](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)
2. **🌐 Explore the Website:** [Project documentation site](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)
3. **💬 Join Discussion:** [BMS Forum Thread](https://forum.falcon-bms.com/topic/32541)
4. **⭐ Star this repo** if you find it useful!

5. **👇Keep browsing this README for more *detailed* information**

---

## 📁 Project Structure

```
tms-dms-cms-usage-guide/
│
├── guide.tex                         # Current production version (.tex)
│
├── TEMPLATES/                        # Structural templates & blueprints
│   ├── template-wip-V1.0.tex         # Canonical WIP file template
│   └── guide-structure-only-v*.tex   # Chapter outline baseline
│
├── docs/                             # Governance & tracking (Markdown)
│   ├── BRIEFING-v0.2.0.1.md          # Project scope, style, layout rules
│   ├── WIP-FILE-NAMING-v1.4.md       # Rules for WIP file naming & status
│   ├── VERSION-SYSTEM-v4.2.1.md      # Guide version numbering & phases
│   ├── PROJECT-TRACKING-v5.0.0.md    # Session log, WIP status, milestones
│   ├── TRAINING-MISSION-ABBREV-TABLE-v1.0.md # Table listing Training Mission Abbreviations
│   └── CHARTS_AND_DIAGRAMS/          # AI-generated images of project workflows
│
├── wip/                              # Active work-in-progress files
│   ├── WIP-life-cycle.png            # AI-generated image depicting WIP file lifecycle
│   ├── section-*.tex                 # Chapter sections under development
│   ├── table-*.tex                   # HOTAS table scaffolds & content
│   ├── notes-*.md                    # Research notes & reference material
│   ├── visual-*.*                    # Diagrams, schematics
│   └── guide/                        # Active guide snapshot files (.tex)
│       └── guide-v*.tex              # Current snapshot version
│
├── archive/                          # Historical & approved files
│   ├── WIP/                          # WIP files integrated into guide
│   ├── GUIDE-STRUCTURE/              # Older structure-only files
│   └── GUIDE/                        # Older snapshot guide versions
│
├── fig/                              # Images used in the guide
│
├── LICENSE                           # CC BY-NC 4.0 license text
├── README.md                         # This file
├── CONTRIBUTING.md                   # Contributions guide
└── wip-version-name-generator.html   # Interactive tool for WIP naming

```

---

## 📋 Key Documentation

### Governance Layer

The project uses **four integrated governance documents** (in `/docs/`) that define rules, structure, and workflows.

[![Github Pages](https://img.shields.io/badge/github%20pages-121013?style=for-the-badge&logo=github&logoColor=white)](https://carlos-nader.github.io/tms-dms-cms-usage-guide/)

1. **Briefing Document (BRIEFING-v0.2.0.1.md)**
   - Project scope, content outline, and style guidelines
   - Layout standards and table formatting rules
   - Current status & roadmap

2. **WIP Naming Conventions Guide (WIP-FILE-NAMING-v1.4.md)**
   - Rules for organizing WIP files (sections, tables, visuals, notes)
   - Status lifecycle: dev → review → final → approved → deprecated
   - How to create and track new WIP files

3. **Versioning System Guide (VERSION-SYSTEM-v4.2.1.md)**
   - Guide version numbering (0.x.x.x pre-publication, x.y.z post-publication)
   - MAJOR/MINOR/PATCH/SUBPATCH semantics
   - Integration workflow from WIP to guide snapshots

4. **Project Tracking (PROJECT-TRACKING-v5.0.0.md)** — Living document
   - Session-by-session progress log
   - WIP status snapshot
   - Integration timeline & milestones
   - Current priorities & phases

All governance documents are available in **Markdown** (for editing) and **html** for easy reading.

---

## 🔄 Workflow (WIP Files)

### For Contributors & Developers:

1. **Create**: Copy template from `TEMPLATES/` to `wip/` folder
2. **Name**: Follow naming conventions (use interactive HTML tool in root if needed, or guides in `docs/`)
3. **Develop**: Edit file with status (`dev` → `review` → `final` → `approved`)
4. **Review**: Human review of narrative, accuracy, and style alignment
5. **Archive**: Integrate approved files into guide, move to `archive/`
6. **Track**: Update project tracking document with new version & session log

### File Status Codes:
- **dev** — Draft stage; not ready for review
- **review** — Under human review; open for feedback
- **final** — Approved and ready for integration
- **approved** — Integrated into guide and archived
- **deprecated** — Intentionally retired or superseded

---

## 📊 Current Project State 

[![v0.3.2.1](https://img.shields.io/badge/Release-v0.3.2.1-blue)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/guide.pdf)

| Metric | Value |
|--------|-------|
| **Guide Version** | v0.3.2.1 | 
| **Total Chapters Planned** | 7 |
| **Chapters with Narrative** | 3/7 |
| **Chapters Scaffolded** | 4/7 |
| **Tables Populated** | Chapters 4 & 5 |
| **Phase** | 0 (Chapter scaffolding and content development) |

---

## 🛠️ Tools & Utilities

### WIP Naming Generator
Interactive HTML tool in project root for generating compliant WIP file names based on chapter, section, status, and date.

---

## 📚 Sources & References

This guide is grounded in:

- **TO 1F-16CMAM-34-1-1** — Falcon BMS Simulator F-16 Avionics & Weapons Manual (Dash-34)
- **TO 1F-16CMAM-1** — Falcon BMS Simulator F-16C/D Flight Manual (Dash-1)
- **Falcon BMS 4.38.1 Training Manual** — Falcon BMS Simulator training missions guide
- **F-16 Combat Aircraft Fundamentals Handbook (MCH 11-F16 Vol 5)** — USAF Multi-Command guidelines
- **Various online sources**

All technical claims are cross-referenced to these sources.

---

## 📜 License
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-blue.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

This project is released under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)** license.

**You are free to:**
- **Share** — Copy, distribute, and print this guide
- **Translate** — Adapt to other languages
- **Adapt** — Use sections or content within your own works (with attribution)
- **Enhance** — Create improved or corrected versions

**Under the following restrictions:**
- **No Commercial Use** — You cannot sell this guide or any derivative work
- **Attribution Required** — You must credit Carlos "Metal" Nader and link to the original repository

For full legal details, see: [Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)

---

## 📋 License & Usage Details

This section clarifies what you can and cannot do with this guide under CC BY-NC 4.0.

### What You CAN Do:

✅ **Copy & Share**
- Make copies and share with others (personally, in communities, on forums)
- Distribute PDF links or physical printouts
- Post in Falcon BMS communities and Discord servers

✅ **Translate**
- Translate the guide to Portuguese, Spanish, German, Russian, etc.
- Share translations with credit to original author
- Translations must also be CC BY-NC (free to all users)

✅ **Adapt for Integration**
- Extract sections (e.g., TMS explanation) and incorporate into your own tactical guides
- Reorganize or reformat for readability in different contexts
- Combine with other materials (e.g., create a "Falcon BMS Starter Pack" that includes this guide)
- **Always include:** Original title, author (Carlos "Metal" Nader), and link to this repository

✅ **Enhance & Improve**
- Create enhanced versions with corrections, additional tables, or new sections
- Publish improved versions (v2.0, v2.1, etc.)
- Improved versions must also be CC BY-NC (free to community)
- **Must clearly label** as "Enhanced/Community Version" or similar (cannot claim official status)
- **Must credit** the original guide and author

### What You CANNOT Do:

❌ **Sell or Monetize**
- You cannot sell this guide (printed, digital, or any format)
- You cannot charge for courses or training that uses this as core material
- You cannot include this in paid products without explicit permission
- You cannot use in commercial products or services

❌ **Claim Official Status**
- Derivative versions cannot be presented as "the official guide"
- Must clearly indicate when content is based on or derived from this work

### Attribution Format (When Sharing or Adapting):

Include **all four elements** when sharing or adapting:

1. **Title:** "TMS, DMS, CMS Usage Guide for Falcon BMS"
2. **Author:** "Carlos 'Metal' Nader"
3. **Source:** Link to `https://github.com/carlos-nader/tms-dms-cms-usage-guide`
4. **License:** "CC BY-NC 4.0" with link to `https://creativecommons.org/licenses/by-nc/4.0/`

#### Example Attribution:

```
Falcon BMS TMS/DMS/CMS Usage Guide by Carlos "Metal" Nader
(https://github.com/carlos-nader/tms-dms-cms-usage-guide)
Licensed under CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/)
Adapted for [your project name]
```

### Frequently Asked Questions:

- **Can I translate?** Yes (free, CC BY-NC)
- **Can I make v2.0?** Yes (free, CC BY-NC, must credit original)
- **Can I use in my blog?** Yes (free, with attribution)
- **Can I print and give to friends?** Yes (free)
- **Can I sell printed copies?** No (violates CC BY-NC)
- **Can I include in a paid course?** No (violates CC BY-NC)
- **Can I use a section in my guide?** Yes (free, with clear attribution to this work)

For full legal text and definitions, see the [LICENSE](./LICENSE) file in the repository.

---

## 👥 Credits & Acknowledgments

**Project Development:**
- Carlos "Metal" Nader — Project lead, content author
- AI Assistant (Perplexity Pro) — Structural guidance, governance framework, documentation

**Technical References:**
- Falcon BMS (official manuals & training materials)
- F-16 community knowledge & subject-matter experts

**Tools & Utilities:**
- Texstudio
- Visual Studio Code
- Git/GitHub
- Perplexity AI Pro

---

## 🤝 Contributing [![Static Badge](https://img.shields.io/badge/how_to-contribute-violet?style=plastic&logoSize=auto)](https://github.com/carlos-nader/tms-dms-cms-usage-guide/blob/main/CONTRIBUTING.md)

Contributions are welcome! If you have:

- **Content corrections** — Inaccuracies or outdated information
- **Structural improvements** — Layout, organization, or clarity suggestions
- **New sections** — Expanded coverage of HOTAS systems or variants
- **Testing feedback** — LaTeX compilation or PDF rendering issues

---
## 📞 Contact & Feedback

For questions, suggestions, or feedback about this guide, please:

- Open an issue in the repository
- Review the **Project Tracking** document (in `/docs/`) for current status
- Check the other **Governance Documents** (in `/docs/`) for workflow details
- Falcon BMS Forum: [Thread](https://forum.falcon-bms.com/topic/32541)

![Gmail](https://img.shields.io/badge/Gmail-D14836?style=plastic=gmail&logoColor=white&logoSize=auto) carlos.snm@gmail.com

---

## 🎯 Community Support

[![Forum Views](https://img.shields.io/badge/Forum%20Views-656%20views-brightgreen)](https://forum.falcon-bms.com/topic/32541)

**💬 Join the Discussion!** This guide is being actively developed for the Falcon BMS community. If you find it useful:
- 👍 [Join us on the Falcon BMS Official Forum](https://forum.falcon-bms.com/topic/32541) to show your support — <u>please drop me a vote</u>!
- 💭 Add a comment, compliment, critique, or contribution.
- 🚀 Your feedback helps prioritize future content and improvements.

**Have questions or suggestions?** [Visit the forum topic](https://forum.falcon-bms.com/topic/32541)!

---
## 📅 Project Timeline & Phases

| Phase | Duration | Target | Milestone |
|:-----:|----------|--------|-----------|
| **0** | Current  | v0.1.0 → v0.7.0 | Chapters scaffolded; layout locked |
| **1** | TBD | v1.0.0 → v1.0.x | First public release |

---

## 🔍 Quick Links

- **Active Guide** — `/guide.tex` (current production version)
- **Work in Progress** — `/wip/` (sections, tables, visuals under development)
- **Governance Docs** — `/docs/` (briefing, naming, versioning, tracking)
- **Templates** — `/TEMPLATES/` (WIP template, guide scaffold)
- **Archived Content** — `/archive/` (completed & deprecated files)
- **License** — `/LICENSE` (full CC BY-NC 4.0 legal text)
---

**Last Updated:** 2026-01-30  
**Status:** Pre-publication v0.3.2.1 (Preamble Infrastructure Upgrade)  
**License:** CC BY-NC 4.0
