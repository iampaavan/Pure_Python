"""rite a Python program to add leading zeroes to a string."""


def add_leading_zeroes(string, string_1):
	"""return leading zeroes to the string."""
	lead_zero = string.ljust(10, '0')
	l_z = string_1.ljust(8, '0')
	length_check = len(l_z)
	return lead_zero, l_z, length_check


print(f"String with leading zeroes: {add_leading_zeroes('122.22', '122.22')[0]}")
print(f'***********************************************************************')
print(f"String with leading zeroes: {add_leading_zeroes('122.22', '122.22')[1]}")
print(f'***********************************************************************')
print(f"Length of the 'string_1': {add_leading_zeroes('122.22', '122.22')[2]}")
print(f'***********************************************************************')


