# -*- coding: utf-8 -*-
# Configuration template file. Copy it to config.py

# True to print all queries and autoreload
DEBUG = True

# change for each installation
SECRET_KEY = 'somerandom-;:=()=yty'

# site title
SITE_TITLE = "GAE-ATUIN"

# multilanguage support
MULTILANGUAGE = False
MULTILANGUAGE_LANGS = ['en'] # , 'es', 'it']

# considered only in production (DEBUG False)
CACHE_CONFIG = {'CACHE_TYPE': 'gaememcached'}

# HTTPS
FORCE_HTTPS = True
