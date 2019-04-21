"""Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20."""


def checker(x, y):
	"""return 20 if sum is between 15 and 20."""
	sum = x + y
	
	if 15 <= sum <= 20:
		result = 20
		
	else:
		result = x + y
		
	return result


print(f"Sum of 2 numbers are: {checker(10, 20)}")
print(f'***************************************')
print(f"Sum of 2 numbers are: {checker(10, 6)}")
print(f'***************************************')
print(f"Sum of 2 numbers are: {checker(10, 5)}")
print(f'***************************************')
print(f"Sum of 2 numbers are: {checker(10, 10)}")
print(f"***************************************")

