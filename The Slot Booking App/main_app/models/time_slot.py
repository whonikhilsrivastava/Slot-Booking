


from main_app.models import db
from datetime import timedelta
from datetime import datetime
from main_app.exceptions import DateTimeformatMisMatch,TimeSlotClash
from pprint import pprint
class TimeSlot(db.Model):
    __tablename__='time_slots'
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    start_time=db.Column(db.DateTime)
    end_time=db.Column(db.DateTime)
    available=db.Column(db.Boolean,default=True)



    @classmethod
    def create(cls,start_time=None,date=None,user_id=None,minute=60):
        try:
            pprint(start_time)
            pprint(date)
            start_time=datetime.strptime(date+" "+start_time,'%m-%d-%Y %H:%M:%S')
        except:
            raise DateTimeformatMisMatch
        end_time=start_time+timedelta(minutes=minute)
        time_slots=cls.query.filter(*[cls.start_time <= start_time,cls.end_time>start_time,cls.user_id==user_id]).all()
        if len(time_slots)!=0:
            db.session.rollback()
            raise TimeSlotClash
        time_slot=cls(start_time=start_time,end_time=end_time,user_id=user_id,available=True)
        db.session.add(time_slot)
        db.session.commit()

    @classmethod
    def delete_slot(cls,slot_id):
        slot=cls.query.filter(cls.id==slot_id).first()
        db.session.delete(slot)
        db.session.commit()

    @classmethod
    def getlist_forbooking(cls,date,user_id):

            try:
                date=datetime.strptime(date,'%m-%d-%Y')
            except:
                raise DateTimeformatMisMatch
            next_day=date+timedelta(days=1)
            time_slots=cls.query.filter(*[cls.start_time >= date,cls.start_time<next_day,cls.user_id==user_id,cls.available==True]).all()
            slots=[]
            for slot in time_slots:
                slots.append({'id':slot.id,'start_time':slot.start_time.strftime('%H:%M:%S'),'end_time':slot.end_time.strftime('%H:%M:%S')})
            return slots
    @classmethod
    def getlist(cls,date,user_id):

            try:
                date=datetime.strptime(date,'%m-%d-%Y')
            except:
                raise DateTimeformatMisMatch
            next_day=date+timedelta(days=1)
            pprint(next_day)
            pprint(date)
            pprint(user_id)
            time_slots=cls.query.filter(*[cls.start_time >= date,cls.start_time<next_day,cls.user_id==user_id]).all()
            slots=[]
            for slot in time_slots:
                slots.append({'id':slot.id,'date':slot.start_time.strftime('%m-%d-%Y'),'start_time':slot.start_time.strftime('%H:%M:%S'),'end_time':slot.end_time.strftime('%H:%M:%S'),'available':slot.available})
            return slots

