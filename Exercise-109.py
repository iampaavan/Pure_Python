import os
"""Write a Python program to find path refers to a file or directory when you encounter a path name."""

os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')


def path():
	"""return path details."""
	
	filename = ['Aruba.txt', 'aws.txt', 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder']
	# print(filename)
	
	for files in filename:
		
		print(f"File Name: {os.path.basename(files)}")
		print(f"Absolute Path: {os.path.isabs(files)}")
		print(f"Is File? : {os.path.isfile(files)}")
		print(f"Is Dir?: {os.path.isdir(files)}")
		print(f"Is Link?: {os.path.islink(files)}")
		print(f"Exists?: {os.path.exists(files)}")
		print(f"Link Exists?: {os.path.lexists(files)}")
		print(f'*****************************************************************')
		

path()
