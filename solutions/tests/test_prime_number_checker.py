"""
Unit test module for checking the correctness of the prime_number_checker function.
PrimeNumberCheckerTests test cases for various scenarios such as:
- Valid prime numbers
- Valid non-prime numbers
- Edge cases
- Invalid input types

Tests are designed to ensure that the prime_number_checker
function handles all relevant cases correctly.
Created on 2024-12-30
Author: Hussaini Ahmed
"""

import unittest

from solutions.prime_number_checker import prime_number_checker


class PrimeNumberCheckerTests(unittest.TestCase):
    """
    Test suite for verifying prime number checking functionality.
    Tests cover prime numbers, non-prime numbers, edge cases,
    and input validation.
    """

    # Prime Number Tests
    def test_two_is_prime(self):
        """Verify that 2 is correctly identified as the smallest prime number."""
        self.assertTrue(prime_number_checker(2))

    def test_ninety_seven_is_prime(self):
        """Verify that 97 is correctly identified as a prime number."""
        self.assertTrue(prime_number_checker(97))

    def test_large_prime_number(self):
        """Verify that a large prime number (7919) is correctly identified."""
        self.assertTrue(prime_number_checker(7919))

    # Non-Prime Number Tests
    def test_zero_is_not_prime(self):
        """Verify that 0 is correctly identified as not prime."""
        self.assertFalse(prime_number_checker(0))

    def test_hundred_is_not_prime(self):
        """Verify that 100 is correctly identified as not prime."""
        self.assertFalse(prime_number_checker(100))

    def test_large_non_prime(self):
        """Verify that a large non-prime number (12345) is correctly identified."""
        self.assertFalse(prime_number_checker(12345))

    # Boundary Cases
    def test_first_prime_after_one(self):
        """Verify the boundary between non-prime 1 and prime 2."""
        self.assertTrue(prime_number_checker(2))

    def test_first_even_non_prime(self):
        """Verify the first even non-prime number (4)."""
        self.assertFalse(prime_number_checker(4))

    def test_smallest_two_digit_prime(self):
        """Verify the first two-digit prime number (11)."""
        self.assertTrue(prime_number_checker(11))

    def test_largest_two_digit_prime(self):
        """Verify the largest two-digit prime number (97)."""
        self.assertTrue(prime_number_checker(97))

    def test_consecutive_numbers_around_prime(self):
        """Verify behavior with consecutive numbers around a prime."""
        self.assertFalse(prime_number_checker(8))

    # Negative Number Tests
    def test_negative_one_is_not_prime(self):
        """Verify that -1 is correctly identified as not prime."""
        self.assertFalse(prime_number_checker(-1))

    def test_negative_prime_equivalent_is_not_prime(self):
        """Verify that negative of a prime number (-7) is not prime."""
        self.assertFalse(prime_number_checker(-7))

    # Input Validation Tests
    def test_string_input_raises_type_error(self):
        """Verify that string input raises TypeError."""
        with self.assertRaises(TypeError):
            prime_number_checker("2")

    def test_float_input_raises_type_error(self):
        """Verify that float input raises TypeError."""
        with self.assertRaises(TypeError):
            prime_number_checker(3.14)

    def test_none_input_raises_type_error(self):
        """Verify that None input raises TypeError."""
        with self.assertRaises(TypeError):
            prime_number_checker(None)

    def test_list_input_raises_type_error(self):
        """Verify that list input raises TypeError."""
        with self.assertRaises(TypeError):
            prime_number_checker([2, 3, 5])

    def test_dict_input_raises_type_error(self):
        """Verify that dictionary input raises TypeError."""
        with self.assertRaises(TypeError):
            prime_number_checker({"number": 7})


if __name__ == "__main__":
    unittest.main()
