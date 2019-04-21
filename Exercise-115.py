"""Write a Python program to filter the positive numbers from a list"""
my_list = [10, -5, -8, 2, 5]


def check_positive():
	"""return positive numbers."""
	my = list(filter(lambda x: (x > 0), my_list))
	return sorted(my)


print(f"List of positive number: {check_positive()}")
print(f'*******************************************')
pos_list = []


def positive():
	"""return positive numbers."""
	for i in my_list:
		if i > 0:
			pos_list.append(i)
			
	return sorted(pos_list)


print(f"Positive Number List: {positive()}")
