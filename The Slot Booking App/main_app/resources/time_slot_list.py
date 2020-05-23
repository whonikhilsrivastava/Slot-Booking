
from main_app.auth import MeetingAuthorizedResource
from flask import render_template, redirect, request
from flask_restful import reqparse,Resource,fields,marshal_with
from main_app.models.time_slot import TimeSlot

class TimeSlotList(MeetingAuthorizedResource):
    def get(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('date',type=str,required=True)
        args=parser.parse_args()
        time_slots=TimeSlot.getlist_forbooking(args['date'],kwargs['user'].id)
        return {'success':True,'message':'List of time slots for the day','time_slots':time_slots}
