import socket, os, glob, time
from os import walk
"""Write a Python program to get a new string from a given string where "Is" has been added to the front.
If the given string already begins with "Is" then return the string unchanged."""


def new_string(string):
	"""Return the same string if doesn't start with Is."""

	if string.startswith("Is") or string.startswith('is') or string.startswith('IS'):
		return string
	
	return "Is" + string


print(f"String unchanged: {new_string( 'IsCheck' )}")
print(f'*****************************************')
print(f"String changed: {new_string( 'Validate' )}")
print(f'*****************************************')


def check_vowels(char):
	if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
		return True
	else:
		return False


print(check_vowels('t'))
print(f'*****************************************************')
print(check_vowels('a'))
print(f'*****************************************************')


def hcf(x, y):
	
	if y == 0:
		return x
	
	else:
		return hcf(y, x % y)


print(f"HCF of 2 numbers are: {hcf(60, 48)}")
print(f'*****************************************************')


def gcd(x, y):
	
	if x > y:
		small = y
		
	else:
		small = x
		
	for i in range(1, small + 1):
		if (x % i == 0) and (y % i == 0):
			gcd = i
			
	return gcd


print(f'GCD of 60 and 48 are: {gcd(60, 48)}')
print(f'*****************************************************')


def lcm(a, b):
	return int((a * b) / hcf(a, b))


print(f"LCM of 10 and 15 are: {lcm(10, 15)}")
print(f'*****************************************************')


def histogram(my_list):
	"""return the histogram of the list."""
	for n in my_list:
		output = ''
		times = n
		
		while (times > 0):
			output += '*'
			times -= 1
			
		print(output)
		
		
histogram([6, 5, 4, 3, 2, 1])
print(f'******************************************************************')


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
print(s.getsockname()[0])
s.close()


print(f'*****************************************************************')

dir = os.getcwd()

my_list = list()

for filenames in walk(dir):
	my_list.append(filenames)
	
print(my_list)

print(f'****************************************************************')


for photos in glob.glob("*.txt"):
	print(photos)


print(10//2)

my_time = 86399
day = my_time // (24 * 3600)
my_time = my_time % (24 * 3600)
hour = my_time // 3600
my_time %= 3600
minutes = my_time // 60
my_time %= 60
seconds = my_time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


def time_func(my_time):
	start_time = round(time.perf_counter(), 10)
	print(f"Function  start time: {start_time}")
	
	day = str(my_time // (24 * 3600)) + ' days'
	my_time %= (24 * 3600)
	hour = str(my_time // 3600) + ' hours'
	my_time %= 3600
	minute = str(my_time // 60) + ' minutes'
	my_time %= 60
	second = str(my_time) + ' seconds'
	
	end_time = time.perf_counter()
	finish = abs(end_time - start_time)
	print(f"Function end time: {finish}")
	return day, hour, minute, second


print(f'****************************************************')
print(f"Time: {time_func( 86399 )}")
print(f'****************************************************')




import os
search_dir = "C:\\Users\\Paavan Gopala\\Desktop\\OS-Demo\\New Folder"

os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] # add path to each file
files.sort(key=lambda x: os.path.getmtime(x))

print(files)

import sys
print(sorted(sys.builtin_module_names))


path = os.getcwd()
print(path)
