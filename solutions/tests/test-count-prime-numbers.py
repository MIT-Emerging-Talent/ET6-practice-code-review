"""
A module for testing the functions is_prime and count_primes.

Tests included:
    - is_prime: tested the cases when the input is a prime number, a non-prime number,
    input is zero, input is one, input is a negative integer, and when the input is a string.
    - count_primes: tested the cases when the input is a list of mixed numbers,
    input is an empty list, and when the input is a list containing non-integer elements.

Created on 10 01 2025
@author: Zeinab Shadabshoar
"""

import unittest

from ..prime_checker import is_prime, count_primes


class TestPrimeFunctions(unittest.TestCase):
    """
    Tests both functions in prime_checker, is_prime and count_primes.
    """

    def test_is_prime_prime(self):
        """
        It should return True if the input is a prime number
        """
        actual = is_prime(7)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_prime_non_prime(self):
        """
        It should return False if the input is a non-prime number
        """
        actual = is_prime(4)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_zero(self):
        """
        It should return False if the input is zero
        """
        actual = is_prime(0)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_one(self):
        """
        It should return False if the input is one
        """
        actual = is_prime(1)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_prime_negative(self):
        """
        It should raise an assertion error if the input is a negative integer
        """
        with self.assertRaises(AssertionError):
            is_prime(-5)

    def test_is_prime_string(self):
        """
        It should raise an assertion error if the input is a non-integer
        """
        with self.assertRaises(AssertionError):
            is_prime("Zeinab")

    def test_count_primes_mixed_list(self):
        """
        It should return the count of prime numbers in a mixed list
        """
        actual = count_primes([2, 3, 4, 5, 6, 7])
        expected = 4
        self.assertEqual(actual, expected)

    def test_count_primes_empty_list(self):
        """
        It should return 0 if the input is an empty list
        """
        actual = count_primes([])
        expected = 0
        self.assertEqual(actual, expected)

    def test_count_primes_non_integer_elements(self):
        """
        It should raise an assertion error if the list contains non-integer elements
        """
        with self.assertRaises(AssertionError):
            count_primes([2, 3, "four", 5])


if __name__ == "__main__":
    unittest.main()
