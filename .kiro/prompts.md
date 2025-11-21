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

### Prompt 18: Make Main Viewing Frame Wider
**Date:** 2025-11-21  
**Request:** Make the main viewing frame wider

**Action Taken:**
- Updated docs/source/_static/custom.css:
  - Added style for .wy-nav-content to increase max-width from 800px to 1200px
  - This gives 50% more width for the main content area

**Notes:**
- Main content area now has max-width of 1200px (was 800px)
- Combined with narrower sidebar (200px), provides much more space for content
- Particularly beneficial for wide tables like the specification table
- Responsive behavior maintained on smaller screens

---

### Prompt 19: Maximize Table Width and Statement/Guidance Columns
**Date:** 2025-11-21  
**Request:** Make the specification table wider, maximizing space for statement and guidance columns

**Action Taken:**
- Updated docs/extensions/yamlspec.py column widths:
  - SATRE Ref: 5 → 4 (narrower)
  - Capability: 15 → 12 (narrower)
  - Statement: 45 → 50 (wider, +5 units)
  - Guidance: 20 → 26 (wider, +6 units)
  - Importance: 10 → 8 (narrower)
- Updated docs/source/_static/custom.css:
  - Added .spec-table width: 100% to use full available width
  - Added word-wrap styles to ensure text wraps properly in cells

**Notes:**
- Statement and guidance columns now get 76% of table width (50+26 out of 100)
- Other columns minimized to essential widths
- Table now uses full width of the 1200px content area
- Better readability for the main content columns

---

### Prompt 20: Make Statement and Guidance Columns Equal Width
**Date:** 2025-11-21  
**Request:** Make the statement and guidance columns the same width

**Action Taken:**
- Updated docs/extensions/yamlspec.py column widths:
  - Statement: 50 → 38
  - Guidance: 26 → 38
  - Both columns now have equal width of 38 units

**Notes:**
- Statement and guidance columns are now balanced at 38 units each
- Total width for these two columns: 76 units (76% of table)
- Other columns remain: SATRE Ref (4), Capability (12), Importance (8)
- Equal width provides visual balance and consistency

---

### Prompt 21: Restore Sidebar to Default Width
**Date:** 2025-11-21  
**Request:** Put the sidebar back to the default

**Action Taken:**
- Updated docs/source/_static/custom.css:
  - Removed custom .wy-nav-side width styling
  - Removed custom .wy-nav-content-wrap margin styling
  - Removed responsive media query for sidebar
  - Sidebar will now use default 300px width

**Notes:**
- Sidebar restored to default 300px width
- Main content area still has 1200px max-width (wider than default)
- Table styling remains (full width, optimized columns)
- Only sidebar customization removed, other improvements kept

---

### Prompt 22: Add Automatic Glossary Links to Specification
**Date:** 2025-11-21  
**Request:** Make glossary terms in the specification clickable links to the UK TRE glossary

**Action Taken:**
- Updated docs/extensions/yamlspec.py:
  - Added import for re and Path modules
  - Created load_glossary_terms() function to read .kiro/sourcefiles/uktre-glossary.yaml
  - Created add_glossary_links() function to automatically link terms to glossary
  - Glossary URL format: https://glossary.uktre.org/en/stable/#term-{term}
  - Terms sorted by length (longest first) to match longer phrases before shorter ones
  - Uses word boundaries to avoid partial matches
  - Applied to both statement and guidance columns
  - Links are added before markdown parsing

**Notes:**
- Automatically links any glossary term found in statement or guidance text
- Case-insensitive matching
- Whole word matching only (won't match partial words)
- Terms like "AAI", "Access Control", "TRE" etc. will be automatically linked
- No manual markup needed in the specification YAML
- Glossary file location: .kiro/sourcefiles/uktre-glossary.yaml

---

### Prompt 23: Fix Glossary Links - Use Docutils Nodes
**Date:** 2025-11-21  
**Request:** Glossary links didn't work when rendered in ReadTheDocs

**Action Taken:**
- Rewrote glossary linking approach in docs/extensions/yamlspec.py:
  - Changed from markdown-style links to direct docutils node manipulation
  - Created create_glossary_term_map() to build term-to-URL mapping
  - Created add_glossary_links_to_node() to recursively process parsed content
  - Processes nodes AFTER markdown parsing, not before
  - Finds text nodes and replaces glossary terms with reference nodes
  - Handles overlapping matches (uses first match)
  - Avoids linking terms that are already inside links
  - Adds CSS class "glossary-term" to links for styling

**Notes:**
- Previous approach tried to add markdown links before parsing (didn't work)
- New approach manipulates the docutils node tree directly
- Works with Sphinx/ReadTheDocs rendering pipeline
- More robust handling of edge cases (overlaps, existing links)

---

### Prompt 24: Add Debugging and Multiple Path Resolution
**Date:** 2025-11-21  
**Request:** Glossary links still didn't work

**Action Taken:**
- Updated docs/extensions/yamlspec.py with debugging and better path resolution:
  - Added multiple possible paths for glossary file location
  - Added print statements to debug glossary loading
  - Tries: extensions/../.kiro/, extensions/../../.kiro/, cwd/.kiro/
  - Prints which path was found and how many terms loaded
  - Prints if term map is empty
  - Added debug parameter to add_glossary_links_to_node

**Notes:**
- Need to check Sphinx build output to see debug messages
- May need to verify glossary file is included in ReadTheDocs build
- Path resolution might be different in ReadTheDocs environment

---

### Prompt 25: Make External Menu Links Open in New Tab
**Date:** 2025-11-21  
**Request:** Make external links in the index menu open in a new browser tab

**Action Taken:**
- Created docs/source/_static/custom.js with JavaScript to:
  - Find all external links in the navigation sidebar (.wy-menu)
  - Find all external links in the table of contents
  - Add target="_blank" to open in new tab
  - Add rel="noopener noreferrer" for security
  - Only affects links to external domains (not same hostname)
- Updated docs/source/conf.py:
  - Added html_js_files = ["custom.js"]

**Notes:**
- Runs on DOMContentLoaded to ensure page is fully loaded
- Checks if link is external by comparing hostname
- Applies to both sidebar menu and TOC links
- Security best practice: rel="noopener noreferrer" prevents window.opener access
- Links like SATRE Architecture and Glossary will now open in new tabs

---

### Prompt 26: Add "About SATRE" Link Above Specification
**Date:** 2025-11-21  
**Request:** Add a link above Specification called "About SATRE" that links to the index

**Action Taken:**
- Updated docs/source/index.md:
  - Added new toctree section with caption "About SATRE"
  - Used "self" keyword to link to the index page itself
  - Positioned above the Specification section

**Notes:**
- "self" is a special Sphinx keyword that refers to the current document
- Creates a link back to the index/home page
- Appears as first item in the navigation menu
- Useful for users to return to the overview/introduction

---

### Prompt 27: Fix FAQs Section in Menu
**Date:** 2025-11-21  
**Request:** Add a link below the Architecture section in the menu to FAQs

**Action Taken:**
- Updated docs/source/index.md:
  - Fixed the FAQs toctree section (was using incorrect syntax)
  - Changed from `:caption: FAQs <faqs.md>` to proper format
  - Now has `:caption: FAQs` with `faqs.md` as content

**Notes:**
- FAQs section was already present but had incorrect syntax
- Caption should not include the file link
- File link goes inside the toctree block
- FAQs now appears as a proper section below Architecture

---

### Prompt 28: Make Pillar Headings Clickable in TOC
**Date:** 2025-11-21  
**Request:** Make the pillars on the specification page subtitles clickable from the index menu

**Action Taken:**
- Updated docs/extensions/yamlspec.py:
  - Changed pillar headings from nodes.rubric to nodes.section
  - Created proper section nodes with IDs (e.g., "information-governance")
  - Added nodes.title for the heading text
  - Tables now added to sections instead of directly to result_nodes
  - Sections appear in the document TOC automatically
- Updated docs/source/new-spec-test.md:
  - Changed title from "Previewing the new spec YAML" to "The SATRE Specification"

**Notes:**
- Pillar sections now have proper IDs for linking
- Will appear in the page's table of contents
- Can be linked directly (e.g., #information-governance)
- Sphinx automatically generates TOC entries for section nodes
- Four pillar sections will be clickable subsections

---

### Prompt 29: Embed YouTube Video in Index Page
**Date:** 2025-11-21  
**Request:** Embed YouTube video "Introduction to the SATRE Project" (https://www.youtube.com/watch?v=auExNHEGwcc) under the "What is SATRE?" section

**Action Taken:**
- Updated docs/source/index.md:
  - Added new subsection "Introduction to the SATRE Project"
  - Embedded YouTube video using raw HTML with responsive iframe
  - Video ID: auExNHEGwcc
  - Used responsive container (16:9 aspect ratio)
  - Positioned after the introductory text about SATRE

**Notes:**
- Used MyST markdown `{raw} html` directive to embed HTML
- Responsive design: video scales with page width
- 16:9 aspect ratio maintained (padding-bottom: 56.25%)
- Includes standard YouTube iframe attributes (allowfullscreen, etc.)
- 20px margin top/bottom for spacing

---

### Prompt 30: Enable Privacy-Enhanced Mode for YouTube Video
**Date:** 2025-11-21  
**Request:** Make sure the video uses privacy-enhanced mode to prevent tracking cookies

**Action Taken:**
- Updated docs/source/index.md:
  - Changed iframe src from `youtube.com` to `youtube-nocookie.com`
  - This enables YouTube's privacy-enhanced mode
  - Prevents YouTube from setting tracking cookies unless user plays the video

**Notes:**
- youtube-nocookie.com is YouTube's privacy-enhanced domain
- Cookies are only set when user actively plays the video
- Complies with GDPR and privacy best practices
- Video functionality remains the same for users

---

### Prompt 31: Add SATRE and TRE Logos for Branding
**Date:** 2025-11-21  
**Request:** Add logos (TRE_LIGHT_STACKED.png and SATRE_Light.png) to brand the pages

**Action Taken:**
- Updated docs/source/conf.py:
  - Added html_logo = "../images/SATRE_Light.png" for sidebar logo
  - Added html_theme_options with logo_only=False, display_version=False
  - SATRE logo will appear in the navigation sidebar
- Updated docs/source/index.md:
  - Added TRE_LIGHT_STACKED.png at the top of the index page
  - Centered, 300px width
  - Positioned above the main heading
- Updated docs/source/_static/custom.css:
  - Styled sidebar logo area with white background
  - Added padding to sidebar logo
  - Centered TRE logo on index page with margin

**Notes:**
- SATRE_Light.png appears in sidebar navigation (all pages)
- TRE_LIGHT_STACKED.png appears at top of index/home page
- Both logos use relative paths from docs/images/
- Responsive sizing for different screen sizes
- White background in sidebar for logo visibility

---

### Prompt 32: Make Embedded Video Smaller
**Date:** 2025-11-21  
**Request:** Make the embedded video smaller

**Action Taken:**
- Updated docs/source/index.md:
  - Added outer container with max-width: 640px
  - Centered the video with margin: 20px auto
  - Kept responsive 16:9 aspect ratio
  - Video now limited to 640px width instead of full page width

**Notes:**
- Video is now 640px wide (standard YouTube medium size)
- Still responsive - will scale down on smaller screens
- Centered on the page for better visual balance
- Maintains 16:9 aspect ratio
- More appropriate size for embedded content

---

### Prompt 33: Replace SATRE Logo with Dark Version
**Date:** 2025-11-21  
**Request:** Replace SATRE_Light.png with SATRE_Stacked_Dark.png

**Action Taken:**
- Updated docs/source/conf.py:
  - Changed html_logo from "../images/SATRE_Light.png" to "../images/SATRE_Stacked_Dark.png"
  - Dark logo will now appear in the sidebar navigation

**Notes:**
- SATRE_Stacked_Dark.png now used for sidebar branding
- Better contrast with white sidebar background
- Stacked version may be more suitable for narrow sidebar

---

### Prompt 34: Move TRE Logo from Index to Sidebar Bottom
**Date:** 2025-11-21  
**Request:** Remove logo from top of main frame and add smaller TRE_LIGHT_STACKED.png to bottom of menu pane

**Action Taken:**
- Updated docs/source/index.md:
  - Removed TRE logo image from top of page
  - Cleaner page header with just the title
- Updated docs/source/_static/custom.js:
  - Added JavaScript to insert TRE logo at bottom of sidebar
  - Creates div with class 'tre-logo-bottom'
  - Appends after navigation menu
- Updated docs/source/_static/custom.css:
  - Styled TRE logo at bottom of sidebar
  - Max width 150px (smaller than before)
  - Centered with padding
  - White background with subtle border
  - Slight opacity (0.8) for subtle appearance

**Notes:**
- TRE logo now appears at bottom of sidebar on all pages
- Smaller and more subtle than previous placement
- SATRE logo remains at top of sidebar
- Both logos now in sidebar for consistent branding

---
