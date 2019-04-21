"""Write a Python program to convert height (in feet and inches) to centimeters."""


def conv_feet_to_inches():
	""":return height in centimeters."""
	height_feet = int(input(f"Enter your height in feet: "))
	height_inches = int(input(f"Enter your height in inches: "))
	height_inches = height_inches + (height_feet * 12)
	height_centimeters = round(height_inches * 2.54, 3)
	return height_centimeters


print(f'Your height in centimeters: {conv_feet_to_inches()}')
