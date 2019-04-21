import math
"""Write a Python program to get the the volume of a sphere with radius 6."""


def sphere_volume():
	"""Return the volume of the sphere."""
	radius = int(input(f"Enter the radius of the sphere:"))
	volume = (4/3) * math.pi * (radius**3)
	return volume


Volume = sphere_volume()
print(f"Volume of the Sphere is: {Volume}")
print(f'***************************************************')


def cal_vol(rad):
	"""Return volume of the sphere."""
	volume = (4/3) * math.pi * (rad**3)
	return volume


sphere = cal_vol(6)
print(f"Volume of the Sphere is: {sphere}")
