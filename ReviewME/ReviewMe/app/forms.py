from flask_wtf import Form
from wtforms import StringField, BooleanField,SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
      username = StringField('username', validators=[DataRequired()])
      password = StringField('password', validators=[DataRequired()])
      submit   = SubmitField('Login')
      remember_me = BooleanField('remember_me', default=False)