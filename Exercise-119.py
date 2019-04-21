"""Write a Python program to create a bytearray from a list."""
my_list = [10, 20, 56, 35, 17, 99]


def convert_byte_array():
	"""return bytearray."""
	my_byte = bytearray(my_list)
	print(my_byte)
	back = list(my_byte)
	print(back)


convert_byte_array()
