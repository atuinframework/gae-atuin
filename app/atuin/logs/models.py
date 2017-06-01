# -*- coding: utf-8 -*-
import datetime

from atuin.datastore import db
from atuin.datastore.types import JSONEncodedDict

class Log(db.Model):
	__tablename__ = 'logs'
	
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime, default=datetime.datetime.now, index=True)
	
	event_type = db.Column(db.String(30))
	event_title =  db.Column(db.String(255))
	event_data = db.Column(db.Text)
	
	__table_args__ = (		db.Index('ix_timestamp_event_type', 'timestamp', 'event_type'),
								)
	
	@classmethod
	def log_event(cls, ev_type, ev_title, ev_data=''):
		l = cls()
		l.event_type = ev_type
		l.event_title = ev_title
		l.event_data = ev_data
		
		tmp_session = db.create_scoped_session()
		tmp_session.add(l)
		tmp_session.commit()
