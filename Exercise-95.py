"""Write a Python program to convert a byte string to a list of integers."""


def byte_str_list_integers(string):
	"""return list of integers."""
	my_list = list(string)
	return my_list


print(f"List of integers: {byte_str_list_integers(b'Abc')}")
