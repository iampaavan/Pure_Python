import glob, os, time
"""Write a Python program to sort files by date."""


def sort_files():
	"""return files in the sorted order."""
	create_file = list()
	modified_file = list()
	
	os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
	for files in glob.glob('*'):
		create_file.append(files)
		modified_file.append(files)
		
	create_file.sort(key=os.path.getctime)
	modified_file.sort(key=os.path.getmtime)
	
	print(f"Files in the order of created date: {create_file}")
	print()
	print(f"Files in the order of modified date: {modified_file}")
	
	
sort_files()
