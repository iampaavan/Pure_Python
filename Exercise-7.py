"""Write a Python program to accept a filename from the user and print the extension of that."""
filename = input(f"Enter the filename: ")
file, ext = filename.split('.')
print(f"Extension of the file: {ext}")
print(f'*********************************************************')

with open(filename, 'r') as file_read:
	c = file_read.read()
print(c)
