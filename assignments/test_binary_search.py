import unittest
import binary_search

class test_binary_search(unittest.TestCase):

    def test_binary_search_returns_true_when_search_key_found(self):
        self.assertTrue(binary_search.binary_search([3, 1, 2], 2))

    def test_binary_search_returns_false_when_search_key_not_found(self):
        self.assertFalse(binary_search.binary_search([3, 1, 2], 0))
