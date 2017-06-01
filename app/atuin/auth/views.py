# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import request, redirect, flash, render_template, session
from flask_login import login_user, logout_user
from atuin.auth import login_manager, login_required

bp = Blueprint('atuin.auth', __name__)

from models import db, User
from atuin.logs.models import Log


@login_manager.user_loader
def load_user(id):
	return User.query.get(id)


@bp.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "POST" and "username" in request.form and "password" in request.form:
		u = User.query.filter_by(username=request.form['username']).first()
		if u:
			res = u.check_password(request.form['password'])
			if res:
				# password ok
				if login_user(u):
					u.last_login = datetime.datetime.now()
					db.session.commit()
					Log.log_event('LOGIN', "{} from {}".format(u.username, request.remote_addr))
					return redirect(request.form.get("next") or '/')
				else:
					# error
					Log.log_event('LOGINERROR', "{} from {}".format(u.username, request.remote_addr))
					flash('Login error')
			else:
				# error invalid user/pass
				Log.log_event('LOGIN-PWDERR', "{} from {}".format(u.username, request.remote_addr))
				flash('Unknown username or password')
		else:
			# invalid user
			flash('Unknown username or password')

	return redirect('/')


@bp.route("/logout", methods=['GET'])
@login_required
def logout():
	logout_user()
	session.pop('table_id', None)
	return redirect(request.args.get("next") or '/')


@login_manager.unauthorized_handler
def unauthorized():
	return render_template('auth/unauthorized.html', menuid="login", next=request.args.get("next")), 401
