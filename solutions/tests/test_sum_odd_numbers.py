#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_odd_numbers function.

Created on 2025-01-03

@author: Sukhrob Muborakshoev
"""

import unittest

from solutions.sum_odd_numbers import sum_odd_numbers


class TestSumOddNumbers(unittest.TestCase):
    """
    This class contains unit tests for the sum_odd_numbers function.
    The function gets a list of integers as an input and returns the sum of odd numbers.
    """

    def test_valid_list(self):
        """It should return 25"""
        self.assertEqual(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 25)

    def test_only_odd_numbers(self):
        """It should return 133"""
        self.assertEqual(sum_odd_numbers([3, 11, 7, 21, 91]), 133)

    def test_only_even_numbers(self):
        """It should return 0"""
        self.assertEqual(sum_odd_numbers([22, 90, 54, 100]), 0)

    def test_empty_list(self):
        """It should return 0"""
        self.assertEqual(sum_odd_numbers([]), 0)


#     def test_empty_second_parameter(self):
#         """It should raise a value error if second parameter is an empty string"""
#         with self.assertRaises(ValueError) as context:
#             count_character_occurrences("Tajikistan", "")

#         self.assertEqual(
#             str(context.exception), "The char parameter must be a single character."
#         )

#     def test_empty_first_parameter(self):
#         """It should return 0 if first parameter is an empty string"""
#         self.assertEqual(count_character_occurrences("", "i"), 0)

#     def test_char_is_none(self):
#         """It should return the text if second parameter is not provided"""
#         self.assertEqual(count_character_occurrences("return me"), "return me")

#     def test_char_as_number(self):
#         """It should raise TypeError with a specific message when the input is not a string"""
#         with self.assertRaises(AssertionError) as context:
#             count_character_occurrences("california", 4)
#         self.assertEqual(str(context.exception), "Second parameter must be a character")

#     def test_text_as_number(self):
#         """It should raise TypeError with a specific message when the text is a number"""
#         with self.assertRaises(AssertionError) as context:
#             count_character_occurrences(223, "i")
#         self.assertEqual(str(context.exception), "First parameter must be a string")

#     def test_both_parameters_are_number(self):
#         """It should raise TypeError with a specific message when the parameters are a number"""
#         with self.assertRaises(AssertionError) as context:
#             count_character_occurrences(223, 2)
#         self.assertEqual(str(context.exception), "First parameter must be a string")

#     def test_char_as_str(self):
#         """It should raise ValueError with a specific message when the input is a number."""
#         with self.assertRaises(ValueError) as context:
#             count_character_occurrences("unittest is fun", "ab")

#         self.assertEqual(
#             str(context.exception), "The char parameter must be a single character."
#         )

#     def test_both_are_empty_parameters(self):
#         """Both parameters are empty strings"""
#         self.assertEqual(count_character_occurrences("", ""), 0)


# if __name__ == "__main__":
#     unittest.main()
