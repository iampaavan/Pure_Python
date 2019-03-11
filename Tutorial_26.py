import os

print()
os.chdir('C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder\\Videos')
print(os.getcwd())

print()
for files in os.listdir():
	
	# print(files)
	split_file_name, split_file_extension = os.path.splitext(files)
	
	# print(split_file_name)
	# print(split_file_name.split('-'))
	
	file_title, file_course, file_number = split_file_name.split('-')
	
	# print(file_number)
	file_title = file_title.strip()
	file_course = file_course.strip()
	# file_number = file_number.strip()
	# file_number = file_number.strip()[1:]
	file_number = file_number.strip()[1:].zfill(2)
	
	# print('{}-{}-{}{}'.format(file_number, file_course, file_title, split_file_extension))
	print('{}-{}{}'.format(file_number, file_title, split_file_extension))
	rename_files = '{}-{}{}'.format(file_number, file_title, split_file_extension)
	
	os.rename(files, rename_files)

