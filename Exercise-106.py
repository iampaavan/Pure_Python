import os
"""Write a Python program to get the users environment."""


def os_env():
	"""return users environment"""
	user_env = os.environ
	return user_env


print(f"Users Environment Variables: {os_env()}")
