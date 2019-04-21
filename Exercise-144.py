import struct
"""Write a Python program to determine if the python shell is executing in 32 bit or 64 bit
mode on operating system."""


def checker():
	"""return if python shell is executing in 32 or 64 bit."""
	value = struct.calcsize('P') * 8
	return value


print(f"Python shell is operating in {checker()} bit mode on OS.")
