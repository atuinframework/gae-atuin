# -*- coding: utf-8 -*-
import datetime
import random
import hashlib
import collections

from passlib.hash import sha256_crypt
from atuin.mailing import send_mail

from atuin.datastore import db, hybrid_property, backref


class classproperty_get(property):

	_get_funct = None

	def __init__(self, get_funct=None, *void):
		self._get_funct = get_funct

	def __get__(self, void=None, cls=None):
		return self._get_funct(cls)

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	public_id = db.Column(db.Integer, index=True)
	usertype = db.Column(db.String(10))
	username = db.Column(db.String(80), unique=True, index=True)
	password = db.Column(db.String(255))
	email = db.Column(db.String(100))
	name = db.Column(db.String(200))
	notes = db.Column(db.Text)
	role = db.Column(db.String(50), index=True)

	birthday = db.Column(db.Date)
	gender = db.Column(db.String(10))

	address_city = db.Column(db.String(255))
	address_zip = db.Column(db.String(10))
	address_country = db.Column(db.String(30))

	otp = db.Column(db.String(255), default=None)
	otp_expire = db.Column(db.DateTime, default=None)

	active_until = db.Column(db.DateTime, default=None, index=True)

	ins_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
	upd_timestamp = db.Column(db.DateTime, default=datetime.datetime.now)

	last_login = db.Column(db.DateTime, default=None)
	
	policy = db.relationship('UserPolicy',
								primaryjoin='User.role==foreign(UserPolicy.role)',
								uselist=False,
								viewonly=True,
								lazy='joined')

	__table_args__ = ( db.Index('ix_otp_expire_otp', 'otp_expire', 'otp'),
						)

	usertypes_d = collections.OrderedDict([
		('staff', "Staff"),
		('customer', "Customer"),
	])

	_roles_d = None

	@classproperty_get
	def roles_d(self):
		if not self._roles_d:
			self._roles_d = dict(UserPolicy.query.with_entities(UserPolicy.role, UserPolicy.desc))
			self._roles_d["ADMIN"] = "Administrator"
			
		return self._roles_d
		

	def __repr__(self):
		return "<User %s %s usertype=%s>" % (self.id, self.username, self.usertype)

	def get_id(self):
		return self.id

	@property
	def is_active(self):
		return True

	@property
	def is_anonymous(self):
		return False

	@property
	def is_authenticated(self):
		return True

	def set_password(self, password):
		pwd = sha256_crypt.encrypt(password)
		self.password = pwd

	def check_password(self, password):
		if sha256_crypt.verify(password, self.password):
			# login ok
			return True

		return False

	def usertype_translated(self):
		return self.usertypes_d.get(self.usertype, self.usertype)

	def role_translated(self):
		return self.roles_d.get(self.role, self.role)

	@property
	def age(self):
		try:
			age = (datetime.date.today() - self.birthday).days / 365.2425
		except:
			age = 0
		return int(age)

	@classmethod
	def check_otp(cls, otp):
		user = cls.query.filter(cls.otp_expire > datetime.datetime.now(), cls.otp == otp).first()
		if user:
			# invalidate it
			user.otp_expire = datetime.datetime.now()

		return user

	def generate_otp(self):
		otp = hashlib.sha256(str(random.randint(99999, 999999))).hexdigest()
		self.otp = otp
		self.otp_expire = datetime.datetime.now() + datetime.timedelta(hours=24)

		return otp

	def send_email(self, subject, message):
		res = send_mail(subject, message, [
			{ 'email': self.username },
		])
		return res

	def _generate_public_id(self):
		self.public_id = int( str(self.id) + str(random.randint(1000, 9999)) )

	def has_function(self, func):
		if self.role == 'ADMIN':
			return True

		if not self.policy:
			return False

		if not hasattr(self, 'functions'):
			self.functions = self.policy.functions.split(',')

		return (func in self.functions)

	def as_dict(self, show=None, hide=None, recurse=None):
		""" Return a dictionary representation of this model.
		"""

		obj_d = {
			'id'				: self.id,
			'public_id'			: self.public_id,
			'usertype'			: self.usertype,
			'username'			: self.username,
			'name'				: self.name,
			'notes'				: self.notes,
			'role'				: self.role,
			'email'				: self.email,
			
			'birthday'			: self.birthday.isoformat() if self.birthday else None,
			'gender'			: self.gender,

			'address_city'		: self.address_city,
			'address_zip'		: self.address_zip,
			'address_country'	: self.address_country,

			'active_until'			: self.active_until.isoformat() if self.active_until else None,
			'last_login'			: self.last_login.isoformat() if self.last_login else None,

			'ins_timestamp'	: self.ins_timestamp.isoformat() if self.ins_timestamp else None,
			'upd_timestamp'	: self.upd_timestamp.isoformat() if self.upd_timestamp else None,
		}

		return obj_d


class UserPolicy(db.Model):
	__tablename__ = 'policies'

	role = db.Column(db.String(50), primary_key=True)
	desc = db.Column(db.String(150))
	functions = db.Column(db.Text)

	def as_dict(self, show=None, hide=None, recurse=None):
		""" Return a dictionary representation of this model.
		"""

		obj_d = {
			'role'				: self.role,
			'functions'			: self.functions,
		}

		return obj_d
