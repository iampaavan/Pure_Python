# Lists
my_lists = [1, 2, 3, 4, 5, 6, 7]
for a in my_lists:
	print(a)

copy_my_lists = my_lists[:]
print(copy_my_lists)

print()
print('********************************************')
print()

# Tuples
my_tuples = (0, 2, 4, 6, 8, 10)
for b in my_tuples:
	print(b)

print()
print('********************************************')
print()

# Dictionaries
my_dicts = {'Name': 'Paavan', 'Age': 27, 'Job': 'Programming'}
for key, value in my_dicts.items():
	print(f'My {key} is {value}')
# print(my_dicts.get('Name'))
# print(my_dicts.values())
print()
print('********************************************')
print()

# Sets
my_sets = {10, 20, 30, 40, 50, 60, 70}
for sets in my_sets:
	print(sets)

print()
print('********************************************')
print()


def fib(num):
	a, b = 0, 1
	for i in range(0, num):
		yield f'{i + 1}: {a}'
		a, b = b, a + b
		

for items in fib(10):
	print(items)
