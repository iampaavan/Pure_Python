import unittest
from my_employee import Employee
from company_employee import Employee
from unittest.mock import patch


class TestMyEmployee(unittest.TestCase):
	
	@classmethod
	def setUpClass(cls):
		print('setupClass')
		
	@classmethod
	def tearDownClass(cls):
		print('teardownClass')
	
	def setUp(self):
		print('setUp')
		self.emp_1 = Employee('Paavan', 'Gopala', 80000)
		self.emp_2 = Employee('Bhushan', 'Gopala', 120000)
	
	def tearDown(self):
		print('tearDown')
	
	def test_email(self):
		print('test_email')
		self.assertEqual(self.emp_1.email, 'Paavan.Gopala@email.com')
		self.assertEqual(self.emp_2.email, 'Bhushan.Gopala@email.com')
		
		self.emp_1.first = 'Test_1'
		self.emp_2.first = 'Test_2'
		
		self.assertEqual(self.emp_1.email, 'Test_1.Gopala@email.com')
		self.assertEqual(self.emp_2.email, 'Test_2.Gopala@email.com')
	
	def test_fullname(self):
		print('test_fullname')
		self.assertEqual(self.emp_1.fullname, 'Paavan Gopala')
		self.assertEqual(self.emp_2.fullname, 'Bhushan Gopala')
		
		self.emp_1.first = 'Test_1'
		self.emp_2.first = 'Test_2'
		
		self.assertEqual(self.emp_1.fullname, 'Test_1 Gopala')
		self.assertEqual(self.emp_2.fullname, 'Test_2 Gopala')
	
	def test_applyraise(self):
		print('test_applyraise')
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()
		
		self.assertEqual(self.emp_1.pay, 84000)
		self.assertEqual(self.emp_2.pay, 126000)
		
	def test_monthly_schedule(self):
		with patch('company_employee.requests.get') as mocked_get:
			mocked_get.return_value.ok = True
			mocked_get.return_value.text = 'Success'
			
			schedule = self.emp_1.monthly_schedule('May')
			mocked_get.assert_called_with('http://company.com/Gopala/May')
			self.assertEqual(schedule, 'Success')
			
			mocked_get.return_value.ok = False
			# mocked_get.return_value.text = 'Success'
			
			schedule = self.emp_2.monthly_schedule('June')
			mocked_get.assert_called_with('http://company.com/Gopala/June')
			self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
	unittest.main()
