# -*- coding: utf-8 -*-
# public site imports
import home.views

import js_translations.views

# admin site imports
import auth.views, auth.admin
import admin.admin

mounts = [
	('/', home.views),
	
	('/auth', auth.views),
	
	('/admin', admin.admin),
	('/admin/auth', auth.admin),
	
	('/', js_translations.views),
]
