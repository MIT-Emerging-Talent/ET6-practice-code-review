"""
Team Number: 28
Team Name: MIT Alpha
Author: Duha Mohammed
"""

import unittest
from solutions.add_2_numbers import add_2_numbers


class TestAdd2Numbers(unittest.TestCase):
    """Test cases for add_2_numbers function."""

    def test_add_integers(self):
        """Test adding two integers."""
        self.assertEqual(add_2_numbers(3, 5), 8)

    def test_add_floats(self):
        """Test adding two float numbers."""
        self.assertAlmostEqual(add_2_numbers(2.5, 4.5), 7.0)

    def test_invalid_input(self):
        """Test that the function raises an AssertionError for invalid inputs."""
        with self.assertRaises(AssertionError):
            add_2_numbers("3", 5)
