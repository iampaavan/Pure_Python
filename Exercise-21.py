"""Write a Python program to get a string which is n (non-negative integer) copies of a given string"""


def count_strings(string, number):
	"""Return the number of times the string is asked for."""
	
	result = ''
	
	for i in range(number):
		result = result + string
	return result
	

print(f"Result string: {count_strings('abc', 3)}")
print(f'******************************************')
print(f'Result string: {count_strings(".java", 4)}')
print(f'******************************************')
