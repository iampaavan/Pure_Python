import sys
"""Write a Python program to determine the largest and smallest integers, longs, floats."""


def data_type_info():
	"""return data type information."""
	float_info = sys.float_info
	int_info = sys.int_info
	max_size_int = sys.maxsize
	return float_info, int_info, max_size_int


print(f"Float Info: {data_type_info()[0]}")
print(f'************************************************')
print(f"Int Info: {data_type_info()[1]}")
print(f'************************************************')
print(f'Max Int Size: {data_type_info()[2]}')
print(f'************************************************')

