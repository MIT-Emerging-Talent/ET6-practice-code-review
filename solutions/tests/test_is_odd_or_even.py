import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from solutions.is_odd_or_even import is_odd_or_even


class TestIsOddOrEven(unittest.TestCase):
    """Unit tests for the is_odd_or_even function."""

    def test_even_numbers(self):
        """Test that even numbers return 'Even'."""
        self.assertEqual(is_odd_or_even(4), "Even")
        self.assertEqual(is_odd_or_even(0), "Even")
        self.assertEqual(is_odd_or_even(-2), "Even")

    def test_odd_numbers(self):
        """Test that odd numbers return 'Odd'."""
        self.assertEqual(is_odd_or_even(7), "Odd")
        self.assertEqual(is_odd_or_even(-3), "Odd")
        self.assertEqual(is_odd_or_even(1), "Odd")


if __name__ == "__main__":
    unittest.main()
