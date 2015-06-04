import unittest
from python.src import coverage_demo

class test_coverage_demo(unittest.TestCase):

	def test_foo_returns_true(self):
		self.assertTrue(coverage_demo.foo(1))

	def test_foo_returns_false(self):
		self.assertFalse(coverage_demo.foo(0))

"""
	def test_foo_throws_exception(self):
		#self.assertFalse(coverage_demo.foo(0----0))
		self.assertRaises(TypeError, coverage_demo.foo(0----0))

"""