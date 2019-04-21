"""Write a Python program to test if a variable is a list or tuple or a set."""


def data_type(x):
	"""return the data type."""
	
	if type(x) is list:
		print(f"{x} is a list.")
		
	elif type(x) is tuple:
		print(f"{x} is a tuple.")
		
	elif type(x) is set:
		print(f"{x} is a set.")
		
	elif type(x) is dict:
		print(f"{x} is a dictionary")
		
	else:
		print(f"{x} is neither a list or tuple or a set.")
		
		
data_type([1, 2, 6])
print(f'************************************************')
data_type((1, 2, 6))
print(f'************************************************')
data_type({1, 2, 6})
print(f'************************************************')
data_type({'s': 4})
print(f'************************************************')
data_type(1)
print(f'************************************************')