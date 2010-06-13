from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1276445923.725774
_template_filename='/home/ravd/TestHard/testhard/templates/repositoryAdd.mako'
_template_uri='/repositoryAdd.mako'
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
        __M_writer(u'\n\n<h2> Repositories </h2>\n\n<form class="feedbackform" method="GET" action="/repository/doAdd">\n<div class="fieldwrapper">\n    <label for="name" class="styled">Name:</label>\n    <div class="thefield">\n        <input type="text" name="name" id="name" value="" size="30" />\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="url" class="styled">Url:</label>\n    <div class="thefield">\n        <input type="text" name="url" id="url" value="" size="30" /><br />\n        <span style="font-size: 80%">*Note: Please make sure it\'s correctly entered!</span>\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="login" class="styled">Login:</label>\n    <div class="thefield">\n        <input type="text" name="login" id="login" value="" size="30" />\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="password" class="styled">Password:</label>\n    <div class="thefield">\n        <input type="text" name="password" id="password" value="" size="30" />\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="type" class="styled">Type:</label>\n    <div class="thefield">\n        <select name="type" id="type">\n')
        # SOURCE LINE 40
        for typ in c.repTypes:
            # SOURCE LINE 41
            __M_writer(u'            <option value="')
            __M_writer(escape(typ.typ))
            __M_writer(u'">')
            __M_writer(escape(typ.typ))
            __M_writer(u'</option>\n')
        # SOURCE LINE 43
        __M_writer(u'        </select>\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="about" class="styled">Test commands:</label>\n    <div class="thefield">\n        <textarea name="test_cmds" id="about"></textarea>\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="about" class="styled">Test output path:</label>\n    <div class="thefield">\n        <textarea name="test_results" id="about"></textarea>\n    </div>\n</div>\n\n<div class="fieldwrapper">\n    <label for="about" class="styled">Comment:</label>\n    <div class="thefield">\n        <textarea name="comment" id="about"></textarea>\n</div>\n</div>\n\n<div class="buttonsdiv">\n    <input type="submit" value="Submit" style="margin-left: 150px;" /> <input type="reset" value="Reset" />\n</div>\n\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


