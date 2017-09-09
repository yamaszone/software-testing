import unittest
from python.src import grader

class test_grader(unittest.TestCase):
	def test_calculate_returns_A(self):
		self.assertEqual('B', grader.calculate(95))
		
	def test_calculate_returns_B(self):
		self.assertEqual('B', grader.calculate(90))

	def test_calculate_returns_C(self):
		self.assertEqual('C', grader.calculate(75))
				
	def test_calculate_returns_None(self):
		self.assertEqual('F', grader.calculate(5))