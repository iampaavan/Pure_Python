# Python Object-Oriented Programming


class Test():
	pass


test_1 = Test()
test_2 = Test()

print(test_1)
print(test_2)

test_1.first = 'test 1'
test_1.last = 'user 1'
test_1.email = 'test 1.user 1@company.com'
test_1.salary = 50000

test_2.first = 'test 2'
test_2.last = 'user 2'
test_2.email = 'test 2.user 2@company.com'
test_2.salary = 60000

print(test_1.email)
print(test_2.email)


print()
print('*******************************************************')


class Employee:
	def __init__(self, first, last, salary):
		self.first = first
		self.last = last
		self.email = '{}.{}@company.com'.format(first, last)
		self.salary = salary
		
	def fullname(self):
		return '{} {}'.format(self.first, self.last)


emp_1 = Employee('paavan', 'gopala', 50000)
emp_2 = Employee('manjula', 'subramanyamachary', 60000)

print(emp_1.email)
print(Employee.fullname(emp_1))
print()
print(emp_2.email)
print(Employee.fullname(emp_2))
print()
print('Full Name: ', emp_1.fullname())
print(Employee.fullname(emp_1))
print()
print('Full Name: ', emp_2.fullname())
print(Employee.fullname(emp_2))


