"""
Unit tests for the cat_dog module.
"""

import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from solutions.cat_dog import cat_dog  # noqa: E402


class TestCatDog(unittest.TestCase):
    """Test cases for the cat_dog function."""

    def test_equal_counts(self):
        """Test when 'cat' and 'dog' appear the same number of times."""
        self.assertTrue(cat_dog("catdog"))

    def test_more_cats(self):
        """Test when 'cat' appears more than 'dog'."""
        self.assertFalse(cat_dog("catcat"))

    def test_more_dogs(self):
        """Test when 'dog' appears more than 'cat'."""
        self.assertFalse(cat_dog("dogdog"))

    def test_no_occurrences(self):
        """Test when neither 'cat' nor 'dog' appear."""
        self.assertTrue(cat_dog(""))

    def test_non_string_input(self):
        """Test when input is not a string."""
        with self.assertRaises(TypeError):
            cat_dog(12345)

    def test_boundary_case(self):
        """Test with mixed cases and adjacent occurrences."""
        self.assertTrue(cat_dog("1cat1cadodog"))


if __name__ == "__main__":
    unittest.main()
