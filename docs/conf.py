# chatterbot-corpus documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 16 23:03:03 2017.

import os
import sys
from pathlib import Path
from datetime import datetime


current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

# Insert the project root dir as the first element in the PYTHONPATH.
# This lets us ensure that the source package is imported, and used to generate the documentation.
sys.path.insert(0, parent_directory)

sys.path.append(str(Path('_ext').resolve()))

from chatterbot_corpus import __version__ as chatterbot_corpus_version

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
    'github',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'chatterbot-corpus'
author = 'Gunther Cox'
copyright = '{}, {}'.format(
    datetime.now().year,
    author
)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags
release = chatterbot_corpus_version

# The short X.Y version
version = chatterbot_corpus_version.rsplit('.', 1)[0]

language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'classic'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {
    'externalrefs': True,
    'sidebarbgcolor': '#300a24',
    'relbarbgcolor': '#26001b',
    'footerbgcolor': '#13000d',
    'headbgcolor': '#503949',
    'headtextcolor': '#e8ffca',
    'headlinkcolor': '#e8ffca',
    'sidebarwidth': '300px',
    # 'collapsiblesidebar': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'style.css',
    'silktide-consent-manager.css'
]

html_js_files = [
    'silktide-consent-manager.js'
]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.

# This is required for the alabaster theme
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html']
}

root_doc = 'index'

html_show_sourcelink = True


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'chatterbot-corpusdoc'

html_favicon = '_static/favicon.ico'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'chatterbot-corpus.tex', 'chatterbot-corpus Documentation',
     'Gunther Cox', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'chatterbot-corpus', 'chatterbot-corpus Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'chatterbot-corpus', 'chatterbot-corpus Documentation',
     author, 'chatterbot-corpus', 'One line description of project.',
     'Miscellaneous'),
]

# Configuration for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None)
}
