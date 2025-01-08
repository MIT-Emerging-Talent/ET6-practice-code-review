"""
Unittest class for a function that takes a list of numbers and returns a
dictionary with sums of the even and odd numbers in the list.
"""

import unittest

from ..sum_even_odd import sum_even_odd


class TestSortandSumNumbers(unittest.TestCase):
    """Tests the sort_and_sum_numbers function"""

    def test_arg_type(self):
        """returns true if assertion error is raised when arg is not a list"""
        with self.assertRaises(AssertionError):
            sum_even_odd(91)

    def test_list_item_type(self):
        """returns true if assertion error is raised when list contains a non int type"""
        with self.assertRaises(AssertionError):
            sum_even_odd([45, "glass", 0.1])

    def test_sum_positive_even_numbers(self):
        """returns a key:value dictionary of the sum,
        if list contains only positive even numbers"""
        self.assertEqual(
            sum_even_odd([2, 4, 6, 8]), {"sum_of_even": 20, "sum_of_odd": 0}
        )

    def test_sum_positive_odd_numbers(self):
        """returns a key:value dictionary of the sum,
        if list contains only positive 0dd numbers"""
        self.assertEqual(
            sum_even_odd([7, 7, 1, 9]), {"sum_of_even": 0, "sum_of_odd": 24}
        )

    def test_sum_mixed_numbers(self):
        """returns a key:value dict of the sum,
        if list contains mixture of even and odd numbers"""
        self.assertEqual(
            sum_even_odd([7, 7, 1, 9, 2, 4, 6, 8]),
            {"sum_of_even": 20, "sum_of_odd": 24},
        )

    def test_sum_negative_numbers(self):
        """returns a key:value dict of the sum,
        if list contains negative even and odd numbers"""
        self.assertEqual(
            sum_even_odd([-7, -20, -1, 9, 2, -4, 6, 8, 0]),
            {"sum_of_even": -8, "sum_of_odd": 1},
        )

    def test_sum_very_large_numbers(self):
        """returns a key:value dict of the sum,
        if list contains very large even and odd numbers"""
        self.assertEqual(
            sum_even_odd([-7000000679, -20, -1, 9, 2, -4, 6000000000, 8, 0]),
            {"sum_of_even": 5999999986, "sum_of_odd": -7000000671},
        )
