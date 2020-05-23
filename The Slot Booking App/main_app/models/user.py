
from main_app.models import db
import datetime
import re
from base64 import b64encode
from hashlib import md5
from sqlalchemy.exc import IntegrityError
from main_app.exceptions import EmailAlreadyRegistered,AuthenticationFailure
email_pattern = re.compile(r'(?P<email>(([^<>()[\]\\.,;:\s@\']+(\.[^<>()[\]\\.,;:\s@\']+)*)|(\'.+\'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,})))')

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String)
    email=db.Column(db.String,unique=True)
    password=db.Column(db.String)
    meeting_token=db.Column(db.String)
    joined_at=db.Column(db.DateTime,default=datetime.datetime.utcnow)

    @classmethod
    def create(cls,email,name,password):
        try:
            user=cls.query.filter(cls.email==email).first()
            if user!=None:
                if user.password==None:
                    user.password=password
                    db.session.commit()
                else:
                    raise EmailAlreadyRegistered
            else:
                user=cls(email=email,name=name,password=password)
                db.session.add(user)
                db.session.commit()
                token =b64encode(bytes(email,'utf-8')).decode('utf-8')
                user.meeting_token=token
                db.session.commit()

        except IntegrityError as e:
            db.session.rollback()
            if 'email' in e.args[0]:
                raise  EmailAlreadyRegistered
            

        return user
    @classmethod
    def signin(cls,email=None,password=None):
        password=md5(password.encode('utf-8')).hexdigest()
        user=cls.query.filter(*[cls.email==email,cls.password==password]).first()
        token=password
        if user is None:
            raise AuthenticationFailure
        return user

    @classmethod
    def authenticate_user(cls,id,secret):
        
        user=cls.query.filter(cls.id==id).filter(cls.password==secret).first()
        if user is None:
            raise AuthenticationFailure
        
        return user
    @classmethod
    def authenticate_user_for_meeting(cls,id,token):
        
        user=cls.query.filter(cls.id==id).filter(cls.meeting_token==token).first()
        if user is None:
            raise AuthenticationFailure
        
        return user

    @classmethod
    def validate_email(cls,email):
        m = email_pattern.search(email)
        if m is None:
            raise UnAcceptableEmail