"""A module for testing the functions `is_prime` and `find_primes_up_to_n`.

Tests included:
    - is_prime: tested with prime numbers, non-prime numbers, zero, one,
      negative integers, and strings.
    - find_primes_up_to_n: tested with positive integers, zero, and strings.

Created on 10-01-2025
@author: Zeinab Shadabshoar
"""

import unittest

from solutions.find_prime_numbers import find_primes_up_to_n, is_prime


class TestPrimeFunctions(unittest.TestCase):
    """Tests both functions `is_prime` and `find_primes_up_to_n`."""

    def test_is_prime_prime(self):
        """It should return True if the input is a prime number."""
        actual = is_prime(7)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_prime_non_prime(self):
        """It should return False if the input is a non-prime number."""
        actual = is_prime(4)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_zero(self):
        """It should return False if the input is zero."""
        actual = is_prime(0)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_one(self):
        """It should return False if the input is one."""
        actual = is_prime(1)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_negative(self):
        """It should raise an assertion error if the input is a negative integer."""
        with self.assertRaises(AssertionError):
            is_prime(-5)

    def test_is_prime_string(self):
        """It should raise an assertion error if the input is a non-integer."""
        with self.assertRaises(AssertionError):
            is_prime("invalid")

    def test_find_primes_up_to_n_positive(self):
        """It should return a list of prime numbers up to the given positive integer."""
        actual = find_primes_up_to_n(20)
        expected = [2, 3, 5, 7, 11, 13, 17, 19]
        self.assertEqual(actual, expected)

    def test_find_primes_up_to_n_zero(self):
        """It should return an empty list if the input is zero."""
        actual = find_primes_up_to_n(0)
        expected = []
        self.assertEqual(actual, expected)

    def test_find_primes_up_to_n_string(self):
        """It should raise an assertion error if the input is a non-integer."""
        with self.assertRaises(AssertionError):
            find_primes_up_to_n("invalid")


if __name__ == "__main__":
    unittest.main()
