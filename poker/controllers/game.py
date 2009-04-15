import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from poker.lib.base import BaseController, render
from poker.model.user import User
from poker.model.game import Game
from poker.model.player import Player
from poker.model import meta

log = logging.getLogger(__name__)

class GameController(BaseController):
    
    def __before__(self):
        #See if there is a user logged in
        self.user_id = session.get('user')
        if self.user_id:
            if not User(self.user_id).valid_user():
                return redirect_to('/login')
        else:
            return redirect_to('/login')
            
    def index(self, game_id = -1):
        
        self.game_id = game_id
        self.Game = Game(self.user_id, self.game_id)
        #Check if game belongs to logged in user
        if not self.Game.load_game():
            return redirect_to('/account')
        else:
            #Game belongs to logged in user, do the stuff
            #self.game.load_players()
            self.Game.load_output_vars()
            #self.Game.load_curr_player()
            #self.Game.bet(20)
            
            c.Game = self.Game
            c.min_raise = self.Game.game.highestraise + self.Game.curr_player.to_call;
            #c.player_ids = self.Game.player_ids
            
            return render('game/index.mako')