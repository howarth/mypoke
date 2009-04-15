<%def name="display_play_content()">
<script type="text/javascript">
    $(document).ready(function() {
        $(".gamemenu").click(function(){
            var id = this.id;
            $(".gamemenu").css('background-color', null);
            $(".gamemenu").css('color', null);
            $("#"+id).css('color', '#FFF');
            $("#"+id).css('background-color', '#333');
            $(".gamecontent").hide();
            $("#"+id+"content").show();
        });
        $("#betInput").keyup(function(e){
            var raise = $("#betInput").val();
            raise = parseInt(raise);
            if(!raise || raise<${c.min_raise} || raise>${c.Game.curr_player.player.in_play}){
                $("#raiseButton").text("Raise");
                $("#betInput").css('background-color', 'pink');
            }
            else{
                $("#betInput").css('background-color', '');
                $("#raiseButton").html("Raise<br/>to $" + raise);
            }
        });
        $(".call").click(function(){
            $(".call").css('background-color', 'purple');
            gameAction(${c.Game.game.id}, 'call', -1);
        });
    });
</script>
<div class="currPlayer">
    <div class="name">${c.Game.curr_player.player.name}</div>
    
    %if c.Game.curr_player.to_call == 0:
        <button type="button" class="call">Check</button>
        <input type="text" name="bet" /><button class="bet" type="button">Bet</button>
    %else:
        <button type="button" class="call">Call <br/>$${c.Game.curr_player.to_call}</button>
        <input type="text" id="betInput" name="bet" value="${c.min_raise}"/>
        <button class="bet" id="raiseButton" type="button">Raise <br/> to $${c.min_raise}</button>
    %endif
    
   <button type="button" id="fold" class="fold">Fold</button>
    <div style="clear:both"></div>
</div>
%for player in c.Game.players:
    %if c.Game.game.on == player.position:
        <div class="playerHolder" style="background-color:green">
    %else:
        <div class="playerHolder">
    %endif
        <div class="name">${player.name}</div>
        <div class="in_play">$${player.in_play}</div>
        <div class="in_pot">$${player.in_pot}</div>
    </div>
%endfor
<div style="clear:both"></div>
</%def>