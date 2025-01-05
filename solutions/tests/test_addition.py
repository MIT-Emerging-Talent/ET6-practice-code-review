
import unittest

from solutions.addition import sum


class TestSum(unittest.TestCase):
    def test_sum_positive_numbers(self):
        """It should return the sum of a positive numbers"""
        actual = sum(1, 2, 3, 4, 5)  # noqa: F841
        expected = 15  # noqa: F841
        self.assertEqual(actual, expected)  # noqa: F821

    def test_sum_negative_numbers(self):
        """It should return the sum of a negative numbers"""
        actual = sum(-1, -2, -3, -5)  # noqa: F841
        expected = -11
        self.assertEqual(actual, expected)

    def test_sum_mixed_numbers(self):
        """It should return the sum of a mix numbers"""

        actual = sum(10, -20, -40, 50)
        expected = 0
        self.assertEqual(actual, expected)

    def test_sum_float_numbers(self):
        """It should return the sum of a float numbers"""

        actual = sum(1.5, 2.5, 3.7, 4.5)
        expected = 12.2
        self.assertEqual(actual, expected)

    def test_sum_zero_numbers(self):
        """It should return the sum of zero numbers"""
        actual = sum(0, 0, 0, 0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_sum_single_argument(self):
        """It should return the single argument when only one is provided."""
        actual = sum(10)
        expected = 10
        self.assertEqual(actual, expected)

    def test_sum_no_arguments(self):
        """It should return 0 when no arguments are provided."""
        actual = sum()
        expected = 0
        self.assertEqual(actual, expected)

    def test_invalid_input_string(self):
        """It should raise a TypeError for string input."""
        with self.assertRaises(TypeError):
            sum(1, 2, "string", 4)

    def test_invalid_input_none(self):
        """It should raise a TypeError for None as an input."""
        with self.assertRaises(TypeError):
            sum(1, None, 3)

    def test_invalid_input_mixed(self):
        """It should raise a TypeError for mixed valid and invalid inputs."""
        with self.assertRaises(TypeError):
            sum(10, 5, "invalid", 2)
