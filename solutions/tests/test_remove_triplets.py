import unittest
from solutions.remove_triplets import remove_triplets


# Test cases for remove_triplets function
class TestRemoveTriplets(unittest.TestCase):
    """
    Unit tests for the remove_triplets function.

    This module contains a set of test cases for the remove_triplets function
    from the solutions package. The function ensures no three consecutive
    characters remain in a string by removing the minimum number of characters
    required.

    The tests cover various scenarios, including:
    - Empty string input
    - Strings without consecutive characters
    - Strings with one or more groups of consecutive characters
    - Boundary cases such as single characters or long sequences
    - Defensive checks for invalid input types

    Test cases are implemented using Python's unittest framework.
    """

    def test_empty_input(self):
        """Test when input is empty"""
        self.assertEqual(remove_triplets(""), "")

    def test_single_character_input(self):
        """Test input with a single character"""
        self.assertEqual(remove_triplets("a"), "a")

    def test_two_identical_characters(self):
        """Test input with two identical characters"""
        self.assertEqual(remove_triplets("aa"), "aa")

    def test_three_identical_characters(self):
        """Test input with three identical characters"""
        self.assertEqual(remove_triplets("aaa"), "aa")

    def test_input_without_consecutive(self):
        """Test input without consecutive characters"""
        self.assertEqual(remove_triplets("abc"), "abc")

    def test_input_with_one_consecutive(self):
        """Test input with one consecutive character"""
        self.assertEqual(remove_triplets("helllo"), "hello")
        self.assertEqual(remove_triplets("leeetcode"), "leetcode")

    def test_input_with_two_consecutive(self):
        """Test input with two consecutive characters"""
        self.assertEqual(remove_triplets("aaabaaaa"), "aabaa")

    def test_mixed_triplets(self):
        """Test input with multiple groups of triplets"""
        self.assertEqual(remove_triplets("aaabbbcccaaa"), "aabbccaa")

    def test_invalid_input_type(self):
        """Test invalid input type"""
        with self.assertRaises(AssertionError):
            remove_triplets(123)  # Passing an integer instead of a string


if __name__ == "__main__":
    unittest.main()
