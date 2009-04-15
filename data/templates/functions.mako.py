from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1239829566.135242
_template_filename='/srv/http/poker/poker/templates/functions.mako'
_template_uri='/functions.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['display_play_content']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_display_play_content(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<script type="text/javascript">\n    $(document).ready(function() {\n        $(".gamemenu").click(function(){\n            var id = this.id;\n            $(".gamemenu").css(\'background-color\', null);\n            $(".gamemenu").css(\'color\', null);\n            $("#"+id).css(\'color\', \'#FFF\');\n            $("#"+id).css(\'background-color\', \'#333\');\n            $(".gamecontent").hide();\n            $("#"+id+"content").show();\n        });\n        $("#betInput").keyup(function(e){\n            var raise = $("#betInput").val();\n            raise = parseInt(raise);\n            if(!raise || raise<')
        # SOURCE LINE 16
        __M_writer(escape(c.min_raise))
        __M_writer(u' || raise>')
        __M_writer(escape(c.Game.curr_player.player.in_play))
        __M_writer(u'){\n                $("#raiseButton").text("Raise");\n                $("#betInput").css(\'background-color\', \'pink\');\n            }\n            else{\n                $("#betInput").css(\'background-color\', \'\');\n                $("#raiseButton").html("Raise<br/>to $" + raise);\n            }\n        });\n        $(".call").click(function(){\n            $(".call").css(\'background-color\', \'purple\');\n            gameAction(')
        # SOURCE LINE 27
        __M_writer(escape(c.Game.game.id))
        __M_writer(u', \'call\', -1);\n        });\n    });\n</script>\n<div class="currPlayer">\n    <div class="name">')
        # SOURCE LINE 32
        __M_writer(escape(c.Game.curr_player.player.name))
        __M_writer(u'</div>\n    \n')
        # SOURCE LINE 34
        if c.Game.curr_player.to_call == 0:
            # SOURCE LINE 35
            __M_writer(u'        <button type="button" class="call">Check</button>\n        <input type="text" name="bet" /><button class="bet" type="button">Bet</button>\n')
            # SOURCE LINE 37
        else:
            # SOURCE LINE 38
            __M_writer(u'        <button type="button" class="call">Call <br/>$')
            __M_writer(escape(c.Game.curr_player.to_call))
            __M_writer(u'</button>\n        <input type="text" id="betInput" name="bet" value="')
            # SOURCE LINE 39
            __M_writer(escape(c.min_raise))
            __M_writer(u'"/>\n        <button class="bet" id="raiseButton" type="button">Raise <br/> to $')
            # SOURCE LINE 40
            __M_writer(escape(c.min_raise))
            __M_writer(u'</button>\n')
        # SOURCE LINE 42
        __M_writer(u'    \n   <button type="button" id="fold" class="fold">Fold</button>\n    <div style="clear:both"></div>\n</div>\n')
        # SOURCE LINE 46
        for player in c.Game.players:
            # SOURCE LINE 47
            if c.Game.game.on == player.position:
                # SOURCE LINE 48
                __M_writer(u'        <div class="playerHolder" style="background-color:green">\n')
                # SOURCE LINE 49
            else:
                # SOURCE LINE 50
                __M_writer(u'        <div class="playerHolder">\n')
            # SOURCE LINE 52
            __M_writer(u'        <div class="name">')
            __M_writer(escape(player.name))
            __M_writer(u'</div>\n        <div class="in_play">$')
            # SOURCE LINE 53
            __M_writer(escape(player.in_play))
            __M_writer(u'</div>\n        <div class="in_pot">$')
            # SOURCE LINE 54
            __M_writer(escape(player.in_pot))
            __M_writer(u'</div>\n    </div>\n')
        # SOURCE LINE 57
        __M_writer(u'<div style="clear:both"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


