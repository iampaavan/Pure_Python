# list of courses
courses = ['History', 'Geography', 'Social', 'Maths', 'CompScience']
print('Index position of History is: ', courses.index('History'))

# find the length of the list
print(len(courses))

# access specific elements in the list
print(courses[0])
print(courses[3])
print(courses[len(courses) - 1])

# access certain elements in the list
print(courses[0:3])
print(courses[:3])

# grab the last 2 elements in the list
print(courses[(len(courses) - 2):])
print(courses[3:])

courses.append('Electronics')
print(courses)

courses.insert(1, 'Games')
print(courses)

courses_1 = ['A', 'B']
courses.extend(courses_1)

print(courses_1)
print(courses)

courses.remove('A')
popped = courses.pop()

print(courses)
print(popped)

courses.reverse()
print(courses)

courses.sort()
print(courses)

sorted_1 = [1, 5, 2, 0, 9, 6]
sorted_1.sort()
print(sorted_1)

sorted_1.sort(reverse=True)
print(sorted)

courses.sort(reverse=True)
print(courses)

sample = [5, 8, 0, 5, 9]
sample.sort()
print(sample)

example = ['a', 'z', 'b', 's']
ex = sorted(example)
print(ex)

s1 = [1, 0, 5, 2, 7]
print(s1)
s1.sort()
print(s1)

s1.sort(reverse=True)
print(s1)

s2 = [1, 5, 4, 3, 2]
print(s2)

print("Minimum value of the list is: ", min(s2))
print("Maximum value of the list is: ", max(s2))
print("Sum of the list is: ", sum(s2))

subjects = ["Java", "Data Networks", "Connected Devices", "Cloud Computing"]
print("Index value of Connected Devices is: ", subjects.index("Connected Devices"))

print('Java' in subjects)
print('abc' in subjects)

print()

fsociety = ['Elliot', 'Darlene', 'Angella Mose', 'Tyrell']

for person in fsociety:
	print(person)
	
print("**********************************")
	
for index, persons in enumerate(fsociety):
	print(index, person)

print()

for i, p in enumerate(fsociety, start=1):
	print(i, p)

print()
print(fsociety)

fsociety_str = ', '.join(fsociety)
print(fsociety_str)

fsociety_hyphen = ' - '.join(fsociety)
print(fsociety_hyphen)

new_list = fsociety_hyphen.split(' - ')
print(new_list)

list_1 = ['Apple', 'Cannabis', 'Cucumber', 'Grapes']
list_2 = list_1

print("Tuples *********************************")

print(list_1)
print(list_2)

list_1[0] = 'Ancient Apps'
print(list_1)
print(list_2)

tuples_1 = ('Accenture', 'CTS', 'Deloitte', 'Amazon', 'Apple')
tuples_2 = tuples_1

print(tuples_1)
print(tuples_2)

# Tuples are immutable, hence can't append or remove or basically cannot to mutable process on tuples

# tuples_1[0] = 'Art'

# sets

set_1 = {'Paavan', 'Manju', 'Thilak', 'Suu', 'Ashuuu'}
print(set_1)

print('A' in set_1)
print('Manju' in set_1)

set_2 = {'Paavan', 'Manju', 'abc', 'Suu', 'xyz'}

print(set_1.intersection(set_2))
print(set_1.difference(set_2))

print(set_1.union(set_2))

# Empty lists
empty_list_1 = []
empty_list_2 = list()

# Empty Tuples
empty_tuple_1 = ()
empty_tuple_2 = tuple()

# Empty set
empty_set_1 = {}  # wrong way!!! it creates an empty dictionary
empty_set_2 = set()
