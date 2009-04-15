from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1239829742.5131011
_template_filename='/srv/http/poker/poker/templates/game/index.mako'
_template_uri='game/index.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('functions', context._clean_inheritance_tokens(), templateuri='/functions.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'functions')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        functions = _mako_get_namespace(context, 'functions')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 7
        __M_writer(u'\n\n<h2>Game: ')
        # SOURCE LINE 9
        __M_writer(escape(c.Game.game.name))
        __M_writer(u'</h2>\n<a href="#" class="gamemenu" id="manage">Manage</a>\n<a href="#" class="gamemenu" id="play">Play</a>\n<div id="managecontent" class="gamecontent">\n    Game ID: ')
        # SOURCE LINE 13
        __M_writer(escape(c.Game.game.id))
        __M_writer(u'<br/>\n    User ID: ')
        # SOURCE LINE 14
        __M_writer(escape(c.Game.game.user_id))
        __M_writer(u'<br/>\n    Name: ')
        # SOURCE LINE 15
        __M_writer(escape(c.Game.game.name))
        __M_writer(u'<br/>\n    Players: ')
        # SOURCE LINE 16
        __M_writer(escape(c.Game.game.players))
        __M_writer(u'<br/>\n    SB: ')
        # SOURCE LINE 17
        __M_writer(escape(c.Game.game.sb))
        __M_writer(u'<br/>\n    BB: ')
        # SOURCE LINE 18
        __M_writer(escape(c.Game.game.bb))
        __M_writer(u'<br/>\n    Anti: ')
        # SOURCE LINE 19
        __M_writer(escape(c.Game.game.anti))
        __M_writer(u'<br/>\n    On: ')
        # SOURCE LINE 20
        __M_writer(escape(c.Game.game.on))
        __M_writer(u' ')
        __M_writer(escape(c.Game.players[c.Game.game.on].name))
        __M_writer(u'<br/>\n    Start: ')
        # SOURCE LINE 21
        __M_writer(escape(c.Game.game.start))
        __M_writer(u'<br/>\n    Dealer: ')
        # SOURCE LINE 22
        __M_writer(escape(c.Game.game.dealer))
        __M_writer(u'<br/>\n    SB ON: ')
        # SOURCE LINE 23
        __M_writer(escape(c.Game.game.sb_on))
        __M_writer(u'<br/>\n    BB ON: ')
        # SOURCE LINE 24
        __M_writer(escape(c.Game.game.bb_on))
        __M_writer(u'<br/>\n    Highestbet: ')
        # SOURCE LINE 25
        __M_writer(escape(c.Game.game.highestbet))
        __M_writer(u'<br/>\n    Pot: ')
        # SOURCE LINE 26
        __M_writer(escape(c.Game.game.pot))
        __M_writer(u'<br/>    \n</div>\n<div id="playcontent" class="gamecontent">\n')
        # SOURCE LINE 29
        __M_writer(escape(functions.display_play_content()))
        __M_writer(u'\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <link rel="stylesheet" type="text/css" href="/css/game.css" />\n  \n  \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


