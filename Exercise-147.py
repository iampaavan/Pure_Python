import os, sys
"""Write a Python program to find the location of Python module sources."""


def path():
	"""return path details"""
	path_os = os.path
	path_sys = sys.path
	
	return path_os, path_sys


print(f"OS Path --> {path()[0]}")
print(f'*********************************************************************')
print(f"Sys Path --> {path()[1]}")
print(f'*********************************************************************')
