person = {'Name': 'Paavan', 'Age': 27, 'Job': 'Programming'}
# person = {'Name': 'Paavan', 'Age': 27}

print()
# LBYL (Non-Pythonic)

if 'Name' in person and 'Age' in person and 'Job' in person:
	print("I'm {Name}. And my age is {Age} and my job is {Job}. ".format(**person))
else:
	print('Missing some keys!!!')

print()
print('****************************************************************************')
print()
# EAFP (Pythonic)

try:
	print("I'm {Name}. And my age is {Age} and my job is {Job}. ".format( **person ))

except KeyError as k:
	print("Missing {} key. ".format(k))
