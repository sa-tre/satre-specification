# Configuration file for the Sphinx documentation builder.
import emoji

# -- Project information

project = "Standard Architecture for Trusted Research Environments"
copyright = ""
html_show_copyright = False
author = "The Contributors"

release = "0.0"
version = "0.0.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "myst_parser",
]

myst_enable_extensions = ["colon_fence", "substitution"]

# Emoji substitutions: replace {{emoji_name}} => unicode
emoji_codes = set(
    [
        emoji_code.replace(":", "")
        for emoji_list in (
            emoji.unicode_codes.get_emoji_unicode_dict("en").keys(),
            emoji.unicode_codes.get_aliases_unicode_dict().keys(),
        )
        for emoji_code in emoji_list
    ]
)
myst_substitutions = {
    emoji_code: emoji.emojize(f":{emoji_code}:", language="alias")
    for emoji_code in emoji_codes
}

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
