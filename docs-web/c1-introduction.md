---
description: Introduction to the TMS, DMS, and CMS Usage Guide — scope, sources, document structure, and typographic conventions.
---

# 1. Introduction

This document is a community-made reference guide for Falcon BMS 4.38.1, focused on practical use of three HOTAS controls: the Target Management Switch (TMS), the Display Management Switch (DMS), and the Countermeasures Management Switch (CMS). The fundamental behavior of these switches has remained consistent since at least Falcon BMS 4.36, making this guide applicable to virtually any Falcon BMS user.

This work is entirely unofficial. The author is not affiliated with Benchmark Sims, MicroProse, any real-world air force, or any aircraft or weapons manufacturer. All interpretations, simplifications, errors, and omissions are solely the responsibility of the author and must not be attributed to the Falcon BMS development team or any real-world organization.

**Nothing in this document should ever be used for real-world operations, training, or procedures.**

## 1.1 Sources and references

This guide is grounded in the following primary Falcon BMS documents:

1. **TO BMS 1F-16CMAM-34-1-1** (Dash-34, Change 4.38) — Avionics and Nonnuclear Weapons Delivery Flight Manual. Primary source for HOTAS behavior, SOI logic, and weapons employment.
2. **BMS Training Manual 4.38.1** (October 2025) — Training missions and learning objectives. Used for practical cross-references and recommended training progression.

All technical claims in this guide are cross-referenced to these sources. Where specific sections are cited, the notation **Dash-34 § X.Y.Z** refers to Dash-34 section X.Y.Z.

## 1.2 Scope and purpose

The guide organizes TMS, DMS, and CMS behavior by operational context: master mode, sensor configuration, and weapon employment scenario, presenting each switch input and its effect in mode-based tables. Other systems, avionics, and controls are described only when essential to understanding the behavior of these three switches.

Knowledge of basic F-16 operation and familiarity with master modes (NAV, A-A, and A-G) is assumed. This is not a comprehensive HOTAS or avionics manual and does not replace the Dash-34 or Training Manual.

## 1.3 Document structure and how to read it

### 1.3.1 Chapter overview

This guide is organized into six chapters:

* **Chapter 2** establishes the conceptual framework for all three switches: Sensor of Interest (SOI), master modes, and a high-level overview of DMS, TMS, and CMS.
* **Chapters 3–5** cover one switch each — DMS (Chapter 3), TMS (Chapter 4), and CMS (Chapter 5) — combining narrative explanation with standardized HOTAS tables organized by master mode and sensor configuration.
* **Chapter 6** is a quick reference chapter, combining the HOTAS tables from Chapters 3–5 with switch diagrams for immediate visual lookup.

### 1.3.2 Table format

Chapters 3, 4, and 5 use a standardized seven-column table format to document switch behavior. Each row describes a single switch action in a specific operational context:

| Column          | Description                                                                       |
| --------------- | --------------------------------------------------------------------------------- |
| Mode            | Operational context: master mode, sensor state, or weapon configuration           |
| Dir.            | Switch direction: Up, Down, Left, or Right                                        |
| Act.            | Actuation type: Short press or Long press                                         |
| Function        | Brief name of the function performed                                              |
| Effect / Nuance | Detailed explanation of system behavior, constraints, and tactical considerations |
| Dash34          | Cross-reference to Dash-34 section(s)                                             |
| Train.          | Recommended BMS training mission number(s)                                        |

### 1.3.3 Typographic conventions

Three inline formatting conventions are used consistently throughout the guide:

* **Bold** identifies the three HOTAS switches covered by this guide and their directions when referenced in prose: **TMS Up**, **CMS Down**, **DMS Left**.
* `Monospace` reproduces strings exactly as they appear on a system display or are generated as system voice messages: `DISPENSE RDY`, `COUNTER`, `STBY`, `AVNC`.
* _Italic_ marks a technical distinction where sentence structure alone does not sufficiently convey the critical information.

## 1.4 About this document

### 1.4.1 Document version and status

| Item                  | Value                      |
| --------------------- | -------------------------- |
| Document Version      | 0.4.2.0-alpha.2.1+20260314 |
| Falcon BMS Version    | 4.38.1 (Update 1)          |
| Development Phase     | Pre-publication (0.x.x.x)  |
| Chapters with Content | 2/7                        |
| Development Start     | 05 January 2026            |
| Last Update           | 14 March 2026              |

### 1.4.2 Authorship and AI assistance

This guide was created by a member of the Falcon BMS community with structured assistance from AI language models:

* **Perplexity Pro** (Perplexity AI) — Research organization, project structuring, governance framework design, coding, initial draft content generation, and technical review; used via web interface.
* **Claude Pro** (Anthropic) — Research, coding, initial draft content generation, technical review, and governance framework; used via web interface and VSCode (Claude Code).
* **GitHub Copilot Pro** (GitHub / Microsoft) — Documentation, coding, repository management, issue and pull request coordination, and collaborative development; used via GitHub web interface and VSCode.

The author identified scope, validated all content against official Falcon BMS documentation, conducted final text review, made all organizational, editorial, and publication decisions, and bears full responsibility for the guide's accuracy and presentation.

### 1.4.3 License and canonical source

The canonical source for this guide is the project repository:

<p align="center"><a href="https://github.com/carlos-nader/tms-dms-cms-usage-guide">https://github.com/carlos-nader/tms-dms-cms-usage-guide</a></p>

The repository contains the authoritative version of all project files, including governance documents and version history. Translations, adaptations, and derivative works should reference this repository as the original source.

The guide is also available as a web-readable version at:

<p align="center"><a href="https://tms-dms-cms-usage-guide.readthedocs.io">https://tms-dms-cms-usage-guide.readthedocs.io</a></p>

The web version provides navigable, searchable access to all guide content and is recommended for online reference alongside the simulator.

This document is released under the **Creative Commons Attribution-NonCommercial 4.0 International** (CC BY-NC 4.0) license. Sharing, copying, translating, and adapting are permitted with attribution. **Commercial use is prohibited.** Derivative works must maintain the same license and cannot claim official status. Full legal terms: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

**Attribution:** When sharing, translating, or adapting, please include: title, author (Carlos "Metal" Nader), source repository URL, and license.

### 1.4.4 Disclaimer

This is an unofficial, community-made document, provided "as-is" for **educational and simulation training** purposes only.

No copyrighted material is reproduced directly.
