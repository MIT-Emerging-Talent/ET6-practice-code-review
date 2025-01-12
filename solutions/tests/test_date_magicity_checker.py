#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 05 01 25

@author: Alona Niechvieieva

Unit tests for the date_magicity_checker function.
"""

import unittest


from ..date_magicity_checker import date_magicity_checker


class TestDateMagicityChecker(unittest.TestCase):
    """Test the date_magicity_checker function"""

    def test_01(self):
        """It should return True for '01.01.0001' as a minimum date"""
        self.assertEqual(date_magicity_checker("01.01.0001"), True)

    def test_magic_date_true(self):
        """It should return True for valid magic dates"""
        self.assertEqual(date_magicity_checker("09.03.1727"), True)

    def test_magic_date_false(self):
        """It should return False for non-magic dates"""
        self.assertEqual(date_magicity_checker("15.09.1998"), False)

    def test_not_a_string(self):
        """It should raise an assertion error if the argument is not a string"""
        with self.assertRaises(AssertionError):
            date_magicity_checker(15)

    def test_wrong_length_of_the_string(self):
        """It should raise an assertion error if the argument does not have ten characters"""
        with self.assertRaises(AssertionError):
            date_magicity_checker("15.9.1991")

    def test_misplaced_dots(self):
        """It should raise an assertion error if the dots are not placed at positions 2 and 5"""
        with self.assertRaises(AssertionError):
            date_magicity_checker("3.103.1978")

    def test_string_to_digits(self):
        """It should raise an assertion error if the arg can not be converted to valid integers"""
        with self.assertRaises(AssertionError):
            date_magicity_checker("03.0a.1995")

    def test_invalid_day(self):
        # Invalid day (out of range)
        with self.assertRaises(AssertionError):
            date_magicity_checker("32.10.1860")

    def test_invalid_month(self):
        # Invalid month (out of range)
        with self.assertRaises(AssertionError):
            date_magicity_checker("06.13.1860")


if __name__ == "__main__":
    unittest.main()
