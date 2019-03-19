import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s: %(name)s: %(message)s')

file_hander = logging.FileHandler('employee_1.log')
file_hander.setFormatter(formatter)

logger.addHandler(file_hander)

# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(levelname)s: %(name)s: %(message)s')


class Employee:
	"""A sample Employee Class"""
	
	def __init__(self, first, last):
		self.first = first
		self.last = last
		
		print(f'Created Employee: {self.fullname} - {self.email}')
		logger.info(f'Created Employee: {self.fullname} - {self.email}')
		
	@property
	def email(self):
		return f'{self.first}.{self.last}@email.com'
	
	@property
	def fullname(self):
		return f'{self.first} {self.last}'
	

emp_1 = Employee('Paavan', 'Gopala')
emp_2 = Employee('Bhushan', 'Gopala')
emp_3 = Employee('Ramakrishna', 'Gopala')
