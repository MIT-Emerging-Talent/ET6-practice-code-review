#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for common_elements function

Test categories:
 -Standard cases: typical inputs
 -Edge cases: extreme inputs and boundaries
 -Defensive tests: wrong input types, assertions

Created on 11/1/2025
@author: Mohamed Altayeb
Group: ET foundations group 16 (Matrix)
"""

import unittest

from ..common_elements import common_elements


class TestCommonElements(unittest.TestCase):
    """Test suite for the common_elements function"""

    # Standard cases
    def test_lists_with_integers(self):
        """it should return a list with the common integers between the two input lists"""
        self.assertEqual(common_elements([1, 2, 3], [2, 3]), [2, 3])

    def test_lists_with_string_elements(self):
        """it should return a list with the common string elements between the two input lists"""
        self.assertEqual(common_elements(["a", "b", "c"], ["b", "c"]), ["b", "c"])

    def test_lists_with_duplicated_elements(self):
        """it should return a list with the common elements between the two input lists
        without duplicating the elements in the output list"""
        self.assertEqual(common_elements(["a", "b", "b"], ["b", "b", "c"]), ["b"])

    def test_lists_with_mixed_string_and_integer_elements(self):
        """it should return a list with the common string elements between the two input lists"""
        self.assertEqual(
            common_elements(["a", "b", 2, 56, "abc"], ["abc", 56, 999]), [56, "abc"]
        )

    def test_lists_within_lists(self):
        """it should return a list with the common elements between the two input lists
        even if the elements are lists as well"""
        self.assertEqual(
            common_elements(
                [[1, 2], [2, 3, 4], ["mohamed"]],
                [["mohamed"], [1, 2, 3], [2, 3, 4], [4, 5, 6]],
            ),
            [[2, 3, 4], ["mohamed"]],
        )

    def test_order_of_elements_in_output_list(self):
        """the function should prioritize the order of the elements in the first input list"""
        self.assertEqual(common_elements([1, 2, 3], [3, 2, 1]), [1, 2, 3])

    # Edge cases
    def test_long_lists(self):
        """it should return a list with the common elements between the two input lists
        regardless of the length of the input lists"""
        self.assertEqual(
            common_elements(
                [
                    1,
                    2,
                    3,
                    4,
                    5,
                    6,
                    7,
                    8,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                ],
                [
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                    9,
                ],
            ),
            [9],
        )

    def test_one_of_the_lists_is_empty(self):
        """it should return an empty list"""
        self.assertEqual(common_elements(["Mohamed", "cat", "1,2,3"], []), [])

    def test_both_of_the_lists_are_empty(self):
        """it should return an empty list"""
        self.assertEqual(common_elements([], []), [])

    # Defensive tests
    def test_input1_is_not_a_list(self):
        """It should raise AssertionError if first input is not a list"""
        with self.assertRaises(AssertionError):
            common_elements("mohamed", [1, 2, 3, 4, 5, 6])

    def test_input2_is_not_a_list(self):
        """It should raise AssertionError if second input is not a list"""
        with self.assertRaises(AssertionError):
            common_elements([1, 2, 3, 4, 5, 6], "numbers")
