# -*- coding: utf-8 -*-
import os

class Config(object):
    DEBUG=True
   
    


class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "postgres://uf54hnqr1b2g67:p6c2vrn9q7oqtd947n6frgrcguh@ec2-54-243-188-17.compute-1.amazonaws.com:5922/dcnft6j1pljtlb"
    '''_POSTGRES = {
        'host': 'localhost',
        'user': 'postgres',
        'password': 'postgres',
        'database': 'testing',
        'port_number': 5432
    }
   
    # SQLALCHEMY_DATABASE_URI = "postgres://uf54hnqr1b2g67:p6c2vrn9q7oqtd947n6frgrcguh@ec2-54-243-188-17.compute-1.amazonaws.com:5922/dcnft6j1pljtlb"
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(password)s@%(host)s:%(port_number)s/%(database)s' % _POSTGRES
    '''
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    URL ='https://calender-meetings.herokuapp.com//'


