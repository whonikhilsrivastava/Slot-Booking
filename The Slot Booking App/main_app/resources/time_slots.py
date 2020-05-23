
from main_app.auth import AuthorizedResource
from flask import render_template, redirect, request
from flask_restful import reqparse,Resource,fields,marshal_with
from main_app.models.time_slot import TimeSlot
from main_app.models.meeting import Meeting
from pprint import pprint
from main_app.models import db
class TimeSlotResource(AuthorizedResource):

    def post(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('date',type=str,required=True)
        parser.add_argument('start_time',type=str,required=True)
        args=parser.parse_args()
        pprint(args['date'])
        TimeSlot.create(start_time=args['start_time'],date=args['date'],user_id=kwargs['user'].id)

        return {'success':True,'message':'time slot created'}

    def get(self,*args,**kwargs):

        parser=reqparse.RequestParser()
        parser.add_argument('date',type=str,required=True)
        args=parser.parse_args()
        time_slots=TimeSlot.getlist(args['date'],kwargs['user'].id)
        return {'success':True,'message':'List of time slots for the day','time_slots':time_slots}

    def delete(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('time_slot_id',type=str,required=True)
        args=parser.parse_args()
        meetings=Meeting.query.filter(Meeting.time_slot_id==args['time_slot_id']).all()
        for meeting in meetings:
            db.session.delete(meeting)
        db.session.commit()
        TimeSlot.delete_slot(args['time_slot_id'])
        return {'success':True,'message':'time_slot_deleted'}
