"""
Unit tests for is_even_number function.
"""

import unittest
from solutions.is_even_number import is_even_number


class TestIsEvenNumber(unittest.TestCase):
    """
    Test cases for the is_even_number function.
    """

    def test_even_number(self):
        """
        Test that the function correctly identifies an even number.
        """
        self.assertTrue(is_even_number(4), "4 should be even.")

    def test_odd_number(self):
        """
        Test that the function correctly identifies an odd number.
        """
        self.assertFalse(is_even_number(5), "5 should be odd.")

    def test_zero(self):
        """
        Test that the function correctly identifies zero as even.
        """
        self.assertTrue(is_even_number(0), "0 should be even.")

    def test_negative_even(self):
        """
        Test that the function correctly identifies a negative even number.

        """
        self.assertTrue(is_even_number(-8), "-8 should be even.")

    def test_negative_odd(self):
        """
        Test that the function correctly identifies a negative odd number.

        """
        self.assertFalse(is_even_number(-3), "-3 should be odd.")

    def test_non_integer(self):
        """
        Test that the function raises an AssertionError for non-integer inputs.

        """
        with self.assertRaises(AssertionError):
            is_even_number(4.5)

    def test_string_input(self):
        """
        Test that the function raises an AssertionError for string inputs.

        """
        with self.assertRaises(AssertionError):
            is_even_number("string")


if __name__ == "__main__":
    unittest.main()
