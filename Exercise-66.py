"""Write a Python program to calculate body mass index."""


def calc_bmi(weight, height):
	"""return bmi of a body."""
	return round((weight) / (height ** 2), 2)


print(f'**************************************************')
print(f'BMI of your body: {calc_bmi(85, 5.8)}')