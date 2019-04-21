"""Write a Python program to calculate the sum over a container."""


def sum_over_container(my_list):
	"""return sum."""
	total = 0
	
	for i in my_list:
		total += i
		
	return total


print(f'********************************************************')
print(f"Sum over a container: {sum_over_container([10, 20, 30])}")
print(f'********************************************************')


def use_built_in(mylist):
	"""return sum."""
	print(f"Sum of a container: {sum(mylist)}")
	
	
use_built_in([10, 20, 30])

