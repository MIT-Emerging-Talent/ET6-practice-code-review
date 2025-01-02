#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for sort_numbers function.

Contains tests for testing sort_numbers function.

Created on 2024-12-30
Author: Viktoriya Haiduk
"""

import unittest

from solutions.sort_numbers import sort_numbers


class TestSortNumbers(unittest.TestCase):
    def test_sorted_numbers(self):
        """
        Test if the func. correctly sorts a list of integers in asc order.
        """
        self.assertEqual(sort_numbers([4, 1, 3, 2]), [1, 2, 3, 4])

    def test_floats(self):
        """
        Test if the func. correctly sorts a list of floats in asc order.
        """
        self.assertEqual(sort_numbers([4.5, 2.3, 1.7, 3.9]), [1.7, 2.3, 3.9, 4.5])

    def test_mixed_numbers(self):
        """
        Test if the func. sorts a list cont. both integers and floats.
        """
        self.assertEqual(sort_numbers([4, 2.5, 3, 1.2]), [1.2, 2.5, 3, 4])

    def test_invalid_input(self):
        """
        Test if the func. raises a ValueError for a list with non-numeric.
        """
        with self.assertRaises(ValueError) as context:
            sort_numbers(["a", None, 3])
        self.assertEqual(
            str(context.exception), "The list contains non-numeric values."
        )

    def test_empty_list(self):
        """
        Test if the func. raises a ValueError for an empty list.
        """
        with self.assertRaises(ValueError) as context:
            sort_numbers([])
        self.assertEqual(
            str(context.exception), "The list is empty. Provide numbers."
        )

    def test_negative_numbers(self):
        """
        Test if the func. correctly sorts a list of neg. numbers.
        """
        self.assertEqual(sort_numbers([-3, -1, -4, -2]), [-4, -3, -2, -1])


if __name__ == "__main__":
    unittest.main()
