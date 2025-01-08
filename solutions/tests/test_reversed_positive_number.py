import unittest
from ..reversed_positive_number import reversed_positive_number


class TestReversedPositiveNumber(unittest.TestCase):
    """
    Unit tests for the `reversed_positive_number` function.
    """

    def test_positive_number(self):
        """Tests reversing a positive integer."""
        self.assertEqual(reversed_positive_number(123), 321)

    def test_single_digit(self):
        """Tests reversing a single-digit integer."""
        self.assertEqual(reversed_positive_number(7), 7)

    def test_zero(self):
        """Tests reversing zero."""
        self.assertEqual(reversed_positive_number(0), 0)

    def test_leading_zeros(self):
        """Tests reversing a number with leading zeros."""
        self.assertEqual(reversed_positive_number(100), 1)

    def test_invalid_negative_number(self):
        """Tests handling of a negative input."""
        with self.assertRaises(ValueError):
            reversed_positive_number(-123)
