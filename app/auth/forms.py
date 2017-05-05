# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, BooleanField, DateTimeField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired

from models import User


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
	role = SelectField(choices=list(User.roles_d.iteritems()), validators=[DataRequired()])
	
	active = BooleanField()
	
	ins_timestamp = DateTimeField()
	upd_timestamp = DateTimeField()
	
	last_login = DateTimeField()
