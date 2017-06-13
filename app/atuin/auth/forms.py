# -*- coding: utf-8 -*-
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, DateTimeField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired

from models import User
from permission_policies import user_roles

class LoginForm(FlaskForm):
	username = StringField(validators=[DataRequired()])
	password = PasswordField(validators=[DataRequired()])
	

class UserFormAdmin(FlaskForm):
	email = StringField()
	username = StringField(validators=[DataRequired()])
	password = PasswordField()

	name = StringField(validators=[DataRequired()])
	surname = StringField(validators=[DataRequired()])
	
	notes = TextAreaField()
	role = SelectField(choices=user_roles, validators=[DataRequired()])
	
	active = BooleanField()
	
	ins_timestamp = DateTimeField()
	upd_timestamp = DateTimeField(datetime.now())
	
	last_login = DateTimeField()
