# -*- coding: utf-8 -*-
#
# Carbon documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  5 17:12:58 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import json
import os
import sys
import datetime

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from sphinx import addnodes
from sphinx.domains.javascript import JSObject

# Import Carbon Sphinx theme from common
sys.path.insert(0, os.path.abspath(
    os.path.dirname(os.path.realpath(__file__)),
))
import carbon_theme

carbonio_package_config = json.loads(
    open(os.path.join(os.path.dirname(__file__), '..', 'package.json')).read())

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    #'sphinx.ext.autosectionlabel',
    'sphinx.ext.todo',
    'sphinx.ext.extlinks',
    #'sphinxcontrib.spelling',
    'carbon_docs',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = [carbon_theme.get_html_templates_path()]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Carbon'
current_year = datetime.datetime.now().year
copyright = u'%s, ObjectLabs Corporation' % current_year
author = u'Carbon'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(carbonio_package_config['version'].split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = carbonio_package_config['version']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build',
    # docs-frags has embedded includes whose relative paths are only valid from
    # the file in which they included. this suppresses the warning that sphinx
    # will spit out on its first pass looking for "rst" files.
    '**/carbon-client-node/docs/doc-frags',
    '**/carbon-client/docs/doc-frags',
    '**/carbond/docs/shell-frags',
    '**/node_modules',
    'client-libs.rst',
    'faq/index.rst',
    'packages/carbon-core/docs/packages/bond/docs/packages/carbon-client-node/docs/index.rst',
    'packages/carbon-core/docs/packages/bond/docs/packages/carbon-client-node/docs/packages/carbon-client/docs/index.rst',
    'packages/carbon-core/docs/packages/bond/docs/index.rst',
    'packages/carbon-core/docs/packages/bond/docs/ref/index.rst',
    'packages/carbon-core/docs/packages/atom/docs/index.rst',
    'packages/carbon-core/docs/packages/atom/docs/ref/index.rst',
    'packages/carbon-core/docs/packages/ejson/docs/index.rst',
    'packages/carbon-core/docs/packages/fibers/docs/index.rst',
    'packages/carbon-core/docs/packages/fibers/docs/ref/index.rst',
    'packages/carbon-core/docs/packages/http-errors/docs/index.rst',
    'packages/carbon-core/docs/packages/leafnode/docs/code-frags/index.rst',
    'packages/carbon-core/docs/packages/leafnode/docs/index.rst',
    'packages/carbon-core/docs/packages/leafnode/docs/ref/index.rst',
    'packages/carbon-core/docs/packages/leafnode/docs/shell-frags/index.rst',
    'packages/carbon-core/docs/packages/test-tube/docs/examples.rst',
    'packages/carbon-core/docs/packages/test-tube/docs/index.rst',
    'packages/carbon-core/docs/packages/test-tube/docs/introduction.rst',
    'packages/carbon-core/docs/packages/test-tube/docs/ref/index.rst',
    'packages/carbond/docs/guide/aac/security-strategies.rst',
    'packages/carbond/docs/guide/admin-interface.rst',
    'packages/carbond/docs/guide/generating-api-documentation.rst',
    'packages/carbond/docs/index.rst',
    'packages/carbond/docs/ref/index.rst',
]

suppress_warnings = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
# NOTE: this is reset below based on `carbonio_env`
todo_include_todos = False

primary_domain = 'js'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'carbon_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'collapse_navigation': False,
    'navigation_depth': 3,
}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [carbon_theme.get_html_theme_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Carbondoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Carbon.tex', u'Carbon Documentation',
     u'Chris Chang, Will Shulman', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'carbon', u'Carbon Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Carbon', u'Carbon Documentation',
     author, 'Carbon', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

# for linking to external dependencies not built with sphinx
extlinks = {
    'express4': (
        'https://expressjs.com/en/4x/api.html#%s', ''
    ),
    'jsonschema': (
        'https://spacetelescope.github.io/understanding-json-schema/%s', ''
    ),
    'ejson': (
        'http://docs.mongodb.org/manual/reference/mongodb-extended-json/%s', ''
    ),
}

intersphinx_mapping = {
    'sphinx': ('http://www.sphinx-doc.org/en/stable/', None),
}

on_rtd = os.environ.get('READTHEDOCS') == 'True'
if on_rtd:
    environment = 'prod'
else:
    environment = 'dev'

carbonio_env = os.environ.get('CARBONIO_DOCS_ENV')
if not carbonio_env:
    carbonio_env = environment

if carbonio_env != 'prod':
    todo_include_todos = True

html_context = {
    'local_rtd_menu': True,
}

def patch_object_description(app):
    from sphinx.domains.javascript import JSXRefRole
    from sphinx.directives import ObjectDescription
    from sphinx import addnodes
    from docutils.parsers.rst import directives
    from docutils import nodes

    # Patch Javascript domain to remove parens on class refs
    app.env.domains['js'].roles['class'] = JSXRefRole()

    # Add hidden flag to object options
    ObjectDescription.option_spec['hidden'] = directives.flag
    ObjectDescription.option_spec['heading'] = directives.flag

    # Patch the run method to remove desc_signature nodes if the hidden flag is
    # specified
    wrapped_run = ObjectDescription.run

    def patched_run(self):
        """Patch the ObjectDescription run method to override return nodes

        This allows for use of the two added options:

        hidden
            Hide the node from output, don't add a linkable node to the output.
            This is useful for breaking up a class definition with headings. You
            should define one similar class without this option, or with the
            ``heading`` option below. This should normally be used with
            ``noindex`` as well

        heading
            Hide the node from output, but give a linkable element in the
            output. If you'd rather use headings in place of the domain
            directive nodes, use this in combination with a heading.
        """
        (index, node) = wrapped_run(self)
        if 'hidden' in self.options:
            for (n, child) in enumerate(node):
                if isinstance(child, addnodes.desc_signature):
                    del node[n]

        if 'heading' in self.options:
            elem = nodes.section()
            for (n, child) in enumerate(node):
                if isinstance(child, addnodes.desc_signature):
                    elem = nodes.container()
                    elem['ids'] = child['ids']
                    elem['names'] = child['names']
                    node[n] = elem

        return [index, node]

    ObjectDescription.run = patched_run


def remove_listener(app):
    # Remove html-page-context override installed by readthedocs_ext
    try:
        from readthedocs_ext.readthedocs import update_body
        for (key, fn) in app.events.listeners['html-page-context'].items():
            if fn is update_body:
                app.disconnect(key)
        app.add_javascript('readthedocs-data.js')
        app.add_javascript('readthedocs-dynamic-include.js')
    except ImportError:
        pass


class DetailsTableDirective(Directive):

    """Directive to output a detail table

    This outputs a custom table used for displaying attribute properties, and
    display nested reST content as the attribute ``description``
    """

    has_content = True
    required_arguments = 1
    final_argument_whitespace = True
    optional_arguments = 0
    option_spec = {
        'required': directives.flag,
        'type': directives.unchanged,
        'default': directives.unchanged,
    }

    def run(self):
        """Output a table that follows a standard output format for attributes"""
        required = 'required' in self.options
        attr_name = self.arguments[0]
        attr_type = self.options.get('type')
        attr_default = self.options.get('default')

        # Create domain indexed object
        dom_obj = JSObject(
            'attribute',
            [attr_name],
            {},
            nodes.Text('', ''),
            self.lineno,
            self.content_offset,
            self.block_text,
            self.state,
            self.state_machine
        )
        (node_index, node_desc) = dom_obj.run()

        # Pull out object name
        node_attr_name = nodes.Text(attr_name, attr_name)
        node_desc_name = node_desc.next_node(addnodes.desc_name)
        if node_desc_name:
            node_attr_name = node_desc_name.next_node(nodes.Text)
        node_desc.next_node(addnodes.desc_signature)
        node_desc_sig = node_desc.next_node(addnodes.desc_signature)
        del node_desc_sig

        table = nodes.table()
        node_desc.append(table)
        table['classes'] = ['details-table']
        tgroup = nodes.tgroup(cols=3)
        tgroup.append(nodes.colspec(colwidth=5))
        tgroup.append(nodes.colspec(colwidth=10))
        table.append(tgroup)

        tbody = nodes.tbody()
        tgroup.append(tbody)

        # Attribute name
        row_head = nodes.row()
        entry_attribute = nodes.entry(classes=['details-table-name'])
        entry_attribute.append(nodes.paragraph('', '', node_attr_name))
        row_head.append(entry_attribute)
        entry_type = nodes.entry(classes=['details-table-type'])
        row_head.append(entry_type)
        tbody.append(row_head)
        if attr_type:
            entry_type.append(
                nodes.paragraph(
                    '', '', addnodes.pending_xref(
                        '',
                        nodes.literal(attr_type, attr_type),
                        refdomain='js',
                        reftype=None,
                        reftarget=attr_type,
                        #refdoc=self.env.docname,
                ))
            )

        # Required
        if required:
            row_required = nodes.row()
            row_required.append(
                nodes.entry(
                    '', nodes.paragraph(
                        '', '', nodes.emphasis(
                            '', nodes.Text('Required', 'Required')
                )))
            )
            row_required.append(nodes.entry())
            tbody.append(row_required)

        # Content
        if self.content:
            row_desc = nodes.row()
            row_desc.append(
                nodes.entry(
                    '', nodes.paragraph('Description', 'Description')
                )
            )
            entry_description = nodes.entry()
            row_desc.append(entry_description)
            self.state.nested_parse(
                self.content,
                self.content_offset,
                entry_description
            )
            tbody.append(row_desc)

        return [node_index, node_desc]


def patch_literal_include(app):
    import re
    import sphinx.directives.code as code

    wrapped_read = code.LiteralIncludeReader.read
    # we need to wrap this because it dedents *before*  the named sections
    # filter can run and results in a bunch of "over dedent" warnings.
    # we can't run the named sections filter first because the filter list
    # is local to code.LiteralIncludeReader.read method :-/
    wrapped_dedent_filter = code.LiteralIncludeReader.dedent_filter

    def patched_read(self, location=None):
        lines, num_lines = wrapped_read(self, location)
        lines = self.named_sections_filter(lines.split(os.linesep), location)
        lines = wrapped_dedent_filter(self, lines, location)
        return os.linesep.join(lines), len(lines)

    def patched_dedent_filter(self, lines, location=None):
        return lines

    def named_sections_filter(self, lines, location=None):
        named_sections = self.options.get('named-sections')
        no_filter_section_markers = self.options.get('no-named-sections-filter')
        section_marker_re = re.compile(r'\s*//\s*(pre|post)-.+')
        if named_sections:
            sections = named_sections.split(',')
            sections.reverse()
            index = 0
            line_list = []
            while len(sections) > 0:
                section = sections.pop()
                start_re = re.compile('.*pre-{}.*'.format(section))
                end_re = re.compile('.*post-{}.*'.format(section))
                recording = False
                for i in range(index, len(lines)):
                    if not recording:
                        if start_re.match(lines[i]):
                            recording = True
                        continue
                    if recording and end_re.match(lines[i]):
                        recording = False
                        index = i + 1
                        break
                    if (not no_filter_section_markers and
                        section_marker_re.match(lines[i])):
                        continue
                    line_list.append(i)
                if recording:
                    raise ValueError('No end section marker found for '
                                     '{}'.format(section))
                if i == len(lines) and len(sections) > 0:
                    raise ValueError('No section markers found for '
                                     '{!r}'.format(sections))
            return [lines[i] for i in line_list]
        return lines

    code.LiteralIncludeReader.read = patched_read
    code.LiteralIncludeReader.dedent_filter = patched_dedent_filter
    code.LiteralIncludeReader.named_sections_filter = named_sections_filter

    code.LiteralInclude.option_spec['named-sections'] = \
        directives.unchanged_required
    # do not filter out any lines that match r'\s*// (pre|post)-.+'
    code.LiteralInclude.option_spec['no-named-sections-filter'] = \
        directives.flag


def setup(app):
    app.connect('builder-inited', patch_object_description)
    app.connect('builder-inited', patch_literal_include)
    app.connect('builder-inited', remove_listener)
    app.add_stylesheet('style.css')
    app.add_javascript('carbon.js')
    app.add_config_value('environment', '', 'env')
    app.add_config_value('carbonio_env', '', 'env')
    directives.register_directive('details-table', DetailsTableDirective)
