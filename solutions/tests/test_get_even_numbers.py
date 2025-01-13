"""
Unit tests for get_even_numbers function.

@created: 01/11/2025
@author: Vahab
"""

import unittest

from solutions.get_even_numbers import get_even_numbers


class TestGetEvenNumbers(unittest.TestCase):
    """
    Tests for the get_even_numbers function.
    """

    def test_basic_functionality(self):
        """
        Test: Check if the function returns the correct even numbers from a list.
        """
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])

    def test_no_even_numbers(self):
        """
        Test: Check if the function returns an empty list when no even numbers are present.
        """
        self.assertEqual(get_even_numbers([1, 3, 5]), [])

    def test_empty_list(self):
        """
        Test: Check if the function handles an empty list correctly.
        """
        self.assertEqual(get_even_numbers([]), [])

    def test_negative_numbers(self):
        """
        Test: Check if the function correctly identifies even negative numbers.
        """
        self.assertEqual(get_even_numbers([-1, -2, -3, -4]), [-2, -4])

    def test_large_numbers(self):
        """
        Test: Check if the function handles large numbers correctly.
        """
        self.assertEqual(get_even_numbers([10**6, 10**9 + 1]), [10**6])

    def test_invalid_input_not_list(self):
        """
        Test: Check if the function raises a TypeError for non-list inputs.
        """
        with self.assertRaises(TypeError):
            get_even_numbers("not a list")

    def test_invalid_input_non_integer_elements(self):
        """
        Test: Check if the function raises a TypeError for lists with non-integer elements.
        """
        with self.assertRaises(TypeError):
            get_even_numbers([1, 2, "three", 4])


if __name__ == "__main__":
    unittest.main()
