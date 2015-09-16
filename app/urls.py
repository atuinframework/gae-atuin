#public site imports
# import section.views / admin
import home.views

#admin & auth
import auth.views, auth.admin
import admin.admin
#import admin.views


mounts = [
	('/', home.views),
	
	('/auth', auth.views),
	
	('/admin', admin.admin),
#	('/admin/auth', auth.admin),
]
