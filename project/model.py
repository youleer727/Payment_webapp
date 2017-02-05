
import datetime
from project import db


class User(db.Model):

    __tablename__ = "user_passowrd"

    id = db.Column(db.Integer, autoincrement=True)
    username = db.Column(db.String(255), primary_key=True)
    password = db.Column(db.String(255), nullable=False)


    def __init__(self, username, password, admin=False):
        self.username = username
        self.password = password
    

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {0}>'.format(self.username)
