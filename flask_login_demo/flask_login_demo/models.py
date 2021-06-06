from flask_login_demo import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String(20),
                         nullable=False,
                         unique=False)
    email = db.Column(db.String(50),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(80),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.username)