#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for greatest_number function

Test categories:
    -Standard test: Tests for typical inputs and expected outputs.
    - Edge test: Tests for boundary conditions and extreme inputs.
    - Defensive test: Tests for invalid input types and assertions.

Created on: 6/1/2025
@author: Razan Ibrahim
Group: Matrix (ET foundations group 16 )
"""

import unittest

from solutions.greatest_number import greatest_number


class TestGreatestNum(unittest.TestCase):
    """Test the greatest_number function"""

    # Test Standard Cases
    def test_list_of_positive_numbers(self):
        """Test case where the list contains only positive numbers.
        The function should return the greatest positive number."""
        actual = greatest_number([30, 51, 4390, 99, 302, 1000])
        expected = 4390
        self.assertEqual(actual, expected)

    def test_list_of_negative_numbers(self):
        """Test case where the list contains only negative numbers.
        The function should return the greatest negative number."""
        actual = greatest_number([-3.4, -90, -201, -0.5])
        expected = -0.5
        self.assertEqual(actual, expected)

    def test_list_of_mixed_numeric_values(self):
        """Test case where the list contains a mix of integers, floats, positive,
        and negative numbers.The function should return
        the greatest numeric value 43.5, regardless of type (int/float)"""
        actual = greatest_number([22, 43.5, -67, -600, -10000, 2.5])
        expected = 43.5
        self.assertEqual(actual, expected)

    def test_list_of_with_non_numeric_element(self):
        """Test case where the list contains mixed types (numeric and non-numeric elements).
        The function should return the greatest numeric value
        which it is 204.37.(ignoring non-numeric elements.)"""
        actual = greatest_number([100, True, -20, 204.37, "MIT"])
        expected = 204.37
        self.assertEqual(actual, expected)

    # Test Edge Cases
    def test_one_element_in_list(self):
        """Test case where the list contains only one element.
        The function should return that element as the greatest number -4."""
        actual = greatest_number([-4])
        expected = -4
        self.assertEqual(actual, expected)

    def test_very_long_list(self):
        """Test case with a very long list containing numbers from 0 to 234544.
        The function should return the greatest number (234544)."""
        # generate a long list contain elements from 0 to 234544
        long_list = [i for i in range(234545)]
        actual = greatest_number(long_list)
        expected = 234544
        self.assertEqual(actual, expected)

    # Test Defensive Cases
    def test_empty_list(self):
        """Test case with an empty list. The function should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            greatest_number([])

    def test_list_with_only_non_numeric_elements(self):
        """Test case with a list containing only non-numeric elements.
        The function should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            greatest_number([True, "great", "number", "MIT Emerging Talent", [1, 2, 3]])

    def test_input_is_not_list(self):
        """Test case where the input is not a list. The function should raise an AssertionError"""
        with self.assertRaises(AssertionError):
            greatest_number(23)


if __name__ == "__main__":
    unittest.main()
