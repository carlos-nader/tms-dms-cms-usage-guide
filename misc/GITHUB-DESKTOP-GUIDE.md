# GitHub Desktop Guide — Falcon BMS TMS/DMS/CMS Guide Repository

**Purpose:** Provide a simple, repeatable workflow for using **GitHub Desktop** with the Falcon BMS TMS/DMS/CMS HOTAS Usage Guide repository, focusing on governance documents (`docs/`), WIP files (`WIP/`), and the main guide source (`guide-v*.tex`).

---

## 1. Prerequisites

- A GitHub account with access to the repository.
- **GitHub Desktop** installed (latest stable version).
- Local LaTeX toolchain (for compiling `guide-v*.tex`).
- Word or compatible editor (for `.docx` governance documents if needed).

Repository root structure (simplified):

```text
project-root/
├── guide-v0.2.2.0-20260108.tex      # Main LaTeX source (active)
├── docs/                            # Governance and tracking documents
├── WIP/                             # Work-in-progress sections, tables, notes, visuals
├── ARCHIVE/                         # Approved or deprecated WIP files and old guide versions
├── README.md                        # Project overview
└── md-to-docx-v2.9.6.bat            # Markdown → DOCX batch converter
```

---

## 2. Cloning and Updating the Repository

### 2.1 First-Time Clone

1. Open **GitHub Desktop**.
2. Click **File → Clone Repository...**.
3. Select the repository from your GitHub account.
4. Choose a local path (e.g. `C:\Projects\falcon-bms-tms-dms-cms-guide`).
5. Click **Clone**.

### 2.2 Regular Updates (Before Working)

Before any editing session:

1. Open the repository in GitHub Desktop.
2. Ensure the **current branch** is `main` (or the designated default branch).
3. Click **Fetch origin**.
4. If there are remote changes, click **Pull origin**.

This ensures local files match the latest committed state before editing.

---

## 3. Editing Governance Documents (Markdown + DOCX)

Governance documents live in `docs/` and are maintained primarily as **Markdown** (`.md`), with `.docx` versions generated for easier reading.

### 3.1 Typical Files in `docs/`

- `BRIEFING-v0-1-4-1.md` / `.docx`
- `version-system-v4-2.md` / `.docx`
- `WIP-FILE-NAMING-v1-3.md` / `.docx`
- `PROJECT-TRACKING-v4-1-2.md` / `.docx`

### 3.2 Edit Workflow

1. **Pull latest changes** in GitHub Desktop.
2. Open the relevant `.md` file in your preferred text editor (VS Code, etc.).
3. Apply the changes (in English, following the brief).
4. Save the `.md` file.
5. Run `md-to-docx-v2.9.6.bat` (from the project root) to regenerate the corresponding `.docx` in `docs/`.
   - Confirm that the script picked up the updated `.md`.
6. Open the new `.docx` to quickly verify formatting if necessary.

### 3.3 Committing Governance Changes

In GitHub Desktop:

1. Verify that the changed files include:
   - The updated `.md` in `docs/`.
   - The regenerated `.docx` in `docs/`.
2. In the **Changes** tab, review the diffs for the `.md` files (these are authoritative).
3. Write a **descriptive commit message**, for example:
   - `docs: update version-system to v4.2 (EN)`
   - `docs: add session 8 phase 2 summary`
4. Click **Commit to main**.
5. Click **Push origin** to publish changes to GitHub.

---

## 4. Working with WIP Files (`WIP/`)

WIP files are governed by **WIP-FILE-NAMING v1.3**, using status codes like `dev`, `review`, `final`, `approved`, `deprecated` embedded in filenames.

### 4.1 Location and Types

- `WIP/section-*.tex` — Section content under development.
- `WIP/table-*.tex` — HOTAS tables under development.
- `WIP/notes-*.md` — Research notes and scratchpads.
- `WIP/visual-*.*` — Diagrams and schematics.

### 4.2 Basic Workflow with GitHub Desktop

1. **Pull origin** before editing.
2. Open the relevant WIP files in your LaTeX or text editor.
3. Make changes according to the brief and WIP naming rules.
4. If status changes (e.g. `dev` → `review` or `review` → `final`), rename the file accordingly.
5. Back in GitHub Desktop, confirm the modified and renamed files appear under **Changes**.
6. Commit with a message like:
   - `wip: refine cms 5.2 tables (review)`
   - `wip: promote cms 5.1 section to final`
7. Push to origin.

No version bump of `guide-v*.tex` is required until WIP content is integrated into the main guide.

---

## 5. Editing and Versioning the Main Guide (`guide-v*.tex`)

The main guide file follows the format:

```text
guide-vMAJOR.MINOR[.PATCH[.SUBPATCH]]-YYYYMMDD.tex
```

### 5.1 Safe Edit Workflow

1. **Pull origin** to ensure you have the latest main guide.
2. Edit `guide-v*.tex` with your LaTeX editor.
3. Run `pdflatex` (or your preferred LaTeX engine) to confirm the document compiles.
4. Update the version macros in the preamble **only if** the change requires a version bump (according to `VERSION-SYSTEM v4.2`).
5. Rename the `.tex` file if `\docversion` or `\docbuild` changed.
6. Update `PROJECT-TRACKING` with the new version and a short description.

### 5.2 Committing Main Guide Changes

After compilation and tracking updates:

1. In GitHub Desktop, review the changed files:
   - New `guide-v*.tex`.
   - Possibly new or moved older `guide-v*.tex` files into `ARCHIVE/`.
   - Updated `PROJECT-TRACKING` and any related docs.
2. Commit with a message such as:
   - `guide: bump to v0.2.3.0 (cms 5.2 integration)`
3. Push to origin.

---

## 6. Branching Strategy

For this project, the primary workflow can remain **single-branch** (`main`) with disciplined commits, as long as:

- Commits are **small and descriptive**.
- Governance docs (`docs/*.md`) are treated as the **single source of truth** for project rules.
- `guide-v*.tex` is only bumped when version criteria are clearly met.

If a separate branch is desired for experimental work:

1. Create a new branch from `main` in GitHub Desktop (e.g. `feature/cms-tables`).
2. Work and commit on that branch.
3. Open a pull request on GitHub when ready and merge back into `main`.

For now, a single-branch model is usually sufficient given the single-author nature of the project.

---

## 7. Typical Session Checklists

### 7.1 Governance-Only Session (Docs)

1. **Pull origin** in GitHub Desktop.
2. Edit one or more `.md` files in `docs/`.
3. Run `md-to-docx-v2.9.6.bat`.
4. Verify the updated `.docx`.
5. Commit `.md` + `.docx` with a descriptive message.
6. Push to origin.

### 7.2 WIP Content Session

1. **Pull origin**.
2. Edit `WIP/section-*`, `WIP/table-*`, `WIP/notes-*` as needed.
3. If status changes, rename files according to WIP naming rules.
4. Compile test snippets if necessary.
5. Commit WIP changes with a clear message.
6. Push to origin.

### 7.3 Integration Session (Guide Version Bump)

1. **Pull origin**.
2. Integrate `WIP/` content into `guide-v*.tex`.
3. Update version macros and file name if needed.
4. Rebuild the guide PDF.
5. Move integrated WIP files to `ARCHIVE/` as `approved`.
6. Update `PROJECT-TRACKING`.
7. Commit and push.

---

## 8. Troubleshooting with GitHub Desktop

### 8.1 Merge Conflicts

If GitHub Desktop reports a conflict:

1. Click **View conflicts**.
2. Use an external editor (VS Code, etc.) to resolve conflicts in `.md` or `.tex` files.
3. Mark conflicts as resolved in GitHub Desktop.
4. Commit the resolution and push.

### 8.2 Accidental Commits

If a commit includes unwanted files (e.g. LaTeX build artifacts):

1. Add those patterns to `.gitignore` (e.g. `*.aux`, `*.log`, `*.synctex.gz`, `*.pdf`).
2. Remove the unwanted files from the index (via GitHub Desktop or command line).
3. Commit a cleanup change.

---

## 9. Conventions and Best Practices

- Always treat `docs/*.md` as the **authoritative source**; `.docx` is an output.
- Commit `.md` and `.docx` together to avoid divergence.
- Keep commit messages short but precise; reference versions when relevant.
- Pull before every session; push after every coherent unit of work.
- Do not manually edit generated `.docx` files; regenerate from Markdown instead.

Following this guide keeps the repository clean, traceable, and aligned with the project's governance model while using GitHub Desktop as the main interface.