# Project Prompts

This file records all prompts and AI interactions for this project.

## Session: 2025-11-21

### Prompt 9: Generate YAML Files from New Source
**Date:** 2025-11-21  
**Request:** Create the YAML files using the new SATRE_source.xlsx file

**Action Taken:**
- Created Python scripts from the Jupyter notebooks (create_yaml.py and create_hierarchy.py)
- Installed required package: ruamel.yaml
- Fixed script to handle cells without hyperlinks
- Successfully ran create_yaml.py to generate specification.yaml (160 requirements)
- Successfully ran create_hierarchy.py to generate specification-pillars.yaml (4 pillars)

**Notes:**
- The YAML files are now generated from SATRE_source.xlsx
- specification.yaml contains flat list of all requirements
- specification-pillars.yaml contains hierarchical structure organized by pillars
- Python scripts can be used instead of Jupyter notebooks for easier automation

---

### Prompt 8: Update Source Excel File Reference
**Date:** 2025-11-21  
**Request:** Update the Jupyter notebooks to use the new SATRE_source.xlsx file as the source for generating YAML

**Action Taken:**
- Updated docs/source/spec/createyaml.ipynb to reference SATRE_source.xlsx instead of SATRE.2.0.-.Reorg.xlsx (2 occurrences)
- hierarchy.ipynb doesn't need updating as it reads from the generated specification.yaml file

**Notes:**
- createyaml.ipynb reads the Excel file and generates specification.yaml
- hierarchy.ipynb then processes specification.yaml to create specification-pillars.yaml
- The old Excel file (SATRE.2.0.-.Reorg.xlsx) can potentially be removed once confirmed the new file works

---

### Prompt 7: Specification Scripts Location
**Date:** 2025-11-21  
**Request:** User indicated that the scripts that create the YAML file with the specification are in docs/source/spec

**Action Taken:**
- Listed contents of docs/source/spec folder
- Found key files:
  - createyaml.ipynb - Jupyter notebook for creating YAML
  - hierarchy.ipynb - Jupyter notebook for hierarchy processing
  - SATRE.2.0.-.Reorg.xlsx - Excel source file
  - specification-pillars.yaml - YAML output (pillars version)
  - specification.yaml - YAML output (main specification)

**Notes:**
- The workflow appears to be: Excel → Jupyter notebooks → YAML files
- Two YAML outputs suggest different formats/structures of the specification

---

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
