import glob, os
"""Write a Python program to find files and skip directories of a given directory."""
path = 'C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder'
l = list()


def return_files():
	"""return only files from a directory"""
	os.chdir(path)
	for files in glob.glob('*.*'):
		l.append(files)
	
	return l


print(f"List: {return_files()}")
print(f'************************************************************************************')
k = list()


def directories():
	"""return only files and skip directories."""
	for f in os.listdir(path):
		if os.path.isdir(os.path.join(path, f)):
			k.append(f)
		
	return k


print(f"List of directories: {directories()}")
print('*************************************************************************************')
