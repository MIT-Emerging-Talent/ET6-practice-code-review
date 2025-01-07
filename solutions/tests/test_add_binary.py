"""
Unit tests for the add_binary method.

This module tests various scenarios for the `add_binary` method
from the `solutions.add_binary` module to ensure its correctness.

Tests include:
    - Simple binary addition
    - Different length binaries
    - Large binary numbers
"""

import unittest

from solutions.add_binary import Solution


class TestAddBinary(unittest.TestCase):
    """Unit tests for the add_binary method."""

    def setUp(self):
        """Set up a Solution instance for testing."""
        self.solution = Solution()

    def test_simple_binary_addition(self):
        """Test binary addition of simple cases."""
        self.assertEqual(self.solution.add_binary("11", "1"), "100")
        self.assertEqual(self.solution.add_binary("1010", "1011"), "10101")

    def test_different_length_binaries(self):
        """Test binary addition with different lengths."""
        self.assertEqual(self.solution.add_binary("1", "111"), "1000")
        self.assertEqual(self.solution.add_binary("10", "10101"), "10111")
