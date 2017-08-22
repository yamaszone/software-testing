import unittest
import util

class test_util(unittest.TestCase):

    def test_get_state_by_code(self):
        self.assertEqual('California', util.get_state_by_code('CA'))
