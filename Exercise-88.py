import os
"""Write a Python program to get the size of a file"""


def get_size_of_file():
	"""return the size of the file."""
	
	try:
		os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
		filename = input(f"Enter the filename:")
		size = os.path.getsize(filename)
		
	except FileNotFoundError:
		print(f'File not found.')

	else:
		print(f"Size of the file is: {size} bytes")


get_size_of_file()
