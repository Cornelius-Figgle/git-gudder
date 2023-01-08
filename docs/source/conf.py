# Configuration file for the Sphinx documentation builder

# -- Project information

project = 'git-gudder'
copyright = 'Max Harrison 2023'
author = 'Cornelius-Figgle'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

root_doc = 'index'
source_suffix = '.md'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
