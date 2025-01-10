#!/usr/bin/env python3
"""
Test module for check_odd_or_even function.

Test categories:
    - Standard cases: even and odd numbers
    - Edge cases: zero, negative numbers, large numbers
    - Defensive tests: wrong input types
"""

import unittest

from ..check_odd_or_even import check_odd_or_even


class TestCheckOddOrEven(unittest.TestCase):
    """Test suite for the check_odd_or_even function."""

    # Standard test cases
    def test_even_number(self):
        """It should return 'Even' for an even integer."""
        self.assertEqual(check_odd_or_even(4), "Even")

    def test_odd_number(self):
        """It should return 'Odd' for an odd integer."""
        self.assertEqual(check_odd_or_even(7), "Odd")

    # Edge cases
    def test_zero(self):
        """It should return 'Even' for zero."""
        self.assertEqual(check_odd_or_even(0), "Even")

    def test_negative_even(self):
        """It should return 'Even' for a negative even number."""
        self.assertEqual(check_odd_or_even(-10), "Even")

    def test_negative_odd(self):
        """It should return 'Odd' for a negative odd number."""
        self.assertEqual(check_odd_or_even(-3), "Odd")

    def test_large_even_number(self):
        """It should return 'Even' for a large even number."""
        self.assertEqual(check_odd_or_even(10**18), "Even")

    def test_large_odd_number(self):
        """It should return 'Odd' for a large odd number."""
        self.assertEqual(check_odd_or_even(10**18 + 1), "Odd")

    # Defensive tests
    def test_non_integer_raises_assertion(self):
        """It should raise AssertionError when passing a non-integer."""
        with self.assertRaises(AssertionError) as context:
            check_odd_or_even(3.14)
        self.assertEqual(str(context.exception), "num must be an integer")


if __name__ == "__main__":
    unittest.main()
