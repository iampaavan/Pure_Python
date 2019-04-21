"""Write a Python function that takes a positive integer and returns the sum of the cube of all
the positive integers smaller than the specified number."""


def cube(number):
	"""return sum of the cubes"""
	number -= 1
	total = 0
	
	while number > 0:
		total += number * number * number
		number -= 1
		
	return total


print(f"Sum of cubes: {cube(8)}")
