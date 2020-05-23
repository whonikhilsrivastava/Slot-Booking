


from main_app.models import db
from main_app.models.time_slot import TimeSlot
from main_app.models.user import User
from sqlalchemy import or_
class Meeting(db.Model):
    __tablename__='meetings'
    id=db.Column(db.Integer,primary_key=True)
    time_slot_id=db.Column(db.Integer,db.ForeignKey('time_slots.id'))
    name=db.Column(db.String)
    email=db.Column(db.String)
    purpose=db.Column(db.String)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    participant_id=db.Column(db.Integer,db.ForeignKey('users.id'))


    @classmethod
    def create(cls,name=None,email=None,time_slot_id=None,purpose=None,user_id=None):
        user=User.query.filter(User.email==email).first()
        participant_id=None
        if user !=None:
            participant_id=user.id
        meeting=cls(name=name,email=email,time_slot_id=time_slot_id,purpose=purpose,user_id=user_id,participant_id=participant_id)

        db.session.add(meeting)
        db.session.commit()
        time_slot=TimeSlot.query.filter(TimeSlot.id==time_slot_id).first()
        time_slot.available=False
        db.session.commit()
    

    @classmethod
    def cancel(cls,id=None,reason=None):
        meeting=cls.query.filter(cls.id==id).first()
        time_slot=TimeSlot.query.filter(TimeSlot.id==meeting.time_slot_id).first()
        time_slot.available=True
        db.session.delete(meeting)
        db.session.commit()

    @classmethod
    def meetings_list(cls,user_id):
        meeting_list={'host':[],'participant':[]}
        meetings=cls.query.filter(cls.user_id==user_id).all()
        for meeting in meetings:
            time_slot=TimeSlot.query.filter(TimeSlot.id==meeting.time_slot_id).first()
            time=time_slot.start_time.strftime('%H:%M:%S')+"-"+time_slot.end_time.strftime('%H:%M:%S')
            meeting_list['host'].append({'meeting_id':meeting.id,'date':time_slot.start_time.strftime('%m-%d-%Y'),'participant_name':meeting.name,'participant_email':meeting.email,'purpose':meeting.purpose,'time':time})  
        
        meetings=db.session.query(cls,User).join(User,cls.user_id==User.id).filter(cls.participant_id==user_id).all()
        for meeting in meetings:
            time_slot=TimeSlot.query.filter(TimeSlot.id==meeting[0].time_slot_id).first()
            time=time_slot.start_time.strftime('%H:%M:%S')+"-"+time_slot.end_time.strftime('%H:%M:%S')
            
            meeting_list['participant'].append({'meeting_id':meeting[0].id,'date':time_slot.start_time.strftime('%m-%d-%Y'),'host_name':meeting[1].name,'host_email':meeting[1].email,'purpose':meeting[0].purpose,'time':time})
        return meeting_list