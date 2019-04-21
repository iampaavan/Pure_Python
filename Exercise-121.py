"""Write a Python program to format a specified string to limit the number of characters to 6."""


def restrict_string_len(string):
	"""return string length of 6."""
	return string[:6]


print(f"String: {restrict_string_len('abcdefghijklmnop')}")