# -*- coding: utf-8 -*-

import json
from hashlib import md5
from base64 import b64encode
import datetime
from flask.views import MethodView
from flask import render_template, redirect, request
from flask_restful import reqparse,Resource,fields,marshal_with
import flask
from main_app import app
from main_app.models.user import User
from main_app.exceptions import AuthenticationFailure
from main_app.helpers import basic_auth
from pprint import pprint


class UserSignin(Resource):


    post_parser=reqparse.RequestParser()
    post_parser.add_argument('email',type=str)
    post_parser.add_argument('password',type=str)
 
   
    
    def post(self,*args,**kwargs):
        
        args=self.post_parser.parse_args()
        try:
            #if user signs in using email and password
            if args['email']!=None and args['password']!=None:
                user=User.signin(email=args['email'],password=args['password'])
            # if user signs in using facebook access token
          
            else:
                raise AuthenticationFailure

        except AuthenticationFailure:
            raise AuthenticationFailure

        return ({"success":True,              
                "message":"signup successful",
                "data":{
                  "authorization_username_token":str(user.id),
                  "authorization_password_token":user.password,
                  "calender_link":app.config['URL']+'calender?calender_id='+str(user.id)+"-"+user.meeting_token
                 }})
