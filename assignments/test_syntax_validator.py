import unittest
import syntax_validator

class test_syntax_validator(unittest.TestCase):

    def test_is_valid_username_returns_true_given_valid_input(self):
        self.assertTrue(syntax_validator.is_valid_username('Abcdefg1'))

    def test_is_valid_username_returns_false_given_invalid_input(self):
        self.assertFalse(syntax_validator.is_valid_username('abcdefg1'))

    def test_is_valid_us_zip_code_returns_true_given_valid_input(self):
        self.assertTrue(syntax_validator.is_valid_us_zip_code('55555'))

    def test_is_valid_us_zip_code_returns_false_given_invalid_input(self):
        self.assertFalse(syntax_validator.is_valid_us_zip_code('5555'))
