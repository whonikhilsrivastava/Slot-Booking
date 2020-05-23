from flask import Flask, request,url_for, redirect, render_template
from flask_restful import Api,fields
import os,sys,traceback


app = Flask(__name__)

app.config.from_object('main_app.config.DevelopmentConfig')

from main_app.models import db

def init_sqlalchemy(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

app = init_sqlalchemy(app)
from main_app.exceptions import AppException
class ModApi(Api):
    def handle_error(self, e):
        if isinstance(e, AppException):
            return self.make_response({'message': e.message,'data':{'error_code': e.error_code}, 'success':False}, e.http_response_code)

        code = getattr(e, 'code', 500)
        if 499 < code < 600:
            tag = request.method + ' ' + request.path
            exc = traceback.format_exc()
            pprint (exc)
            sys.stdout.flush()
            return self.make_response({'message': 'something went wrong', 'trace': exc}, 500)
        return super(ModApi, self).handle_error(e)

api = ModApi(app)

from main_app.models import *
from main_app.resources import *

api.add_resource(UserSignUp, '/user_signup')
api.add_resource(UserSignin,'/user_signin') 
api.add_resource(TimeSlotResource,'/time_slots')
api.add_resource(BookMeetings,'/book_meetings')
api.add_resource(TimeSlotList,'/time_slot_booking')
api.add_resource(MeetingsList,'/meetings')
api.add_resource(CalenderToken,'/calender')
