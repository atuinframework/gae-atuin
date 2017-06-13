# -*- coding: utf-8 -*-
# public site imports
import home.views

import js_translations.views

# admin site imports
import atuin.auth.views, atuin.auth.admin
import admin.admin

mounts = [
	('/', home.views),
	
	('/', atuin.auth.views),
	
	('/admin', admin.admin),
	('/admin/auth', atuin.auth.admin),
	
	('/', js_translations.views),
]

