#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-01-06

@author: Ajanduna Emmanuel
"""

import unittest


def find_the_maximum_of_two_numbers(num1, num2):
    """
    This function finds the maximum of two given numbers.

    Args:
        num1: The first number.
        num2: The second number.

    Returns:
        The maximum of num1 and num2.
    """
    if num1 > num2:
        return num1
    else:
        return num2


class TestFindMaximum(unittest.TestCase):
    """
    Unit tests for the find_the_maximum_of_two_numbers function.
    """

    def test_first_number_greater(self):
        """
        Tests if the function correctly identifies the maximum when the first number is greater.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(5, 3), 5)

    def test_second_number_greater(self):
        """
        Tests if the function correctly identifies the maximum when the second number is greater.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(2, 8), 8)

    def test_numbers_equal(self):
        """
        Tests if the function correctly handles the case where both numbers are equal.
        """
        self.assertEqual(find_the_maximum_of_two_numbers(7, 7), 7)


if __name__ == "__main__":
    unittest.main()
