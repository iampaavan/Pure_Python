import os
"""Write a Python program to divide a path on the extension separator."""


def splitter():
	"""return filename and it's extension."""
	
	l = ['sample.txt', 'test.py', 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Aruba.txt', 'paavan']
	d = dict()
	
	for i in l:
		# filename, extension = i.split('.')
		filename, extension = os.path.splitext(i)
		d[filename] = extension
	
	return d


print(f"Output: {splitter()}")
