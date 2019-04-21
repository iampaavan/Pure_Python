"""Write a Python program to check if an integer fits in 64 bits."""


def bit_length_checker():
	"""return if an integer fits in 64 bits."""
	int_value = 30
	
	if int_value.bit_length() <= 63:
		a = (-2 ** 63).bit_length()
		b = (2 ** 63).bit_length()
	
	return a, b


print(f"Bit Length: {bit_length_checker()}")