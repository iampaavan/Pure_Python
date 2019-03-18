import os
from contextlib import contextmanager

cwd = os.getcwd()
print(cwd)
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\Python_1')
print(os.getcwd())
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
print(cwd)
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\Python_2')
print(os.getcwd())
print(os.listdir())
os.chdir(cwd)

print()
print('*********************************************************')
print()


@contextmanager
def change_dir(destination):
	try:
		cwd = os.getcwd()
		os.chdir(destination)
		yield
	finally:
		os.chdir(cwd)
		

with change_dir('C:\\Users\\Paavan Gopala\\Desktop\\Python_1'):
	print(os.listdir())
	
with change_dir('C:\\Users\\Paavan Gopala\\Desktop\\Python_2'):
	print(os.listdir())

