import unittest
from solutions.sum_two_numbers import sum_two_numbers


"""
Test module for the sum_two_numbers function.
This file includes unittest to verify the correctness of the sum_two_numbers function.
It tests the function with standard cases, edge cases, and exception handling.

Test categories:
    - Standard cases: Correct summation of integers and floats.
    - Edge cases: Handling of zero values and mixed types.
    - Exception handling: Tests for ValueError and TypeError.

Created on: 09 January 2025
Author: Hope Udoh
"""


class TestSumTwoNumbers(unittest.TestCase):
    """
    Test suite for the sum_two_numbers function.
    """

    # Standard Cases
    def test_integer_sum(self):
        """
        Standard Case: Test that the function correctly sums two integers.

        Example:
        >>> sum_two_numbers(7, 10)
        'The sum of 7 and 10 is 17'
        """
        self.assertEqual(sum_two_numbers(7, 10), "The sum of 7 and 10 is 17")

    def test_float_sum(self):
        """
        Standard Case: Test that the function correctly sums two floats.

        Example:
        >>> sum_two_numbers(2.5, 3.1)
        'The sum of 2.5 and 3.1 is 5.6'
        """
        self.assertEqual(sum_two_numbers(2.5, 3.1), "The sum of 2.5 and 3.1 is 5.6")

    def test_integer_float_sum(self):
        """
        Standard Case: Test that the function correctly sums an integer and a float.

        Example:
        >>> sum_two_numbers(3, 4.75)
        'The sum of 3 and 4.75 is 7.75'
        """
        self.assertEqual(sum_two_numbers(3, 4.75), "The sum of 3 and 4.75 is 7.75")

    # Edge Cases
    def test_zero_sum(self):
        """
        Edge Case: Test that the function correctly sums when one or both values are zero.

        Example:
        >>> sum_two_numbers(0, 5)
        'The sum of 0 and 5 is 5'
        """
        self.assertEqual(sum_two_numbers(0, 5), "The sum of 0 and 5 is 5")
        self.assertEqual(sum_two_numbers(0, 0), "The sum of 0 and 0 is 0")

    # Exception Handling
    def test_none_input(self):
        """
        Exception Case: Test that the function raises a ValueError when either argument is None.

        Raises:
            ValueError: If either argument is None.

        Example:
        >>> sum_two_numbers(None, 5)
        Traceback (most recent call last):
        ...
        ValueError: Enter two numbers to use this function
        """
        with self.assertRaises(ValueError):
            sum_two_numbers(None, 5)

    def test_string_input(self):
        """
        Exception Case: Test that the function raises a TypeError when either argument is a string.

        Raises:
            TypeError: If either argument is a string.

        Example:
        >>> sum_two_numbers("10", 5)
        Traceback (most recent call last):
        ...
        TypeError: Both arguments must be int or float.
        """
        with self.assertRaises(TypeError):
            sum_two_numbers("10", 5)
        with self.assertRaises(TypeError):
            sum_two_numbers(10, "5")

    def test_list_input(self):
        """
        Exception Case: Test that the function raises a TypeError when either argument is a list.

        Raises:
            TypeError: If either argument is a list.

        Example:
        >>> sum_two_numbers([1, 2], 5)
        Traceback (most recent call last):
        ...
        TypeError: Both arguments must be int or float.
        """
        with self.assertRaises(TypeError):
            sum_two_numbers([1, 2], 5)

    def test_dict_input(self):
        """
        Exception Case: Test that the function raises a TypeError when either argument is a dictionary.

        Raises:
            TypeError: If either argument is a dictionary.

        Example:
        >>> sum_two_numbers({"a": 1}, 5)
        Traceback (most recent call last):
        ...
        TypeError: Both arguments must be int or float.
        """
        with self.assertRaises(TypeError):
            sum_two_numbers({"a": 1}, 5)

    def test_empty_input(self):
        """
        Exception Case: Test that the function raises a ValueError when either argument is empty.

        Raises:
            ValueError: If either argument is empty.

        Example:
        >>> sum_two_numbers("", 5)
        Traceback (most recent call last):
        ...
        ValueError: Enter two numbers to use this function
        """
        with self.assertRaises(ValueError):
            sum_two_numbers("", 5)
        with self.assertRaises(ValueError):
            sum_two_numbers(5, "")


if __name__ == "__main__":
    unittest.main()
