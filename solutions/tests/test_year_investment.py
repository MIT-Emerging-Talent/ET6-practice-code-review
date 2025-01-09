"""
Test for year_investment

created by Dmytro Klymenko

1/8/2025

"""

import unittest

from solutions.year_investment import year_investment


class TestYearInvestment(unittest.TestCase):
    """This class is designed to check year_investments.

    Function calculates yearly income with desired number
    and percantage.

    """

    def test_numbers(self):
        """Basic test case"""
        self.assertEqual(year_investment(5, 3), 5.15)

    def test_numbers_float(self):
        """Test if variables are floats"""
        self.assertEqual(year_investment(5.4, 2.4), 5.5296)

    def test_numbers_big(self):
        """Test variables with big numbers"""
        self.assertEqual(year_investment(1856278, 2146), 41692003.88)

    def test_negative_number(self):
        """Test if number is negative"""
        with self.assertRaises(AssertionError):
            year_investment(-1, 5)

    def test_if_number(self):
        """Test if all variables are numbers"""
        with self.assertRaises(AssertionError):
            year_investment(1, "y")
        with self.assertRaises(AssertionError):
            year_investment("y", 2)
