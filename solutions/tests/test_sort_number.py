#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for sort_number function
Contains correct tests to help identify bugs in the implementation

Test categories:
    - Standard cases:
        - typical cases with a list of integers only or floating point numbers only
    - Edge cases:
        - a mixed list of integers and floating points
        - a mixed list containing very close values of numbers
        - a mixed list containing very small numbers
        - a mixed list containing very large numbers
        - a mixed list of same numbers
        - a long list of numbers
        - an empty list
    - Defensive tests:
        - invalid input that is not a list
        - a list containing strings

Created on 8-Jan-2025

@author: Aung Myin Moe
"""

import unittest

from ..sort_number import sort_number


class TestMergeSort(unittest.TestCase):
    """Test suite for the sort_number function."""

    # Standard test cases
    def test_integers(self):
        """A standard test case with a list of integers"""
        array = [5, 4, 3, 2, 1, 0, -1, -2]
        self.assertEqual(sort_number(array), [-2, -1, 0, 1, 2, 3, 4, 5])

    def test_floats(self):
        """A standard test case with a list of floating points"""
        array = [5.0, 4.0, 3.5, 1.2, 1.0, 0.0]
        self.assertEqual(sort_number(array), [0.0, 1.0, 1.2, 3.5, 4.0, 5.0])

    def test_large_integers(self):
        """A standard test case with a list of large integers"""
        array = [1000000, 100000, 10000, 1000, 100, 10]
        self.assertEqual(sort_number(array), [10, 100, 1000, 10000, 100000, 1000000])

    def test_large_floats(self):
        """A standard test case with a list of large floating points"""
        array = [1000000.00, 100000.00, 10000.00, 1000.00, 100.00, 10.00]
        self.assertEqual(
            sort_number(array),
            [10.00, 100.00, 1000.00, 10000.00, 100000.00, 1000000.00],
        )

    # Edge cases
    def test_int_float_mix(self):
        """An edge case for a mixed list of integers and floating points"""
        array = [6.0, 5, 7, 9.0, 8.5, 9.7, -4.5, -5, 11.65, 11.7]
        self.assertEqual(
            sort_number(array), [-5, -4.5, 5, 6.0, 7, 8.5, 9.0, 9.7, 11.65, 11.7]
        )

    def test_close_values(self):
        """An edge case for a mixed list containing very close values of numbers"""
        array = [
            -0.99999,
            -0.999999,
            2.34445,
            2.344444444,
            5.00000001,
            5,
            8.9999999999,
            9.0000001,
            9.0000002,
        ]
        self.assertEqual(
            sort_number(array),
            [
                -0.999999,
                -0.99999,
                2.344444444,
                2.34445,
                5,
                5.00000001,
                8.9999999999,
                9.0000001,
                9.0000002,
            ],
        )

    def test_very_small_numbers(self):
        """An edge case for a mixed list containing very small numbers"""
        array = [
            0.00000001,
            0.00000000001,
            0.0000000000000001,
            0.000001,
            0.01,
            0.000000000000000001,
            1,
        ]
        self.assertEqual(
            sort_number(array),
            [
                0.000000000000000001,
                0.0000000000000001,
                0.00000000001,
                0.00000001,
                0.000001,
                0.01,
                1,
            ],
        )

    def test_very_large_numbers(self):
        """An edge case for a mixed list containing very large numbers"""
        array = [
            9999,
            999999999,
            99999999,
            999999,
            9999999,
            9999999999999,
            9999999999,
            99999.01,
        ]
        self.assertEqual(
            sort_number(array),
            [
                9999,
                99999.01,
                999999,
                9999999,
                99999999,
                999999999,
                9999999999,
                9999999999999,
            ],
        )

    def test_same_values(self):
        """An edge case for a mixed list containing same numbers"""
        array = [1.00, 1, 1.0, 1.000, 1.0000, 1.000000, 1.000000000]
        self.assertEqual(
            sort_number(array), [1.00, 1, 1.0, 1.000, 1.0000, 1.000000, 1.000000000]
        )

    def test_long_list(self):
        """An edge case for a long list of numbers"""
        array = [
            9,
            8,
            6,
            7,
            4,
            5,
            1,
            2,
            3,
            10,
            13,
            12,
            11,
            16,
            17,
            15,
            14,
            19,
            18,
            20,
            31,
            21,
            24,
            22,
            23,
            25,
            27,
            26,
            29,
            28,
            30,
        ]
        self.assertEqual(
            sort_number(array),
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
                10,
                11,
                12,
                13,
                14,
                15,
                16,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                25,
                26,
                27,
                28,
                29,
                30,
                31,
            ],
        )

    def test_empty_list(self):
        """An edge case for an empty list"""
        array = []
        self.assertEqual(sort_number(array), [])

    # Defensive cases
    def test_not_list(self):
        """A defensive case for a non-list input"""
        array = 5, 4, 3, 2, 1
        with self.assertRaises(AssertionError):
            sort_number(array)

    def test_string_in_list(self):
        """A defensive case for a list containing strings"""
        array = [5, 4, 3, 2, 1, "AB"]
        with self.assertRaises(AssertionError):
            sort_number(array)
