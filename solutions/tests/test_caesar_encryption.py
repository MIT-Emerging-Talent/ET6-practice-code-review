import unittest

from ..caesar_encryption import caesar_encryption


class TestSequencedList(unittest.TestCase):
    """ """

    def test_non_alpha_characters(self):
        """ """
        actual = caesar_encryption("Hello, World!", 3)
        expected = "Khoor, Zruog!"
        self.assertEqual(actual, expected)

    def test_negative_shift(self):
        """ """
        actual = caesar_encryption("ABC", -1)
        expected = "ZAB"
        self.assertEqual(actual, expected)

    def test_no_shift(self):
        """ """
        actual = caesar_encryption("abc", 0)
        expected = "abc"
        self.assertEqual(actual, expected)

    def test_negative_numbers_list(self):
        """ """
        actual = caesar_encryption("Python 3.9!", 5)
        expected = "Udymts 3.9!"
        self.assertEqual(actual, expected)

