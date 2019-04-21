"""Write a Python program to determine if variable is defined or not."""


def variable():
	"""check if variable is defined or not."""
	try:
		x = 1
		
	except NameError:
		print(f"Variable 'x' is not defined.")
		
	else:
		print(f"Variable 'x' is defined.")
	
	print(f"***************************************************")
	
	try:
		y
	
	except NameError:
		print(f"Variable 'y' is not defined")
		
	else:
		print(f"Variable 'x' is defined.")
		
		
variable()