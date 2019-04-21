"""Write a Python program to test whether a number is within 100 of 1000 or 2000."""


def near_thousand(number):
	"""Return boolean value."""
	return (abs(number - 1000) <= 100) or (abs(number - 2000) <= 100)


print(f"Boolean Value: {near_thousand(1000)}")
print(f'************************************')
print(f"Boolean Value: {near_thousand(900)}")
print(f'************************************')
print(f"Boolean Value: {near_thousand(800)}")
print(f'************************************')
print(f"Boolean Value: {near_thousand(2200)}")
print(f'************************************')
