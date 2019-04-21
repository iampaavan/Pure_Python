"""Write a Python program to swap two variables."""

print(f"Swapping using the third variable")


def swap(a, b):
	"""swap a and b."""
	print(f"Before swapping: {(a, b)}")
	temp = a
	a = b
	b = temp
	
	return a, b


print(f"After swapping: {swap(10, 5)}")
print(f"**********************************************************")
print(f"Swapping without the third variable.")


def swap_without_temp(x, y):
	"""swap x and y."""
	print(f"Before Swapping: {(x, y)}")
	
	x = x + y
	y = x - y
	x = x - y
	
	return x, y


print(f"After swapping: {swap_without_temp(10, 5)}")
