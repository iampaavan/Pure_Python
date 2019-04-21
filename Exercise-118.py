"""Write a Python program to prove that two string variables of same value point same memory location."""


def memory_location():
	"""return the address location of strings of same value."""
	str1 = 'Python'
	str2 = 'Python'
	addr1 = hex(id(str1))
	addr2 = hex(id(str2))
	return addr1, addr2


print(f"Address Location of 'str1' is: {memory_location()[0]}")
print(f'********************************************')
print(f"Address Location of 'str2' is: {memory_location()[1]}")
print(f'********************************************')
