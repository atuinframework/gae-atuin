import datetime
import random
import hashlib
import collections

from google.appengine.ext import ndb

class User(ndb.Model):
	
	username = ndb.StringProperty(required=True)
	password = ndb.StringProperty(indexed=False)
	
	name = ndb.StringProperty()
	
	notes = ndb.StringProperty(indexed=False)
	roles = ndb.StringProperty(repeated=True)
	
	ins_timestamp = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
	upd_timestamp = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
	
	last_login = ndb.DateTimeProperty(auto_now_add=True)
	
	roles_d = collections.OrderedDict([
		('ADMIN', "Administrator"),
		('CUSTOMER', "Customer"),
	])
	
	def __repr__(self):
		return "<User %s %s usertype=%s>" % (self.id, self.username, self.usertype)
	
	def get_id(self):
		return self.id
	
	def is_active(self):
		return True
	
	def is_anonymous(self):
		return False
	
	def is_authenticated(self):
		return True
	
	def __pwd(self, password, salt=None):
		if not salt:
			salt = ''
			for x in xrange(random.randint(6, 10)):
				salt += chr(random.randint(ord('0'), ord('z')))
			
		hashed = hashlib.sha256(salt + password).hexdigest()
		pwd = '$$'.join((salt, hashed))
		return pwd
	
	def set_password(self, password):
		pwd = self.__pwd(password)
		self.password = pwd
		
	def check_password(self, password):
		salt = self.password.split('$$')[0]
		pwd = self.__pwd(password, salt)
		
		if pwd == self.password:
			#login ok
			return True
		
		return False
		
	def usertype_translated(self):
		return self.usertypes_d.get(self.usertype, self.usertype)
		
	def role_translated(self):
		return self.roles_d.get(self.role, self.role)
	
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

