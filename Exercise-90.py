"""Write a Python program to perform an action if a condition is true."""


def boolean_check():
	"""return the string if true."""
	
	try:
		user_input = int(input(f"Enter the value:"))
		if user_input != 1:
			exit()
		else:
			print(f"First Day of the Month!")
			
	except ValueError:
		print(f"Please enter an integer.")

		
boolean_check()