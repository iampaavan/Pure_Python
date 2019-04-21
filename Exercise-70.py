"""Write a Python program to sort three integers without using conditional statements and loops."""


def my_sort(x, y, z):
	"""sort the 3 numbers."""
	l = list()
	l.append(x)
	l.append(y)
	l.append(z)
	
	return sorted(l)


print(f"My sorted numbers: {my_sort(5, 1, 7)}")
