import datetime
import random
import collections

from passlib.hash import sha256_crypt

from google.appengine.ext import ndb

class User(ndb.Model):
	
	auth_ids = ndb.StringProperty(repeated=True)
	
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(indexed=False)
	
	name = ndb.StringProperty()
	
	notes = ndb.StringProperty(indexed=False)
	roles = ndb.StringProperty(repeated=True)
	
	active = ndb.BooleanProperty(default=True)
	
	ins_timestamp = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
	upd_timestamp = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
	
	last_login = ndb.DateTimeProperty(auto_now_add=True)
	
	roles_d = collections.OrderedDict([
		('ADMIN', "Administrator"),
		('USER', "Normal User"),
	])
	
	def __repr__(self):
		return "<User %s %s roles=%s>" % (self.key, self.username, self.roles)
	
	def get_id(self):
		return self.key.id()
	
	def is_active(self):
		return self.active
	
	def is_anonymous(self):
		return False
	
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
		
	def roles_translated(self):
		return [(role, self.roles_d.get(role, role)) for role in self.roles]
	
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

