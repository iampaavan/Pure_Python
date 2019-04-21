"""Write a Python program to calculate the sum of three given numbers, if the values are
equal then return thrice of their sum."""


def sum_thrice(x, y, z):
	"Return thrice the sum if x=y=z"
	
	total = x + y + z
	
	if x == y == z:
		total = (x + y + z) * 3
		return total
	
	return total


print(f"Sum of three numbers when they aren't equal: {sum_thrice(1, 2, 3)}")
print(f'******************************************************************')
print(f"Sum of three numbers when they are equal: {sum_thrice(3, 3, 3)}")
print(f'******************************************************************')
