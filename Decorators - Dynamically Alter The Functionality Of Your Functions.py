import time
import logging
from functools import wraps

def outer_function():
	message = 'Hi'

	def inner_function():
		print(message)
	return inner_function()


outer_function()

print()
print('****************************************')


def outer_funtion_1():
	message_1 = 'Hi'
	
	def inner_function_1():
		print(message_1)
	return inner_function_1


outer_funtion_1()
my_func = outer_funtion_1()
my_func()
my_func()
my_func()

print()
print('****************************************')


def outer_function_2(msg):
	message_2 = msg
	
	def inner_function_2():
		print(message_2)
	return inner_function_2


hi_func = outer_function_2('Hi')
bye_func = outer_function_2('Bye')

hi_func()
bye_func()


print()
print('**********************************')


def sample(message):
	m = message
	return m


a = sample('Hello')
print(a)

print()
print('***********************************')


def outer_function_4(msg):
	def inner_function_4():
		print(msg)
	return inner_function_4


hi_func_1 = outer_function_4('Hello')
bye_func_1 = outer_function_4('Bubye')

hi_func_1()
bye_func_1()

print()
print('**********************************************')

# Decorators

print()


def decorator_function(original_function):
	def wrapper_function():
		print(f'Wrapper function ran before {original_function.__name__} function. ')
		# print('Wrapper function ran before the {} method. '.format(original_function.__name__))
		return original_function()
	return wrapper_function


def display():
	print('Run the display function! ')


decorated_display = decorator_function(display)
decorated_display()


print()
print('*************************************************')


def decorator_function_1(original_function):
	def wrapper_function_1():
		# print(f'Wrapper function ran before {original_function.__name__} function. ')
		print('{} function ran before the {} method. '.format(wrapper_function_1.__name__, original_function.__name__))
		return original_function()
	return wrapper_function_1


@decorator_function_1
def display_1():
	print('Ran the {} function using @{} method. '.format(display_1.__name__, decorator_function_1.__name__))
	# print(f'Ran the display function using @{decorator_function_1.__name__} method')


display_1()


print()
print('*************************************************************')


def decorator_function_2(original_function):
	def wrapper_function_2(*args, **kwargs):
		# print(f'Wrapper function ran before {original_function.__name__} function. ')
		print('{} function ran before the {} method. '.format(wrapper_function_2.__name__, original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function_2


@decorator_function_2
def display_2():
	print()
	print('Ran the {} function using @{} method. '.format(display_2.__name__, decorator_function_2.__name__))
	# print(f'Ran the display function using @{decorator_function_1.__name__} method')


@decorator_function_2
def display_info(name, age):
	print()
	print('{} function ran with two arguments ({}, {})'.format(display_info.__name__, name, age))


display_2()
display_info('Paavan', 27)

print()
print('*********************************************************')


def decorator_function_3(original_function):
	def wrapper_function_3(*args, **kwargs):
		# print(f'Wrapper function ran before {original_function.__name__} function. ')
		print('{} function ran before the {} method. '.format(wrapper_function_3.__name__, original_function.__name__))
		return original_function(*args, **kwargs)
	return wrapper_function_3


class decorator_class(object):
	def __init__(self, original_function):
		self.original_function = original_function
		
	def __call__(self, *args, **kwargs):
		print('call method ran before the {} method. '.format(self.original_function.__name__ ))
		return self.original_function(*args, **kwargs)


@decorator_class
def display_3():
	print()
	print('Ran the display function using @{} class. '.format(decorator_class.__name__))
	# print(f'Ran the display function using @{decorator_function_3.__name__} method')


@decorator_class
def display_info_1(name, age):
	print()
	print('display_info_1 function ran with two arguments ({}, {})'.format(name, age))


display_3()
display_info_1('Paavan', 27)

print()
print('*********************************************************')

# Practical Examples


def my_logger(orig_func):
    
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper


@my_logger
@my_timer
def display_4():
	time.sleep(5)
	print()
	print('Ran the display function using @{} class. '.format(decorator_class.__name__))
	# print(f'Ran the display function using @{decorator_function_3.__name__} method')
	

@my_logger
@my_timer
def display_info_2(name, age):
	time.sleep(5)
	print()
	print('display_info_1 function ran with two arguments ({}, {})'.format(name, age))


display_4()
display_4()
display_4()
display_4()
display_info_2('Manju', 28)
display_info_2('Paavan', 27)
display_info_2('Ashuuuu', 27)
display_info_2('Suhasini', 24)
