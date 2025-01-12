"""Tests for check_coprime function.


This module contains unit tests to ensure the check_coprime function works as expected,
including handling edge cases and defensive assertions.

@author: Vahab
@created: 11/01/2025
"""

import unittest


from solutions.check_coprime import check_coprime


class TestCoprimeFunction(unittest.TestCase):
    """Test cases for the check_coprime function."""

    def test_coprime_true(self):
        """Test case where the numbers are relatively prime."""
        self.assertTrue(check_coprime(15, 28))

    def test_coprime_false(self):
        """Test case where the numbers are not relatively prime."""
        self.assertFalse(check_coprime(8, 12))

    def test_coprime_same_value(self):
        """Test case where both numbers are the same and greater than 1."""
        self.assertFalse(check_coprime(12, 12))

    def test_coprime_negative_input(self):
        """Test case where negative numbers are provided."""
        with self.assertRaises(ValueError):
            check_coprime(-5, 28)

    def test_coprime_non_integer_input(self):
        """Test case where non-integer inputs are provided."""
        with self.assertRaises(TypeError):
            check_coprime("15", 28)

    def test_coprime_large_numbers(self):
        """Test case with large numbers to check performance."""
        self.assertTrue(check_coprime(1, 100))

    def test_coprime_edge_case(self):
        """Test case where one input is 0."""
        with self.assertRaises(ValueError):
            check_coprime(0, 10)


if __name__ == "__main__":
    unittest.main()
