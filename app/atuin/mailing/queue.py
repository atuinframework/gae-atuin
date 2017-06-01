# -*- coding: utf-8 -*-
import uuid
import json
import redis
import time

def enqueue_email(subject, message, tolist, cclist=[], bcclist=[], tags=[], track_clicks=False, track_opens=False):
	
	mail_data = {
		'subject': subject,
		'message': message,
		'tolist': tolist,
		'cclist': cclist,
		'bcclist': bcclist,
		'tags': tags,
		'track_clicks': track_clicks,
		'track_opens': track_opens,
		'enqueue_timestamp': time.time()
	}
	
	# generate uuid
	key = uuid.uuid4()
	r = redis.StrictRedis(host='redis')
	r.set(key, json.dumps(mail_data))
	r.lpush('mailing', key)
	
	return
	
	