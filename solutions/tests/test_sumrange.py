import unittest
# The line `from solutions.sum_range import sum_range` is importing the
# `sum_range` function from a module named `sum_range` located in a package named
# `solutions`. This allows you to use the `sum_range` function in your test cases
# without having to define it again in the test file. This is a common practice in
# Python to organize code into modules and packages for better maintainability and
# reusability.
from solutions.sum_range import sum_range

class TestSumRange(unittest.TestCase):
    """Unit tests for the Sum_range function."""

    def test_positive_range(self):
        """Test with a normal positive range."""
        self.assertEqual(sum_range(1, 5), 15)

    def test_reversed_range(self):
        """Test when start > end (reversed input)."""
        self.assertEqual(sum_range(5, 1), 15)

    def test_single_number(self):
        """Test a range with a single number."""
        self.assertEqual(sum_range(10, 10), 10)

    def test_negative_range(self):
        """Test a range that includes negative numbers."""
        self.assertEqual(sum_range(-3, 3), 0)

    def test_large_range(self):
        """Test with a large range."""
        self.assertEqual(sum_range(1, 100), 5050)

    def test_large_range_reversed(self):
        """Test with a large range."""
        self.assertEqual(sum_range(100, 1), 5050)

    def test_float_range(self):
        """Test with a range that includes floats."""
        with self.assertRaises(AssertionError):
            sum_range(0.5, 3.5) 
