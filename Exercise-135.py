"""Write a Python program to input two integers in a single line."""


def input_two_integers():
	"""input 2 integers in a single line."""
	x, y = map(int, input(f"Enter two integers:").split(','))
	return x, y


print(f"Display the two integers entered: {input_two_integers()}")
