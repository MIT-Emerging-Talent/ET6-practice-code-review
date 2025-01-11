#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_elements function

Created on 2025-01-06

@author: Rumiya Ismatova
"""

import unittest
from solutions.sum_elements import sum_elements


class TestSumElements(unittest.TestCase):
    # Unit test class for verifying the functionality of the sum_elements function.

    def test_positive_numbers(self):
        # Test the function with a list of positive numbers to ensure the sum is correct.
        self.assertEqual(sum_elements([1, 2, 3]), 6)

    def test_negative_numbers(self):
        # Test the function with a list of negative numbers to ensure the sum is correct.
        self.assertEqual(sum_elements([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        # Test the function with a list of positive, negative, and zero values to ensure the sum is correct.
        self.assertEqual(sum_elements([-1, 0, 1]), 0)

    def test_empty_list(self):
        # Test the function with an empty list to ensure it returns 0.
        self.assertEqual(sum_elements([]), 0)

    def test_non_integer_list(self):
        # Test that a ValueError is raised when the list contains non-integer elements.
        with self.assertRaises(ValueError) as context:
            sum_elements([1, 2, "a"])
        self.assertEqual(
            str(context.exception), "All elements in the list must be integers."
        )


# Run the unit tests when this script is executed
if __name__ == "__main__":
    unittest.main()
