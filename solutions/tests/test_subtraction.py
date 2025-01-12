"""This is the unittest for the subtraction function."""

import unittest

from solutions.subtraction import subtract


class TestSubtract(unittest.TestCase):
    """It should return the subtraction of positive numbers"""

    def test_subtract_positive_numbers(self):
        actual = subtract(10, 2, 3)
        expected = 5
        self.assertEqual(actual, expected)

    """It should return the subtraction of negative numbers"""

    def test_subtract_negative_numbers(self):
        actual = subtract(-10, -2, -3)
        expected = -5
        self.assertEqual(actual, expected)

    """It should return the subtraction of mixed numbers"""

    def test_subtract_mixed_numbers(self):
        actual = subtract(10, -20, -40, 50)
        expected = 20
        self.assertEqual(actual, expected)

    """It should return the subtraction of float numbers"""

    def test_subtract_float_numbers(self):
        actual = subtract(10.5, 2.5, 3.0)
        expected = 5.0
        self.assertEqual(actual, expected)

    """It should return the subtraction of zero numbers"""

    def test_subtract_zero_numbers(self):
        actual = subtract(0, 0, 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_no_arguments(self):
        """It should return 0 when no arguments are provided."""
        actual = subtract()
        expected = 0
        self.assertEqual(actual, expected)

    def test_single_argument(self):
        """It should return the single argument when only one is provided."""
        actual = subtract(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_invalid_input_string(self):
        """It should raise a TypeError for string input."""
        with self.assertRaises(TypeError):
            subtract(10, "string")

    def test_invalid_input_none(self):
        """It should raise a TypeError for None as an input."""
        with self.assertRaises(TypeError):
            subtract(10, None)

    def test_invalid_input_mixed(self):
        """It should raise a TypeError for mixed valid and invalid inputs."""
        with self.assertRaises(TypeError):
            subtract(10, 2, "invalid", 5)
