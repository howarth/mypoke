import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from poker.model.user import User
from poker.model import meta

from poker.lib.base import BaseController, render

log = logging.getLogger(__name__)

class AccountController(BaseController):

    
        
    def index(self):
        if session.get('user'):
            c.user = session.get('user')
            return render('account/index.mako')
        else:
            return render('account/login.mako')
    
    def login(self):
        if len(request.params) > 1:
            post_email = request.params['email']
            post_password = request.params['password']
            User().login(post_email, post_password)
            
        return render('account/login.mako')
    
    def logout(self):
        session.clear()
        session.save()
        return redirect_to('/')