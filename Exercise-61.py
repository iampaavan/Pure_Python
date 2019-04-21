import math
"""Write a Python program to calculate the hypotenuse of a right angled triangle."""


def calc_hypotenuse():
	"""return the length of the hypotenuse."""
	a = int(input(f"Enter the length of one side of right angled triangle:"))
	b = int(input(f"Enter the length of another side of right angled triangle:"))
	c = math.sqrt((a ** 2) + (b ** 2))
	return int(c)


print(f"Length of the Hypotenuse: {calc_hypotenuse()}")
