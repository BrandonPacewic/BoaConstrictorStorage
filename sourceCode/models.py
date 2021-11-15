from . import db
from flask_login import UserMixin

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)



class userBoa(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    boa_inital = db.Column(db.String(30), unique = True)
    boa_color = db.Column(db.String(30))
    boa_size = db.Column(db.String(30))
    boa_sequence = db.Column(db.String(30), unique = True)
