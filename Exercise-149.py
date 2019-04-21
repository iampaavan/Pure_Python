"""Write a Python function to find the maximum and minimum numbers from a sequence of numbers."""
my_list = [100, 256, 10, 98, 74, 65]


def find_min_max():
	"""return min and max from a sequence of numbers"""
	
	min_value = 20
	max_value = 20
	
	for i in my_list:
		if i > max_value:
			max_value = i
	
	for i in my_list:
		if i < min_value:
			min_value = i
			
	return min_value, max_value


print(f"Minimum Value from the list is: {find_min_max()[0]}")
print(f'***************************************************')
print(f"Maximum Value from the List is: {find_min_max()[1]}")
print(f'***************************************************')
