from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274654201.7906699
_template_filename='/home/kaisen/plons/TestHard/testhard/templates/repository.mako'
_template_uri='/repository.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/szablon.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'\n<h2> Repositories </h2>\n\n<table border="1">\n<tr>\n    <th>No.</th>\n    <th>Name</th>\n    <th>Url</th>\n    <th>Type</th>\n    <th>Auth</th>\n    <th>remove</th>\n</tr>\n')
        # SOURCE LINE 15
        if c.repos:
            # SOURCE LINE 16
            for rep in c.repos:
                # SOURCE LINE 17
                __M_writer(u'    <tr>\n        <td>')
                # SOURCE LINE 18
                __M_writer(escape(c.repos.index(rep)))
                __M_writer(u'</td>\n        <td>')
                # SOURCE LINE 19
                __M_writer(escape(rep.name))
                __M_writer(u'</td>\n        <td>')
                # SOURCE LINE 20
                __M_writer(escape(rep.url))
                __M_writer(u'</td>\n        <td>')
                # SOURCE LINE 21
                __M_writer(escape(rep.typ))
                __M_writer(u'</td>\n        <td>')
                # SOURCE LINE 22
                __M_writer(escape(rep.Auth))
                __M_writer(u'</td>\n        <td><a href="/repository/remove?name=')
                # SOURCE LINE 23
                __M_writer(escape(rep.name))
                __M_writer(u'">remove</a></td>\n    </tr>\n')
        # SOURCE LINE 27
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 29
        __M_writer(escape(h.link_to('Add', url('/repository/add'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


