# Configuration template file. Copy it to config.py

# True to print all queries and autoreload
DEBUG = True

# change for each installation
SECRET_KEY = 'somerandom-;:=()=yty'

# site title
SITE_TITLE = "AWESOMESITE"

# multilanguage support
MULTILANGUAGE = True
MULTILANGUAGE_LANGS = ['en', 'it']

# considered only in production (DEBUG False)
#CACHE_CONFIG = {'CACHE_TYPE': 'memcached'}
CACHE_CONFIG = {'CACHE_TYPE': 'simple'}

# whether to use newrelic (autodiscovery mode)
NEWRELIC = False
NEWRELIC_CONFIG = "newrelic.ini"

# whether to use sentry
SENTRY_DSN = False