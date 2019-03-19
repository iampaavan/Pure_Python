def add(x, y):
	"""Addition Function"""
	return x + y


def sub(x, y):
	"""Subtraction Function"""
	return x - y


def mul(x, y):
	"""Multiplication Function"""
	return x * y


def div(x, y):
	"""Division Function"""
	if y == 0:
		raise ValueError('Can\'t divide a number by 0. ')
	else:
		return x / y

