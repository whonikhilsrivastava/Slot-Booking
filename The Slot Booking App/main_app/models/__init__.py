
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from main_app.models.user import User
from main_app.models.time_slot import TimeSlot
from main_app.models.meeting import Meeting
