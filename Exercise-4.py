from math import pi
"""Write a Python program which accepts the radius of a circle from the user and compute the area."""


def radius():
	"""Calculate the radius"""
	r = int(input(f"Enter the radius of the circle:"))
	Area = pi * (r * r)
	return f"Area of the circle is: {Area}"


c = radius()
print(c)
print(f'*******************************************')
