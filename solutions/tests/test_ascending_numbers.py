#!usr/bin/env python3
# -*- coding : utf-8 -*-

"""
Created on 12 25 2024.

@author : Osei Agyemang Sarfo.
"""

import unittest

from ..ascending_numbers import ascending_numbers


class TestAscendingNumbers(unittest.TestCase):
    """Test the ascending_numbers function"""

    def ascending_integers(self):
        "It should evaluate [56,78, 45, 22] to [22, 45, 56, 78]"
        actual = ascending_numbers(
            [56, 78, 45, 22]
        )  # Call function with test argument.
        expected = [22, 45, 56, 78]  # hand-written answer.
        self.assertEqual(actual, expected)

    def ascending_floats(self):
        "It should evaluate [27.8,34.9,67.9,22.1] to [22.1, 27.8, 34.9, 67.9]"
        actual = ascending_numbers(
            [27.8, 34.9, 67.9, 22.1]
        )  # Call function with test argument
        expected = [22.1, 27.8, 34.9, 67.9]  # Hand-written answer
        self.assertEqual(actual, expected)
