# -*- coding: utf-8 -*-
from flask import Flask, g, request, url_for, session
from werkzeug.routing import BuildError
from flask_caching import Cache
from flask_babel import Babel, get_locale as babel_get_locale
import os
import jinja2
import settings
import version
import languages
import datastore
import auth

app = Flask(__name__)
app.debug = settings.DEBUG
app.secret_key = settings.SECRET_KEY

# DB
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_POOL_RECYCLE'] = 300

# print "DB: {}".format(settings.SQLALCHEMY_DATABASE_URI)

app.config['SQLALCHEMY_ECHO'] = settings.DEBUG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

datastore.db.init_app(app)
# Signal to manage model delete events
# a class needs to have a __commit_delete__ function which will be called after
# a succesful commit of a deletion

@datastore.models_committed.connect_via(app)
def on_models_committed(sender, changes):
	for obj, change in changes:
		if change == 'delete' and hasattr(obj, '__commit_delete__'):
			obj.__commit_delete__()

#Auth
auth.login_manager.setup_app(app)

#Babel
babel = Babel(app)

#Cache
if settings.DEBUG:
	cache = Cache(app, config={'CACHE_TYPE': 'simple'})
else:
	cache = Cache(app, config=settings.CACHE_CONFIG)

def lurl_for(ep, language=None, **kwargs):
	if language:
		# language override
		# try the url with *language*, then without
		# index_it variation
		try:
			return url_for(ep[:-2]+language, **kwargs)
		except Exception:
			pass
		# index variation
		try:
			return url_for(ep+'_'+language, **kwargs)
		except BuildError:
			return url_for(ep, **kwargs)
	
	# no override, current language
	try:
		return url_for(ep+'_'+g.language, **kwargs)
	except BuildError:
		try:
			return url_for(ep+'_'+settings.MULTILANGUAGE_LANGS[0], **kwargs)
		except BuildError:
			return url_for(ep, **kwargs)
	

@app.before_request
def func():
	g.cache = cache
	try:
	  g.sentry = sentry
	except:
	  pass
	
	if settings.MULTILANGUAGE:
		g.babel = babel
		g.available_languages = settings.MULTILANGUAGE_LANGS
		g.language = babel_get_locale().language
		g.languages = languages.lang_title
		g.lurl_for = lurl_for
	else:
		g.lurl_for = url_for

if settings.MULTILANGUAGE:
	@babel.localeselector
	def get_locale():
		# lang in path
		lang = request.path[1:].split('/', 1)[0]
		if lang in settings.MULTILANGUAGE_LANGS:
			sessionlang = session.get('lang')
			if sessionlang != lang:
				session['lang'] = lang
			return lang

		# lang in session
		if 'lang' in session:
			if session['lang'] in settings.MULTILANGUAGE_LANGS:
				return session['lang']
			
		# last-resort: lang in accept-language header
		if request.accept_languages:
			lang = request.accept_languages[0][0].split('-')[0]
			if lang in settings.MULTILANGUAGE_LANGS:
				return lang

		# default lang
		return settings.MULTILANGUAGE_LANGS[0]
	
# Jinja related

@app.context_processor
def inject_custom():
	d = {
			'SITE_TITLE': settings.SITE_TITLE,
			'SITE_VERSION': version.string,
			'SITE_VERSION_DATE': version.date_string,
			'SITE_VERSION_FULL': version.full_string,
			'lurl_for': g.lurl_for,
			'languages': languages,		}
	return d

# Mount points

for (mount_position, mount_module) in settings.mounts:
	app.register_blueprint(mount_module.bp, url_prefix=mount_position)
	
if settings.NEWRELIC:
	try:
		import newrelic.agent
		newrelic.agent.initialize(settings.NEWRELIC_CONFIG)
		app2 = newrelic.agent.wsgi_application()(app)
		#monkey patching
		app2.run = app.run
		app2.test_request_context = app.test_request_context
		app = app2
	except:
		pass
	
if settings.SENTRY_DSN:
	from raven.contrib.flask import Sentry
	app.config['SENTRY_DSN'] = settings.SENTRY_DSN
	sentry = Sentry(app)

# if settings.S3_ACCESS_KEY_ID:
# 	app.config['S3_ACCESS_KEY_ID'] = settings.S3_ACCESS_KEY_ID
# 	app.config['S3_SECRET_ACCESS_KEY'] = settings.S3_SECRET_ACCESS_KEY
# 	app.config['S3_REGION_NAME'] = settings.S3_REGION_NAME
