try:
	with open('test.txt') as contents:
		abc = contents.read()
		var = bad_var

except FileNotFoundError:
	print('Sorry, this file doesn\'t exist')

except Exception:
	print('Sorry, something went wrong')
	print()

print('*****************************************************************************************')


try:
	with open('test.txt') as file:
		print()
		print('Inside the try block, printing it!!! ')
		content = file.read()
		
except FileNotFoundError as f:
	print('Inside 1st except block, printing the typical python file not found exception below')
	print(f)
	
except Exception as e:
	print('Inside 2nd except block, printing general exception')
	print(e)

else:
	print()
	print('Inside else block only if there is no exception raised')
	print()
	print(content)
	file.close()
	
	
finally:
	print()
	print('Inside the finally block of code')
	print()
	print('Run this code snippets no matter what!!! ')
	print()

print('*****************************************************************************************')
print()

try:
	
	f = open('corrupt.txt')
	
	# if f.name == 'corrupt.txt':
		# raise Exception

except FileNotFoundError as e:
	print()
	print(e)

except Exception as e:
	print()
	print('Error! ')

else:
	print()
	print(f.read())
	f.close()

finally:
	print()
	print("Executing Finally...")

print()
print('End of program')
