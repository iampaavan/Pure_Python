"""Write a Python program to input a number, if it is not a number generate an error message."""


def check():
	"""return an error message if entered value is not a number."""
	while True:
		try:
			number = int(input(f"Enter a number:"))
			break
			
		except ValueError:
			print(f"Not a number. Try again.")
			
	return number


print(f"Result --> Entered Number is: {check()}")
