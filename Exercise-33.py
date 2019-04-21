"""Write a Python program to get the least common multiple (LCM) of two positive integers."""


def gcd(a, b):
	""":return the gcd of a and b"""
	
	if b == 0:
		return a
	
	else:
		return gcd(b, a % b)
	

print(f'******************************************************')


def lcm(x, y):
	"""return the lcm of x and y"""
	return int((x * y) / gcd(x, y))


print(f"LCM of the 10 and 15 are: {lcm(10, 15)}")
print(f'******************************************************')
