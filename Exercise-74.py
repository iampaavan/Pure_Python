"""Write a Python program to calculate midpoints of a line."""


def midpoint(x1, y1, x2, y2):
	"""return midpoint of a line."""
	midpoint_x = ((x1 + x2) / 2)
	midpoint_y = ((y1 + y2) / 2)
	t = tuple((midpoint_x, midpoint_y))
	print(f"length of x1 is: {x1}")
	print(f"length of y1 is: {y1}")
	print(f"length of x2 is: {x2}")
	print(f"length of y2 is: {y2}")
	return t


print(f"Midpoint of a line: {midpoint(2, 2, 4, 4)}")