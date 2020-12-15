from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp, Email, EqualTo, ValidationError

from app.models.user_models import User


class LoginForm(FlaskForm):
    username = StringField('Your username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(3, 80), Regexp('^[A-Za-z0-9_]{3,}$',
                                                                                         message='Usernames consist of numbers, letters and underscore.')])
    password = PasswordField('Password',
                             validators=[DataRequired(), EqualTo('password2', message='Password must match.')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 120), Email()])
    submit = SubmitField('Sign Up')

    @staticmethod
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address')

    @staticmethod
    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is already taken.')

    # validatory muszą się w ten sposób nazywać validate_nazwaformularza(inaczej nie będą działąć)
    # self jest dlatego, że te medoty są wykorzystywane też jako metody obiektu


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Current Password: ', validators=[DataRequired()])
    new_password = PasswordField('New Password: ', validators=[DataRequired()])
    new_password2 = PasswordField('Repeat New Password: ',
                                  validators=[DataRequired(), EqualTo('new_password', message='Passwords must match.')])
    submit = SubmitField('Submit')


class DeleteUserForm(FlaskForm):
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Delete your account')
