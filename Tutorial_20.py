nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('My old list is: ', nums)

# We want 'n' for each 'n' in nums

my_list_1 = []

for i in nums:
	my_list_1.append(i)

print()
print('My newly created list is: ', my_list_1)
print()
print('**************************************************')
print()

my_list_2 = []

for j in nums:
	my_list_2.append(j * j)

print('Square of numbers between 1 and 10: ', my_list_2)
print()
print('**************************************************')
print()

my_list_3 = [k for k in nums]
print('Simplest comprehension: ', my_list_3)

print()
print('**************************************************')
print()

my_list_4 = [l * l for l in nums]
print(my_list_4)
print()
print('**************************************************')

# using map + lambda
my_list_5 = list(map(lambda m: m * m, nums))
print()
print('Square of numbers between 1 and 10 using map and lambda: ', my_list_5)
print()
# We want 'n' for each 'n' in nums if n is even
print('**************************************************')

my_list_6 = []

for n in nums:
	if n % 2 == 0:
		my_list_6.append(n)
print()
print('List of even numbers: ', my_list_6)
print()

print('**************************************************')
print()

my_list_7 = list(filter(lambda o: o % 2 == 0, nums))
print('Using Filter and Lambda, List of even numbers are: ', my_list_7)
print()


print('**************************************************')
print()

my_list_8 = [p for p in nums if p % 2 == 0]
print('Using comprehension, List of even numbers is: ', my_list_8)
print()

print('**************************************************')

print()

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'

my_list_9 = []

for letter in 'abcd':
	for nums in range(4):
		my_list_9.append((letter, nums))

print('Letter & Number Pairs: ', my_list_9)

print()
print('**************************************************')
print()

my_list_10 = [(letter, nums) for letter in 'abcd' for nums in range(4)]
print('Using Comprehension, Letter & Number Pairs are: ', my_list_10)

print()
print('**************************************************')
print()

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
my_list_11 = list(zip(names, heroes))
print(my_list_11)

print()
print('**************************************************')
print()

# I want a dict {'name': 'hero'} for each name, hero in zip(names, heroes)
my_list_12 = {}

for name, hero in zip(names, heroes):
	my_list_12[name] = hero
	
print('Using traditional For Loop: ', my_list_12)

print()
print('**************************************************')
print()

my_list_13 = {name: hero for name, hero in zip(names, heroes)}
print('Using Dictionary Comprehension: ', my_list_13)

print()
print('**************************************************')
print()


# set comprehensions
numbers = []



