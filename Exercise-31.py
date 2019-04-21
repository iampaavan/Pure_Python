"""Write a Python program that will accept the base and height of a triangle and compute the area."""


def calc_triangle_area(base, height):
	"""Return the area of the triangle."""
	area = (1/2) * base * height
	return area


print(f'*****************************************************')
print(f"Area of the triangle is: {calc_triangle_area(10, 15)}")
print(f'*****************************************************')


def triangle():
	':return the area of the triangle'
	base = int(input(f'Enter the base of the triangle:'))
	height = int(input(f"Enter the height of the triangle:"))
	area = (1/2) * base * height
	return area


print(f'********************************************')
print(f"Custom Area of the Triangle is: {triangle()}")
print(f'********************************************')
