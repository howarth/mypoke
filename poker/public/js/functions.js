function gameAction(gameId, action, amount){
    
    $.get("/ajaxgame/gameaction/", {action: action, amount: amount},function(data){
        $("#playcontent").html(data);
    });
   
}