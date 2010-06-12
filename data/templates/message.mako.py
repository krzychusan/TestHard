from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274654422.2615499
_template_filename='/home/kaisen/plons/TestHard/testhard/templates/message.mako'
_template_uri='/message.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(escape(c.message))
        __M_writer(u'\n<br>\n')
        # SOURCE LINE 6
        if c.link:
            # SOURCE LINE 7
            __M_writer(u'<a href="')
            __M_writer(escape(c.link))
            __M_writer(u'">Return</a>\n')
            # SOURCE LINE 8
        else:
            # SOURCE LINE 9
            __M_writer(u'<a href="/">Return</a>\n')
        # SOURCE LINE 11
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


