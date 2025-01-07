"""
Module represents unit test for fizzbuzz_challenge

Created on 01/05/2024
Author Svitlana Musiienko
"""

import unittest

from ..fizzbuzz_challenge import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Test the fizzbuzz function"""

    def test_fizz(self):
        """It should print "Fizz" instead 3 and 6 and return other numbers till 6"""
        actual = fizzbuzz(6)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz"]
        self.assertEqual(actual, expected)

    def test_buzz(self):
        """It should print "Buzz" instead 5 and 10 and return other numbers till 10"""
        actual = fizzbuzz(10)
        expected = [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
        self.assertEqual(actual, expected)

    def test_fizzbuzz(self):
        """It should print "FizzBuzz" for 15 and other according to rules"""
        actual = fizzbuzz(15)
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
        self.assertEqual(actual, expected)

    def test_other(self):
        """It should return numbers till 2"""
        actual = fizzbuzz(2)
        expected = [
            1,
            2,
        ]
        self.assertEqual(actual, expected)

    def test_less_than_0(self):
        """It should raise an assertion error if the argument is less than 0"""
        with self.assertRaises(AssertionError):
            fizzbuzz(-1)

    def test_not_an_integer(self):
        """It should raise an assertion error if the argument is not integer"""
        with self.assertRaises(AssertionError):
            fizzbuzz(2.0)


if __name__ == "__main__":
    unittest.main()
