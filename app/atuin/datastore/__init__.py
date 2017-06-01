# -*- coding: utf-8 -*-
#db utilities
from flask_sqlalchemy import SQLAlchemy, models_committed, BaseQuery

db = SQLAlchemy(session_options={"query_cls": BaseQuery})

from sqlalchemy import event
from sqlalchemy.orm.attributes import NO_VALUE, NEVER_SET
from sqlalchemy.ext.hybrid import *
from sqlalchemy.orm import backref

def create_tables(db_handler, *tables):
	"""
		Creates all the tables from their models.
		Needs the db_handler as first parameter, and all the models thereafter
		Returns a tuple of models used	
	"""
	for t in tables:
		t.__table__.create(db_handler.engine, checkfirst=True)

	return tables


def drop_tables(db_handler, *tables):
	"""
		drop all the tables from their models.
		Needs the db_handler as first parameter, and all the models thereafter
		Returns a tuple of models used	
	"""
	for t in tables:
		t.__table__.drop(db_handler.engine, checkfirst=True)

	return tables


#Mokey patching to permit:
#	db.create_tables(Model1, Model2, ...)
#	db.drop_tables(Model1, Model2, ...)
db.create_tables = create_tables
db.drop_tables = drop_tables
