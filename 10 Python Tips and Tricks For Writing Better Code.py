from getpass import getpass

# Tip 1
condition = True
x = 1 if condition else 0
print(x)

print('******************************************************')

# Tip 3
num1 = 10_000_000_000
num2 = 10_000_000
total = num1 + num2
print(f'{total:,}')

print('******************************************************')

# Tip 3
with open('common_words.txt', 'r') as file_reader:
    contents = file_reader.read()

words = contents.split(' ')
words_count = len(words)
print(f'{words_count:,} words')

print('******************************************************')

# Tip 4
names = ['Paavan', 'Bhushan', 'Nishanth', 'Prateek', 'Karthik']

for index, name in enumerate(names, start=1):
    print(index, name)

print('******************************************************')

# Tip 5
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}.")

print('******************************************************')

# Tip 6 --> Unpacking

a, _ = (1, 2)
print(a)

print('******************************************************')

a, b, *c = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)

print(f'*****************************************************')

a, b, *c, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(c)
print(d)

print(f'*****************************************************')

a, b, *_, d = (1, 2, 3, 4, 5)
print(a)
print(b)
print(d)

print(f'*****************************************************')

# Tip 7 --> Dynamically set the attributes


class Person:
    pass


person = Person()
first_key = 'first'
first_value = 'Paavan'

setattr(person, first_key, first_value)
first = getattr(person, first_key)
print(f'Person Name via setattr: {person.first}')
print(f"person Name via getattr: {first}")

print(f'*****************************************************')

person_info = {'first': 'Paavan', 'last': 'Gopala'}
for key, value in person_info.items():
    setattr(person, key, value)

print(person.first)
print(person.last)

print(f'*****************************************************')
for key in person_info.keys():
    print(getattr(person, key))

print(f'*****************************************************')

# Tip 8 --> GetPass

username = input(f"Username: ")
password = getpass(f"Password: ")

print(f"Logging In . . . . . ")

print(f'*****************************************************')

# Tip 9 --> Help

from datetime import datetime
print(help(datetime))
print(dir(datetime))