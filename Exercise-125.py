"""Write a Python program to check if multiple variables have the same value."""


def checker(x, y, z):
	"""return true if all variables have same values."""
	user_input = int(input("Enter a number:"))
	
	if x == y == z == user_input:
		return True
	
	else:
		return False
	
	
print(f"Is the variables having the same values?: {checker(10, 10, 10)}")
print(f"**************************************************************")
print(f"Is the variables having the same values?: {checker(10, 20, 15)}")
print(f'**************************************************************')
