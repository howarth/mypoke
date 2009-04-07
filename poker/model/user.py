from poker.model import meta
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

class User(object):
    
    def login(self, post_email='', post_password=''):
        if(post_email == '' or post_password==''):
            return False
        else:
            user = meta.Session.query(User).filter_by(email=post_email).first()
            if user.password == post_password:
                session['user'] = user.id
                session.save()
                return redirect_to('/account')
            else:
                return False
    
    #Function checks if user_id is a valid user
    def auth(self):
        user_id = session.get('user')
        user = meta.Session.query(User).filter_by(id=user_id).first()
        if user:
            pass
        else:
            return redirect_to('/login')