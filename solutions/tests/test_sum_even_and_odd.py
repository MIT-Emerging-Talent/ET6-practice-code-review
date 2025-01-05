"""
This module contains unit tests for the `sum_even_and_odd` function.

The tests ensure that the function correctly calculates the sums of
positive even, positive odd, negative even, and negative odd numbers in a list.
"""

import unittest

from solutions.sum_even_and_odd import sum_even_and_odd  # Import the function to test


class TestSumEvenAndOdd(unittest.TestCase):
    """
    Unit tests for the function `sum_even_and_odd`.
    """

    def test_positive_numbers(self):
        """
        Test the function with only positive even and odd numbers.
        """
        self.assertEqual(
            sum_even_and_odd([2, 4, 6, 8]),
            {
                "positive_even": 20,
                "positive_odd": 0,
                "negative_even": 0,
                "negative_odd": 0,
            },
        )

    def test_negative_numbers(self):
        """
        Test the function with only negative even and odd numbers.
        """
        self.assertEqual(
            sum_even_and_odd([-2, -4, -6, -8]),
            {
                "positive_even": 0,
                "positive_odd": 0,
                "negative_even": -20,
                "negative_odd": 0,
            },
        )

    def test_mixed_numbers(self):
        """
        Test the function with a mix of positive and negative numbers.
        """
        self.assertEqual(
            sum_even_and_odd([-2, -3, 4, 5]),
            {
                "positive_even": 4,
                "positive_odd": 5,
                "negative_even": -2,
                "negative_odd": -3,
            },
        )

    def test_empty_list(self):
        """
        Test the function with an empty list.
        """
        self.assertEqual(
            sum_even_and_odd([]),
            {
                "positive_even": 0,
                "positive_odd": 0,
                "negative_even": 0,
                "negative_odd": 0,
            },
        )

    def test_invalid_input(self):
        """
        Test the function with invalid input (non-list).
        """
        with self.assertRaises(ValueError):
            sum_even_and_odd("invalid_input")  # Example of invalid input


if __name__ == "__main__":
    unittest.main()
