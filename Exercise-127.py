from inspect import getmodule
from math import sqrt
from os import path
"""Write a Python program to get the actual module object for a given object."""


def get_module_info():
	"""return module info."""
	result = getmodule(sqrt)
	a = getmodule(getmodule)
	p = getmodule(path)
	return result, a, p


print(f"Module Info: {get_module_info()[0]}")
print(f'***********************************')
print(f"Module Info: {get_module_info()[1]}")
print(f'***********************************')
print(f"Module Info: {get_module_info()[2]}")

