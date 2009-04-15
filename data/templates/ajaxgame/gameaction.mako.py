from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1239829937.6992371
_template_filename='/srv/http/poker/poker/templates/ajaxgame/gameaction.mako'
_template_uri='ajaxgame/gameaction.mako'
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
    # SOURCE LINE 1
    ns = runtime.Namespace('functions', context._clean_inheritance_tokens(), templateuri='/functions.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'functions')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        functions = _mako_get_namespace(context, 'functions')
        __M_writer = context.writer()
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(escape(functions.display_play_content()))
        return ''
    finally:
        context.caller_stack._pop_frame()


