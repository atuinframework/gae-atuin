# - coding: utf-8 -
import datetime
from flask.blueprints import Blueprint
from flask import render_template, jsonify, flash, request, session, redirect, url_for

from auth import login_required, current_user

bp = Blueprint('admin', __name__)

@bp.route("/")
@login_required
def index():
	
	return render_template("admin/index.html", menuid='admin', submenuid='')
