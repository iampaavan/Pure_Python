import time
"""Write a Python program to get the system time."""


def get_system_time():
	"""return system time."""
	my_sys_time = time.ctime()
	return my_sys_time


print(f"System Current Time is: {get_system_time()}")
