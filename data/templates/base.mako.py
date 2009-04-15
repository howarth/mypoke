from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1239825511.785892
_template_filename='/srv/http/poker/poker/templates/base.mako'
_template_uri='/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html>\n  <head>\n    <link rel="stylesheet" type="text/css" href="/css/base.css" />\n    <script src="/js/jquery.js" language="javascript" type="text/javascript"></script>\n    <script src="/js/functions.js" language="javascript" type="text/javascript"></script>\n    ')
        # SOURCE LINE 8
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n  </head>\n  <body>\n    <div id="site">\n      <div id="banner">\n\t<div class="logo">MyPokerStatus</div>\n\t<div class="links">\n\t<ul>\n\t  <li><a href="/">Home</a></li>\n\t  <li><a href="/login">Login</a></li>\n\t  <li><a href="/logout">Logout</a></li>\n\t  <li><a href="/account">Account</a></li>\n\t</ul>\n\t</div>\n\t<div style="clear:both"></div>\n      </div>\n      <div id="content">\n\t')
        # SOURCE LINE 25
        __M_writer(escape(self.body()))
        __M_writer(u'\n      </div>\n    </div>\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


