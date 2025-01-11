"""
Module represents unit test for fist_and_last_same

Created on 01/07/2025
Author Svitlana Musiienko
"""

import unittest

from ..first_and_last_same import first_and_last_same


class TestFirstAndLastSame(unittest.TestCase):
    """Test the first_and_last_same function"""

    def test_true(self):
        """It should return True"""
        actual = first_and_last_same([1, 2, 3, 1])
        self.assertEqual(actual, True)

    def test_false(self):
        """It should return False"""
        actual = first_and_last_same([1, 2, 3, 4])
        self.assertEqual(actual, False)

    def test_empty(self):
        """It should print 'The list is empty'"""
        actual = first_and_last_same([])
        expected = print("The list is empty")
        self.assertEqual(actual, expected)

    def test_only_numbers(self):
        """It should print 'The list must contain only numbers'"""
        actual = first_and_last_same([1, "a", 3, 1])
        expected = print("The list must contain only numbers")
        self.assertEqual(actual, expected)

    def test_float(self):
        """Check floats numbers"""
        actual = first_and_last_same([1.5, 2.3, 3.5, 1.5])
        self.assertEqual(actual, True)


if __name__ == "__main__":
    unittest.main()
