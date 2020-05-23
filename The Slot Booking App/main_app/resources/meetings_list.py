
from main_app.auth import AuthorizedResource
from main_app.models.meeting import Meeting
from flask_restful import reqparse,Resource,fields,marshal_with

class MeetingsList(AuthorizedResource):

    def get(self,*args,**kwargs):
        meetings=Meeting.meetings_list(kwargs['user'].id)
        return{'success':True,'message':'meeting list','data':{'list':meetings}}

    
    def delete(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('meeting_id',type=str,required=True)
        args=parser.parse_args()
        Meeting.cancel(args['meeting_id'])
        return {'success':True,'message':'meeting cancelled'}