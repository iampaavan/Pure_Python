import sys
"""Write a Python program to get the size of an object in bytes."""


def size_of_data_types():
	"""return size of datatypes."""
	str1 = 'Paavan'
	str2 = 'Manju'
	number_1 = 12345
	number_2 = 10
	
	print(f'**********************************************************')
	print(f"Size of 'str1' is: {sys.getsizeof(str1)}")
	print(f'**********************************************************')
	print(f"Size of 'str2' is: {sys.getsizeof(str2)}")
	print(f'**********************************************************')
	print(f"Size of 'number_1' is: {sys.getsizeof(number_1)}")
	print(f'**********************************************************')
	print(f"Size of 'number_2' is: {sys.getsizeof(number_2)}")


size_of_data_types()