"""
Unit tests for the palindrome_checker function.

These tests cover:

- Basic functionality
- Defensive assertions
- Boundary cases
"""

import unittest
from solutions.palindrome_checker import palindrome_checker


class TestPercentageLetter(unittest.TestCase):
    """ """

    def test_0(self):
        """ """
        actual = palindrome_checker("racecar")
        expected = True
        self.assertEqual(actual, expected)
if __name__ == "__main__":
    unittest.main()
