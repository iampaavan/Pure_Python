import os
from datetime import datetime

print(os.getcwd())

os.chdir('C:\\Users\\Paavan Gopala')
print(os.getcwd())

# print(os.listdir())

# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2\\New Folder')
# print(os.listdir())

os.chdir('Desktop')
print(os.getcwd())
print(os.listdir())

os.chdir('C:\\Users\\Paavan Gopala')
# os.removedirs('OS-Demo-2\\New Folder')
print(os.listdir())

os.chdir('Desktop')
print(os.getcwd())
print(os.listdir())

# os.makedirs('OS-Demo\\New Folder')

print(os.listdir())
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
print(os.getcwd())

# os.rename('test.txt', 'demo.txt')
print()

print(os.stat('demo.txt'))
print(os.stat('demo.txt').st_size)

print(os.stat('demo.txt').st_mtime)


print()
mod_time = os.stat('demo.txt').st_mtime
print('Modified Timestamp of the file: ', datetime.fromtimestamp(mod_time))

print()
os.chdir('C:\\Users\\Paavan Gopala\\Desktop')
print(os.getcwd())
print('****************************************')
print()

for dirpath, dirnames, filenames in os.walk('C:\\Users\\Paavan Gopala\\Desktop'):
	print('Current Path: ', dirpath)
	print('Directories: ', dirnames)
	print('Files: ', filenames)

print()
print('****************************************************')
print(os.getcwd())

print(os.environ)
print()
print(os.environ.get('HOME'))

print('****************************************************')
print()
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder')
print(os.getcwd())

file_path = os.path.join('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder', 'test.txt')
print(file_path)

with open(file_path, 'w') as f:
	f.write('Hello There !!')

print()
print('*******************************************************')
print(os.path.basename('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))
print(os.path.dirname('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))
print(os.path.split('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))

print()
print('*******************************************************')

print(os.path.exists('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))
print(os.path.exists('D:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))

print()
print('*******************************************************')

print(os.path.splitext('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\test.txt'))




