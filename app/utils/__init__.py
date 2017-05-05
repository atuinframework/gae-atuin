# -*- coding: utf-8 -*-

okchars = ''.join(map(chr, range(ord('A'), ord('Z')+1)) + map(chr, range(ord('a'), ord('z')+1))) + '._-1234567890'


def slugify(string):
	"""
	Returns a slug from a string
	"""
	string_clean = string.lower().replace(' ', '-')
	string_clean = ''.join([c for c in string_clean if c in okchars])
	
	return string_clean


def update_searchable_set(ns, string_to_split):
	"""
	Split string_to_split and add to ns
	"""
	
	parts = string_to_split.lower().split()
	
	for part in parts:
		ns = ns.union( [ part[:i] for i in range(2, len(part)+1) ] )
	
	return ns
