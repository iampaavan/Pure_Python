if True:
	print('Inside if --> True - Condition')
	
if False:
	print('Inside if --> False - Condition')

language = 'Java'

if language == 'Python':
	print('Language is Python')
	
elif language == 'Java':
	print('Language is Java')

elif language == 'JavaScript':
	print('Language is JavaScript')
	
else:
	print('No Match')

print()

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
	print('Admin Page. ')

else:
	print('Bad Request. ')

print()

user_1 = 'Practise Lead'
logger = False

if user_1 == 'Practise Lead' or logger:
	print('Login Page.')
	
else:
	print('Bad Credentials')

print()

name = 'Admin'
log_in = False

if not log_in:
	print('Please LogIn')
	
else:
	print('Welcome')

print()

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("ID of a is: ", id(a))
print("ID of b is: ", id(b))
print("ID of c is: ", id(c))

print()

print("A is equal to B: ", a == b)
print("A is B: ", a is b)
print("A is equal to C: ", a == c)
print("A is C: ", a is c)
print("A is C: ", id(a) == id(c))
print()

# False Values are as follows:
# False
# None
# Zero of any numeric type
# Any empty sequence, for example: '', (), [].
# Any empty mapping, for example: {}.

condition_1 = False

if condition_1:
	print('Evaluated to True')

else:
	print('False: ', 'Evaluated to False')
	
print('******************')

condition_2 = None

if condition_2:
	print('Evaluated to True')

else:
	print('None: ', 'Evaluated to False')

print('*************************')

condition_3 = 0

if condition_3:
	print('Evaluated to True')

else:
	print('Zero of any data type: ', 'Evaluated to False')

print('**************************')

condition_4 = ''

if condition_4:
	print('Evaluated to True')

else:
	print('Empty String: ', 'Evaluated to False')

print('***************************')

condition_5 = ()

if condition_5:
	print('Evaluated to True')

else:
	print('Empty Tuple: ', 'Evaluated to False')
	
print('**********************')

condition_6 = []

if condition_6:
	print('Evaluated to True')

else:
	print('Empty List: ', 'Evaluated to False')
	
print('**************************')

condition_7 = {}

if condition_7:
	print('Evaluated to True')

else:
	print('Empty Dictionary: ', 'Evaluated to False')

condition_8 = 'Test'

if condition_8:
	print('Some String: ', 'Evaluated to True')

else:
	print('Evaluated to False')

