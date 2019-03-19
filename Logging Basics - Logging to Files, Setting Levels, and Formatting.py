import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s: %(levelname)s: %(message)s')


def add_function(x, y):
	"""Addition Function"""
	return x + y


def sub_function(x, y):
	"""Subtraction Function"""
	return x - y


def mul_function(x, y):
	"""Multiplication Function"""
	return x * y


def div_function(x, y):
	"""Division Function"""
	return x / y


num_1 = 20
num_2 = 10


addition_result = add_function(num_1, num_2)
print(f'Add: {num_1} + {num_2} = {addition_result}')
logging.debug(f'Add: {num_1} + {num_2} = {addition_result}')

subtraction_result = sub_function(num_1, num_2)
print(f'Sub: {num_1} - {num_2} = {subtraction_result}')
logging.debug(f'Sub: {num_1} - {num_2} = {subtraction_result}')

multiplication_result = mul_function(num_1, num_2)
print(f'Mul: {num_1} * {num_2} = {multiplication_result}')
logging.debug(f'Mul: {num_1} * {num_2} = {multiplication_result}')

division_result = div_function(num_1, num_2)
print(f'Div: {num_1} / {num_2} = {division_result}')
logging.debug(f'Div: {num_1} / {num_2} = {division_result}')
