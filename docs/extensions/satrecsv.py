"""Create a SATRE evaluation CSV from the docs."""

from __future__ import annotations

import warnings
from os import path
from typing import TYPE_CHECKING, Any, Sequence

from docutils import nodes, writers
from docutils.frontend import OptionParser
from docutils.io import FileOutput

from sphinx import addnodes
from sphinx.builders import Builder
from sphinx.locale import __
from sphinx.util import logging
from sphinx.util.console import darkgreen  # type: ignore[attr-defined]
from sphinx.util.display import progress_message
from sphinx.util.nodes import inline_all_toctrees
from sphinx.util.osutil import ensuredir, make_filename_from_project
from sphinx.writers.text import TextTranslator, Table

if TYPE_CHECKING:
    from sphinx.application import Sphinx
    from docutils.nodes import Element, Text


logger = logging.getLogger(__name__)


class SatreCsvWriter(writers.Writer):
    """
    Write the extracted SATRE evaluation statements to a tabular file.
    """

    supported = ("text",)
    settings_spec = ("No options here.", "", ())
    settings_defaults: dict[str, Any] = {}

    output: str

    def __init__(self, builder: SatreCsvBuilder) -> None:
        super().__init__()
        self.builder = builder
        self.interested = None

    def translate(self) -> None:
        visitor = self.builder.create_translator(self.document, self.builder)
        self.document.walkabout(visitor)

        tsv_lines = [
            "Section\tItem\tStatement\tImportance\tScore\tResponse\tImprovements"
        ]
        for section in visitor.interested:
            title = section["section"][1][1].strip()
            # print(title)
            tables = section["table"]
            for table in tables:
                header = table.lines[0]
                # Is this a statement?
                if header[1].text.strip() == "Statement":
                    for line in table.lines[1:]:
                        number = line[0].text.strip()
                        statement = line[1].text.strip()
                        # guidance = (
                        #     line[2]
                        #     .text.replace("\t", "    ")
                        #     .replace("\n", "    ")
                        #     .strip()
                        # )
                        importance = line[3].text.strip()
                        tsv_lines.append(
                            f"{title}\t{number}\t{statement}\t{importance}\t\t\t"
                        )
        self.output = "\n".join(tsv_lines)


class SatreCsvTranslator(TextTranslator):
    """
    Extract SATRE evaluation statements from the docs and save as tabular file.

    sphinx.writers.text.TextTranslator converts a document into a single plain text file
    https://github.com/sphinx-doc/sphinx/blob/v7.2.5/sphinx/writers/text.py#L384-L1305

    This class extends TextTranslator to ignore everything apart from the relevant SATRE
    evaluation tables.
    """

    builder: SatreCsvBuilder

    def __init__(self, document: nodes.document, builder: SatreCsvBuilder) -> None:
        super().__init__(document, builder)
        self.interested = []

    # Disable default wrapping
    def end_state(
        self,
        wrap: bool = True,
        end: Sequence[str] | None = ("",),
        first: str | None = None,
    ) -> None:
        super().end_state(False, end, first)

    def visit_section(self, node: Element) -> None:
        self.new_state(0)
        self._title_char = self.sectionchars[self.sectionlevel]
        self.sectionlevel += 1
        if self.sectionlevel == 2:
            self.interested.append({"table": [], "section": None})

    def depart_section(self, node: Element) -> None:
        self.interested[-1]["section"] = self.states[-1][0]
        self.sectionlevel -= 1
        self.end_state()

    def visit_table(self, node: Element) -> None:
        if hasattr(self, "table"):
            msg = "Nested tables are not supported."
            raise NotImplementedError(msg)
        self.new_state(0)
        self.table = Table()

    def depart_table(self, node: Element) -> None:
        self.interested[-1]["table"].append(self.table)
        self.add_text(str(self.table))
        # print(repr(self.table))
        del self.table
        self.end_state(wrap=False)

    def visit_start_of_file(self, node: Element) -> None:
        pass

    def depart_start_of_file(self, node: Element) -> None:
        pass


class SatreCsvBuilder(Builder):
    """
    Builds a SATRE evaluation TSV file.

    Based on https://github.com/sphinx-doc/sphinx/blob/v7.2.5/sphinx/builders/manpage.py#L29-L106
    """

    name = "satrecsv"
    format = "tsv"
    epilog = __("The output is in %(outdir)s.")

    default_translator_class = SatreCsvTranslator
    supported_image_types: list[str] = []

    def init(self) -> None:
        # section numbers for headings in the currently visited document
        self.secnumbers: dict[str, tuple[int, ...]] = {}

    def get_outdated_docs(self) -> str | list[str]:
        return "all documents"

    def get_target_uri(self, docname: str, typ: str | None = None) -> str:
        return ""

    @progress_message(__("writing"))
    def write(self, *ignored: Any) -> None:
        docwriter = SatreCsvWriter(self)
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)
            # DeprecationWarning: The frontend.OptionParser class will be replaced
            # by a subclass of argparse.ArgumentParser in Docutils 0.21 or later.
            docsettings: Any = OptionParser(
                defaults=self.env.settings,
                components=(docwriter,),
                read_config_files=True,
            ).get_default_values()

        docname = self.config.root_doc

        # targetname = make_filename_from_project(self.config.project) + ".tsv"
        targetname = "satrecsv.tsv"

        logger.info(darkgreen(targetname) + " { ", nonl=True)
        destination = FileOutput(
            destination_path=path.join(self.outdir, targetname), encoding="utf-8"
        )

        tree = self.env.get_doctree(docname)
        docnames: set[str] = set()
        largetree = inline_all_toctrees(
            self, docnames, docname, tree, darkgreen, [docname]
        )
        largetree.settings = docsettings
        logger.info("} ", nonl=True)
        self.env.resolve_references(largetree, docname, self)
        # remove pending_xref nodes
        for pendingnode in largetree.findall(addnodes.pending_xref):
            pendingnode.replace_self(pendingnode.children)

        docwriter.write(largetree, destination)


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Register the extension as a builder.
    """
    app.add_builder(SatreCsvBuilder)

    return {
        "version": "0.0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
