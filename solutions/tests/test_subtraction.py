"""
Unit tests for the subtraction function.
"""

import unittest

from ..subtract import subtract  # type: ignore


class TestSubtract(unittest.TestCase):  # noqa: F821
    """
    Test cases for the subtraction function.
    """

    def test_subtract_positive_numbers(self):
        """It should return the subtraction of positive numbers"""
        actual = subtract(10, 2, 3)
        expected = 5
        self.assertEqual(actual, expected)

    def test_subtract_negative_numbers(self):
        """It should return the subtraction of negative numbers"""
        actual = subtract(-10, -2, -3)
        expected = -5
        self.assertEqual(actual, expected)

    def test_subtract_mixed_numbers(self):
        """It should return the subtraction of mixed numbers"""
        actual = subtract(10, -20, -40, 50)
        expected = 20
        self.assertEqual(actual, expected)

    def test_subtract_float_numbers(self):
        """It should return the subtraction of float numbers"""
        actual = subtract(10.5, 2.5, 3.0)
        expected = 5.0
        self.assertEqual(actual, expected)

    def test_subtract_zero_numbers(self):
        """It should return the subtraction of zero numbers"""
        actual = subtract(0, 0, 0)
        expected = 0
        self.assertEqual(actual, expected)
