from poker.model import meta
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

class User(object):
    
    def valid_login(self, post_email='', post_password=''):
        user = meta.Session.query(User).filter_by(email=post_email).first()
        if user.password == post_password:
            return user
        else:
            return False
    
    #Function checks if user_id is a valid user
    def valid_user(self, user_id):
        user = meta.Session.query(User).filter_by(id=user_id).first()
        if user:
            return user
        else:
            return False