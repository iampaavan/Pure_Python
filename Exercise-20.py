"""Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged."""


def new_string(string):
	"""Return the same string if doesn't start with Is."""
	
	
	if len(string) >= 2 and string[:2] == "Is" and "is" and "IS":
		result = string
	
	else:
		result = "Is" + string

	return result


print(f"String unchanged: {new_string('IsCheck')}")
print(f'*****************************************')
print(f"String changed: {new_string('Validate')}")
print(f'*****************************************')
