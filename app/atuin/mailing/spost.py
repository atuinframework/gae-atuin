# -*- coding: utf-8 -*-
# from sparkpost import SparkPost
# 
# from logs.models import Log
# 
# SPARKPOST_API_KEY = '---'
# 
# DEBUG = False
# def send_mail(subject, message, tolist, cclist=[], bcclist=[], tags=[], track_clicks=False, track_opens=False):
# 	sp = SparkPost(SPARKPOST_API_KEY)
# 	Log.log_event('MAIL', 'To: {} - Subj: {}'.format(','.join(tolist), subject))
# 
# 	if DEBUG:
# 		return True
# 	else:
# 		r = sp.transmissions.send(
# 			recipients=tolist,
# 			html=message,
# 			from_email='Atuin <info@scalebox.it>',
# 			subject=subject,
# 			transactional=False,
# 			track_clicks=track_clicks,
# 			track_opens=track_opens
# 		)
# 		return r
