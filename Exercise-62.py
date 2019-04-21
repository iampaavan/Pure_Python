"""Write a Python program to convert the distance (in feet) to inches, yards, and miles."""


def conversion():
	"""return distance in inches, yards and miles"""
	distance_feet = int(input(f"Enter the distance in feet: "))
	distance_inches = distance_feet * 12
	distance_yards = distance_feet / 3
	distance_miles = distance_feet / 5280
	return distance_inches, distance_yards, distance_miles


print(f'******************************************************')
print(f"Distance from Feet to Inches: {conversion()[0]} inches")
print(f'******************************************************')
print(f"Distance from Feet to Inches: {conversion()[1]} yards")
print(f'******************************************************')
print(f"Distance from Feet to Inches: {conversion()[2]} miles")
print(f'******************************************************')
