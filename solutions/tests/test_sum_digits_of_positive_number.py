import unittest
from ..sum_digits_of_positive_number import sum_digits_of_positive_number

class TestSumDigitsOfPositiveNumber(unittest.TestCase):
    """
    Unit tests for the `sum_digits_of_positive_number` function.
    """

    def test_single_digit(self):
        """Tests single-digit numbers."""
        self.assertEqual(sum_digits_of_positive_number(5), 5)
        self.assertEqual(sum_digits_of_positive_number(0), 0)

    def test_multi_digit(self):
        """Tests multi-digit numbers."""
        self.assertEqual(sum_digits_of_positive_number(1234), 10)
        self.assertEqual(sum_digits_of_positive_number(222), 6)
        self.assertEqual(sum_digits_of_positive_number(9876), 30)

    def test_large_number(self):
        """Tests very large numbers."""
        self.assertEqual(sum_digits_of_positive_number(999999999), 81)

    def test_negative_number(self):
        """Tests negative numbers raise ValueError."""
        with self.assertRaises(ValueError):
            sum_digits_of_positive_number(-123)
