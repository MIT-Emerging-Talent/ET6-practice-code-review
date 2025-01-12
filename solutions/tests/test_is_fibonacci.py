"""unittest code verifies the behavior of is_fibonacci_number to
check whether a number is fibonaaci number or not"""

import unittest

from solutions.is_fibonacci import is_fibonacci_number


class TestIsFibonacciNumber(unittest.TestCase):
    """Test the is_fibonacci_number function"""

    def test_fibonacci_numbers(self):
        """Test known Fibonacci numbers"""
        self.assertTrue(is_fibonacci_number(0))
        self.assertTrue(is_fibonacci_number(1))
        self.assertTrue(is_fibonacci_number(2))
        self.assertTrue(is_fibonacci_number(3))
        self.assertTrue(is_fibonacci_number(5))
        self.assertTrue(is_fibonacci_number(8))
        self.assertTrue(is_fibonacci_number(13))
        self.assertTrue(is_fibonacci_number(21))
        self.assertTrue(is_fibonacci_number(34))
        self.assertTrue(is_fibonacci_number(144))

    def test_non_fibonacci_numbers(self):
        """Test non-Fibonacci numbers"""
        # Test non-Fibonacci numbers
        self.assertFalse(is_fibonacci_number(4))
        self.assertFalse(is_fibonacci_number(6))
        self.assertFalse(is_fibonacci_number(7))
        self.assertFalse(is_fibonacci_number(9))
        self.assertFalse(is_fibonacci_number(10))
        self.assertFalse(is_fibonacci_number(11))
        self.assertFalse(is_fibonacci_number(15))
        self.assertFalse(is_fibonacci_number(20))

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertFalse(is_fibonacci_number(-1))
        self.assertFalse(is_fibonacci_number(-5))
        self.assertFalse(is_fibonacci_number(-8))

    def test_large_fibonacci_numbers(self):
        """Test larger Fibonacci numbers"""
        # Test larger Fibonacci numbers
        self.assertTrue(is_fibonacci_number(233))
        self.assertTrue(is_fibonacci_number(377))

    def test_large_non_fibonacci_numbers(self):
        """Test larger non-Fibonacci numbers"""
        self.assertFalse(is_fibonacci_number(300))
        self.assertFalse(is_fibonacci_number(400))


if __name__ == "__main__":
    unittest.main()
