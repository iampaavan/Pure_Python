"""Write a python program to convert decimal to hexadecimal."""


def dec_to_hex():
	"""return hexadecimal value of an integer."""
	number = int(input(f"Enter the number to convert: "))
	print(f"Entered number is: {number}")
	print(f'*********************************************')
	
	try:
		hex_format = input(f"Enter your desired hexadecimal format: ")
		hexadecimal = format(number, hex_format)
	
	except ValueError:
		print(f"Enter the correct format to convert the number to binary.")
	
	else:
		print(hexadecimal)
		
		
dec_to_hex()
