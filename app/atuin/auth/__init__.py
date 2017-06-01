# -*- coding: utf-8 -*-
import flask_login as login
setattr(login.AnonymousUserMixin, "username", "GUEST")

login_manager = login.LoginManager()
login_required = login.login_required
current_user = login.current_user