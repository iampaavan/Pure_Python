"""Write a Python program to convert an integer to binary keep leading zeros."""


def int_to_binary():
	"""return binary of an integer."""
	number = int(input(f"Enter the number to convert: "))
	print(f"Entered number is: {number}")
	print(f'*********************************************')
	
	try:
		bin_format = input(f"Enter your desired binary format: ")
		binary = format(number, bin_format)
		
	except ValueError:
		print(f"Enter the correct format to convert the number to binary.")
		
	else:
		print(binary)


int_to_binary()
