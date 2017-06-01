# -*- coding: utf-8 -*-
# Settings file
# Why this file works like this?
# When updating the application, it should ensure the application will run without updating config.py
# each new features should have a default here

# basic configuration - these MUST BE present
import config
import datastore

DEBUG = config.DEBUG
SECRET_KEY = config.SECRET_KEY
SITE_TITLE = config.SITE_TITLE

try:
	SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
except AttributeError:
	SQLALCHEMY_DATABASE_URI = datastore.settings.SQLALCHEMY_DATABASE_URI

try:
	MULTILANGUAGE = config.MULTILANGUAGE
	MULTILANGUAGE_LANGS = config.MULTILANGUAGE_LANGS
except AttributeError:
	MULTILANGUAGE = False

try:
	NEWRELIC = config.NEWRELIC
	NEWRELIC_CONFIG = config.NEWRELIC_CONFIG
except AttributeError:
	NEWRELIC = False
	NEWRELIC_CONFIG = ''
	
try:
	CACHE_CONFIG = config.CACHE_CONFIG
except AttributeError:
	CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
	
try:
	SENTRY_DSN = config.SENTRY_DSN
except AttributeError:
	SENTRY_DSN = False

try:
	S3_ACCESS_KEY_ID = config.S3_ACCESS_KEY_ID
	S3_SECRET_ACCESS_KEY = config.S3_SECRET_ACCESS_KEY
	S3_REGION_NAME = config.S3_REGION_NAME
	S3_BUCKET_NAME = config.S3_BUCKET_NAME
except AttributeError:
	S3_ACCESS_KEY_ID = None
	S3_SECRET_ACCESS_KEY = None
	S3_REGION_NAME = None
	S3_BUCKET_NAME = None


# apps mounts MUST BE present
from urls import mounts

