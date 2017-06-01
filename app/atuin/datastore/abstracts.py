# -*- coding: utf-8 -*-
import datetime
import random
import hashlib
import collections
import copy

from passlib.hash import sha256_crypt
from mailing import send_mail

from sqlalchemy.orm.session import make_transient
from sqlalchemy.ext.declarative import declared_attr

from datastore import db, hybrid_property, backref
from datastore.types import JSONEncodedDict


class BaseModelCommonFields(db.Model):
	__abstract__ = True
	
	id = db.Column(db.Integer, primary_key=True)
	
	ins_username = db.Column(db.String(30))
	ins_address = db.Column(db.String(50))
	ins_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)

	upd_username = db.Column(db.String(30))
	upd_address = db.Column(db.String(50))
	upd_timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
	
	__table_args__ = (		#db.Index('ix_otp_expire_otp', 'otp_expire', 'otp'),
		
							)
	def __repr__(self):
		return "<BaseCommonFields {}>".format(self.id)
	
	def detach(self):
		return make_transient(self)

	def as_dict(self, show=None, hide=None, recurse=None):
		""" Return a dictionary representation of this model.
		"""
		
		obj_d = {
			'id'			: self.id,

			'ins_username'	: self.ins_username,
			'ins_address'	: self.ins_address,
			'ins_timestamp'	: self.ins_timestamp.isoformat() if self.ins_timestamp else None,

			'upd_username'	: self.upd_username,
			'upd_address'	: self.upd_address,
			'upd_timestamp'	: self.upd_timestamp.isoformat() if self.upd_timestamp else None,
		}
		
		return obj_d



	def log_user(self, username, address=""):
		address = address or ""
		
		if not self.ins_username:
			self.ins_username = username
		
		if not self.ins_address:
			self.ins_address = address

		self.upd_username = username
		self.upd_address = address
		
		self.log_timestamp()
		
		return self


	def log_timestamp(self):
		if self.upd_timestamp:
			self.upd_timestamp = datetime.datetime.now()
		
		return self


	def set_user(self, req, user):
		
		return self.log_user(user.username, req.remote_addr)
	
	#omnisearch methods
	__search_fields__ = ("id",)

	@classmethod
	def omnisearch(cls, txt):
		"""
			Search every field defined in __search_fields__ who got 'txt' inside.
			Returns query object with such elements
		"""
		txt_like = "%{}%".format(txt)

		args = [getattr(cls, f).like(txt_like) for f in cls.__search_fields__]
		
		return cls.query.filter(db.or_(*args))
	
	@property
	def is_omnisearched(self, txt):
		
		txt_lower = txt.lower()
		
		return any(txt_lower in getattr(cls, f).lower() for f in self.__search_fields__)
		

	@classmethod
	def add_new(cls, *args, **kwargs):
		kw = kwargs.copy()
		db_session = kw.pop("db_session", None) or db.session

		item = cls(*args, **kw)

		db_session.add(item)

		return item

	@classmethod
	def find_or_create(cls, *args, **kwargs):
		
		kw = kwargs.copy()
		db_session = kw.pop("db_session", None)
		add_new = kw.pop("add_new", None)
		
		item = cls.query.filter_by(*args, **kw).first()

		if not item:
			if add_new or db_session:
				kw["db_session"] = db_session
				return cls.add_new(*args, **kw)
			else:
				item = cls(*args, **kwargs)
			
		return item
	

	@property
	def serialized_id(self):
		return "{}:{}".format(self.__class__.__name__, self.id)


	@classmethod
	def get_from_serialized(cls, serial_id):
		(cls_name, cls_id) = serial_id.split(":")[:2]

		if cls_name != cls.__name__:
			raise Exception("MODEL INTEGRITY ERROR: Serial id not valid")
		
		return cls.query.get(cls_id)


class StatusCommonField(object):

	status_values = (
		("INSERT", "Inserito"),
		("ACTIVE", "Attivo"),
		("DISABLED", "Non attivo"),
		("DELETED", "Rimosso"),
	)

	_status_d = None

	@declared_attr
	def status(cls):
		return db.Column(db.String(20), index=True, default="INSERT")

	@property
	def status_desc(self):
		""" Returns description of status value"""

		if self._status_d is None:
			self._status_d = dict(self.status_values)

		return self._status_d.get(self.status, self.status)
