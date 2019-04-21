"""Write a Python program to sum of three given integers. However, if two values are equal sum will be zero."""


def sum():
	"""return sum."""
	
	x = int(input(f"Enter the first number:"))
	y = int(input(f"Enter the second number:"))
	z = int(input(f"Enter the third number:"))
	
	if (x == y) or (y == z) or (x == z):
		sum = 0
		
	else:
		sum = x + y + z
		
	return sum


print(f"Sum of three numbers if all three are unique: {sum()}")
print(f'**********************************************************')
print(f"Sum of three numbers if any two numbers are equal: {sum()}")
print(f'**********************************************************')


def checks(a, b, c):
	""":return sum of a, b and c."""
	
	if (a == b) or (b == c) or (a == c):
		sum = 0
		
	else:
		sum = a + b + c
		
	return sum


print(f"Sum of three numbers: {checks(10, 20, 30)}")
print(f'******************************************************************')
print(f"Sum of three numbers: {checks(10, 10, 0)}")
print(f'******************************************************************')



