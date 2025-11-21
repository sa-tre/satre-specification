import os
import re
import yaml
from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.docutils import SphinxDirective
from pathlib import Path

# Define the columns and their proportional widths for the table
# Format: (field_name, width, display_name)
# Note: pillar column removed as it will be shown as section headings
# Statement and guidance columns have equal width for balance
COLUMNS = [
    ("requirement_index", 4, "SATRE Ref"),
    ("capability", 12, None),
    ("statement", 38, None),
    ("guidance", 38, None),
    ("importance", 8, None),
]

# Glossary base URL
GLOSSARY_BASE_URL = "https://glossary.uktre.org/en/stable/#term-"

def load_glossary_terms():
    """Load glossary terms from the YAML file."""
    # Try multiple possible paths
    possible_paths = [
        Path(__file__).parent.parent / ".kiro" / "sourcefiles" / "uktre-glossary.yaml",
        Path(__file__).parent.parent.parent / ".kiro" / "sourcefiles" / "uktre-glossary.yaml",
        Path.cwd() / ".kiro" / "sourcefiles" / "uktre-glossary.yaml",
    ]
    
    glossary_path = None
    for path in possible_paths:
        if path.exists():
            glossary_path = path
            print(f"Found glossary at: {glossary_path}")
            break
    
    if not glossary_path:
        print(f"Warning: Could not find glossary file. Tried: {[str(p) for p in possible_paths]}")
        return []
    
    try:
        with open(glossary_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            if "glossary" in data and isinstance(data["glossary"], list):
                # Extract terms and sort by length (longest first) to match longer terms first
                terms = [item["term"] for item in data["glossary"] if "term" in item]
                print(f"Loaded {len(terms)} glossary terms")
                return sorted(terms, key=len, reverse=True)
    except Exception as e:
        print(f"Warning: Could not load glossary: {e}")
    
    return []

def create_glossary_term_map(glossary_terms):
    """Create a mapping of terms to their URLs."""
    term_map = {}
    for term in glossary_terms:
        # Create URL-safe version of term (lowercase, replace spaces with hyphens)
        term_url = term.lower().replace(" ", "-").replace("(", "").replace(")", "")
        url = f"{GLOSSARY_BASE_URL}{term_url}"
        term_map[term.lower()] = (term, url)
    return term_map

def add_glossary_links_to_node(node, term_map, debug=False):
    """
    Recursively process a docutils node tree and add glossary links.
    Replaces text nodes containing glossary terms with reference nodes.
    """
    if isinstance(node, nodes.Text):
        # Process text node
        text = str(node)
        parent = node.parent
        
        if parent is None or isinstance(parent, nodes.reference):
            # Don't process if already in a link
            return
        
        # Find all glossary terms in this text
        new_nodes = []
        last_end = 0
        
        # Sort terms by position in text
        matches = []
        for term_lower, (term_original, url) in term_map.items():
            pattern = r'\b' + re.escape(term_original) + r'\b'
            for match in re.finditer(pattern, text, flags=re.IGNORECASE):
                matches.append((match.start(), match.end(), match.group(0), url))
        
        # Sort by position and remove overlaps
        matches.sort()
        filtered_matches = []
        last_match_end = -1
        for start, end, matched_text, url in matches:
            if start >= last_match_end:
                filtered_matches.append((start, end, matched_text, url))
                last_match_end = end
        
        # Build new node list
        for start, end, matched_text, url in filtered_matches:
            # Add text before match
            if start > last_end:
                new_nodes.append(nodes.Text(text[last_end:start]))
            
            # Add reference node for the match
            ref_node = nodes.reference("", matched_text, refuri=url, classes=["glossary-term"])
            new_nodes.append(ref_node)
            last_end = end
        
        # Add remaining text
        if last_end < len(text):
            new_nodes.append(nodes.Text(text[last_end:]))
        
        # Replace the text node with new nodes if we found any matches
        if new_nodes:
            index = parent.index(node)
            parent.remove(node)
            for i, new_node in enumerate(new_nodes):
                parent.insert(index + i, new_node)
    else:
        # Recursively process child nodes
        for child in list(node.children):
            add_glossary_links_to_node(child, term_map, debug)


class YamlSpecDirective(SphinxDirective):
    """
    Sphinx directive to read a YAML specification file and render it as a table.
    Usage:
        .. yaml-specification:: path/to/spec.yaml
    """

    # The directive requires exactly one argument: the filename
    required_arguments = 1
    has_content = False

    def run(self):
        # 1. Resolve File Path
        yaml_filename = self.arguments[0]

        # Use env.relfn2path to robustly resolve the path relative to the current
        # document (self.env.docname).
        try:
            # relfn2path returns (relative_path_from_srcdir, absolute_path)
            # We take index [1] for the absolute path.
            _, abs_path = self.env.relfn2path(yaml_filename, self.env.docname)
        except Exception as e:
            error_msg = f"Could not resolve file path for {yaml_filename}. Error: {e}"
            return [nodes.error("", nodes.paragraph(text=error_msg))]

        # 2. Load YAML Data
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
        except FileNotFoundError:
            error_msg = f"YAML specification file not found at: {abs_path}"
            return [nodes.error("", nodes.paragraph(text=error_msg))]
        except yaml.YAMLError as e:
            error_msg = f"Error parsing YAML file {yaml_filename}: {e}"
            return [nodes.error("", nodes.paragraph(text=error_msg))]

        if "specification" not in data or not isinstance(data["specification"], list):
            error_msg = f"YAML file {yaml_filename} must contain a list under the 'specification' key."
            return [nodes.error("", nodes.paragraph(text=error_msg))]

        specifications = data["specification"]

        # 3. Load glossary terms for linking
        glossary_terms = load_glossary_terms()
        term_map = create_glossary_term_map(glossary_terms)
        if term_map:
            print(f"Created term map with {len(term_map)} terms")
        else:
            print("Warning: No glossary terms loaded")

        # 4. Group specifications by pillar
        pillars = {}
        for item in specifications:
            pillar_name = item.get("pillar", "Unknown")
            if pillar_name not in pillars:
                pillars[pillar_name] = []
            pillars[pillar_name].append(item)

        # 5. Create a list of nodes (headings + tables) for each pillar
        result_nodes = []

        for pillar_name, pillar_items in pillars.items():
            # Add pillar heading
            heading = nodes.rubric(text=pillar_name)
            result_nodes.append(heading)

            # Create table for this pillar
            table = nodes.table(classes=["spec-table", "colwidths-given"])
            tgroup = nodes.tgroup(cols=len(COLUMNS))
            table += tgroup

            # Add column specifications (colspec)
            for _, width, _ in COLUMNS:
                tgroup += nodes.colspec(colwidth=width)

            # Table Header (thead)
            thead = nodes.thead()
            header_row = nodes.row()
            for field_name, _, display_name in COLUMNS:
                entry = nodes.entry(classes=["head"])
                # Use custom display name if provided, otherwise format field name
                header_text = display_name if display_name else field_name.replace("_", " ").capitalize()
                entry += nodes.paragraph(text=header_text)
                header_row += entry
            thead += header_row
            tgroup += thead

            # Table Body (tbody)
            tbody = nodes.tbody()

            for item in pillar_items:
                row = nodes.row()
                for key, _, _ in COLUMNS:
                    entry = nodes.entry()
                    content_text = str(item.get(key, "") or "")

                    # Use nested_parse for multi-line fields to process reST content (like links)
                    if key in ["statement", "guidance"]:
                        # Create a ViewList of lines for nested parsing
                        view_list = ViewList()
                        # Add content line by line, ensuring correct source/line references
                        for line in content_text.splitlines():
                            view_list.append(line, yaml_filename, self.lineno)

                        # FIX: Use nodes.container instead of nodes.section to avoid the
                        # AssertionError when children are appended to the entry node.
                        content_node = nodes.container()

                        # Nested parse the content
                        self.state.nested_parse(view_list, 0, content_node)

                        # Add glossary links to the parsed content
                        add_glossary_links_to_node(content_node, term_map)

                        # Add the children (paragraphs, links, etc.) of the parsed container to the entry
                        entry.extend(content_node.children)
                    elif key == "capability":
                        # Make capability a clickable link to architecture_url
                        arch_url = item.get("architecture_url", "")
                        if arch_url and content_text:
                            reference_node = nodes.reference(
                                "",
                                nodes.Text(content_text),
                                refuri=arch_url,
                                classes=["external"],
                            )
                            paragraph_node = nodes.paragraph("")
                            paragraph_node.append(reference_node)
                            entry += paragraph_node
                        else:
                            # No URL, just display text
                            entry += nodes.paragraph(text=content_text)
                    else:
                        # Simple text fields (requirement, importance) are wrapped in a paragraph
                        entry += nodes.paragraph(text=content_text)

                    row += entry
                tbody += row

            tgroup += tbody
            result_nodes.append(table)

        # 5. Return all nodes (headings + tables)
        return result_nodes


# Setup function to register the directive
def setup(app):
    """Register the directive with Sphinx."""
    app.add_directive("yaml-specification", YamlSpecDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
