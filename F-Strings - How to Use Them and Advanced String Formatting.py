from datetime import datetime

first_name = 'Paavan'
last_name = 'Gopala'

print()
sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

print()
sentence_1 = f'My name is {first_name} {last_name}'
print(sentence_1)

print()
sentence_2 = f'My name is {first_name.upper()} {last_name.upper()}'
print(sentence_2)

print()
person = {'Name': 'Manju', 'Age': 28}
print('My friend\'s name is {} and her age is {}. '.format(person['Name'], person['Age']))

print()
person_1 = {'Name': 'Manju', 'Age': 28}
sentence_2 = f"My bestie\'s name is {person_1['Name']} and her age is {person_1['Age']}. "
print(sentence_2)

print()
calculation = f'4 times 11 is equal to {4 * 11}. '
print(calculation)

print()
for n in range(1, 11):
	# sentence_3 = f'The value of {n}'
	sentence_4 = f'The value of {n:02} with zero padding. '
	print(sentence_4)
	
print()
pi = 3.14159265
sentence_5 = f'Value of pi is {pi:.4f}'
print(sentence_5)

print()
birthday = datetime(1992, 10, 21)
sentence_6 = f'My birthday is on {birthday:%B %d, %Y}'
print(sentence_6)
