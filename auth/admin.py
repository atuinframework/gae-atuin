# - coding: utf-8 -
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, session, redirect, url_for

from auth import login_required, current_user

bp = Blueprint('auth.admin', __name__)

from models import db, User

@bp.route("/users")
@login_required
def users_index():
	users = User.query.order_by(User.name).all()
	usertypes = User.usertypes_d
	userroles = User.roles_d
	
	return render_template("auth/admin/users.html", menuid='admin', submenuid='users', users=users, usertypes=usertypes, userroles=userroles)


@bp.route("/users/<int:userid>")
@login_required
def users_get(userid):
	user = User.query.get_or_404(userid)
	user_d = {
		'id': user.id,
		'usertype': user.usertype,
		'username': user.username,
		'name': user.name,
		'notes': user.notes,
		'role': user.role,
	}
	if user.last_login:
		user_d['last_login'] = user.last_login.ctime()
	else:
		user_d['last_login'] = None
	
	return jsonify(user_d)


@bp.route("/users/save", methods=['POST'])
@bp.route("/users/<int:userid>", methods=['POST'])
@login_required
def users_save(userid=None):
	if not request.form.get('usertype') or not request.form.get('username') or not request.form.get('role'):
		return 'MISSING_PARAMETERS', 400
	
	if userid:
		#edit user
		user = User.query.get_or_404(userid)
	else:
		#new user
		user = User()
		
	user.usertype = request.form['usertype']
	user.username = request.form['username']
	user.name = request.form['name']
	user.notes = request.form['notes']
	user.role = request.form['role']
	
	if request.form['password'] != '':
		user.set_password(request.form['password'])
		
	db.session.add(user)
	db.session.commit()
	
	flash(u'User %s saved' % user.username)
	return redirect(url_for('auth.admin.users_index'))

@bp.route("/users/<int:userid>", methods=['DELETE'])
@login_required
def users_delete(userid):
	user = User.query.get_or_404(userid)
	db.session.delete(user)
	db.session.commit()
	
	return 'OK'
