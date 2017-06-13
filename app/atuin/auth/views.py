# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import request, redirect, flash, render_template, g, session
from flask_babel import _
from atuin.auth import login_manager, login_required
from flask_login import login_user, logout_user
from google.appengine.api import users as gae_users

bp = Blueprint('atuin.auth', __name__)

from models import User
from forms import LoginForm
from atuin.logs.models import Log

@login_manager.user_loader
def load_user(id):
	u = User.get_by_id(id)
	if u and u.active:
		return u


@bp.route("auth/login", methods=['GET', 'POST'])
@bp.route("en/auth/login", methods=['GET', 'POST'], endpoint='login_en')
def login():
	login_form = LoginForm()
	if login_form.validate_on_submit():
		u = User.query(User.username == login_form.username.data).get()
		if u and u.active:
			res = u.check_password(login_form.password.data)
			if res:
				# password ok
				if login_user(u):
					u.last_login = datetime.datetime.now()
					u.put()
					Log.log_event('LOGIN', "{} from {}".format(u.username, request.remote_addr))
					return redirect(request.form.get("next") or '/')
				else:
					# error
					flash(_('Login error'))
					Log.log_event('LOGIN_ERROR', "{} from {}".format(u.username, request.remote_addr))
			else:
				# error invalid user/pass
				Log.log_event('LOGIN_PWDERR', "{} from {}".format(u.username, request.remote_addr))
				flash(_('Unknown username or password'))
		else:
			# invalid user
			Log.log_event('LOGIN_PWDERR', "{} from {}".format(u.username, request.remote_addr))
			flash(_('Unknown username or password'))
	
	return render_template('auth/loginpage.html', menuid="login", loginform=login_form, next=request.args.get("next"))


@bp.route("auth/logout", methods=['GET'])
@bp.route("en/auth/logout", methods=['GET'], endpoint='logout_en')
@login_required
def logout():
	logout_user()
	return redirect(request.args.get("next") or '/')


@bp.route("auth/external/google")
@bp.route("en/auth/external/google", endpoint='external_login_google_en')
def external_login_google():
	gae_current_user = gae_users.get_current_user()
	if gae_current_user:
		# Google AppEngine Logged in user
		# * check if there's a corresponding local user
		auth_id = 'google_' + gae_current_user.user_id()
		user = User.query(User.auth_ids == auth_id).get()
			
		if not user:
			# not present by social id. let's try by email
			user = User.query(User.username == gae_current_user.email()).get()
			if not user:
				# not present - let's create it
				# print "!!! CREATE USER !!!"
				user = User()
				user.username = gae_current_user.email()
				user.name = gae_current_user.nickname()
			
			user.auth_ids.append(auth_id)
			if gae_users.is_current_user_admin():
				user.role = 'ADMIN'
			else:
				user.role = 'USER'
			user.active = True
			user.put()
		
		if login_user(user):
			user.last_login = datetime.datetime.now()
			user.put()
			return redirect(g.lurl_for('home.index'))
		
	
	flash('Login error')
	return render_template('auth/loginpage.html', menuid="login")

@login_manager.unauthorized_handler
def unauthorized():
	return render_template('auth/unauthorized.html', menuid="login", next=request.args.get("next")), 401
