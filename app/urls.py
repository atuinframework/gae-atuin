# -*- coding: utf-8 -*-
# public site imports
import home.views

import atuin.js_translations.views

# admin site imports
import atuin.auth.views, atuin.auth.admin

mounts = [
	('/', home.views),

	# ATUIN
	('/', atuin.auth.views),
	('/admin/auth', atuin.auth.admin),
	('/', atuin.js_translations.views),
]
