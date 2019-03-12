import os

my_file = "test.txt"

# Race Condition

if os.access(my_file, os.R_OK):
	with open(my_file) as f:
		print(f.read())

else:
	print('File can\'t be accessed')

print()
print('****************************************************')
print()

# No race condition

try:
	file = open(my_file)
	
except Exception as a:
	print(a)

except IOError as e:
	print('File can\'t be accessed! ')
	
else:
	with file:
		print(file.read())

