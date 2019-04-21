"""Write a Python program to concatenate N strings."""


def concatenate_strings(my_list):
	""":return string concatenation."""
	
	output = ''
	
	for i in my_list:
		output += i + '-'
		
	return output


print(f"Concatenated String: {concatenate_strings(['Red', 'White', 'Black'])}")


def conc_strings(list_mine):
	output = '-'.join(list_mine)
	return output


print(conc_strings(['Red', 'White', 'Black']))
