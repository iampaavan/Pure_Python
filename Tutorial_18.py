"""LEBG, Local, Enclosing, Global, and Built-In"""
import builtins
import winsound


print(dir(builtins))

print()
x = 'Global x'

print('*************** Default Test Method **************')


def test():
	y = 'Local y'
	print(y)
	print(x)

	
test()
# print(y) # --> not found in local, enclosing, global or built-in scope
print(x)

print('*************** Test Method 1 **************')


def test_1():
	x = 'local x'
	print(x)
	
test_1()
print(x)

print('*************** Test Method 2 **************')


def test_2():
	global x
	x = 'Local x'
	print(x)

	
test_2()
print(x)


print('*************** Test Method 3 **************')


def test_3(z):
	x = 'local x'
	print(z)
	

test_3('My String')
print(x)

m = min([5, 4, 3, 8, 9])
print(m)


print('*************** Test Method 4 **************')


def outer():
	a = 'outer a'

	def inner():
		a = 'inner a'
		print(a)
		
	inner()
	print(a)
	
	
outer()


print('*************** Test Method 5 **************')


def outer_1():
	a = 'outer a'
	
	def inner_1():
		nonlocal a
		a = 'inner a'
		print(a)
	
	inner_1()
	print(a)


outer_1()

winsound.Beep(9000, 1000)






