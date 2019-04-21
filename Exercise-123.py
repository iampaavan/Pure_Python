"""Write a Python program to empty a variable without destroying it."""


def destroy():
	"""empty the variable w\o destroying it."""
	n = 20
	l = [1, 3, 5]
	d = {'paavan': 5}
	t = (5, 8, 9)
	
	empty_n = type(n)()
	empty_l = type(l)()
	empty_d = type(d)()
	empty_t = type(t)()

	
	return empty_n, empty_l, empty_d, empty_t


print(f"Empty Variable: {destroy()[0]}")
print(f'******************************')
print(f"Empty List: {destroy()[1]}")
print(f'******************************')
print(f"Empty Dictionary: {destroy()[2]}")
print(f'******************************')
print(f"Empty Tuple: {destroy()[3]}")
print(f'******************************')

