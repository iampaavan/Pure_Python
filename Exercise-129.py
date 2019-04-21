"""Write a Python program to check if lowercase letters exist in a string."""


def check_lower(string):
	"""return boolean if string has any lower case letters."""
	for i in string:
		if i.islower():
			print(f"Lower case found.")
			return True
		
	print(f"There are no lower case letters in the string.")
	return False


print(f"Does the string contain any lower case letters?: {check_lower('DFDFD')}")
print(f'***********************************************************************')


def check_lower(string):
	"""return boolean if lower is found."""
	result = any((i.islower()) for i in string)
	return result


print(f"Does the string can any lowercase letters?: {check_lower('asdasdasWEQWEQ')}")
print(f'***************************************************************************')
print(f"Does the string can any lowercase letters?: {check_lower('WEQWEQ')}")
print(f'***************************************************************************')
