class Employee:
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = '{}.{}@company.com'.format(first, last)
		self.pay = pay
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	def __repr__(self):
		return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)
	
	def __str__(self):
		return "{} - {}".format(self.fullname(), self.email)

	def __add__(self, other):
		return self.pay + other.pay
	
	def __len__(self):
		return len(self.fullname())


emp_1 = Employee('Paavan', 'Gopala', 75000)
emp_2 = Employee('Test', 'User', 80000)

print()
print(emp_1)

print()
print('*************************************************')

print(repr(emp_1))
print(str(emp_1))

print()
print('*************************************************')

print(emp_1.__repr__())
print(emp_1.__str__())

print()
print('*************************************************')

print(1 + 2)
print(int.__add__(1, 2))

print()
print('*************************************************')

print('a' + 'b')
print(str.__add__('a', 'b'))

print()
print('*************************************************')

print(emp_1 + emp_2)

print()
print('*************************************************')

print(len('test'))
print('test'.__len__())

print()
print('*************************************************')

print(len(emp_1))
print(len(emp_2))

print()
print('*************************************************')

