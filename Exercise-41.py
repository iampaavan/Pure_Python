import math
"""Write a Python program to compute the distance between the points (x1, y1) and (x2, y2)."""


def distance(list1, list2):
	"""return distance between 2 points."""
	result = math.sqrt(((list1[0] - list2[0])**2) + (((list1[1]) - list2[1])**2))
	return round(result, 2)


print(f'**********************************************************')
print(f"Distance between two points is: {distance([4, 0], [6, 6])} meters.")
print(f'**********************************************************')
