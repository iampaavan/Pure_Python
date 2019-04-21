import os
"""Write a Python program to list home directory without absolute path."""


def list_home_dir():
	"""return home directory."""
	result = os.path.expanduser('~')
	return result


print(f"Home Directory: {list_home_dir()}")
