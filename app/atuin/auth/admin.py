# -*- coding: utf-8 -*-
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, session, redirect, url_for

from atuin.auth import login_required, current_user

bp = Blueprint('atuin.auth.admin', __name__)

from models import db, User

@bp.route("/users")
@login_required
def users_index():
	users = User.query.order_by(User.name).all()
	usertypes = User.usertypes_d
	userroles = User.roles_d
	
	return render_template("atuin/auth/admin/users.html", menuid='admin', submenuid='users', users=users, usertypes=usertypes, userroles=userroles)


@bp.route("/users/<int:userid>")
@bp.route("/users/<int:userid>/<links>")
@login_required
def users_get(userid, links=False):
	user = User.query.get_or_404(userid)
	user_d = {
		'id': user.id,
		'usertype': user.usertype,
		'username': user.username,
		'name': user.name,
		'notes': user.notes,
		'role': user.role,
		'email': user.email,
		
		'activeuntil': user.active_until.isoformat() if user.active_until else None,
		'birthday': user.birthday.isoformat() if user.birthday else None,
		'gender': user.gender,
		
		'url_links': url_for('.users_get', userid=user.id, links='links'),
		'url_visibility': url_for('.users_get_visibility', userid=user.id),
	}
	if user.last_login:
		user_d['last_login'] = user.last_login.ctime()
	else:
		user_d['last_login'] = None
	
	if links:
		user_d['linked_users'] = []
		for lu in user.linked_users:
			user_d['linked_users'].append(
				{
					'id': lu.id,
					'username': lu.username,
					'name': lu.name,
					'linked_users_num': len(lu.get_linked_users())
				}
			)
	
	return jsonify(user_d)


@bp.route("/users/<int:userid>/visibility")
@login_required
def users_get_visibility(userid):
	user = User.query.get_or_404(userid)
	
	r = {
		'viewedby': [],
		'views': []
	}
	
	for pu in user.get_parents(10):
		r['viewedby'].append(
			{
				'id': pu.id,
				'username': pu.username,
				'name': pu.name,
			}
		)
	
	for lu in user.get_linked_users(10):
		r['views'].append(
			{
				'id': lu.id,
				'username': lu.username,
				'name': lu.name,
			}
		)
	
	return jsonify(r)


@bp.route("/users/search")
@login_required
def users_search():
	q = request.args['q']
	if len(q) < 3:
		return 'QUERY_TOO_SHORT', 400
	
	users = User.query.filter(User.name.like('%'+q+'%') | User.username.like('%'+q+'%')).limit(12).all()
	result = {
		'count': len(users),
		'results': [
			{
				'id': user.id,
				'usertype': user.usertype,
				'username': user.username,
				'name': user.name,
				'notes': user.notes,
				'role': user.role,
				'email': user.email,
				
				'activeuntil': user.active_until.isoformat() if user.active_until else None,
				'birthday': user.birthday.isoformat() if user.birthday else None,
				'gender': user.gender,
				
				'linked_users_num': len(user.get_linked_users())
			} for user in users
		]
	}
	
	return jsonify(**result)


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
		db.session.add(user)
	
	user.usertype = request.form['usertype']
	user.username = request.form['username']
	user.name = request.form['name']
	user.notes = request.form['notes']
	user.role = request.form['role']
	user.email = request.form['email']
	
	user.gender = request.form['gender']
	
	if ('birthday' in request.form) and (request.form['birthday']):
		user.birthday = datetime.datetime.strptime(request.form['birthday'], '%d/%m/%Y')
	
	if ('activeuntil' in request.form) and (request.form['activeuntil']):
		user.active_until = datetime.datetime.strptime(request.form['activeuntil'], '%d/%m/%Y')
	
	if request.form['password'] != '':
		user.set_password(request.form['password'])
		
	db.session.commit() #TOFIX caso di inserimento di username non univoco (try/except ?)
	
	# public ID based on generated ID
	if not user.public_id:
		user._generate_public_id()
		db.session.commit()
	
	flash(u'User %s saved' % user.username)
	return redirect(url_for('auth.admin.users_index'))

@bp.route("/users/<int:userid>", methods=['DELETE'])
@login_required
def users_delete(userid):
	if (current_user.role != 'ADMIN'):
		return 'Nice try... :D', 403
	
	user = User.query.get_or_404(userid)
	
	db.session.delete(user)
	db.session.commit()
	
	return 'OK'

