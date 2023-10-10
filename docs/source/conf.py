# Configuration file for the Sphinx documentation builder.

# -- Project information
from pathlib import Path
import sys

project = "Standard Architecture for Trusted Research Environments"
copyright = ""
html_show_copyright = False
author = "The Contributors"

release = "0.0"
version = "0.0.0"

# -- General configuration

extensions_dir = Path(__file__).absolute().parent.parent / "extensions"
print(extensions_dir)
sys.path.append(str(extensions_dir))

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "satrecsv",
]

# The :download: role inserts a hash into the URL which varies between builds
# attrs_inline allows us to use a consistent URL by copying in satre.xlsx
# outside sphinx and treating it as an external URL
# https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#customising-external-url-resolution
linkcheck_ignore = [
    # satre.xlsx is a local file that's copied into place, but since we treat the hyperlink
    # as an external link (to bypass the :download: role that inserts a hash into the path)
    # we need to exclude it from the linkchecker
    r"\./satre\.xlsx",
]


# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html
myst_enable_extensions = ["attrs_inline", "colon_fence", "deflist", "fieldlist"]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "myst-parser": ("https://myst-parser.readthedocs.io/en/latest/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinx_rtd_theme"

# -- Options for EPUB output
epub_show_urls = "footnote"

# -- Allow markdown as well as rst
source_suffix = [".rst", ".md"]
