





from flask import request
from flask_restful import Resource
from functools import wraps
from main_app.models.user import User
from main_app.exceptions import UnauthorizedAccess,AuthenticationFailure


def auth_user(func):
    @wraps(func)
    def authenticate(*args,**kwargs):
        auth = request.authorization
        if not auth:
            raise UnauthorizedAccess
        try:
            user_id = auth.username
        except ValueError:
                raise UnauthorizedAccess
        
        try:
            user=User.authenticate_user(user_id,auth.password)
            kwargs['user']=user

        except AuthenticationFailure:
            raise UnauthorizedAccess
        
        return func(*args, **kwargs)  

    return authenticate

def auth_meeting(func):
    @wraps(func)
    def authenticate(*args,**kwargs):
        auth = request.authorization
        if not auth:
            raise UnauthorizedAccess
        try:
            user_id = auth.username
        except ValueError:
                raise UnauthorizedAccess
        
        try:
            user=User.authenticate_user_for_meeting(user_id,auth.password)
            kwargs['user']=user

        except AuthenticationFailure:
            raise UnauthorizedAccess
        
        return func(*args, **kwargs)  

    return authenticate


def auth_super(func):
    @wraps(func)
    def authenticate(*args,**kwargs):
        auth = request.authorization
        if not auth:
            raise UnauthorizedAccess
        try:
            user_id = auth.username
        except ValueError:
                raise UnauthorizedAccess
        
        try:
            user=User.authenticate_user_for_meeting(user_id,auth.password)
            kwargs['user']=user

        except AuthenticationFailure:
            try:
                user=User.authenticate_user(user_id,auth.password)
                kwargs['user']=user
            except AuthenticationFailure:
                raise UnauthorizedAccess
        
        return func(*args, **kwargs)  

    return authenticate
class AuthorizedResource(Resource):
    method_decorators=[auth_user]


class MeetingAuthorizedResource(Resource):
    method_decorators=[auth_meeting]

class SuperAuthorizedResource(Resource):
    method_decorators=[auth_super]