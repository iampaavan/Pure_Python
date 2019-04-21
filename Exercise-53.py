from __future__ import print_function
import sys
"""Write a Python program to print to stderr."""


def eprint(*args, **kwargs):
	"""print standard errors"""
	print(*args, file=sys.stderr, **kwargs)
	
	
eprint('abc', 'efg', 'xyz', sep='--')
eprint('This is how we print standard errors in the console.')
