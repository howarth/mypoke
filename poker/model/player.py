from poker.model import meta

class Player(object):
    
    def __init__(self, id = -1):
        self.player_id = id
        
    def load_player(self):
        self.player = meta.Session.query(Player).filter_by(id = self.player_id).one()
        if not self.player:
            return 'Error'
    
    def by_game_id(self, game_id):
        players = meta.Session.query(Player).filter_by(game_id = game_id).order_by("position asc").all()
        if players:
            return players
        else:
            return False    

    def bet(self, amount):
        self.player.in_pot += amount
        self.player.round_bet += amount
        self.player.in_play -= amount
        meta.Session.commit()
    
    def load_to_call(self, amount):
        self.to_call = amount - self.player.round_bet
    
    def call(self, amount):
        load_to_call(amount)
        self.player.in_play -= self.to_call
        self.player.round_bet +=  self.to_call
        self.player.in_pot += self.to_call
        meta.Session.commit()
        return to_call
    
    def fold(self):
        self.player.fold = 1
        meta.Session.commit()
    
    def next_player_pos(self, game_id, start_pos, players):
        if start_pos == players -1:
            next = 1
        else:
            next = start_pos + 1
        
        players = self.by_game_id(self, game_id)
        
        if players[next].fold == 0:
            return next
        else:
            return next_player_pos(game_id, next, players)
        

