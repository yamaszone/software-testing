import unittest
from python.src import largest_number_finder

class test_largest_number_finder(unittest.TestCase):

	def test_a_largest(self):
		self.assertEqual(10, largest_number_finder.find(5,2,3))
		self.assertEqual(5, largest_number_finder.find(5,3,2))

	def test_b_largest(self):
		self.assertEqual(5, largest_number_finder.find(2,5,3))
		self.assertEqual(5, largest_number_finder.find(5,3,2))

	def test_c_largest(self):
		self.assertEqual(5, largest_number_finder.find(2,3,5))
		self.assertEqual(5, largest_number_finder.find(5,3,2))

	def test_none_largest(self):
		self.assertEqual(2, largest_number_finder.find(2,2,2))
		self.assertEqual(3, largest_number_finder.find(2,3,2))
