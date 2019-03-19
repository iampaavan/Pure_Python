import logging
import employeelogs

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s: %(name)s: %(message)s')

# file_hander = logging.FileHandler('sample.log')
file_hander = logging.FileHandler('sample_1.log')
file_hander.setLevel(logging.ERROR)
file_hander.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_hander)
logger.addHandler(stream_handler)


# logging.basicConfig(filename='sample.log', level=logging.DEBUG, format='%(asctime)s: %(name)s: %(message)s')


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
	try:
		result = x / y
	except ZeroDivisionError:
		# logger.error('Tried to divide the number by 0. ')
		logger.exception('Tried to divide the number by 0. ')
	else:
		return result
	# return x / y


num_1 = 20
# num_2 = 10
num_2 = 0


addition_result = add_function(num_1, num_2)
print(f'Add: {num_1} + {num_2} = {addition_result}')
# logging.debug(f'Add: {num_1} + {num_2} = {addition_result}')
# logging.info(f'Add: {num_1} + {num_2} = {addition_result}')
logger.debug(f'Add: {num_1} + {num_2} = {addition_result}')

subtraction_result = sub_function(num_1, num_2)
print(f'Sub: {num_1} - {num_2} = {subtraction_result}')
# logging.debug(f'Sub: {num_1} - {num_2} = {subtraction_result}')
# logging.info(f'Sub: {num_1} - {num_2} = {subtraction_result}')
logger.debug(f'Sub: {num_1} - {num_2} = {subtraction_result}')

multiplication_result = mul_function(num_1, num_2)
print(f'Mul: {num_1} * {num_2} = {multiplication_result}')
# logging.debug(f'Mul: {num_1} * {num_2} = {multiplication_result}')
# logging.info(f'Mul: {num_1} * {num_2} = {multiplication_result}')
logger.debug(f'Mul: {num_1} * {num_2} = {multiplication_result}')

division_result = div_function(num_1, num_2)
print(f'Div: {num_1} / {num_2} = {division_result}')
# logging.debug(f'Div: {num_1} / {num_2} = {division_result}')
# logging.info(f'Div: {num_1} / {num_2} = {division_result}')
logger.debug(f'Div: {num_1} / {num_2} = {division_result}')
