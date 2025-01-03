"""
Test module for the prime_checker function.

Created on: 04/01/2025
@author: Thilakan Jegatheeswaran
"""

import os
import sys
import unittest

from ..prime_checker import prime_checker

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


class TestPrimeChecker(unittest.TestCase):
    """
    Unit tests for the prime_checker function.
    """

    def test_prime_number(self):
        """It should return 'Prime' for prime numbers."""
        self.assertEqual(prime_checker(2), "Prime")
        self.assertEqual(prime_checker(13), "Prime")
        self.assertEqual(prime_checker(17), "Prime")
        self.assertEqual(prime_checker(19), "Prime")

    def test_not_prime_number(self):
        """It should return 'Not Prime' for non-prime numbers."""
        self.assertEqual(prime_checker(4), "Not Prime")
        self.assertEqual(prime_checker(20), "Not Prime")
        self.assertEqual(prime_checker(1), "Not Prime")

    def test_negative_number(self):
        """It should return 'Not Prime' for negative numbers."""
        self.assertEqual(prime_checker(-5), "Not Prime")
        self.assertEqual(prime_checker(-2), "Not Prime")

    def test_zero(self):
        """It should return 'Not Prime' for zero."""
        self.assertEqual(prime_checker(0), "Not Prime")

    def test_large_prime(self):
        """It should handle large prime numbers."""
        self.assertEqual(prime_checker(101), "Prime")

    def test_large_not_prime(self):
        """It should handle large non-prime numbers."""
        self.assertEqual(prime_checker(100), "Not Prime")


if __name__ == "__main__":
    unittest.main()
