import os
import yaml
from docutils import nodes
from docutils.statemachine import ViewList
from sphinx.util.docutils import SphinxDirective

# Define the columns and their proportional widths for the table
COLUMNS = [
    ("requirement", 10),
    ("importance", 10),
    ("capability", 25),
    ("statement", 40),
    ("guidance", 15),
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

        # 3. Create Table Structure
        # Ensure only keyword arguments are used for table/tgroup
        table = nodes.table(classes=["spec-table", "colwidths-given"])
        tgroup = nodes.tgroup(cols=len(COLUMNS))
        table += tgroup

        # Add column specifications (colspec)
        for _, width in COLUMNS:
            tgroup += nodes.colspec(colwidth=width)

        # Table Header (thead)
        # FIX: Removed empty positional arguments from structural nodes (thead, row, entry)
        thead = nodes.thead()
        header_row = nodes.row()
        for title, _ in COLUMNS:
            entry = nodes.entry(classes=["head"])
            entry += nodes.paragraph(text=title.capitalize())
            header_row += entry
        thead += header_row
        tgroup += thead

        # Table Body (tbody)
        # FIX: Removed empty positional arguments from structural nodes (tbody, row, entry)
        tbody = nodes.tbody()

        for item in specifications:
            row = nodes.row()
            for key, _ in COLUMNS:
                entry = nodes.entry()
                content_text = str(item.get(key, ""))

                # Use nested_parse for multi-line fields to process reST content (like links)
                if key in ["capability", "statement", "guidance"]:
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
                else:
                    # Simple text fields (requirement, importance) are wrapped in a paragraph
                    entry += nodes.paragraph(text=content_text)

                row += entry
            tbody += row

        tgroup += tbody

        # 4. Return the completed table node
        return [table]


# Setup function to register the directive
def setup(app):
    """Register the directive with Sphinx."""
    app.add_directive("yaml-specification", YamlSpecDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
