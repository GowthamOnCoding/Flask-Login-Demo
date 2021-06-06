from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField,SubmitField
from wtforms.validators import InputRequired, Email, Length, ValidationError
from .models import User

class LoginForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(max=20,min=5)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=6,max=80)])
    remember = BooleanField('remember me')

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[InputRequired(),Length(max=20,min=5)])
    email = StringField('email',validators=[InputRequired(),Email(), Length(max=50,min=5)])
    password = PasswordField('password',validators=[InputRequired(),Length(min=6,max=80)])
    #signup = SubmitField('Sign Up')
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken')
