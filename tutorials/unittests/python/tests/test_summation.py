import unittest
from python.src import summation

class test_summation(unittest.TestCase):

	def test_find_sum(self):
		self.assertEqual(0, summation.find_sum(0))
		self.assertEqual(1, summation.find_sum(1))
		self.assertEqual(3, summation.find_sum(2))
		self.assertEqual(5050, summation.find_sum(100))
