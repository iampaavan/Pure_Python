from functools import reduce
"""Write a Python program to compute the product of a list of integers (without using for loop). """
my_list = [2, 5, 8, 6, 7]


def product():
	"""return product of a list."""
	result = reduce(lambda x, y: (x * y), my_list)
	return result


print(f"Product of numbers: {product()}")
print(f"*********************************************************")
my = list()


def prod():
	"""return product."""
	product = 1
	for i in my_list:
		product *= i
		
	return product


print(f"Product: {prod()}")
