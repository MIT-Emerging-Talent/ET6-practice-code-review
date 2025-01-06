"""
Unit tests for the check_cat_dog module.
"""

import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))


class TestHasEqualCatDogOccurrences(unittest.TestCase):
    """Test cases for the has_equal_cat_dog_occurrences function."""

    def test_equal_counts(self):
        """Test when 'cat' and 'dog' appear the same number of times."""
        self.assertTrue(has_equal_cat_dog_occurrences("catdog"))

    def test_more_cats(self):
        """Test when 'cat' appears more than 'dog'."""
        self.assertFalse(has_equal_cat_dog_occurrences("catcat"))

    def test_more_dogs(self):
        """Test when 'dog' appears more than 'cat'."""
        self.assertFalse(has_equal_cat_dog_occurrences("dogdog"))

    def test_no_occurrences(self):
        """Test when neither 'cat' nor 'dog' appear."""
        self.assertTrue(has_equal_cat_dog_occurrences(""))

    def test_non_string_input(self):
        """Test when input is not a string."""
        with self.assertRaises(TypeError):
            has_equal_cat_dog_occurrences(12345)

    def test_boundary_case(self):
        """Test with mixed cases and adjacent occurrences."""
        self.assertTrue(has_equal_cat_dog_occurrences("1cat1cadodog"))

    def test_input_too_long(self):
        """Test when input string exceeds the maximum allowed length."""
        with self.assertRaises(AssertionError):
            has_equal_cat_dog_occurrences("catdogcatdogcatdog")


if __name__ == "__main__":
    unittest.main()
