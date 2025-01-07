# test_prime_filter_challenge
"""
Test module for filter_primes function.
Contains correct tests to help identify bugs in the implementation.

Test categories:
    - Standard cases: Lists with various integers, both prime and non-prime.
    - Edge cases: Empty lists, lists with only non-prime numbers.
    - Defensive cases: Invalid inputs (e.g., non-list types, mixed data types).

Created on 2025-01-05
Author: Aseel AbuKmail
"""

import sys
import os
import unittest

# Add the directory containing mirror_words_challenge.py to the module search path
sys.path.append(
    "C:/Users/pc/.vscode/VS code Files/MIT - Project/ET6-foundations-group-17-main/solutions"
)

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from solutions.prime_filter_challenge import filter_primes


class TestPrimeFilter(unittest.TestCase):
    """Tests for filter_primes function"""

    # Standard test cases
    def test_filter_primes_regular_list(self):
        """It should return a list containing only prime numbers"""
        actual = filter_primes([2, 3, 4, 5, 6, 7])
        expected = [2, 3, 5, 7]
        self.assertEqual(actual, expected)

    def test_filter_primes_with_negative_numbers(self):
        """It should return a list of primes, ignoring negative numbers"""
        actual = filter_primes([-2, -3, 4, 5, 6, -7])
        expected = [5]
        self.assertEqual(actual, expected)

    def test_filter_primes_with_no_primes(self):
        """It should return an empty list if there are no primes"""
        actual = filter_primes([4, 6, 8, 10])
        expected = []
        self.assertEqual(actual, expected)

    # Edge cases
    def test_empty_list(self):
        """It should return an empty list for an empty input list"""
        actual = filter_primes([])
        expected = []
        self.assertEqual(actual, expected)

    def test_single_number(self):
        """It should return a list with the single number if it's prime, or empty if not"""
        actual = filter_primes([7])
        expected = [7]
        self.assertEqual(actual, expected)

    def test_list_with_only_non_prime_numbers(self):
        """It should return an empty list if all numbers are non-prime"""
        actual = filter_primes([1, 4, 6, 8])
        expected = []
        self.assertEqual(actual, expected)

    # Defensive test cases
    def test_non_list_input(self):
        """It should raise TypeError for non-list input"""
        with self.assertRaises(TypeError):
            filter_primes(12345)

    def test_input_with_mixed_data_types(self):
        """It should raise TypeError for input with mixed types"""
        with self.assertRaises(ValueError):
            filter_primes([2, "3", 5])


if __name__ == "__main__":
    unittest.main()
