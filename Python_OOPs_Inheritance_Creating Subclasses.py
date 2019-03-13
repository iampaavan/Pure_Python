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


class Developers(Employee):
	raise_amount = 1.10
	
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		# Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang
		

class Manager(Employee):
	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
			
	def print_emp(self):
		for emp in self.employees:
			print('-->', emp.fullname())
			

emp_1 = Employee('Employee', 'Check', 50000)
# dev_1 = Developers('Paavan', 'Gopala', 85000)
# dev_2 = Developers('Test', 'User', 90000)
dev_1 = Developers('Paavan', 'Gopala', 85000, 'Python')
dev_2 = Developers('Test', 'User', 90000, 'Java')
# print(help(Deveopers))
# print(dev_2.email)
# print(dev_1.email)

print(dev_1.raise_amount)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print()
print('*************************************************')
print()

print(emp_1.raise_amount)
print(emp_1.pay)


print()
print('*************************************************')

print(dev_1.prog_lang)
print(dev_2.prog_lang)

print()
print('*************************************************')

mgr_1 = Manager('Asvini', 'Yekkelli', 100000, [dev_1, dev_2])
print(mgr_1.email)
mgr_1.add_emp(emp_1)
mgr_1.print_emp()

print()
print('*************************************************')

mgr_1.remove_emp(dev_2)
mgr_1.print_emp()

print()
print('*************************************************')

print(isinstance(mgr_1, Developers))
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))

print()
print('*************************************************')

print(issubclass(Developers, Employee))
print(issubclass(Manager, Employee))

print()
print('*************************************************')

