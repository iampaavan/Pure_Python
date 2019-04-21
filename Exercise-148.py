"""Write a Python function to check whether a number is divisible by another number.
Accept two integers values form the user."""


def function():
	"""return if a number is divisble by another number"""
	a = int(input(f"Enter the first integer number: "))
	b = int(input(f"Enter the second integer number: "))
	
	try:
		if a % b == 0:
			print(f"{a} is divided by {b}.")
			
		else:
			print(f"{a} cannot be divided by {b}.")
	
	except ZeroDivisionError:
		print(f"{a} cannot be divided by {b}. Zero Division Error.")

	except ValueError:
		print(f"Enter integer values only.")
		
		
function()