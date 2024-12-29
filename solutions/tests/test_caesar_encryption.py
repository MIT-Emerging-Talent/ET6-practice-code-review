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


