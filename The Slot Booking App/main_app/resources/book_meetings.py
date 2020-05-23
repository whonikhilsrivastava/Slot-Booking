

from main_app.auth import SuperAuthorizedResource
from main_app.models.meeting import Meeting
from flask_restful import reqparse,Resource,fields,marshal_with

class BookMeetings(SuperAuthorizedResource):


    def post(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True)
        parser.add_argument('name',type=str,required=True)
        parser.add_argument('time_slot_id',type=int,required=True)
        parser.add_argument('purpose',type=str,required=True)
        args=parser.parse_args()
        Meeting.create(email=args['email'],name=args['name'],time_slot_id=args['time_slot_id'],purpose=args['purpose'],user_id=kwargs['user'].id)
        return {'success':True,'message':'Meeting booked'}
    
    
   

