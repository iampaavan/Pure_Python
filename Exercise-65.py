import os
"""Write a Python program to get an absolute file path."""


def path(path_fname):
	"""return absolute path name."""
	os.chdir('C:\\Users\\Paavan Gopala\\PycharmProjects\\Practise_Problems\\Basics_Part-2\\')
	return os.path.abspath(path_fname)


print(f"Absolute file path: {path('sample.txt')}")
print(f"Absolute file path: {path('__init__.py')}")
