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

### Prompt 11: Delete Incompatible Pillar File
**Date:** 2025-11-21  
**Request:** Still getting KeyError for 'capability_index' in ReadTheDocs build

**Action Taken:**
- Validated that specification.yaml has all required fields (160 items, all valid)
- Discovered that ReadTheDocs builds all .md files in the source directory, not just those in toctree
- Deleted docs/source/new-spec-test-pillar.md file completely to prevent it from being built
- This file was using specification-pillars.yaml which has incompatible hierarchical structure

**Notes:**
- ReadTheDocs processes all markdown files in docs/source/, not just those referenced in index
- Removing from toctree wasn't enough - file needed to be deleted
- specification-pillars.yaml remains for potential future use with a different directive
- The build should now succeed with only new-spec-test.md using specification.yaml

---

### Prompt 12: Regenerate YAML from Updated Excel File
**Date:** 2025-11-21  
**Request:** User updated SATRE.2.0.-.Reorg.xlsx and requested to regenerate YAML files

**Action Taken:**
- Updated create_yaml.py to use SATRE.2.0.-.Reorg.xlsx as source
- Added UTF-8 encoding to file operations to prevent encoding errors
- Recreated create_hierarchy.py script with UTF-8 encoding
- Successfully generated specification.yaml (160 requirements)
- Successfully generated specification-pillars.yaml (4 pillars)

**Notes:**
- Had to wait for user to close Excel file (permission error when file was open)
- UTF-8 encoding was critical to avoid UnicodeDecodeError
- Both YAML files now reflect the updated Excel data
- Scripts are ready for future regeneration when Excel file is updated

---

### Prompt 13: Fix Missing Architecture URLs
**Date:** 2025-11-21  
**Request:** Some architecture URLs were missing from the YAML (e.g., requirement 1.0.1)

**Action Taken:**
- Created diagnostic script (check_excel.py) to investigate the Excel file structure
- Discovered that some cells have URL text but no hyperlink object
- Updated create_yaml.py to extract URLs from both:
  - Hyperlink objects (c.hyperlink.target)
  - Cell text values (c.value) when they start with 'http'
- Regenerated both YAML files successfully
- Verified that requirement 1.0.1 now has its architecture URL

**Notes:**
- Excel file has mixed format: some cells have hyperlinks, others just have URL text
- Script now handles both cases to ensure all URLs are captured
- All 160 requirements now have their architecture URLs properly extracted

---

### Prompt 14: Improve Table Columns - Replace Capability Index with Clickable Capability
**Date:** 2025-11-21  
**Request:** Remove capability_index column and replace with capability from spreadsheet, making it a clickable link to architecture view URL

**Action Taken:**
- Updated docs/extensions/yamlspec.py:
  - Changed COLUMNS to replace capability_index with capability
  - Added logic to render capability as a clickable link using architecture_url
  - Removed architecture_url from displayed columns (now used for capability link)
- Updated docs/source/spec/create_yaml.py:
  - Added "Capability" field extraction from Excel
  - YAML now includes both capability (name) and capability_index (for reference)
- Regenerated both YAML files with new structure

**Notes:**
- Table now shows: Pillar | Capability (clickable) | Requirement Index | Statement | Guidance | Importance
- Capability column links to the architecture view for that capability
- More user-friendly than showing numeric capability_index
- capability_index still in YAML for backward compatibility/reference

---

### Prompt 15: Move and Rename Requirement Index Column
**Date:** 2025-11-21  
**Request:** Move requirement_index column to the left (first position), rename to "SATRE Ref", and make it as narrow as possible

**Action Taken:**
- Updated docs/extensions/yamlspec.py:
  - Modified COLUMNS structure to include display names: (field_name, width, display_name)
  - Moved requirement_index to first position (leftmost column)
  - Reduced width from 10 to 5 to make it narrower
  - Added custom display name "SATRE Ref" for requirement_index
  - Updated header rendering logic to use custom display names when provided
  - Updated all column iteration code to handle new 3-tuple format

**Notes:**
- New column order: SATRE Ref | Pillar | Capability | Statement | Guidance | Importance
- SATRE Ref column is now 5 units wide (half the previous width)
- Makes it easier to reference specific requirements by their SATRE reference number
- No YAML regeneration needed (only display changes)

---

### Prompt 16: Split Table by Pillar with Subheadings
**Date:** 2025-11-21  
**Request:** Split the table into 4 separate tables (one per pillar) with subheadings for each pillar, and remove the pillar column

**Action Taken:**
- Updated docs/extensions/yamlspec.py:
  - Removed pillar from COLUMNS definition
  - Added logic to group specifications by pillar
  - Modified to create multiple tables instead of one
  - Added rubric (subheading) node for each pillar name
  - Returns list of nodes (heading + table for each pillar)
  - Increased statement column width from 40 to 45 (reclaimed from pillar column)
  - Increased guidance column width from 15 to 20

**Notes:**
- Now creates 4 separate tables, one for each pillar
- Each table has a heading with the pillar name
- Pillar column removed from table (redundant with heading)
- More space for content columns (statement and guidance)
- Better visual organization and readability
- No YAML changes needed (only display logic)

---

### Prompt 17: Narrow Left Sidebar Menu
**Date:** 2025-11-21  
**Request:** Narrow the menu on the left of the index page

**Action Taken:**
- Created docs/source/_static/custom.css with custom styles:
  - Reduced sidebar width from 300px to 200px
  - Adjusted main content margin to match new sidebar width
  - Added responsive media query to maintain usability on mobile devices
- Updated docs/source/conf.py:
  - Added html_static_path = ["_static"]
  - Added html_css_files = ["custom.css"]

**Notes:**
- Sidebar is now 200px wide (was 300px)
- Gives more space to the main content area
- Maintains responsive behavior on smaller screens
- Custom CSS will be applied when documentation is built

---
