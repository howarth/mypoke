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
            return redirect_to('/login')
    
    #TODO look in function for todos
    def login(self):
        #check to see if already logged in
        if User().valid_user(session['user']):
            return redirect_to('/account')
        #Checl to see if fields were even filled in
        if len(request.params) > 1:
            post_email = request.params['email']
            post_password = request.params['password']
            
            #Make sure both email and password were filled in
            if(post_email != '' and post_password != ''):
                user = User().valid_login(post_email, post_password)
                if user:             
                    session['user'] = user.id
                    session.save()
                    return redirect_to('/account')
                else:
                    #TODO Add error that username/password don't match
                    return render('account/login.mako')
            else:
                #TODO One field was left blank
                pass
        
        return render('account/login.mako')
    
    def logout(self):
        session.clear()
        session.save()
        return redirect_to('/')