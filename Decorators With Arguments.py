def decorator_prefix(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args, **kwargs):
			print(prefix, 'Executed Before', original_function.__name__)
			result = original_function(*args, **kwargs)
			print(prefix, 'Executed After', original_function.__name__)
			return result
		return wrapper_function
	return decorator_function


@decorator_prefix('TESTING: ')
def display_info(name, age):
	print('{} function ran with two arguments ({}, {})'.format(display_info.__name__, name, age))


display_info('Paavan', 27)
print()
display_info('Manju', 28)
