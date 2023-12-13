# -*- coding: utf-8 -*-
#
# cu_cat documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 13 14:34:47 2018.
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
import os
import shutil
import sys
import warnings
from datetime import datetime

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, os.path.abspath("sphinxext"))
from github_link import make_linkcode_resolve
from sphinx_gallery.notebook import add_code_cell, add_markdown_cell

# -- Copy files for docs --------------------------------------------------
#
# We avoid duplicating the information, but we do not use symlinks to be
# able to build the docs on Windows
shutil.copyfile("../RELEASE_PROCESS.md", "RELEASE_PROCESS.md")
shutil.copyfile("../CHANGES.md", "CHANGES.md")
shutil.copyfile("../CONTRIBUTING.md", "CONTRIBUTING.md")

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    # builtin
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx.ext.linkcode",
    "sphinx.ext.autodoc.typehints",
    # contrib
    "numpydoc",
    "sphinx_issues",
    "sphinx_copybutton",
    "sphinx_gallery.gen_gallery",
]

try:
    import sphinxext.opengraph  # noqa

    extensions.append("sphinxext.opengraph")
except ImportError:
    print("ERROR: sphinxext.opengraph import failed")

try:
    import jupyterlite_sphinx  # noqa: F401

    extensions.append("jupyterlite_sphinx")
    with_jupyterlite = True
except ImportError:
    # In some cases we don't want to require jupyterlite_sphinx to be installed,
    # e.g. the doc-min-dependencies build
    warnings.warn(
        "jupyterlite_sphinx is not installed, you need to install it "
        "if you want JupyterLite links to appear in each example"
    )
    with_jupyterlite = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.md', '.md']
source_suffix = ".md"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "cu_cat"
copyright = (
    f"2018-2023, the dirty_cat developers, 2023-{datetime.now().year}, the cu_cat"
    " developers"
)
author = "cu_cat contributors"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version_file = os.path.join("..", "cu_cat", "VERSION.txt")
with open(version_file) as fh:
    version = fh.read().strip()
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for autodoc / autosummary ----------------------------------------
# generate autosummary even if no references
autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

autodoc_default_flags = ["members", "inherited-members"]


# -- Options for HTML output --------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "logo": {
        "image_relative": "_static/cu_cat.svg",
        "image_light": "_static/cu_cat.svg",
        "image_dark": "_static/cu_cat.svg",
    },
    # "external_links": [
    #     {
    #         "url": "https://pydata.org",
    #         "name": "PyData",
    #     },
    # ],
    "header_links_before_dropdown": 4,
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/cu_cat_data",
            "icon": "fa-brands fa-twitter",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/graphistry/cu-cat/",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/cu_cat",
            "icon": "fa-custom fa-pypi",
        },
    ],
    # alternative way to set twitter and github header icons
    # "github_url": "https://github.com/pydata/pydata-sphinx-theme",
    # "twitter_url": "https://twitter.com/PyData",
    "use_edit_page_button": True,
    "show_toc_level": 1,
    # "navbar_align": [left, content, right] to test that navbar items align properly
    "navbar_align": "left",
    # "navbar_center": ["version-switcher", "navbar-nav"],
    "navbar_center": ["navbar-nav"],
    "announcement": (
        "https://raw.githubusercontent.com/graphistry/cu_cat/main/doc/announcement.html"
    ),
    # "show_nav_level": 2,
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template.html", "sidebar-ethical-ads.html"],
    # "article_footer_items": ["prev-next.html", "test.html", "test.html"],
    # "content_footer_items": ["prev-next.html", "test.html", "test.html"],
    # "footer_start": ["test.html", "test.html"],
    # "secondary_sidebar_items": ["index.html"],  # Remove the source buttons
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {"index": "index.html"}

# Needed for the edit button
html_context = {
    "github_user": "cu_cat-data",
    "github_repo": "cu_cat",
    "github_version": "main",
    "doc_path": "doc",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]
html_js_files = []


# Project logo, to place at the top of the sidebar.
html_logo = "_static/cu_cat.svg"

# Icon to put in the browser tab.
html_favicon = "_static/skrub.svg"

# Modify the title to get good social-media links
html_title = "cu_cat"


# -- Options for HTMLHelp output ----------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "cu_catdoc"


# -- Options for LaTeX output -------------------------------------------------

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
    (
        master_doc,
        "cu_cat.tex",
        "cu_cat Documentation",
        "cu_cat developers",
        "manual",
    ),
]


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "cu_cat", "cu_cat Documentation", [author], 1)]


# -- Options for Texinfo output -----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "cu_cat",
        "cu_cat Documentation",
        author,
        "cu_cat",
        "Prepping tables for machine learning.",
        "Data Science",
    ),
]


# Configuration for intersphinx
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable", None),
    "scipy": ("https://docs.scipy.org/doc/scipy", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "sklearn": ("https://scikit-learn.org/stable", None),
    "skimage": ("https://scikit-image.org/docs/stable", None),
    "mayavi": ("http://docs.enthought.com/mayavi/mayavi", None),
    "statsmodels": ("https://www.statsmodels.org/stable", None),
    "pandas": ("http://pandas.pydata.org/pandas-docs/stable", None),
    "polars": ("https://pola-rs.github.io/polars/py-polars/html", None),
    "seaborn": ("http://seaborn.pydata.org", None),
}


# -- sphinx-gallery configuration ---------------------------------------------
from sphinx_gallery.sorting import FileNameSortKey  # noqa

if "dev" in release:
    binder_branch = "main"
else:
    binder_branch = release


def notebook_modification_function(notebook_content, notebook_filename):
    notebook_content_str = str(notebook_content)
    warning_template = "\n".join(
        [
            "<div class='alert alert-{message_class}'>",
            "",
            "# JupyterLite warning",
            "",
            "{message}",
            "</div>",
        ]
    )

    if "06_ken_embeddings_example" in notebook_filename:
        message_class = "danger"
        message = (
            "This example requires PyArrow, which is currently unavailable in Pyodide"
            " (see https://github.com/pyodide/pyodide/issues/2933). Thus, this example"
            " cannot be run in JupyterLite."
        )
    else:
        message_class = "warning"
        message = (
            "Running the cu_cat examples in JupyterLite is experimental and you may"
            "encounter some unexpected behavior.\n\n"
            "The main difference is that imports will take a lot longer than usual, "
            "for example the first `import cu_cat` can take roughly 10-20s.\n\n"
            "If you notice problems, feel free to open an "
            "[issue](https://github.com/graphistry/cu-cat/issues/new/choose) about it."
        )

    markdown = warning_template.format(message_class=message_class, message=message)

    dummy_notebook_content = {"cells": []}
    add_markdown_cell(dummy_notebook_content, markdown)

    # TODO: in the next release, we need to uncomment the following line that should
    # replace the manual install from TestPyPI
    # code_lines = ["%pip install cu_cat"]
    code_lines = []
    code_lines.extend(
        [
            "import micropip",
            (
                "await micropip.install("
                "'https://test-files.pythonhosted.org/packages/3c/03/"
                "e1598c7abe536e56834f568f61497ad075d966c4c8fb7d0ad004b81e7bfc/"
                "cu_cat-0.0.1.dev1-py3-none-any.whl')"
            ),
        ]
    )

    if "seaborn" in notebook_content_str:
        code_lines.append("%pip install seaborn")
    if "statsmodel" in notebook_content_str:
        code_lines.append("%pip install statsmodels")
    if "fetch_" in notebook_content_str:
        code_lines.extend(
            [
                "%pip install pyodide-http",
                "import pyodide_http",
                "pyodide_http.patch_all()",
            ]
        )
    # always import matplotlib and pandas to avoid Pyodide limitation with
    # imports inside functions
    code_lines.extend(["import matplotlib", "import pandas"])

    if code_lines:
        code_lines = ["# JupyterLite-specific code"] + code_lines
        code = "\n".join(code_lines)
        add_code_cell(dummy_notebook_content, code)

    notebook_content["cells"] = (
        dummy_notebook_content["cells"] + notebook_content["cells"]
    )


sphinx_gallery_conf = {
    "doc_module": "cu_cat",
    "backreferences_dir": os.path.join("generated"),
    "reference_url": {
        # The module we locally document (so, cu_cat) uses None
        "cu_cat": None,
        # We don't specify the other modules as we use the intershpinx ext.
        # See https://sphinx-gallery.github.io/stable/configuration.html#link-to-documentation  # noqa
    },
    "filename_pattern": ".*",
    "examples_dirs": "../examples",
    "gallery_dirs": "auto_examples",
    "within_subsection_order": FileNameSortKey,
    "download_all_examples": False,
    "binder": {
        "org": "cu_cat-data",
        "repo": "cu_cat",
        "binderhub_url": "https://mybinder.org",
        "branch": binder_branch,
        "dependencies": "./binder/requirements.txt",
        "use_jupyter_lab": True,
    },
}
if with_jupyterlite:
    sphinx_gallery_conf["jupyterlite"] = {
        "notebook_modification_function": notebook_modification_function
    }

# -- sphinx.ext.opengraph configuration ---------------------------------------
ogp_site_url = "https://cu_cat-data.github.io/stable/"
ogp_image = "https://cu_cat-data.github.io/stable/_static/cu_cat.svg"
ogp_use_first_image = True
ogp_site_name = "cu_cat"

# -- numpydoc configuration ---------------------------------------------------

# Produce `plot::` directives for examples that contain `import matplotlib` or
# `from matplotlib import`.
numpydoc_use_plots = True

# this is needed for some reason...
# see https://github.com/numpy/numpydoc/issues/69
numpydoc_class_members_toctree = False

numpydoc_xref_param_type = True
numpydoc_xref_aliases = {
    # Python
    "file-like": ":term:`file-like <python:file object>`",
    "iterator": ":term:`iterator <python:iterator>`",
    "path-like": ":term:`path-like`",
    "Path": ":class:`python:pathlib.Path`",
    "bool": ":class:`python:bool`",
    # Matplotlib
    "colormap": ":doc:`colormap <matplotlib:tutorials/colors/colormaps>`",
    "color": ":doc:`color <matplotlib:api/colors_api>`",
    "Axes": "matplotlib.axes.Axes",
    "Figure": "matplotlib.figure.Figure",
    "Axes3D": "mpl_toolkits.mplot3d.axes3d.Axes3D",
    "ColorbarBase": "matplotlib.colorbar.ColorbarBase",
    # sklearn
    "LeaveOneOut": "sklearn.model_selection.LeaveOneOut",
    "Transformer": "sklearn.base.TransformerMixin",
    "HashingVectorizer": "sklearn.feature_extraction.text.HashingVectorizer",
    "CountVectorizer": "sklearn.feature_extraction.text.CountVectorizer",
    "_VectorizerMixin": "sklearn.feature_extraction.text._VectorizerMixin",
    "StandardScaler": "sklearn.preprocessing.StandardScaler",
    "KMeans": "sklearn.cluster.KMeans",
    "ColumnTransformer": "sklearn.compose.ColumnTransformer",
    "OneHotEncoder": "sklearn.preprocessing.OneHotEncoder",
    "Pipeline": "sklearn.pipeline.Pipeline",
    "GridSearchCV": "sklearn.model_selection.GridSearchCV",
    "fetch_openml": "sklearn.datasets.fetch_openml",
    # other libraries
    "joblib.Parallel": "joblib.Parallel",
    "joblib.delayed": "joblib.delayed",
    "joblib.parallel_backend": "joblib.parallel_backend",
    "ndarray": "numpy.ndarray",
    "pathlib.Path": "pathlib.Path",
    "float64": "numpy.float64",
    "RandomState": "numpy.random.RandomState",
    "Series": "pandas.Series",
    "pandas.Index": "pandas.Index",
    "read_csv": "pandas.read_csv",
    "pandas.merge": "pandas.merge",
    # cu_cat
    "fetch_ken_table_aliases": "cu_cat.datasets.fetch_ken_table_aliases",
    "fetch_ken_types": "cu_cat.datasets.fetch_ken_types",
    "fetch_ken_embeddings": "cu_cat.datasets.fetch_ken_embeddings",
    "fuzzy_join": "cu_cat.fuzzy_join",
    "Joiner": "cu_cat.Joiner",
    "GapEncoder": "cu_cat.GapEncoder",
    "MinHashEncoder": "cu_cat.MinHashEncoder",
    "SimilarityEncoder": "cu_cat.SimilarityEncoder",
    "DatetimeEncoder": "cu_cat.DatetimeEncoder",
    "deduplicate": "cu_cat.deduplicate",
    "TableVectorizer": "cu_cat.TableVectorizer",
    "DatasetInfoOnly": "cu_cat.datasets._fetching.DatasetInfoOnly",
    "DatasetAll": "cu_cat.datasets._fetching.DatasetAll",
    "_replace_false_missing": "cu_cat._table_vectorizer._replace_false_missing",

}
numpydoc_xref_ignore = "all"

# -- sphinx.ext.autodoc configuration -----------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autodoc_typehints = "none"

# -- sphinx_favicon configuration ---------------------------------------------
favicons = {"rel": "icon", "href": "_static/cu_cat.svg", "type": "image/svg+xml"}

# -- github links -------------------------------------------------------------

# we use the issues path for PRs since the issues URL will forward
issues_github_path = "graphistry/cu_cat"

# The following is used by sphinx.ext.linkcode to provide links to GitHub
linkcode_resolve = make_linkcode_resolve(
    "cu_cat",
    "https://github.com/graphistry/cu-cat/blob/{revision}/{package}/{path}#L{lineno}",
)

# -- Sphinx-Copybutton configuration -----------------------------------------
copybutton_prompt_text = r">>> |\.\.\. |\$ "
copybutton_prompt_is_regexp = True
