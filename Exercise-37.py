"""Write a Python program to add two objects if both objects are an integer type."""


def add_numbers(x, y):
	""":return sum of two integer objects."""
	
	try:
		if not ((isinstance(x, int)) and (isinstance(y, int))):
			raise TypeError

	except TypeError:
		print(f"Inputs must be integer.")
		
	else:
		return x + y


print(f'Result of two numbers: {add_numbers(10, 20)}')
print(f'**************************************************')
print(f'Result of two numbers: {add_numbers("m", "n")}')
print(f'**************************************************')
print(f"Result of two float number: {add_numbers(10.25, 3.25)}")
print(f'**************************************************')
print(f"Result of one int and one float: {add_numbers(10, 2.5)}")
print(f'**************************************************')




