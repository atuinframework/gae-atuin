# -*- coding: utf-8 -*-
from flask.blueprints import Blueprint
from flask import render_template

bp = Blueprint('home', __name__)

@bp.route("/")
def index():
	return render_template("home/index.html")
