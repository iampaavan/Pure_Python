def hello_func():
	pass


print(hello_func())


def func_call():
	print('Inside function. ')

	
func_call()
func_call()
func_call()
func_call()


def hello():
	return "Hi Peeps. "


print(hello())
print(hello().upper())
print(hello().lower())


def dev(greeting):
	return '{} Function'.format(greeting)
	
	
print(dev('Parameterized'))


def test(greeting, name='You'):
	return '{}, {}'.format(greeting, name)


print(test(greeting='Hey', name='There'))
print(test('Hello', name='Paavan'))
	

def student_info(*args, **kwargs):
	print(args)
	print(kwargs)
	

student_info('Maths', 'Science', name='Paavan', age=27)


def student(*args, **kwargs):
	print(args)
	print(kwargs)
	

courses = ['Maths', 'Science']
info = {'Name': 'Manju', 'Age': 27}

student(courses, info)
student(*courses, **info)

def tester(*args, **kwargs):
	print(args)
	print(kwargs)

	
cricket = ['India', 'Australia', 'South Africa', 'England']
players = {'India': 'Virat Kohli', 'Australia': 'Maxwell', 'South Africa': 'ABD', 'England': 'Buttler'}

tester(cricket, players)
tester(*cricket, **players)




