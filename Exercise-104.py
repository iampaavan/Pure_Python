import os
"""Write a Python program to extract the filename from a given path."""


def extract_filename():
	"""return only filename from path"""
	os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
	filename = os.path.basename('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Aruba.txt')
	return filename


print(f"Filename: {extract_filename()}")
