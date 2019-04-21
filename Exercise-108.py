import time, os
"""Write a Python program to retrieve file properties."""

os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')


def file_properties():
	"""return file properties"""
	
	file = os.path.basename("C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Aruba.txt")
	mod_time = time.ctime(os.path.getmtime(file))
	access_time = time.ctime(os.path.getatime(file))
	creation_time = time.ctime(os.path.getctime(file))
	file_size = os.path.getsize(file)
	return file, mod_time, access_time, creation_time, file_size


print(f"File Name: {file_properties()[0]}")
print(f'*********************************')
print(f"File Modified Time: {file_properties()[1]}")
print(f'*********************************')
print(f"File Access Time: {file_properties()[2]}")
print(f'*********************************')
print(f"File Creation Time: {file_properties()[3]}")
print(f'*********************************')
print(f"File Size: {file_properties()[4]} bytes")
print(f'*********************************')
