# Project Prompts

This file records all prompts and AI interactions for this project.

## Session: 2025-11-21

### Prompt 6: Add SATRE Control Alignment Link
**Date:** 2025-11-21  
**Request:** Add a link to alignment.md under the Specification heading in index.md, labeled as "SATRE Control Alignment"

**Action Taken:**
- Added alignment.md link to the Specification section in docs/source/index.md
- Used custom label "SATRE Control Alignment" for the link

---

### Prompt 5: Move Publicly Available Evaluations Section
**Date:** 2025-11-21  
**Request:** Move the "Publicly available evaluations" section to between "Why should I evaluate my institution's TRE?" and "Method" sections

**Action Taken:**
- Moved the "Publicly available evaluations" section from the end of the document
- Positioned it after the note about SATRE not being a formal standard
- Now appears before the "Method" section for better flow

---

### Prompt 4: Update Evaluation Page
**Date:** 2025-11-21  
**Request:** Update docs/source/evaluation.md to:
- Remove references to old example evaluations (Alan Turing Institute and Dundee HIC)
- Add new section for "Publicly available evaluations"
- Point to the main SATRE site for examples
- Encourage organizations to share evaluations for community benefit and openness

**Action Taken:**
- Removed paragraph referencing old example evaluations
- Added new "Publicly available evaluations" section at the end
- Linked to Standard Architecture for Trusted Research Environments site
- Added encouragement for organizations to share evaluations publicly

**Notes:**
- Old evaluation examples are no longer in this repository
- Promotes community contribution and transparency

---

### Prompt 3: Reorganize Site Structure
**Date:** 2025-11-21  
**Request:** Reorganize the site structure in docs/source/index.md with 3 sections:
1. Specification - links to new-spec-test.md and evaluation.md
2. Architecture - links to architecture.md, external SATRE Architecture link, and roles.md
3. Contributing - keep existing structure

**Action Taken:**
- Updated docs/source/index.md with new toctree structure
- Removed old Overview, Specification (pillars), Evaluation, and Glossary sections
- Created new simplified structure with 3 main sections
- Added external link to SATRE Architecture ReadTheDocs site
- Maintained same formatting style with hidden toctrees and captions

**Notes:**
- Old sections removed: Overview, numbered Specification with pillars, separate Evaluation section, Glossary
- Next steps: Remove unused files from the repository

---

### Prompt 1: Initial Setup
**Date:** 2025-11-21  
**Request:** Create a .kiro folder and create a markdown file to record all the prompts for this project

**Action Taken:**
- Created `.kiro` folder
- Created `prompts.md` file to track project prompts and AI interactions

---

### Prompt 2: Project Context
**Date:** 2025-11-21  
**Request:** Read the README to understand the SATRE project

**Action Taken:**
- Read README.md to understand project scope and structure
- Identified project as SATRE (Standard Architecture for Trusted Research Environments)
- Key findings:
  - Community-driven specification for standardizing TREs in the UK
  - Funded by DARE UK with multiple university/institution partners
  - Documentation built with Sphinx and hosted on ReadTheDocs
  - 41+ contributors from various organizations
  - Bi-weekly collaboration cafes for community engagement
  - Documentation written in markdown files in `docs/` folder

**Notes:**
- Main documentation likely in `docs/source/` folder
- Project uses ReadTheDocs for hosting specification
- Active community with regular meetings and contributions

---

## Template for Future Entries

### Prompt [Number]: [Brief Description]
**Date:** YYYY-MM-DD  
**Request:** [User's request or question]

**Action Taken:**
- [What was done]
- [Results or outcomes]

**Notes:**
- [Any relevant observations or follow-up items]

---

### Prompt 10: Fix ReadTheDocs Build Error
**Date:** 2025-11-21  
**Request:** Fix KeyError: 'capability_index' error in ReadTheDocs build from yamlspec.py extension

**Action Taken:**
- Identified the issue: new-spec-test-pillar.md was using specification-pillars.yaml which has a hierarchical structure
- The yamlspec.py extension expects a flat structure with all fields (pillar, capability_index, etc.) at the top level
- specification-pillars.yaml has nested structure: pillar → capabilities → statements (missing pillar and capability_index in statements)
- Removed the pillar version link from docs/source/index.md to fix the build error

**Notes:**
- specification.yaml (flat structure) works fine with yamlspec.py
- specification-pillars.yaml (hierarchical) is incompatible with current yamlspec.py
- new-spec-test-pillar.md file still exists but is no longer referenced
- Could create a separate directive for hierarchical format if needed in the future

---
