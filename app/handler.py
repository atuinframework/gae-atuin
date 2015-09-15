import os, sys

sys.path.insert(1, os.path.join(os.path.abspath('.'), 'lib'))

from flask import Flask, g, request, url_for
from werkzeug.routing import BuildError
#from flask.ext.cache import Cache
from flask.ext.babel import Babel, get_locale as babel_get_locale

import settings
import auth

app = Flask(__name__)
app.debug = settings.DEBUG
app.secret_key = settings.SECRET_KEY

#Auth
auth.login_manager.setup_app(app)

#Babel
babel = Babel(app)

#Cache
# if settings.DEBUG:
# 	cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# else:
# 	cache = Cache(app, config=settings.CACHE_CONFIG)

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
		except Exception:
			return url_for(ep, **kwargs)
	
	# no override, current language
	try:
		return url_for(ep+'_'+g.language, **kwargs)
	except BuildError:
		return url_for(ep, **kwargs)
	

@app.before_request
def func():
	#g.cache = cache
	
	if settings.MULTILANGUAGE:
		g.babel = babel
		g.available_languages = settings.MULTILANGUAGE_LANGS
		g.language = babel_get_locale().language
		g.lurl_for = lurl_for
	else:
		g.lurl_for = url_for

if settings.MULTILANGUAGE:
	@babel.localeselector
	def get_locale():
		# lang in path
		lang = request.path[1:].split('/', 1)[0]
		if lang in settings.MULTILANGUAGE_LANGS:
			return lang

		#lang in accept-language header
		if request.accept_languages:
			lang = request.accept_languages[0][0].split('-')[0]
			if lang in settings.MULTILANGUAGE_LANGS:
				return lang

		# default lang
		return settings.MULTILANGUAGE_LANGS[0]
	

@app.context_processor
def inject_custom():
	d = {
			'SITE_TITLE': settings.SITE_TITLE,
			'lurl_for': g.lurl_for,
			'users': auth.users,
			'current_user': auth.current_user,
		}
	return d

for (mount_position, mount_module) in settings.mounts:
	app.register_blueprint(mount_module.bp, url_prefix=mount_position)
	
