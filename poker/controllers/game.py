import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from poker.lib.base import BaseController, render
from poker.model.user import User
from poker.model import meta

log = logging.getLogger(__name__)

class GameController(BaseController):
    
    def __before__(self):
        user_id = session.get('user')
        User().valid_user(user_id)
            
    def index(self, gameid=''):
        
        return 'Auth'
