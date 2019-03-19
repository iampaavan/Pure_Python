import unittest
import calc

# python -m unittest test_calc.py


class TestCalc(unittest.TestCase):
	
	def test_add(self):
		# result = calc.add(10, 5)
		self.assertEqual(calc.add(10, 5), 15)
		self.assertEqual(calc.add(-1, 1), 0)
		self.assertEqual(calc.add(-2, -2), -4)
		
	def test_sub(self):
		# result = calc.sub(10, 5)
		self.assertEqual(calc.sub(10, 5), 5)
		self.assertEqual(calc.sub(-1, 1), -2)
		self.assertEqual(calc.sub(-2, -2), 0)
		
	def test_mul(self):
		# result = calc.mul(10, 5)
		self.assertEqual(calc.mul(10, 5), 50)
		self.assertEqual(calc.mul(-1, 1), -1)
		self.assertEqual(calc.mul(-2, -2), 4)
		
	def test_div(self):
		# result = calc.div(10, 5)
		self.assertEqual(calc.div(10, 5), 2)
		self.assertEqual(calc.div(-1, 1), -1)
		self.assertEqual(calc.div(-2, -2), 1)
		self.assertEqual(calc.div(5, 2), 2.5)
		
		# self.assertRaises(ValueError, calc.div, 10, 0)
		with self.assertRaises(ValueError):
			calc.div(10, 0)
		
		
# to run this module directly from here, use this (optional)
if __name__ == '__main__':
	unittest.main()

