from poker.model import meta
from poker.model.player import Player
class Game(object):
    
    def __init__(self, user_id = -1, game_id = -1):
        self.user_id = user_id
        self.game_id = game_id
        return None
    
    def load_game(self):
        #Check if valid game, and load that game
        self.game = meta.Session.query(Game).filter_by(id = self.game_id, user_id = self.user_id).first()
        if self.game:
            return True
        else:
            return False
    
    def load_player_ids(self):
        players = meta.Session.query(Player.id).filter_by(game_id = self.game_id).order_by('position asc')
        self.player_ids = []
        for player in players:
            self.player_ids.append(player[0]);
        return None
    
    def load_curr_player(self):
        player_id = self.player_ids[self.game.on]
        self.curr_player = Player(player_id)
        self.curr_player.load_player()
        
    def by_user_id(self, user_id):
        games = meta.Session.query(Game).filter_by(user_id = user_id).all()
        if games:
            return games
        else:
            return False
    
    def load_output_vars(self):
        self.load_game()
        self.load_player_ids()
        self.players = Player().by_game_id(self.game.id)
        self.load_curr_player()
        self.curr_player.load_to_call(self.game.highestbet)
        
    def bet(self, amount):
        self.curr_player.bet(amount)
        self.game.highestbet = amount
        self.game.pot += amount
        meta.Session.commit()
    
    def fold(self):
        self.curr_player.fold()
    
    def call(self):
        to_call = self.curr_player.call(self.game.highestbet)
        self.game.pot += to_call
        meta.Session.commit()
    
    def next_player(self):
        if self.game.on == self.game.players:
            self.game.on = 1
        else:
            self.game.on += 1
            
        meta.Session.commit()