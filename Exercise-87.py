"""Write a Python program to get the ASCII value of a character"""


def ascii():
	"""return ascii value of a character"""
	user_input = input(f"Enter a character:")
	ascii = ord(user_input)
	return ascii


print(f"ASCII value of a character: {ascii()}")