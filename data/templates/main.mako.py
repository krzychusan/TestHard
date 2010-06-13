from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1276431151.172981
_template_filename='/home/vrok/testhard/TestHard/testhard/templates/main.mako'
_template_uri='/main.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'\n<p>\n<h2> TestHard</h2>\nTestHard is a distributed testing framework written in python. It uses Pylons as a web framework together with mako templates.\n</p>\n\n\n<p>\n<h2> Statistics</h2>\nScheduled tests:<br>\n123\n321<br>\nRepositories:<br>\n156\n31<br>\n</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


