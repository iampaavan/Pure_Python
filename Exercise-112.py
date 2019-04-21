import glob, os
"""Write a Python program to make file lists from current directory using a wildcard."""


def list_all_files():
	"""return all files in a directory."""
	os.chdir("C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder")
	my_files_list = glob.glob('*.*')
	return my_files_list


print(f"List of all the files in the directory: {list_all_files()}")
