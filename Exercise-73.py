import math
"""Write a Python program to get the details of math module."""


def list_math_functions():
	"""return all built-in math functions."""
	my_math_list = dir(math)
	return my_math_list


print(f"My Math module built-in functions: {list_math_functions()}")
