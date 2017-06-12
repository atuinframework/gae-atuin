# -*- coding: utf-8 -*-
# Roles define classes of users. Each user has to be assigned at least (and at most) to one role.
# A role defines multiple policies. Policies can be used in more than one role.
# A policy is a group of functions.

user_role_polices = {
	'ADMIN': {
		'title': 'Administrator',
		'description': 'Administrator. All rights.',
		'policies': None
	}
}

role_policy_functions = {
}
