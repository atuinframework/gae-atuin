#public site imports
import home.views

#admin & auth
import auth.views, auth.admin
import admin.views


mounts = [
	('/', home.views),
	
	('/auth', auth.views),
	
	('/admin', admin.views),
	('/admin/auth', auth.admin),


]
