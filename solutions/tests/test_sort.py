"""
Test module for the sort function.

This file includes unittest to verify the correctness of the sort function. 
It tests the function with standard cases and edge cases.

Test categories:
    - Standard cases: lists with mixed integers, already sorted lists
    - Edge cases: empty lists, one-element lists, lists with duplicate values
    - Large input: lists with a large range of integers (e.g., thousands)

Created on: 03 January 2025
Author: Safiya Hash
"""

import unittest
from solutions.sort import sort

class TestSort(unittest.TestCase):  # noqa: F821
    """These unittest cases will test the sort function using bubble sort algorithm."""

    def test_empty_list(self):
        """it should return an empty list"""
        self.assertEqual(sort([]), [])

    def test_one_element_list(self):
        """it should return that one integer from the list"""
        self.assertEqual(sort([3]), [3])

    def test_already_sorted_list(self):
        """it should return the same order from the list"""
        self.assertEqual(sort([1, 2, 3]), [1, 2, 3])

    def test_multiple_elements_list(self):
        """it should return the list of integers from smallest to largest"""
        self.assertEqual(sort([5, 9, 4, 3, 7]), [3, 4, 5, 7, 9])

    def test_duplicate_int_list(self):
        """it should return the list with duplicates placed side by side"""
        self.assertEqual(sort([7, 7, 1, 2, 9]), [1, 2, 7, 7, 9])

    def test_range_int_10_99(self):
        """it should return the list of integers from smallest to largest"""
        self.assertEqual(
            sort([95, 12, 54, 76, 87, 18, 33, 60]),
            [12, 18, 33, 54, 60, 76, 87, 95],
        )

    def test_negative_int_list(self):
        """it should return the list of negative integers from smallest to largest"""
        self.assertEqual(
            sort([-3, -54, -1, -9, -23, -99, -12, -34]),
            [-99, -54, -34, -23, -12, -9, -3, -1],
        )

    def test_mixed_of_positive_and_negative_int_list(self):
        """it should return the list of positive and negative integers from smallest to largest"""
        self.assertEqual(sort([11, -43, -36, 5, 43]), [-43, -36, 5, 11, 43])

    def test_zero_with_positive_int_list(self):
        """it should return the list of integers from smallest to largest starting from zero"""
        self.assertEqual(
            sort([16, 44, 0, 23, 555, 3, 200, 101]),
            [0, 3, 16, 23, 44, 101, 200, 555],
        )

    def test_zero_with_negative_int_list(self):
        """it should return the sorted list of negative integers finishing at zero"""
        self.assertEqual(
            sort([-16, -44, 0, -23, -555, -3, -200, -101]),
            [-555, -200, -101, -44, -23, -16, -3, 0],
        )

    def test_zero_with_positive_and_negative_int_list(self):
        """it should return the sorted list of negative and positive integers including zero"""
        self.assertEqual(
            sort(
                [-16, 16, -44, 44, 0, -23, 23, -555, 555, -3, 3, -200, 200, -101, 101]
            ),
            [-555, -200, -101, -44, -23, -16, -3, 0, 3, 16, 23, 44, 101, 200, 555],
        )

    def test_large_range_int_list(self):
        """it should return the list of large integers from smallest to largest"""
        self.assertEqual(
            sort([35236, 555555, 98732145, 100, 7543, 894521, 99991200]),
            [100, 7543, 35236, 555555, 894521, 98732145, 99991200],
        )


if __name__ == "__main__":
    unittest.main()
