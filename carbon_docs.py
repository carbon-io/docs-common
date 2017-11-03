# -*- coding: utf-8 -*-

from docutils import nodes
from docutils.transforms import Transform
from sphinx import addnodes
from sphinx.domains.javascript import JavaScriptDomain
from sphinx.domains.javascript import JSObject, JSCallable
from sphinx.domains.python import PyXrefMixin
from sphinx.locale import l_
from sphinx.util.docfields import Field, GroupedField, TypedField


# Annotate types
ANNOTATE_TYPE = 'type'
ANNOTATE_READ_ONLY = 'readonly'
ANNOTATE_OVERRIDES = 'override'
ANNOTATE_EXTENDS = 'extends'


class BoolField(Field):

    """Adds a field type which doesn't expect content and displays in italics"""

    def make_field(self, types, domain, item, env=None):
        fieldarg, content = item
        fieldname = nodes.field_name('', '', nodes.emphasis('', self.label))
        fieldbody = nodes.field_body('')
        return nodes.field('', fieldname, fieldbody)


class AnnotateField(Field):

    """This field type is used to annotate the first table line with properties

    These properties are handled by the transformer, when manipulating the field
    list node. The annotations are moved up to the top row of the table, instead
    of sitting as rows in the table.
    """

    def __init__(self, *args, **kwargs):
        self.annotate_type = kwargs.pop('annotate_type', None)
        super(AnnotateField, self).__init__(*args, **kwargs)

    def make_field(self, types, domain, item, env=None):
        field = super(AnnotateField, self).make_field(types, domain, item, env)
        field['annotate_type'] = self.annotate_type
        return field


class StyledTypedField(TypedField):

    def make_field(self, types, domain, item, env=None):
        field = super(StyledTypedField, self).make_field(types, domain, item, env)
        field['classes'] = ['arguments-field']
        return field


class JSCustomCallable(JSCallable):

    doc_field_types = [
        StyledTypedField(
            'arguments', label=l_('Arguments'),
            names=('argument', 'arg', 'parameter', 'param'), typerolename='func',
            typenames=('paramtype', 'type')
        ),
        GroupedField('errors', label=l_('Throws'), rolename='err',
                     names=('throws', ),
                     can_collapse=True),
        Field('returnvalue', label=l_('Returns'), has_arg=False,
              names=('returns', 'return')),
        Field('returntype', label=l_('Return type'), has_arg=False,
              names=('rtype', 'returntype'), bodyrolename='class'),
        Field('default', label=l_('Default'), names=('default',), has_arg=False),
        BoolField('required', label=l_('Required'), names=('require', 'required'),
                  has_arg=False),
        BoolField('static', label=l_('Static'), names=('static',), has_arg=False),
        AnnotateField('overrides', label=l_('Overrides'), names=('override', 'overrides'),
                      annotate_type=ANNOTATE_OVERRIDES, bodyrolename='class', has_arg=False),
        AnnotateField('extends', label=l_('Extends'), names=('extend', 'extends'),
                      annotate_type=ANNOTATE_EXTENDS, has_arg=False),
    ]


class JSAttribute(JSObject):

    doc_field_types = [
        AnnotateField('type', label=l_('Type'), names=('type',),
                      bodyrolename='class', annotate_type=ANNOTATE_TYPE,
                      has_arg=False),
        Field('default', label=l_('Default'), names=('default',), has_arg=False),
        BoolField('required', label=l_('Required'), has_arg=False,
                  names=('require', 'required')),
        BoolField('static', label=l_('Static'), names=('static',), has_arg=False),
        AnnotateField('readonly', label=l_('Read-only'), names=('readonly', 'ro'),
                      annotate_type=ANNOTATE_READ_ONLY, has_arg=False),
        AnnotateField('extends', label=l_('Extends'),
                      names=('extend', 'extends', 'inherits', 'inherit'),
                      annotate_type=ANNOTATE_EXTENDS, bodyrolename='class',
                      has_arg=False),
    ]


class RandoTransform(Transform):

    default_priority = 999

    def apply(self):
        for node_desc in self.document.traverse(addnodes.desc):
            if node_desc['domain'] == 'js' and node_desc['objtype'] in ['attribute', 'function', 'method']:
                node_sig, node_content = node_desc
                if node_sig["fullname"] == "carbond.collections.Collection.idHeader":
                    print "NODE: %s" % node_desc
                node_new_content = addnodes.desc_content()

                table = nodes.table()
                node_new_content.append(table)
                table['classes'] = ['details-table']
                tgroup = nodes.tgroup(cols=3)
                tgroup.append(nodes.colspec(colwidth=5))
                tgroup.append(nodes.colspec(colwidth=10))
                table.append(tgroup)

                tbody = nodes.tbody()
                tgroup.append(tbody)

                # Handle signature
                node_id = node_sig["ids"]

                row_header = nodes.row()
                entry_name = nodes.entry()
                node_desc_name = node_sig.next_node(addnodes.desc_name)
                if node_desc_name:
                    entry_paragraph = nodes.paragraph()
                    entry_paragraph.append(node_desc_name.next_node(nodes.Text))
                    entry_name.append(entry_paragraph)
                row_header.append(entry_name)
                entry_annotate = nodes.entry()
                row_header.append(entry_annotate)
                tbody.append(row_header)

                # Remove node signature children, but keep the anchor
                for child in node_sig.traverse(include_self=False):
                    if child.parent == node_sig:
                        node_sig.remove(child)

                node_field_list = node_content.next_node(nodes.field_list)
                if node_field_list:
                    for field in node_field_list:
                        (field_name, field_body) = field

                        # Handle type fields specially
                        if 'annotate_type' in field:
                            self.handle_annotate_type(entry_annotate, field)
                            continue

                        node_paragraph = nodes.paragraph()
                        field_copy = field_name.deepcopy()
                        node_paragraph.extend(field_copy.children)
                        field_name = node_paragraph

                        node_paragraph = nodes.paragraph()
                        field_copy = field_body.deepcopy()
                        node_paragraph.extend(field_copy.children)
                        field_body = node_paragraph

                        row = nodes.row()
                        row['classes'] = field.get('classes', [])
                        node_entry_name = nodes.entry()
                        node_entry_name.append(field_name)
                        row.append(node_entry_name)
                        node_entry_value = nodes.entry()
                        node_entry_value.append(field_body)
                        row.append(node_entry_value)
                        tbody.append(row)

                    node_content.remove(node_field_list)

                    if node_content:
                        rows = self.handle_node_content_children(node_content)
                        for row in rows:
                            tbody.append(row)

                    node_content.replace_self(node_new_content)

    def handle_node_content_children(self, node_content):
        rows = []
        for child in node_content.children:
            if child.__class__.__name__ == 'paragraph':
                row = nodes.row()
                node_entry_name = nodes.entry()
                node_entry_name.append(nodes.paragraph('Description', 'Description'))
                row.append(node_entry_name)
                node_entry_value = nodes.entry()
                node_entry_value.extend([child])
                row.append(node_entry_value)
                rows.append(row)
            elif child.__class__.__name__ == 'table':
                row = nodes.row()
                node_entry_name = nodes.entry()
                node_entry_name.append(nodes.paragraph('Nested Properties', 'Nested Properties'))
                row.append(node_entry_name)
                node_entry_value = nodes.entry()
                node_entry_value.extend([child])
                row.append(node_entry_value)
                rows.append(row)
            return rows

    def handle_annotate_type(self, entry_annotate, field):
        """Adds to right side table field for object annotations

        Depending on the type of the annotation defined by the field, add text
        to a container and append that to the table cell. The text will vary
        depending on the type.
        """
        annotate_type = field['annotate_type']
        node_annotate = nodes.container()
        node_annotate['classes'] = [
            'annotate-field',
            'annotate-field-{0}'.format(annotate_type),
        ]
        field_name, field_body = field
        # Field types come first in the annotation list
        if annotate_type == ANNOTATE_TYPE:
            node_para = field_body.next_node(nodes.paragraph)
            if node_para is not None:
                node_annotate.extend([
                    nodes.literal('', '', *node_para.children),
                    nodes.Text(' ', ' '),
                ])
                entry_annotate.insert(0, node_annotate)
        # Handle fields that have leading text. These go second in line, after
        # the type
        elif annotate_type in [ANNOTATE_OVERRIDES, ANNOTATE_EXTENDS]:
            node_emph = nodes.emphasis()
            if annotate_type == ANNOTATE_OVERRIDES:
                node_emph.append(nodes.Text('overrides ', 'overrides '))
            elif annotate_type == ANNOTATE_EXTENDS:
                node_emph.append(nodes.Text('extends ', 'extends '))
            node_para = field_body.next_node(nodes.paragraph)
            if node_para is not None:
                node_emph.extend(node_para.children)
            node_emph.append(nodes.Text(' ', ' '))
            node_annotate.append(node_emph)
            entry_annotate.insert(1, node_annotate)
        # Other fields can be added as text annotations
        elif annotate_type == ANNOTATE_READ_ONLY:
            node_annotate.append(
                nodes.emphasis('(read-only)', '(read-only)')
            )
            entry_annotate.append(node_annotate)


def patch_domain(app):
    JavaScriptDomain.directives['attribute'] = JSAttribute
    JavaScriptDomain.directives['function'] = JSCustomCallable
    JavaScriptDomain.directives['method'] = JSCustomCallable
    app.override_domain(JavaScriptDomain)


def setup(app):
    app.connect('builder-inited', patch_domain)
    app.add_transform(RandoTransform)
