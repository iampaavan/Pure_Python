class Employee:
	num_of_employees = 0
	raise_amount = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = '{}.{}@company.com'.format(first, last)
		self.pay = pay
		Employee.num_of_employees += 1
	
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)
		# self.pay = int(self.pay * Employee.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount


print()
print('Initial Employees: ', Employee.num_of_employees)
emp_1 = Employee('paavan', 'gopala', 50000)
emp_2 = Employee('manjula', 'subramanyamachary', 60000)
print('After a while: ', Employee.num_of_employees)
print()
print('****************************************************')

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(emp_1.pay)
print(emp_1.raise_amount)
emp_1.raise_amount = 1.10
print(emp_1.raise_amount)
emp_1.apply_raise()
print(emp_1.pay)