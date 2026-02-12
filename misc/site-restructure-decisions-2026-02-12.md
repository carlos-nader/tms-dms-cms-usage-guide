# Site Restructure - Architectural Decisions

**Date:** 2026-02-12
**Purpose:** Document structural decisions for GitHub Pages site reorganization
**Goal:** Separate end-user audience from contributor audience

---

## 📋 Decisions Summary

### **1. Architecture: Pragmatic Hybrid**
- Main pages in **pure HTML** (index.html, contributing.html)
- Technical documentation in **Markdown** (briefing, project-tracking, etc.)
- Jekyll active for automation, but doesn't control everything

---

### **2. Audience Separation**
- **index.html** → 100% focused on **end users** (BMS pilots who want to use the guide)
- **contributing.html** → 100% focused on **contributors** (developers who want to help the project)
- Objective: End user doesn't see development information

---

### **3. Jekyll Automation**
- **jekyll-sitemap** enabled → Generates sitemap.xml automatically
- **jekyll-seo-tag** enabled → Generates meta tags for Markdown pages
- HTML pages use **YAML frontmatter** to control sitemap (priority, changefreq)

---

### **4. SEO Meta Tags**
- **index.html** and **contributing.html** → Manual tags (keep existing, copy/adjust)
- **Markdown docs** → jekyll-seo-tag automatic via frontmatter
- Full control on main pages, automation on secondary pages

---

### **5. Sitemap Priorities**
- **index.html** → Priority 1.0 (maximum)
- **contributing.html** → Priority 0.4-0.5 (low)
- **Technical docs** (WIP naming, version system, etc.) → Priority 0.2 OR `sitemap: false` (no indexing)

---

### **6. Content Redistribution**

#### **What LEAVES index.html:**
- Project Governing Documentation (briefing, project-tracking, integrated-files)
- Development Standards (wip-naming, version-system)
- Tools & Utilities (WIP Filename Generator)
- Workflow Diagrams (all workflow SVG/PNG files)

#### **What GOES TO contributing.html:**
- ALL development documentation listed above
- Contributor instructions
- Links to GitHub, setup guide, changelog

#### **What STAYS in index.html:**
- About This Guide (introduction)
- What You'll Learn (guide content overview)
- **HUGE EMPHASIS**: Link/button to PDF
- Target Audience
- Related Resources (Falcon BMS, community)
- License & Attribution
- Discreet footer link: "Want to contribute? See contributing guide"

---

### **7. File Structure (no folder changes)**
```
docs/
├── index.html              (end users - CLEANED)
├── contributing.html       (contributors - CREATED)
├── guide-web.pdf          (keep)
├── briefing-v0.2.0.1.md   (can convert or keep .html)
├── project-tracking-v5.0.0.md
├── wip-naming-v1.4.md
├── version-system-v4.2.1.md
├── _config.yml            (add plugins)
├── sitemap.xml            (will be generated automatically)
└── robots.txt             (keep)
```

---

### **8. Maintenance Philosophy**
- **Don't throw away work** (leverage existing HTML)
- **Automation where it makes sense** (sitemap, docs SEO)
- **Control where it matters** (main page design)
- **Sustainable** (easy to maintain long-term)

---

## ✅ Next Steps

Define **content structure** for each page:
1. What exactly goes in **index.html** (sections, order, emphasis)
2. What exactly goes in **contributing.html** (dev doc organization)

---

## 🎯 Key Principles

1. **User first**: End user should immediately understand the site is for them
2. **PDF prominent**: Main CTA should be downloading/viewing the guide
3. **Contributors welcome**: But their docs are in a separate, dedicated page
4. **SEO smart**: High priority for user content, low/no index for dev docs
5. **Pragmatic approach**: Use automation where it helps, manual control where needed

---

## 📝 Open Questions

- [ ] Should technical docs be converted to Markdown or keep as HTML?
- [ ] Exact content structure for index.html hero section
- [ ] Exact content structure for contributing.html organization
- [ ] Design/styling for contributing.html (match index.html style?)

---

**Status:** Architectural decisions finalized, ready to proceed with implementation
