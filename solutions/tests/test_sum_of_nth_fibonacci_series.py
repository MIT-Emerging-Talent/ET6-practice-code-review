"""
Test cases for the `sum_of_nth_fibonacci_series` function.

This module contains unit tests for verifying the functionality of the
`sum_of_nth_fibonacci_series` function, which computes the sum of the
first n Fibonacci numbers.

@author: Yonatan Y. Yifat
"""

import unittest

from solutions.sum_of_nth_fibonacci_series import sum_of_nth_fibonacci_series


class TestSumOfNthFibonacciSeries(unittest.TestCase):
    """Test suite for the sum_of_nth_fibonacci_series function."""

    # Standard test cases
    def test_zero_terms(self):
        """It should return 0 for n = 0 (no terms to sum)."""
        self.assertEqual(sum_of_nth_fibonacci_series(0), 0)

    def test_single_term(self):
        """It should return 0 for n = 1 (only the first term)."""
        self.assertEqual(sum_of_nth_fibonacci_series(1), 0)

    def test_two_terms(self):
        """It should return 1 for n = 2 (0 + 1)."""
        self.assertEqual(sum_of_nth_fibonacci_series(2), 1)

    def test_three_terms(self):
        """It should return 2 for n = 3 (0 + 1 + 1)."""
        self.assertEqual(sum_of_nth_fibonacci_series(3), 2)

    def test_four_terms(self):
        """It should return 4 for n = 4 (0 + 1 + 1 + 2)."""
        self.assertEqual(sum_of_nth_fibonacci_series(4), 4)

    def test_five_terms(self):
        """It should return 7 for n = 5 (0 + 1 + 1 + 2 + 3)."""
        self.assertEqual(sum_of_nth_fibonacci_series(5), 7)

    def test_six_terms(self):
        """It should return 12 for n = 6 (0 + 1 + 1 + 2 + 3 + 5)."""
        self.assertEqual(sum_of_nth_fibonacci_series(6), 12)

    # Edge cases
    def test_negative_input(self):
        """It should return 0 for negative input (no terms to sum)."""
        self.assertEqual(sum_of_nth_fibonacci_series(-5), 0)

    def test_large_input(self):
        """It should correctly compute the sum for a large number of terms."""
        self.assertEqual(sum_of_nth_fibonacci_series(10), 88)


if __name__ == "__main__":
    unittest.main()
