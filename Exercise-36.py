"""Write a Python program that will return true if the two given integer values are equal or
their sum or difference is 5."""


def boolean(x, y):
	""":return boolean value."""
	
	sum = x + y
	difference = abs(x - y)
	
	if (x == y) or (sum == 5) or (difference == 5):
		result = True
		
	else:
		result = False
		
	return result


print(f"Result of two numbers are: {boolean(10, 5)}")
print(f'*******************************************')
print(f"Result of two numbers are: {boolean(2, 3)}")
print(f'*******************************************')
print(f'Result of two numbers are: {boolean(2, 2)}')
print(f'*******************************************')
print(f'Result of two numbers are: {boolean(10, 20)}')
print(f'*******************************************')
print(f"Result of two numbers are: {boolean(5, 10)}")
print(f'*******************************************')

