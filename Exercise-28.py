"""Write a Python program to concatenate all elements in a list into a string and return it."""


def concatenate(my_list):
	"""Return a string."""
	output = ''
	for i in my_list:
		string = str(i)
		output += string
		
	return output


print(concatenate([1, 2, 3, 4, 5]))


