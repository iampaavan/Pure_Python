"""Write a Python program to compute the future value of a specified principal amount,
rate of interest, and a number of years."""
"""A = P(1+(R\\N)^T)"""


def compound_interest(amount, interest, years):
	"""return compound interest"""
	result = amount * ((1 + (interest/100))**years)
	return round(result, 2)


print(f'*****************************************************')
print(f"Compound Interest: {compound_interest(10000, 3.5, 7)}")
print(f'*****************************************************')
