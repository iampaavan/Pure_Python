"""Write a Python program to calculate the sum of the digits in an integer."""


def summation(number):
	"""return the sum of the integer."""
	
	l = list()
	
	for i in str(number):
		l.append(int(i))
	
	print(l)
	return sum(l)


print(f"Sum of the integer: {summation(12345)}")
