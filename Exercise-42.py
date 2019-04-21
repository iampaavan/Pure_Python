"""Write a Python program to check whether a file exists."""

filename = input(f"Enter the filename:")

try:
	with open(filename, 'r') as file_read:
		contents = file_read.read()
		
except FileNotFoundError:
	print(f'Error --> File not found.')
	
else:
	print(f"File Contents --> {contents}")

print(f'**************************************************************')
