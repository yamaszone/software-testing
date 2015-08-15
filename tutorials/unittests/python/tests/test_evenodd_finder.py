import unittest
from python.src import evenodd_finder

class test_evenodd_finder(unittest.TestCase):

	def test_is_even_returnsTrue_givenEvenInputs(self):
		self.assertTrue(evenodd_finder.is_even(2))
		self.assertTrue(evenodd_finder.is_even(4))
		self.assertTrue(evenodd_finder.is_even(0))
		self.assertTrue(evenodd_finder.is_even(1000000))
		self.assertTrue(evenodd_finder.is_even(12345678))

	def test_is_even_returnsFalse_givenOddInputs(self):
		self.assertFalse(evenodd_finder.is_even(1))
		self.assertFalse(evenodd_finder.is_even(3))
		self.assertFalse(evenodd_finder.is_even(1000001))

	def test_is_even_returnsThrowsException_givenTypeMismatch(self):
		with self.assertRaises(TypeError):
		    evenodd_finder.is_even('a')
		    evenodd_finder.is_even()