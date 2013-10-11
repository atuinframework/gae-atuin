# Settings file
# Why this file works like this?
# When updating the application, it should ensure the application will run without updating config.py
# each new features should have a default here

# basic configuration - these MUST BE present
import config

DEBUG = config.DEBUG
SECRET_KEY = config.SECRET_KEY
SITE_TITLE = config.SITE_TITLE

try:
	MULTILANGUAGE = config.MULTILANGUAGE
	MULTILANGUAGE_LANGS = config.MULTILANGUAGE_LANGS
except Exception:
	MULTILANGUAGE = False

try:
	NEWRELIC = config.NEWRELIC
	NEWRELIC_CONFIG = config.NEWRELIC_CONFIG
except Exception:
	NEWRELIC = False
	NEWRELIC_CONFIG = ''
	
try:
	CACHE_CONFIG = config.CACHE_CONFIG
except Exception:
	CACHE_CONFIG = {'CACHE_TYPE': 'simple'}
	
try:
	SENTRY_DSN = config.SENTRY_DSN
except Exception:
	SENTRY_DSN = False

# apps mounts MUST BE present
from urls import mounts

