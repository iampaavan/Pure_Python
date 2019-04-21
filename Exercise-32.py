"""Write a Python program to compute the greatest common divisor (GCD) of two positive integers."""


def calc_gcd(x, y):
	""":return gcd of the 2 numbers."""
	
	if y == 0:
		return x
	
	else:
		return calc_gcd(y, x % y)
	

print(f'****************************************')
print(f"GCD of 2 numbers are: {calc_gcd(60, 48)}")
print(f'****************************************')


def gcd(a, b):
	""":return gcd of a and b."""
	
	if a > b:
		small = b
		
	else:
		small = a
		
	for i in range(1, small + 1):
		if (a % i == 0) and (b % i == 0):
			gcd = i
			
	return gcd


print(f"GCD of 60 and 48 are: {gcd(60, 48)}")
print(f'****************************************')


def lcm(a, b):
	return int((a*b) / gcd(a, b))


print(f"LCM of 2 numbers are: {lcm(15, 20)}")
print(f'*****************************************')
