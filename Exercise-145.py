"""Write a Python program to check if a variable is integer or string."""


def checker(user_input):
	"""return if the object is int or str."""
	print(f"Entered value is: {user_input}")
	print(f'**************************************')
	
	if isinstance(user_input, int):
		print(f"Entered value is an integer object")
		print(f'**************************************')
		
	elif isinstance(user_input, float):
		print(f"Entered value is a float object.")
		print(f'**************************************')
		
	else:
		print(f"Entered value is a string object")
		print(f'**************************************')

		
checker(10)
print(f'**********************************************')
checker(56.23)
print(f'**********************************************')
checker('anb')
print(f'**********************************************')


