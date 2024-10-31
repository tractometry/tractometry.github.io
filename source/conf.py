# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'tractometry'
copyright = '2024, Ariel Rokem'
author = 'Ariel Rokem'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    ]

templates_path = ['_templates']
exclude_patterns = ['.DS_Store']
source_suffix = ['.rst', '.md']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']

# Added theme configuration. See: https://pydata-sphinx-theme.readthedocs.io/

html_logo = "_static/logo.png"

html_theme_options = {
    "use_edit_page_button": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/tractometry/",
            "icon": "fab fa-github-square",
        }]

}

html_context = {
    "github_url": "https://github.com",
    "github_user": "tractometry",
    "github_repo": "tractometry.github.io",
    "github_version": "main",
    "doc_path": "source",
}