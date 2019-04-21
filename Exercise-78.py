import sys
"""Write a Python program to test whether the system is a big-endian platform or little-endian platform."""


def endian_check():
	"""return type of endian."""
	
	if sys.byteorder == 'little':
		print(f'Endian Type --> Little_Endian Platform')
		
	else:
		print('Endian Type --> Big-Endian Platform')
		
		
endian_check()
