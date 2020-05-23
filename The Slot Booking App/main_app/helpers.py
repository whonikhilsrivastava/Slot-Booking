
import json
from base64 import b64encode
from hashlib import md5

from flask_restful import fields
from flask import Flask, request,url_for, redirect, render_template
import os
from main_app import app
import math
import random
import re

def convert(resp):
        return json.loads(resp.decode('utf-8'))


def basic_auth(id,password):
    if not isinstance(id,str):
        id=str(id)
    return "Basic "+b64encode(bytes(id+':'+password,'utf-8')).decode('utf-8')
    
def int_array_split(string):
        if isinstance(string, str):
                lst=string.split(',')
        try:
                return list(map(int,lst))
        except:
                raise ValueError('not int type in list of integers')





