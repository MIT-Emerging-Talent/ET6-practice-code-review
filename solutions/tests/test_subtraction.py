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
