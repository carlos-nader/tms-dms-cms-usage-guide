# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project follows a custom versioning system (see docs/version-system.md).

---

## [0.4.1.1] - 2026-02-18
### Changed
- Wording: Removed 9 redundant passages across the whole document, per BMS forum feedback.

### Fixed
- HOTAS tables: Added missing `\label` tags to 5 `hotastable` environments in Chapter 5.

## [0.4.1.0] - 2026-02-11
### Added
- hotastable v2.1: Optimized HOTAS table environment.
- List of HOTAS Tables: Automated indexing feature with clickable navigation.
- Cross-reference macros: Internal linking macros.
- PDF metadata: Document properties configuration.
- enumitem package: Enhanced list customization support.

### Changed
- Training column format: Simplified from full mission descriptions to numbers.
- LaTeX templates: Updated `TEMPLATES/template-wip-V1.0.tex` and `guide-structure-only-v0.4.0.0.tex` with new preamble.
- WIP files: Updated `chapter-C4-tms-structure-dev-2026-02-11.tex` with new preamble.
- Documentation: Updated `briefing.md` with complete new preamble specifications.

### Fixed
- PDF bookmark navigation: List of HOTAS Tables bookmark now points to correct page.
- Table overflow: Eliminated overflow issues in HOTAS tables through optimized column widths.

### Removed
- `docs/training-mission-abbrev-table-v1.0.md` — Obsolete with simplified Training column format.

## [0.4.0.0] - 2026-02-10
### Added
- Chapter 2 (HOTAS Fundamentals): Complete integration establishing conceptual foundation for SOI, master modes, and HOTAS switch behavior.
- Chapter 3 (DMS): Complete integration (renumbered from Chapter 4).

### Changed
- Chapter reorganization: DMS moved from C4→C3, TMS moved from C3→C4 (pedagogical sequence: teach display selection before target manipulation).
- SOI content refactored: Conceptual foundation in C2 (Section 2.1), operational details in C3 (Section 3.1).
- Labels and cross-references: All systematically updated to reflect new chapter structure.

### Fixed
- C2 critical errors: Corrected TMS/CMS switch locations (both on flight stick, not throttle).
- C2 content refinement: Removed redundant operational details, eliminated grammatical errors.

---

## [0.3.3.0] - 2026-02-02
### Added
- Chapter 4 (DMS): Complete chapter integration with all sections and tables.
- Chapter 1 (Introduction): Revised and re-integrated with updated structure.

### Changed
- Table layout: Updated to 15.6 cm standard width.
- Cross-references: Revised Dash-34 links and internal references.

### Fixed
- Minor typographical and formatting errors in previous chapters.

---

## [0.3.2.1] - 2026-01-29
### Added
- INTEGRATED-FILES.md: Automated report generation via GitHub Actions.

### Changed
- hotastable environment: Upgraded `\arraystretch` to 1.25 for improved table spacing.
- Automation: Enhanced snapshot and versioning workflows.

---

## [0.3.2.0] - 2026-01-19
### Added
- Section 4.3 (DMS Down): Toggle SOI Among Displays functionality integrated with complete tables and operational details.

### Changed
- LaTeX preamble: Style adjustments for improved document structure.

---

## [0.3.1.0] - 2026-01-18
### Added
- DMS chapter structure: Initial scaffolding for Chapter 4 (DMS) sections and subsections.

### Changed
- Document class upgrade: Migrated from `article` to `report` class for professional multi-chapter structure.
- Preamble infrastructure: Enhanced for report-style document with improved chapter hierarchy.

---

## [0.3.0.1] - 2026-01-16
### Added
- Integrated files report: Automated generation of `INTEGRATED-FILES.md` via GitHub Actions.
- DMS Section file: Created `section-C4-S1-S3.tex` for development.

### Changed
- CI/CD workflows: Enhanced automation for version tracking and file validation.
- README.md: Updated with current project status and structure.
- File naming: Standardized according to WIP-FILE-NAMING conventions.

---

## [0.3.0.0] - 2026-01-15
### Added
- Section 4.1 (Concept and SOI): DMS conceptual foundation and Sensor of Interest framework integrated.
- Section 4.2 (DMS Up): HDU Designation as SOI functionality integrated with complete tables.
- Guide scaffolding: Established main chapter and section structure for all planned chapters.

---

## [0.2.4.0] - 2026-01-12
### Added
- Chapter 5 (CMS): Complete integration with all sections (§5.1 Concept and Interactions, §5.2 Switch Actuation, §5.3 Block/Variant Notes) and 6 HOTAS tables.
- WIP file validation: Automated workflow for validating WIP/ARCHIVE file naming conventions.

---

## [0.2.0.0] - 2026-01-11
### Added
- Chapter 5 (CMS): Initial integration with foundational sections.
- WIP template: Established `TEMPLATES/template-wip-V1.0.tex` as canonical template for all work-in-progress files.

---

## [0.1.4.0] - 2026-01-07
### Added
- Layout standard (Geometry D): A4 paper with 2.0cm left/right, 2.5cm top/bottom margins, 17.0cm text width.
- hotastable standard: 15.6 cm table width with 7-column HOTAS layout.
- BRIEFING document: Project brief establishing content standards, layout parameters, and governance rules.

### Changed
- Geometry locked: All future content must conform to Geometry D standard.

---

## [0.1.0.0] - 2026-01-05
### Added
- Project initialization: Repository structure, governance documents, and version system established.
- Chapter scaffolding: Initial LaTeX structure for all 7 planned chapters.
- Chapter 1 (Introduction): First complete chapter integrated.

---

<!-- Add new versions above this line following the same pattern. -->
