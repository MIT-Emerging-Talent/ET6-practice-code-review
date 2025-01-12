"""
Unit tests for the fizzbuzz function from the solutions.fizz_buzz module.

This class uses the unittest framework to validate the behavior of the fizzbuzz function
across various input values, ensuring it produces the correct output lists. Tests include
cases for n = 0, 1, 3, 5, and 15, verifying the proper inclusion of Fizz, Buzz, and FizzBuzz 
in the outputs.
"""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from solutions.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Test cases for the fizzbuzz function.

    This class contains unit tests for the fizzbuzz function to ensure
    that it produces the expected output for various input values.
    """

    def test_fizzbuzz_15(self):
        """Test FizzBuzz for n = 15.

        This test checks that the output for n=15 matches the expected
        list which includes Fizz, Buzz, and FizzBuzz at the correct
        positions.
        """
        expected = [
            1,
            2,
            "Fizz",
            4,
            "Buzz",
            "Fizz",
            7,
            8,
            "Fizz",
            "Buzz",
            11,
            "Fizz",
            13,
            14,
            "FizzBuzz",
        ]
        self.assertEqual(fizz_buzz(15), expected)

    def test_fizzbuzz_3(self):
        """Test FizzBuzz for n = 3.

        This test checks that for n=3, the output should return
        a list containing the numbers 1, 2, and 'Fizz'.
        """
        expected = [1, 2, "Fizz"]
        self.assertEqual(fizz_buzz(3), expected)

    def test_fizzbuzz_5(self):
        """Test FizzBuzz for n = 5.

        This test verifies that for n=5, the output list includes
        numbers 1, 2, 'Fizz', 4, and 'Buzz'.
        """
        expected = [1, 2, "Fizz", 4, "Buzz"]
        self.assertEqual(fizz_buzz(5), expected)

    def test_fizzbuzz_1(self):
        """Test FizzBuzz for n = 1.

        This test checks that for n=1, the output should simply be
        a list containing the number 1.
        """
        expected = [1]
        self.assertEqual(fizz_buzz(1), expected)

    def test_fizzbuzz_0(self):
        """Test FizzBuzz for n = 0.

        This test checks that for n=0, the output should be an
        empty list since there are no numbers to include.
        """
        expected = []
        self.assertEqual(fizz_buzz(0), expected)


if __name__ == "__main__":
    unittest.main()
