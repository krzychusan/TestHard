from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274450012.109967
_template_filename='/home/kaisen/plons/TestHard/testhard/templates/hello.mako'
_template_uri='/hello.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'Hello World, the environ variable looks like: <br />\n\n')
        # SOURCE LINE 3
        __M_writer(escape(request.environ))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


