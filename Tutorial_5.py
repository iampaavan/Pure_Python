student = {'name': 'Paavan', 'age': '27', 'courses': ['Java', 'Cloud']}
print(student['name'])
print(student['age'])
print(student['courses'])

student_1 = {1: 'Paavan', 'age': '27', 'courses': ['Java', 'Cloud']}
print(student_1[1])

# try to access a key not present in the dictionary
print(student_1.get('phone'))  # by default --> returns 'None' if the key isn't present

# customized return value if key isn't present
print(student_1.get('phone', 'Not Found'))

student_2 = {1: 'Paavan', 'age': '27', 'courses': ['Java', 'Cloud']}
student_2['phone'] = '857-230-8401'
print(student_2.get('phone', 'Not Found'))

student_3 = {'name': 'Suha', 'age': '23', 'courses': ['Java', 'Cloud']}
print(student_3)
student_3.update({'name': 'Manju', 'age': '27', 'phone': '962-056-4856'})
print(student_3)

del student_2['age']
print(student_2)

phone = student_2.pop('phone')
print(phone)
print(student_2)

print(len(student_3))
print(student_3.values())
print(student_3.items())

for key in student_3:
	print(key)

for key, value in student_3.items():
	print(key, ":", value)

