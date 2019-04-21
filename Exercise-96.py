"""Write a Python program to check if a string is numeric."""


def check_string_numeric(string):
	"""return if string is numeric or not"""
	
	try:
		i = float(string)
		
	except (ValueError, TypeError):
		print(f"String is not numeric")
	
	else:
		print(f"String {i} is numeric")


print(f"********************************************************")
check_string_numeric('1a23')
print(f'********************************************************')
check_string_numeric('123')
print(f'********************************************************')

