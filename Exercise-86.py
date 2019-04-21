import os
"""Write a Python program to check if a file path is a file or a directory."""

os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
path = os.getcwd()
print(path)


def dir_or_file():
	"""return whether path is a dir or file."""
	
	if os.path.isdir('Aruba.txt'):
		print(f"It is a directory.")
		
	elif os.path.isfile('Aruba.txt'):
		print(f"It is a file.")
		
	else:
		print(f'It is a special file.')
		
		
dir_or_file()