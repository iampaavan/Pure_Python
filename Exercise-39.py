"""Write a Python program to solve (x + y) * (x + y)"""


def compute(x, y):
	"""return (x+y)*(x+y)"""
	return ((x + y) * (x + y))

	
print(f"((4 + 3) ^ 2) = {compute(4, 3)}")
print(f'************************************************')

a, b = 4, 3
result = ((a + b) * (a + b))
print(f"(({a}+{b})^2) = {result}")


