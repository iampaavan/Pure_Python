import os, time
"""Write a Python program to get file creation and modification date/times."""


def creation_time():
	"""return time of file creation time."""
	return time.ctime(os.path.getctime('sample.txt'))


def modified_time():
	"""return file modification time"""
	return time.ctime(os.path.getmtime('sample.txt'))


print(f'**********************************************')
print(f"File Creation Time: {creation_time()}")
print(f'**********************************************')
print(f'File Modified Time: {modified_time()}')
print(f'**********************************************')
