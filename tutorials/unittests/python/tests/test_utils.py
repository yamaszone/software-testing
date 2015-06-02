import unittest
from python.src import utils

class test_utils(unittest.TestCase):

	def test_add(self):
		self.assertEqual(5, utils.add(2,3))

	def test_divide(self):
		self.assertEqual(2, utils.divide(4,2))

class Test_Calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(5, utils.Calculator().add(2, 3))