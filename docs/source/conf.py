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
    "sphinxcontrib.datatemplates",
    "myst_parser",
    "satrecsv",
    "yamlspec",
]

# The :download: role inserts a hash into the URL which varies between builds
# html_extra_pathand attrs_inline allows us to use a consistent URL by copying
# in satre.xlsx outside sphinx and treating it as an external URL
# https://myst-parser.readthedocs.io/en/latest/syntax/cross-referencing.html#customising-external-url-resolution
html_extra_path = ["../generated/"]

linkcheck_ignore = [
    "satre.xlsx",
    # DOS/bot protection returns 403 for clients like curl, httpie
    "^https://www.turing.ac.uk/.*",
    # These MSOffice forms are public, but seem to be blocked to the CI check
    "https://forms.office.com/e/FuFyNGx3hw",
    "https://forms.office.com/e/HdaVSj2V0c",
    # Blocked in CI
    "https://www.dundee.ac.uk/hic",
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

# Theme options for logo
html_theme_options = {
    "logo_only": False,
    "display_version": False,
}

# Logo configuration
html_logo = "../images/SATRE_Stacked_Dark.png"

# Add custom CSS and JavaScript
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["custom.js"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# -- Allow markdown as well as rst
source_suffix = [".rst", ".md"]
