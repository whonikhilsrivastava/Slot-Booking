from flask_restful import reqparse,Resource,fields,marshal_with

class CalenderToken(Resource):
    def get(self,*args,**kwargs):
        parser=reqparse.RequestParser()
        parser.add_argument('calender_id',type=str,required=True)
        args=parser.parse_args()
        token=args['calender_id'].split('-')
        return{'success':True,'message':'token for people to book meetings on other people calenders',
                'data':{'meeting_id_token':token[0],'meeting_password_token':token[1]}}


