"""Write a python program to sum of the first n positive integers."""


def sum_of_n_numbers(number):
	"""return sum of integers."""
	result = ((number * (number + 1))/ 2)
	return int(result)


print(f'**************************************')
print(f"Sum of integers: {sum_of_n_numbers(8)}")
print(f'**************************************')


def summation(x):
	"""return summation."""
	
	print(f"Sum of {x} integers is:")
	sum = 0
	
	for i in range(x + 1):
		sum = sum + i
		
	return sum


print(f'**********************************************')
print(f"{summation(8)}")
print(f'**********************************************')
