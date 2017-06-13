# -*- coding: utf-8 -*-
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
except AttributeError:
	MULTILANGUAGE = False

try:
	CACHE_CONFIG = config.CACHE_CONFIG
except AttributeError:
	CACHE_CONFIG = {'CACHE_TYPE': 'simple'}

try:
	FORCE_HTTPS = config.FORCE_HTTPS
except AttributeError:
	FORCE_HTTPS = False

# apps mounts MUST BE present
from urls import mounts
