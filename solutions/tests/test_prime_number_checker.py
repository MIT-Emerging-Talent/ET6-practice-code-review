"""
Unit test module for checking the correctness of the is_prime function.
This module contains test cases for various scenarios such as:
- Valid prime numbers
- Valid non-prime numbers
- Edge cases
- Invalid input types

Tests are designed to ensure that the is_prime function handles all relevant cases correctly.
Created on 2024-12-30
Author: Hussaini Ahmed
"""

import unittest

from solutions.prime_number_checker import is_prime


class TestIsPrime(unittest.TestCase):
    """
    Test case class for the is_prime function. This class includes various test methods to validate
    the correctness of the is_prime function. The test cases cover prime numbers, non-prime numbers,
    edge cases, negative numbers, and invalid input types.

    Methods:
        - test_prime_numbers: Tests known prime numbers.
        - test_non_prime_numbers: Tests known non-prime numbers.
        - test_negative_numbers: Tests negative numbers (which should all be non-prime).
        - test_edge_cases: Tests edge cases like small and consecutive numbers.
        - test_invalid_input: Tests invalid input types and ensures TypeError is raised.
    """

    def test_prime_numbers(self):
        """
        Test method to validate the correctness of is_prime for known prime numbers.
        """
        self.assertTrue(is_prime(2))  # 2 is prime
        self.assertTrue(is_prime(3))  # 3 is prime
        self.assertTrue(is_prime(13))  # 13 is prime
        self.assertTrue(is_prime(97))  # 97 is prime
        self.assertTrue(is_prime(7919))  # Large prime number

    def test_non_prime_numbers(self):
        """
        Test method to validate the correctness of is_prime for known non-prime numbers.
        """
        self.assertFalse(is_prime(0))  # 0 is not prime
        self.assertFalse(is_prime(1))  # 1 is not prime
        self.assertFalse(is_prime(4))  # 4 is not prime
        self.assertFalse(is_prime(100))  # 100 is not prime
        self.assertFalse(is_prime(12345))  # 12345 is not prime

    def test_negative_numbers(self):
        """
        Test method to validate that all negative numbers are correctly identified as non-prime.
        """
        self.assertFalse(is_prime(-1))  # -1 is not prime
        self.assertFalse(is_prime(-10))  # -10 is not prime
        self.assertFalse(is_prime(-97))  # -97 is not prime

    def test_edge_cases(self):
        """
        Test method to validate edge cases, such as the smallest numbers and consecutive numbers.
        """
        self.assertFalse(is_prime(0))  # 0 is not prime
        self.assertFalse(is_prime(1))  # 1 is not prime
        self.assertTrue(is_prime(2))  # 2 is the smallest prime
        self.assertTrue(is_prime(3))  # 3 is a prime number

    def test_invalid_input(self):
        """
        Test method to validate that invalid input types raise a TypeError.
        This includes inputs like strings, floats, None, lists, and dictionaries.
        """
        with self.assertRaises(TypeError):
            is_prime("string")  # Invalid input: string
        with self.assertRaises(TypeError):
            is_prime(3.14)  # Invalid input: float
        with self.assertRaises(TypeError):
            is_prime(None)  # Invalid input: None
        with self.assertRaises(TypeError):
            is_prime([2, 3, 5])  # Invalid input: list
        with self.assertRaises(TypeError):
            is_prime({"number": 7})  # Invalid input: dictionary


if __name__ == "__main__":
    unittest.main()
