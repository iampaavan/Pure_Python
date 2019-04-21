"""Write a Python program to check whether a specified value is contained in a group of values. """


def test_number(my_list, number):
	"""Return boolean based on the checks"""
	for i in my_list:
		if i == number:
			return True
	
	return False
		

print(f"Checks: {test_number([1, 5, 8, 3], 3)}")
print(f'**************************************')
print(f"Checks: {test_number([1, 5, 8, 2], 0)}")
print(f'**************************************')

