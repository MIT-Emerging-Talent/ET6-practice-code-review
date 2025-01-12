"""
Test cases for Function to Find the Largest Number in a List
@author: msrak
@date: January 1, 2025

Description:
This function identifies and returns the largest number from a given list of numbers.
"""

import unittest
from solutions.find_largest_number import largest_number


class TestLargestNumber(unittest.TestCase):
    def test_largest_positive(self):
        numbers = [1, 2, 3, 4, 21, 12, 8]
        result = largest_number(numbers)
        self.assertEqual(result, 21)

    def test_largest_negative(self):
        numbers = [-1, -2, -3, -4, -21, -42, -8]
        result = largest_number(numbers)
        self.assertEqual(result, -1)

    def test_largest_mix(self):
        numbers = [-1, 2, -3, 4, 79, 12, 8]
        result = largest_number(numbers)
        self.assertEqual(result, 79)


if __name__ == "__main__":
    unittest.main()
