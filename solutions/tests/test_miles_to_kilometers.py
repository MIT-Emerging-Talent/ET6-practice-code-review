#!/usr/bin/env python3
"""
Test module for the miles_to_kilometers function.

Test categories:
    - Standard cases: Positive numbers and zero.
    - Defensive tests: Non-numeric inputs and negative values.
"""

import unittest
from ..miles_to_kilometers import miles_to_kilometers


class TestMilesToKilometers(unittest.TestCase):
    """Test suite for the miles_to_kilometers function."""

    # Standard test cases
    def test_positive_miles(self):
        """Test case for positive miles."""
        self.assertEqual(miles_to_kilometers(1), 1.609344)

    def test_zero_miles(self):
        """Test case for zero miles."""
        self.assertEqual(miles_to_kilometers(0), 0.0)

    def test_large_miles(self):
        """Test case for a large value of miles."""
        self.assertEqual(miles_to_kilometers(100), 160.9344)

    # Defensive tests
    def test_negative_miles(self):
        """Test case for negative miles."""
        with self.assertRaises(ValueError):
            miles_to_kilometers(-5)

    def test_non_numeric_input(self):
        """Test case for non-numeric input."""
        with self.assertRaises(ValueError):
            miles_to_kilometers("ten")


if __name__ == "__main__":
    unittest.main()
