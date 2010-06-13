from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1276431151.217505
_template_filename='/home/vrok/testhard/TestHard/testhard/templates/szablon.mako'
_template_uri='/szablon.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"\n  "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">\n<html>\n    <head>\n        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">\n        <meta name="keywords" content="">\n        <meta name="description" content="">\n        <title>TestHard</title>\n        ')
        # SOURCE LINE 9
        __M_writer(escape(h.stylesheet_link('/template.css')))
        __M_writer(u'\n    </head>\n\n<body>\n    <div id="doc4" class="yui-t1">\n        <div id="hd">\n            <h1> TestHard </h1>\n        </div>\n        <div id="bd">\n            <div id="yui-main">\n                <div class="yui-b">\n                   ')
        # SOURCE LINE 20
        __M_writer(escape(next.body()))
        __M_writer(u'\n                </div>\n            </div>\n            <div class="yui-b">\n                <ul>\n                    <li>')
        # SOURCE LINE 25
        __M_writer(escape(h.link_to('Main page', url('/'))))
        __M_writer(u'</li>\n                    <li>')
        # SOURCE LINE 26
        __M_writer(escape(h.link_to('Repository', url('/repository'))))
        __M_writer(u'</li>\n                    <li>')
        # SOURCE LINE 27
        __M_writer(escape(h.link_to('Run', url('/run'))))
        __M_writer(u'</li>\n                    <li>')
        # SOURCE LINE 28
        __M_writer(escape(h.link_to('Schedule', url('/schedule'))))
        __M_writer(u'</li>\n                    <li>')
        # SOURCE LINE 29
        __M_writer(escape(h.link_to('Results', url('/results'))))
        __M_writer(u'</li>\n                </ul>\n            </div>\n        </div>\n        <div id="ft">\n            <p>All rights reserved 2010</p>\n        </div>\n    </div>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


