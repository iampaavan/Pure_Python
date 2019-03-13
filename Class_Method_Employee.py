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

	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-80000'
emp_str_3 = 'Jane-Doe-90000'


print()

print('Initial Employees: ', Employee.num_of_employees)

emp_1 = Employee('paavan', 'gopala', 50000)
emp_2 = Employee('manjula', 'subramanyamachary', 60000)
emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
emp_5 = Employee.from_string(emp_str_3)

print('After a while: ', Employee.num_of_employees)

print()
print('****************************************************')

print(emp_4.fullname())
print(emp_4.pay)