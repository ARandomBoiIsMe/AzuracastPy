# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

project = 'AzuracastPy'
copyright = '2024, Abah Olotuche Gabriel'
author = 'Abah Olotuche Gabriel'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx_rtd_dark_mode"
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_dark_mode'
html_static_path = ['_static']

default_dark_mode = True


def skip(app, what, name, obj, would_skip, options):
    if name in {
        "__call__",
        "__init__"
    }:
        return False
    return would_skip

def setup(app):
    app.connect("autodoc-skip-member", skip)