import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from solutions.is_odd_or_even import is_odd_or_even
import unittest

class TestIsOddOrEven(unittest.TestCase):
    
    def test_is_odd(self):
        """Test for odd numbers."""
        self.assertEqual(is_odd_or_even(7), "Odd")

    def test_is_even(self):
        """Test for even numbers."""
        self.assertEqual(is_odd_or_even(4), "Even")

    def test_is_zero(self):
        """Test for zero (even)."""
        self.assertEqual(is_odd_or_even(0), "Even")

    def test_is_negative_odd(self):
        """Test for negative odd numbers."""
        self.assertEqual(is_odd_or_even(-3), "Odd")

    def test_is_negative_even(self):
        """Test for negative even numbers."""
        self.assertEqual(is_odd_or_even(-2), "Even")

if __name__ == '__main__':
    unittest.main()
