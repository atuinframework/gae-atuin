# -*- coding: utf-8 -*-
import datetime
import random
import collections

from passlib.hash import sha256_crypt
import hashlib
from flask_babel import lazy_gettext

from google.appengine.ext import ndb, blobstore
from google.appengine.api import images as gapi_images
from utils import update_searchable_set

class User(ndb.Model):
	
	auth_ids = ndb.StringProperty('ai', repeated=True)
	
	email = ndb.StringProperty('em', required=False, indexed=True, default='')
	username = ndb.StringProperty('un', required=True, indexed=True, default='')
	password = ndb.StringProperty('pwd', indexed=False)
	
	prefix = ndb.StringProperty('px', indexed=False, default='')
	name = ndb.StringProperty('n', indexed=True, default='')
	surname = ndb.StringProperty('s', indexed=True, default='')
	
	logo_image = ndb.BlobKeyProperty('li', indexed=False)
	logo_image_url = ndb.StringProperty('liu', indexed=False)
	
	preferences = ndb.PickleProperty('p')
	notes = ndb.StringProperty(indexed=False)
	role = ndb.StringProperty()
	active = ndb.BooleanProperty('ac', default=False)
	
	otp = ndb.StringProperty('o', default='', indexed=True)
	otp_expire = ndb.DateTimeProperty('o_e', auto_now_add=True, indexed=False)
	
	name_searchable = ndb.StringProperty('ns', repeated=True)

	ins_timestamp = ndb.DateTimeProperty('i_ts', auto_now_add=True, indexed=False)
	upd_timestamp = ndb.DateTimeProperty('u_ts', auto_now_add=True, indexed=False)
	
	last_login = ndb.DateTimeProperty('ll', auto_now_add=True)
	
	roles_d = collections.OrderedDict([
		('ADMIN', "Administrator"),
		('USER', "Normal User"),
	])
	
	prefixes_d = collections.OrderedDict([
		('', ''),
		('MR', lazy_gettext('Mr.')),
		('MRS', lazy_gettext('Mrs.')),
	])
	
	def __repr__(self):
		return "<User %s %s role=%s>" % (self.key, self.username, self.role)
	
	def get_id(self):
		return self.key.id()
	
	@classmethod
	def get_by_key(cls, k):
		return ndb.Key(urlsafe=k).get()
	
	@classmethod
	def get_by_otp(cls, otp):
		otp = otp.strip()
		if otp:
			c = cls.query(cls.otp == otp).get()
			if c:
				if datetime.datetime.now() < c.otp_expire:
					return c
	
	@property
	def is_active(self):
		return self.active
	
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
			#login ok
			return True
		
		return False
	
	def generate_otp(self):
		otp = hashlib.sha256(str(random.randint(99999, 999999))).hexdigest()
		self.otp = otp
		self.otp_expire = datetime.datetime.now() + datetime.timedelta(hours=24)
		
		return otp

	def has_function(self, function):
		# TODO @xcash implement this
		return True
	
	def role_translated(self):
		return self.roles_d.get(self.role)
	
	@property
	def friendly_name(self):
		return "{} {}".format(self.name, self.surname)
	
	def set_logo_image(self, blob):
		"""
		Sets logo_image and logo_image_url
		 - blob - uploaded blobstore
		"""
		
		bk = blob.key()
		
		if self.logo_image:
			old_blob = blobstore.get(self.logo_image)
			if old_blob:
				old_blob.delete()
			
		self.logo_image = bk
		self.logo_image_url = gapi_images.get_serving_url(bk, secure_url=True)

	def _pre_put_hook(self):
		ns = set()
		ns = update_searchable_set(ns, self.name)
		ns = update_searchable_set(ns, self.surname)
		ns.add(self.username)

		self.name_searchable = list(ns)
		


	
	
#class UserSession(db.Model):
#	id = db.Column(db.Integer, primary_key=True)
#	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#	
#	#session info
#	ip = db.Column(db.String)
#	user_agent = db.Column(db.String)
#	
#	#expiring info	
#	created = db.Column(db.DateTime, default=datetime.datetime.now)
#	expires_on = db.Column(db.DateTime, default=datetime.datetime.now)
#	
#	def __repr__(self):
#		return "<UserSession %s for user %s expires on >" % (self.id, self.user_id, self.expires_on)

