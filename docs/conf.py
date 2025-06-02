# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mange cow'
copyright = '2025, Jurandy Soares'
author = 'Jurandy Soares'
release = '2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'myst_parser',
        ]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_title = html_short_title = project

html_theme_options = {
        "repository_provider": "github",
        "repository_url": "https://github.com/mange-ifrn/mange-cow",
        "use_source_button": True,
        "repository_branch": "main",
        "use_repository_button": True,
        "path_to_docs": "docs",
        "use_edit_page_button": True
        }
