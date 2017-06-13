# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, abort

from permission_policies import user_role_polices

from atuin.auth import login_role_required
from models import ndb, User
from forms import UserFormAdmin

bp = Blueprint('atuin.auth.admin', __name__)

@bp.route("/users")
@login_role_required("ADMIN")
def users_index():
	users = User.query().order(User.name).fetch(100)
	usform = UserFormAdmin()

	return render_template("atuin/auth/admin/users.html",
	                       menuid='admin', submenuid='users',
	                       usform=usform,
	                       users=users,
	                       user_role_polices=user_role_polices)

@bp.route("/users/<userkey>")
@login_role_required("ADMIN")
def users_get(userkey):
	user = User.get_by_key(userkey)
	if not user:
		abort(404)
	
	user_d = user.to_dict(exclude=['password', 'logo_image', 'preferences'])
	
	return jsonify(user_d)


@bp.route("/user")
@login_role_required("ADMIN")
def search_user():
	res = []
	search = request.args.get('q', '').strip().lower()

	if search:
		users = User.query().filter(User.name_searchable == search).fetch(30)

		for u in users:
			usr = u.to_dict(include=[
				'name',
				'surname',
				'username',
				'email',
				'logo_image_url'
			])
			usr['key'] = u.get_urlsafe()
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

	user.upd_timestamp = datetime.datetime.now()
	user.email = form.email.data
	user.username = form.username.data
	if form.password.data != '':
		user.set_password(form.password.data)

	user.name = form.name.data
	user.surname = form.surname.data

	user.notes = form.notes.data
	user.role = form.role.data

	user.active = form.active.data

	# TODO what about insertion of repeated usernames?
	user.put()

	flash(u'User %s saved' % user.username)
	user_d = user.to_dict(exclude=['password', 'logo_image'])

	return jsonify(user_d)


@bp.route("/users/<userkey>", methods=['DELETE'])
@login_role_required("ADMIN")
def users_delete(userkey):
	ndb.Key(urlsafe=userkey).delete()
	return 'OK'
