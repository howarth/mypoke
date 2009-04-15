<%inherit file="/base.mako" />
<%namespace name="functions" file="/functions.mako" />
<%def name="head_tags()">
  <link rel="stylesheet" type="text/css" href="/css/game.css" />
  
  
</%def>

<h2>Game: ${c.Game.game.name}</h2>
<a href="#" class="gamemenu" id="manage">Manage</a>
<a href="#" class="gamemenu" id="play">Play</a>
<div id="managecontent" class="gamecontent">
    Game ID: ${c.Game.game.id}<br/>
    User ID: ${c.Game.game.user_id}<br/>
    Name: ${c.Game.game.name}<br/>
    Players: ${c.Game.game.players}<br/>
    SB: ${c.Game.game.sb}<br/>
    BB: ${c.Game.game.bb}<br/>
    Anti: ${c.Game.game.anti}<br/>
    On: ${c.Game.game.on} ${c.Game.players[c.Game.game.on].name}<br/>
    Start: ${c.Game.game.start}<br/>
    Dealer: ${c.Game.game.dealer}<br/>
    SB ON: ${c.Game.game.sb_on}<br/>
    BB ON: ${c.Game.game.bb_on}<br/>
    Highestbet: ${c.Game.game.highestbet}<br/>
    Pot: ${c.Game.game.pot}<br/>    
</div>
<div id="playcontent" class="gamecontent">
${functions.display_play_content()}
</div>
