import cProfile

"""Write a Python program to determine profiling of Python programs."""
"""Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed.
These statistics can be formatted into reports via the pstats module."""


def sum():
	"""return sum of two numbers"""
	print(2 + 5)
	

print(f'*****************************************')
cProfile.run('sum()')
print(f'*****************************************')


def histogram(my_list):
	"""return histogram of the given list."""
	
	for n in my_list:
		output = ''
		times = n
		
		while times > 0:
			output = output + '*'
			times = times - 1
			
		print(output)
		

print(f'*****************************************************')
cProfile.run('histogram([5, 8, 9, 0, 1, 5])')
print(f'*****************************************************')


def gcd(x, y):
	"""return gcd of x and y."""
	
	if y == 0:
		return x
	
	else:
		return gcd(y, x % y)
	
	
print(f'****************************************************')
cProfile.run('gcd(60, 48)')
print(f'****************************************************')


def lcm(a, b):
	"""return lcm of a and b"""
	return ((a * b) / gcd(a, b))


cProfile.run('lcm(10, 12)')
