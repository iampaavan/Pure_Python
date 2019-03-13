import datetime


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

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True
	
		
emp_1 = Employee('paavan', 'gopala', 50000)
emp_2 = Employee('manjula', 'subramanyamachary', 60000)

my_date = datetime.date(2019, 3, 17)
print(Employee.is_workday(my_date))
