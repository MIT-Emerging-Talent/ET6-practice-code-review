# tests/test_prime_numbers.py

"""
Unit tests for the get_prime_numbers function.
"""

import unittest
from solutions.get_prime_numbers import get_prime_numbers


class TestGetPrimeNumbers(unittest.TestCase):
    """Test cases for the get_prime_numbers function."""

    def test_primes_up_to_10(self):
        """Test that the function returns correct primes up to 10."""
        self.assertEqual(get_prime_numbers(10), [2, 3, 5, 7])

    def test_primes_up_to_2(self):
        """Test that the function returns correct primes up to 2."""
        self.assertEqual(get_prime_numbers(2), [2])

    def test_no_primes_below_2(self):
        """Test that the function returns an empty list for n < 2."""
        self.assertEqual(get_prime_numbers(1), [])
        self.assertEqual(get_prime_numbers(0), [])
        self.assertEqual(get_prime_numbers(-5), [])

    def test_large_number(self):
        """Test the function with a larger number."""
        self.assertEqual(get_prime_numbers(20), [2, 3, 5, 7, 11, 13, 17, 19])


if __name__ == "__main__":
    unittest.main()
