"""
Test module for fizz_buzz implementation.

This module contains unit tests for the fizz_buzz function using the unittest framework.
The tests verify correct behavior for valid inputs and proper error handling for invalid inputs.

Created: 25/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Ghyath Ibrahim
"""

import unittest
from ..fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Test cases for fizz_buzz function.

    Test suite verifies:
    - Input validation (type checking, value bounds)
    - Correct string conversions
    - FizzBuzz rules implementation
    - Edge cases and boundary values
    """

    def test_invalid_type_raises_assertion_error(self):
        """Test that non-integer input raises AssertionError."""
        with self.assertRaises(AssertionError):
            fizz_buzz(3.14)

    def test_zero_raises_assertion_error(self):
        """Test that zero input raises AssertionError."""
        with self.assertRaises(AssertionError):
            fizz_buzz(0)

    def test_negative_raises_assertion_error(self):
        """Test that negative input raises AssertionError."""
        with self.assertRaises(AssertionError):
            fizz_buzz(-1)

    def test_one_returns_single_item(self):
        """Test output for input of 1."""
        self.assertEqual(fizz_buzz(1), ["1"])

    def test_up_to_three(self):
        """Test output including first Fizz."""
        self.assertEqual(fizz_buzz(3), ["1", "2", "Fizz"])

    def test_up_to_five(self):
        """Test output including first Buzz."""
        self.assertEqual(fizz_buzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_up_to_fifteen(self):
        """Test output including first FizzBuzz."""
        result = fizz_buzz(15)
        self.assertEqual(result[-3:], ["13", "14", "FizzBuzz"])

    def test_string_conversion(self):
        """Test that non-special numbers are converted to strings."""
        result = fizz_buzz(2)
        self.assertTrue(
            all(isinstance(x, str) for x in result), "All elements should be strings"
        )
