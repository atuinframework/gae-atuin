# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, session, redirect, url_for, abort

from auth import login_required, login_role_required, current_user

bp = Blueprint('auth.admin', __name__)

from models import ndb, User

from forms import UserFormAdmin

@bp.route("/users")
@login_role_required("ADMIN")
def users_index():
	user_list = User.query().order(User.name)
	userroles = User.roles_d
	umform = UserFormAdmin()
	
	return render_template("auth/admin/users.html", menuid='users', user_list=user_list, umform=umform, userroles=userroles)


@bp.route("/users/<userkey>")
@login_role_required("ADMIN")
def users_get(userkey):
	user = User.get_by_key(userkey)
	if not user:
		abort(404)
	
	user_d = user.to_dict(exclude=['password', 'logo_image'])
	
	return jsonify(user_d)


@bp.route("/user")
@login_role_required("ADMIN")
def search_user():
	res = []

	search = request.args.get('q', '').strip().lower()

	if search:
		users = User.query().filter(User.name_searchable == search).fetch(30)

		for u in users:
			usr = {}
			usr['id'] = u.key.urlsafe()
			usr['name'] = u.name
			usr['surname'] = u.surname
			usr['username'] = u.username
			usr['email'] = u.email
			usr['logo_image_url'] = u.logo_image_url
			res.append(usr)

	return jsonify(results=res)


@bp.route("/users/", methods=['POST'])
@bp.route("/users/<userkey>", methods=['POST'])
@login_role_required("ADMIN")
def users_save(userkey=None):
	# form validation
	form = UserFormAdmin()
	if not form.validate_on_submit():
		return "VALIDATION_ERROR", 400

	if userkey:
		#edit user
		user = User.get_by_key(userkey)
		if not user:
			abort(404)
	else:
		#new user
		user = User()
		user.ins_timestamp = datetime.datetime.now()

	user.email = form.email.data
	user.username = form.username.data
	if form.password.data != '':
		user.set_password(form.password.data)
	user.name = form.name.data
	user.surname = form.surname.data
	user.notes = form.notes.data
	user.role = form.role.data
	user.active = form.active.data
	user.upd_timestamp = form.upd_timestamp.data

	user.put()

	flash(u'User %s saved' % user.username)
	user_d = user.to_dict(exclude=['password', 'logo_image'])

	return jsonify(user_d)


@bp.route("/users/<userkey>", methods=['DELETE'])
@login_role_required("ADMIN")
def users_delete(userkey):
	ndb.Key(urlsafe=userkey).delete()
	return 'OK'
