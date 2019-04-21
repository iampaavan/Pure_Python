"""Write a Python program to get numbers divisible by fifteen from a list using an anonymous function."""
my_list = [45, 55, 60, 37, 100, 105, 220]


def filter_div_by_15():
	"""return list of numbers divisible by 15."""
	result = list(filter(lambda x: (x % 15 == 0), my_list))
	return result


print(f"List of numbers divisible by 15: {filter_div_by_15()}")
print(f'*****************************************************')

my = list()


def checker():
	"""return list of numbers divisible by 15."""
	for l in my_list:
		if l % 15 == 0:
			my.append(l)
			
	return my


print(f"List of numbers divisible by 15: {checker()}")
