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

        # 3. Validate and group specifications by pillar
        pillars = {}
        for idx, item in enumerate(specifications):
            # Validate required fields
            if not isinstance(item, dict):
                error_msg = f"Item {idx} in specification is not a dictionary: {type(item)}"
                return [nodes.error("", nodes.paragraph(text=error_msg))]
            
            # Check for required fields and provide helpful error messages
            required_fields = ["pillar", "capability", "requirement_index", "statement", "importance"]
            missing_fields = [f for f in required_fields if f not in item]
            if missing_fields:
                error_msg = f"Item {idx} (requirement {item.get('requirement_index', 'unknown')}) is missing required fields: {', '.join(missing_fields)}"
                return [nodes.error("", nodes.paragraph(text=error_msg))]
            
            pillar_name = item.get("pillar", "Unknown")
            if pillar_name not in pillars:
                pillars[pillar_name] = []
            pillars[pillar_name].append(item)

        # 4. Create a list of nodes (headings + tables) for each pillar
        result_nodes = []

        for pillar_name, pillar_items in pillars.items():
            # Add pillar heading as a proper section so it appears in TOC
            section = nodes.section(ids=[pillar_name.lower().replace(" ", "-")])
            section['names'] = [pillar_name]
            
            # Create the heading
            title = nodes.title(text=pillar_name)
            section += title

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
                    # Use .get() with empty string default to avoid KeyError
                    content_text = str(item.get(key, "") or "")
                    
                    # Debug: log if capability_index is missing (though we don't display it)
                    if key == "capability" and "capability_index" not in item:
                        print(f"Warning: Item {item.get('requirement_index', 'unknown')} missing capability_index")

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
            
            # Add table to the section
            section += table
            
            # Add section to result nodes
            result_nodes.append(section)

        # 5. Return all nodes (sections with headings + tables)
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
