"""Write a Python program to check if a number is positive, negative or zero."""


def check_number():
	"""return whether number is 0 or positive or negative."""
	number = float(input(f"Enter the number:"))
	
	if number > 0:
		print(f"Number is positive.")
		
	elif number == 0:
		print(f"Number is equal to 0.")
		
	else:
		print(f"Number is negative.")
		
		
check_number()