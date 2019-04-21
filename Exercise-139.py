"""Write a Python program to convert true to 1 and false to 0."""


def convert():
	"""return int value of True and False."""
	x = 'true'
	x = int(x == 'true')

	y = 'false'
	y = int(y == 'true')
	
	return x, y


print(f"Convert True to an Integer Value: {convert()[0]}")
print(f'*************************************************')
print(f"Convert False to an Integer Value: {convert()[1]}")
print(f'*************************************************')
