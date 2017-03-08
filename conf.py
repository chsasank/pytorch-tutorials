#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyTorch Tutorials documentation build configuration file, created by
# sphinx-quickstart on Wed Mar  8 22:38:10 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import torch
import glob
import shutil
try:
    import torchvision
except ImportError:
    import warnings
    warnings.warn('unable to load "torchvision" package')
import sphinx_rtd_theme

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.mathjax',
              'sphinx_gallery.gen_gallery']

sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs': 'tutorial_source',
    # path where to save gallery generated examples
    'gallery_dirs': 'tutorials',
    'filename_pattern': '_tutorial.py'
}

# Create tutorials folder if it doesn't exist
try:
    import os
    os.mkdir('tutorials')
except FileExistsError:
    pass

# Copy rst files from tutorial_source folder to tutorials
for f in glob.glob('tutorial_source/*.rst'):
    shutil.copy(f, 'tutorials')

exclude_patterns = ['tutorials/index.rst']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyTorch Tutorials'
copyright = '2017, PyTorch'
author = 'PyTorch contributors'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# # Theme options are theme-specific and customize the look and feel of a theme
# # further.  For a list of options available for each theme, see the
# # documentation.
# #

# html_theme_options = {
#     'page_width': '1000px',
#     'fixed_sidebar': True,
#     'code_font_size': '0.87em',
#     'sidebar_includehidden': True
# }

# # Add any paths that contain custom static files (such as style sheets) here,
# # relative to this directory. They are copied after the builtin static files,
# # so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# # Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#     'index': ['sidebarlogo.html', 'globaltoc.html', 'searchbox.html', 'sourcelink.html'],
#     '**': ['sidebarlogo.html', 'globaltoc.html', 'searchbox.html', 'sourcelink.html']
# }


html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = '_static/img/pytorch-logo-dark.svg'
html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
    'logo_only': False,
}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyTorchTutorialsdoc'


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
    (master_doc, 'PyTorchTutorials.tex', 'PyTorch Tutorials Documentation',
     'Sasank, PyTorch contributors', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pytorchtutorials', 'PyTorch Tutorials Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'PyTorchTutorials', 'PyTorch Tutorials Documentation',
     author, 'PyTorchTutorials', 'One line description of project.',
     'Miscellaneous'),
]


