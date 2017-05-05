# -*- coding: utf-8 -*-
import time
from flask.blueprints import Blueprint
from flask import render_template, make_response

bp = Blueprint('js_translations', __name__)

@bp.route(u'it/js_translations.js', endpoint='index_it')
@bp.route(u'en/js_translations.js', endpoint='index_en')
@bp.route(u'de/js_translations.js', endpoint='index_de')
@bp.route(u'fr/js_translations.js', endpoint='index_fr')
@bp.route(u'es/js_translations.js', endpoint='index_es')
def index():
	resp = make_response(render_template('js_translations/base.js'))
	resp.headers['Content-Type'] = 'application/javascript'
	resp.cache_control.max_age = 60*60
	resp.expires = int(time.time() + 60*60)
	
	return resp
