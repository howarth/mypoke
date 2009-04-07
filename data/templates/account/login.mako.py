from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1239069157.386553
_template_filename='/srv/http/poker/poker/templates/account/login.mako'
_template_uri='account/login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<form action=\'/login\' method=\'post\'>\n\nEmail: <input type="text" name="email" /><br/>\nPassword: <input type="text" name="password" /><br/>\n<input type="submit" value="login" />\n</form>\n\n')
        # SOURCE LINE 8
        __M_writer(escape(c.login))
        return ''
    finally:
        context.caller_stack._pop_frame()


