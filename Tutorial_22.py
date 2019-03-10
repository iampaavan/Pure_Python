import  datetime
person = {'Name': 'Paavan', 'Age': 27, 'Job': 'Programming'}

sentence = 'My name is ' + person['Name'] + ' and my age is ' + str(person['Age']) + ' and my job is ' + person['Job']
print('Using Traditional way: ', sentence)

print()
print('*************************************')
print()

sentence_1 = 'My name is {}, my age is {}, and my Job is {}'.format(person['Name'], person['Age'], person['Job'])
print('Using Place-Holders: ', sentence_1)

print()
print('*************************************')
print()

sentence_2 = 'My name is {0}, my age is {1}, and my Job is {2}'.format(person['Name'], person['Age'], person['Job'])
print('Using Place Holders with index: ', sentence_2)

print()
print('*************************************')
print()

tag = 'hi'
text = 'This is a header-line'

sentence_3 = '<{0}> {1} </{0}>'.format(tag, text)
print(sentence_3)

print()
print('*************************************')
print()

sentence_4 = 'My name is {0[Name]}, my Age is {1[Age]}, and my Job is {2[Job]}'.format(person, person, person)
print('Using Place Holders with index and adjacent values: ', sentence_4)

print()
print('*************************************')
print()

sentence_5 = 'My Name is {0[Name]}, my Age is {0[Age]}, and my Job is {0[Job]}'.format(person)
print('Using Place Holders with index and adjacent values, with single Dictionary: ', sentence_5)

print()
print('*************************************')
print()


my_list = ['Jane', 25]
print('My List Contents: ', my_list)

sentence_6 = 'My name is {0[0]} and my Age is {0[1]}'.format(my_list)
print(sentence_6)

print()
print('*************************************')
print()

class Person():
	
	def __init__(self, name, age):
		self.name = name
		self.age = age
		

sentence_7 = 'My name is {name}, and my age is {age}'.format(name='Paavan', age=27)
print(sentence_7)


print()
print('*************************************')
print()

person_1 = Person('Manju', 28)
sentence_8 = 'My bestie\'s name is {0.name}, and her age is {0.age}'.format(person_1)
print(sentence_8)

print()
print('*************************************')
print()

person_2 = {'Name': 'Thilak', 'Age': 29, 'Job': 'Musician'}
sentence_9 = 'My friend\'s name is {Name}, and his age is {Age}, and his job is {Job}'.format(**person_2)
print(sentence_9)

print()
print('*************************************')
print()

for a in range(1, 11):
	sentence_10 = 'The value is {:02} '.format(a)
	print(sentence_10)
	
print()
print('*************************************')
print()

pi = 3.14159265
sentence_11 = 'Pi is equal to {:.03f} '.format(pi)
print(sentence_11)

print()
print('*************************************')
print()

sentence_12 = '1MB is equal to {:,.2f}'.format(1000 ** 2)
print(sentence_12)

print()
print('*************************************')
print()

my_date = datetime.datetime(2016, 9, 26, 12, 30, 45)
print(my_date)

print()
print('*************************************')
print()

sentence_13 = '{:%B %d, %Y}'.format(my_date)
print(sentence_13)

print()
print('*************************************')
print()

sentence_14 = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} of the year'.format(my_date)
print(sentence_14)

