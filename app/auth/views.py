from flask.blueprints import Blueprint
from flask import request, redirect, flash, render_template, session
from auth import login_manager, login_required
from flask.ext.login import login_user, logout_user
from google.appengine.api import users as gae_users

import datetime

bp = Blueprint('auth', __name__)

from models import User

@login_manager.user_loader
def load_user(id):
	return User.get_by_id(id)


@bp.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "POST" and "username" in request.form and "password" in request.form:
		u = User.query.filter_by(username = request.form['username']).first()
		if u:
			res = u.check_password(request.form['password'])
			if res:
				#password ok
				if login_user(u):
					u.last_login = datetime.datetime.now()
					db.session.commit()
					return redirect(request.form.get("next") or '/')
				else:
					#error
					flash('Login error')
			else:
				#error invalid user/pass
				flash('Unknown username or password')
		else:
			#invalid user
			flash('Unknown username or password')
	
	return render_template('auth/loginpage.html', menuid="login", next=request.args.get("next"))

@bp.route("/logout", methods=['GET'])
@login_required
def logout():
	logout_user()
	session.pop('table_id', None)
	return redirect(request.args.get("next") or '/')

@bp.route("/external/google")
def external_login_google():
	gae_current_user = gae_users.get_current_user()
	if gae_current_user:
		# Google AppEngine Logged in user
		# * check if there's a corresponding local user
		auth_id = 'google_' + gae_current_user.user_id()
		user = User.query(User.auth_ids == auth_id).get()
		if not user:
			# not present - let's create it
			print "!!! CREATE USER !!!"
			user = User()
			user.username = gae_current_user.email()
			user.name = gae_current_user.nickname()
			user.auth_ids.append(auth_id)
			user.roles.append('USER')
			user.put()
		
		if login_user(user):
			user.last_login = datetime.datetime.now()
			user.put()
			return redirect('/')
		
	
	flash('Login error')
	return render_template('auth/loginpage.html', menuid="login")

@login_manager.unauthorized_handler
def unauthorized():
	return render_template('auth/unauthorized.html', menuid="login", next=request.args.get("next")), 401


