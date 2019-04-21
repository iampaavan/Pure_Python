"""Write a Python program to test whether all numbers of a list is greater than a certain number."""


def great_of_all(my_list):
	"""return boolean value"""
	user_input = int(input(f"Enter the number to test against the list:"))
	print(f"Entered number is: {user_input}")
	boolean = all(user_input > x for x in my_list)
	print(f"Members in the list: {my_list}")
	return boolean


print(f'**************************************************************************************')
print(f"Is the entered number greater than all the members in the list: {great_of_all([10, 15, 23])}")
print(f'**************************************************************************************')

