#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX
@author: Saadet Kalender
"""
import unittest


# Function to test
def find_smallest_number(numbers):
    """
    Finds and returns the smallest number in a list.

    :param numbers: List of numbers
    :return: The smallest number in the list
    """
    if not numbers:
        raise ValueError("The list is empty.")

    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


# Unit test class
class TestFindSmallestNumber(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(find_smallest_number([10, 20, 5, 7]), 5)

    def test_negative_numbers(self):
        self.assertEqual(find_smallest_number([-10, -20, -5, -7]), -20)

    def test_mixed_numbers(self):
        self.assertEqual(find_smallest_number([10, -20, 0, 7, -3]), -20)

    def test_single_element(self):
        self.assertEqual(find_smallest_number([42]), 42)

    def test_identical_elements(self):
        self.assertEqual(find_smallest_number([7, 7, 7, 7]), 7)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_smallest_number([])


# Run the tests
if __name__ == "__main__":
    unittest.main()
