# GitHub Issue Templates — Installation Guide

## 📦 What You Have

4 YAML template files for GitHub issue creation:

1. **wip-dev-template.yml** — [WIP DEV] Create structure and first draft
2. **wip-review-template.yml** — [WIP REVIEW] Review and refine content
3. **wip-final-template.yml** — [WIP FINAL] Approve and lock
4. **wip-approved-template.yml** — [WIP APPROVED] Integrate and release

---

## 📥 Installation Steps

### Step 1: Create Folder in Your Repository

In your GitHub repository, you need to create a special folder structure:

```
seu-repo/
├─ .github/
│  └─ ISSUE_TEMPLATE/
│     ├─ wip-dev-template.yml
│     ├─ wip-review-template.yml
│     ├─ wip-final-template.yml
│     ├─ wip-approved-template.yml
│     └─ config.yml (optional)
```

**If `.github/` doesn't exist:**
- Create it at repository root
- Then create `ISSUE_TEMPLATE/` folder inside

**If `.github/ISSUE_TEMPLATE/` already exists:**
- Just add the 4 YAML files

### Step 2: Copy Files

Copy each YAML file into `.github/ISSUE_TEMPLATE/`:

```bash
# From your local machine:
cp wip-dev-template.yml your-repo/.github/ISSUE_TEMPLATE/
cp wip-review-template.yml your-repo/.github/ISSUE_TEMPLATE/
cp wip-final-template.yml your-repo/.github/ISSUE_TEMPLATE/
cp wip-approved-template.yml your-repo/.github/ISSUE_TEMPLATE/
```

**Or via GitHub Web UI:**
1. Go to your repo
2. Click "Add file" → "Create new file"
3. Path: `.github/ISSUE_TEMPLATE/wip-dev-template.yml`
4. Paste content from the file
5. Commit
6. Repeat for other 3 templates

### Step 3: Commit and Push

```bash
git add .github/ISSUE_TEMPLATE/
git commit -m "feat: Add GitHub issue templates for WIP workflow"
git push origin main
```

### Step 4: Verify

1. Go to your GitHub repo
2. Click "Issues" tab
3. Click "New Issue"
4. You should see a prompt: **"Choose an issue type"**
5. Templates should appear as options:
   - ✅ [WIP DEV] Define structure and generate first version
   - ✅ [WIP REVIEW] Review content and refine
   - ✅ [WIP FINAL] Approve and lock for integration
   - ✅ [WIP APPROVED] Integrate into guide and create release

---

## 🎯 How to Use After Installation

### Creating a New Milestone

**For Section C4:S4 (TMS Right/Left):**

#### Issue #13 (DEV)
1. Click "New Issue"
2. Select template: **"[WIP DEV] Define structure..."**
3. Fill in:
   - Chapter and Section: `C4:S4`
   - Topic Title: `TMS Right/Left`
4. Check the deliverables checklist
5. Click "Create Issue"
6. GitHub auto-populates:
   - ✅ Title: `[C4:S4] DEV — Define structure...`
   - ✅ Labels: `documentation`, `wip`
   - ✅ Assignee: `carlos-nader`
7. Click "Mark as blocking" → select Issue #14 (when created)

#### Issue #14 (REVIEW)
1. Click "New Issue"
2. Select template: **"[WIP REVIEW] Review content..."**
3. Fill in same fields + review notes
4. Create Issue
5. After creation:
   - Click "Mark as blocked by" → Issue #13
   - Click "Mark as blocking" → Issue #15 (when created)

#### Issue #15 (FINAL)
1. New Issue → Select "[WIP FINAL] Approve..."
2. Fill in fields
3. After creation:
   - Click "Mark as blocked by" → Issue #14
   - Click "Mark as blocking" → Issue #16 (when created)

#### Issue #16 (APPROVED)
1. New Issue → Select "[WIP APPROVED] Integrate..."
2. Fill in fields + follow integration steps
3. After creation:
   - Click "Mark as blocked by" → Issue #15

---

## 🔄 Workflow Visualization

```
Issue #13 (DEV)
    ↓ blocks
Issue #14 (REVIEW)
    ↓ blocks
Issue #15 (FINAL)
    ↓ blocks
Issue #16 (APPROVED)
    ↓ closes
Milestone Complete ✅
```

---

## 💡 Template Field Reference

### All Templates Include:

- **Chapter and Section ID** (e.g., C4:S4)
- **Section Title** (e.g., TMS Right/Left)
- **WIP Target Filename** (pre-filled based on status)
- **Checklist of Deliverables** (customized per phase)
- **Notes/Comments section** (for iteration tracking)
- **Related Documentation links** (quick reference)

### Status Transitions:

| Phase | Filename Pattern | GitHub Status |
|-------|------------------|---------------|
| DEV | `-dev-` | 🔵 In Progress |
| REVIEW | `-review-` | 🟡 In Progress |
| FINAL | `-final-` | 🟢 Ready |
| APPROVED | `-approved-` | ✅ Integrated |

---

## 🚨 Troubleshooting

### Templates Not Appearing

**Problem:** You click "New Issue" but don't see the templates.

**Solution:**
1. Verify folder path: `.github/ISSUE_TEMPLATE/` (exactly)
2. Verify filenames end with `.yml` (not `.yaml`)
3. Files must be committed to `main` branch (not in draft)
4. Wait 5 minutes and refresh GitHub page
5. Hard refresh browser (Ctrl+Shift+R)

### Template Name Wrong

**Problem:** You see filenames instead of nice names in the chooser.

**Solution:**
- Check `name:` field in YAML file (line 1)
- The `name:` value is what appears in GitHub UI
- Must come **before** `description:`

### Checklist Items Not Working

**Problem:** Checkboxes don't appear or are malformed.

**Solution:**
- YAML indentation must be exactly 2 spaces (not tabs)
- Each `- label:` must be same indent level as others
- Verify no trailing spaces

---

## 📖 Additional Resources

- [GitHub Issue Templates Documentation](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests)
- [YAML Syntax Guide](https://docs.ansible.com/ansible/latest/reference_appendices/YAMLSyntax.html)
- Your project docs:
  - WIP-FILE-NAMING-v1.4
  - VERSION-SYSTEM-v4.2.1
  - PROJECT-TRACKING-v5.0.0

---

## ✅ Checklist: Installation Complete

After following the steps above:

- [ ] Created `.github/ISSUE_TEMPLATE/` folder
- [ ] Copied all 4 YAML files
- [ ] Committed and pushed to `main` branch
- [ ] Verified templates appear in "New Issue" chooser
- [ ] Created test issue using one template
- [ ] Test issue has correct title, labels, assignee
- [ ] Closed test issue
- [ ] Ready to use for real work

---

**You're all set!** 🚀

Next time you start a new section milestone, just:
1. Click "New Issue"
2. Select the appropriate template
3. Fill in chapter/section/title
4. Check the deliverables
5. Click "Create"
6. Then use "Relationships" to set dependencies

Happy templating! 📋