#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Monday/ 30/ December/2024
@author: Mayar Ali

"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..TestEvenNumberCount import TestEvenNumberCount

# class TestTestEvenNumberCount(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..even_number_count import even_number_count  # type: ignore


class TestEvenNumberCount(unittest.TestCase):
    """test the even_number_count function"""

    def test_0(self):
        """It should return zero"""
        self.assertEqual(even_number_count([1]), 0)

    def test_1(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2]), 1)

    def test_2(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2, 3]), 1)

    def test_3(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2, 3, 4]), 2)

    def test_4(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2, 3, 4, 5]), 2)

    def test_5(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2, 3, 4, 5, 6]), 3)

    def test_6(self):
        """Count the number of even numbers in a countdown from n to 1"""
        self.assertEqual(even_number_count([1, 2, 3, 4, 5, 6, 7]), 3)

    # Boundary case

    def test_big_numbers(self):
        """it should evaluate 100 to [1,2,3,4,5,...]"""
        self.assertEqual(
            even_number_count(
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
                    32,
                    33,
                    34,
                    35,
                    36,
                    37,
                    38,
                    39,
                    40,
                    41,
                    42,
                    43,
                    44,
                    45,
                    46,
                    47,
                    48,
                    49,
                    50,
                    51,
                    52,
                    53,
                    54,
                    55,
                    56,
                    57,
                    58,
                    59,
                    60,
                    61,
                    62,
                    63,
                    64,
                    65,
                    66,
                    67,
                    68,
                    69,
                    70,
                    71,
                    72,
                    73,
                    74,
                    75,
                    76,
                    77,
                    78,
                    79,
                    80,
                    81,
                    82,
                    83,
                    84,
                    85,
                    86,
                    87,
                    88,
                    89,
                    90,
                    91,
                    92,
                    93,
                    94,
                    95,
                    96,
                    97,
                    98,
                    99,
                    100,
                    101,
                    102,
                    103,
                    104,
                    105,
                    106,
                    107,
                    108,
                    109,
                    110,
                    111,
                    112,
                    113,
                    114,
                    115,
                    116,
                    117,
                    118,
                    119,
                    120,
                    121,
                    122,
                    123,
                    124,
                    125,
                    126,
                    127,
                    128,
                    129,
                    130,
                    131,
                    132,
                    133,
                    134,
                    135,
                    136,
                    137,
                    138,
                    139,
                    140,
                    141,
                    142,
                    143,
                    145,
                    146,
                    147,
                    148,
                    149,
                    150,
                    151,
                    152,
                    153,
                    154,
                    155,
                    156,
                    157,
                    158,
                    159,
                    160,
                    161,
                    162,
                    163,
                    164,
                    165,
                    166,
                    167,
                    168,
                    169,
                    170,
                    171,
                    172,
                    173,
                    174,
                    175,
                    176,
                    177,
                    178,
                    179,
                    180,
                    181,
                    182,
                    183,
                    184,
                    185,
                    186,
                    187,
                    188,
                    189,
                    190,
                    191,
                    192,
                    193,
                    194,
                    195,
                    196,
                    197,
                    198,
                    199,
                    200,
                ]
            ),
            99,
        )

    # Defensive cases

    def test_0_less_than_0(self):
        """Raise an assertion error if the there is a string within a list"""
        with self.assertRaises(AssertionError):
            (even_number_count([1, 2, "-6", 4]),)

    def test_0_less_than_1(self):
        """Raise an assertion error if the there is a list within a list"""
        with self.assertRaises(AssertionError):
            even_number_count([1, 2, [1, 2, 3], 4])
