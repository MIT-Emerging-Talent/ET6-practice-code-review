"""unittest code is a test suite that verifies the behavior of the function find_primes_in_list"""

import unittest

from solutions.primes import find_primes_in_list


class TestFindPrimesInList(unittest.TestCase):
    """To test the function find_primes_in_list"""

    def test_with_prime_numbers(self):
        """Verifies the function correctly identifies a list containing only prime numbers"""
        self.assertEqual(find_primes_in_list([2, 3, 5, 7]), [2, 3, 5, 7])

    def test_with_mixed_numbers(self):
        """Checks the function handles a mix of prime and non-prime numbers"""
        self.assertEqual(find_primes_in_list([1, 4, 6, 9, 11, 13]), [11, 13])

    def test_with_no_primes(self):
        """Tests the function when no prime numbers are in the input list"""
        self.assertEqual(find_primes_in_list([0, 1, 4, 6, 8, 10]), [])

    def test_with_large_range(self):
        """This function works correctly for a range of numbers, including consecutive primes"""
        self.assertEqual(
            find_primes_in_list(range(1, 20)), [2, 3, 5, 7, 11, 13, 17, 19]
        )

    def test_with_empty_list(self):
        """Ensures the function returns an empty list for an empty input"""
        self.assertEqual(find_primes_in_list([]), [])

    def test_with_negative_numbers(self):
        """Verifies the function ignores negative numbers, as they are not prime"""
        self.assertEqual(find_primes_in_list([-10, -3, -1, 0, 2, 3]), [2, 3])

    def test_with_duplicates(self):
        """Ensures the function includes duplicates if they are prime"""
        self.assertEqual(find_primes_in_list([2, 3, 3, 5, 5, 5]), [2, 3, 3, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()
