"""Write a Python program to remove the first item from a specified list."""


def remove_first_element():
	"""return the list after first item removal"""
	my_list = ["Red", "Black", "Green", "White", "Orange"]
	print(f"Original List: {my_list}")
	my_list.remove('Red')
	return my_list


print(f"Altered List: {remove_first_element()}")