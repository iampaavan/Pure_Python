"""Write a Python program to get the difference between a given number and 17, if the number is greater
than 17 return double the absolute difference."""


def difference(number):
	"""return the difference"""
	
	if number <= 17:
		return abs(number - 17)
	
	else:
		return (number - 17) * 2
	

print(f"Difference when given number is less than or equal to 17: {difference(14)}")
print(f'**************************************************************************')
print(f"Double the difference value when number is greater than 17: {difference(22)}")
print(f'**************************************************************************')


def diff():
	"""return the difference"""
	number = int(input(f"Enter the number:"))
	
	if number <= 17:
		print(f"Given number is: {number}")
		return abs(number - 17)
	
	else:
		print(f"Given number is: {number}")
		return (number - 17) * 2
	
	
print(f"Difference when given number is less than or equal to 17: {diff()}")
print(f'**************************************************************************')
print(f"Double the difference value when number is greater than 17: {diff()}")
print(f'**************************************************************************')
