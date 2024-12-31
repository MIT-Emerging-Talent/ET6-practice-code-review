import unittest
from solutions.length_of_longest_substring import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    """Unit tests for lengthOfLongestSubstring function."""

    def test_basic_cases(self):
        """Test basic cases."""
        self.assertEqual(Solution().lengthOfLongestSubstring("abcabcbb"), 3)
        self.assertEqual(Solution().lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(Solution().lengthOfLongestSubstring("pwwkew"), 3)

    def test_edge_cases(self):
        """Test edge cases."""
        self.assertEqual(Solution().lengthOfLongestSubstring(""), 0)  # Empty string
        self.assertEqual(Solution().lengthOfLongestSubstring("a"), 1)  # Single character
        self.assertEqual(Solution().lengthOfLongestSubstring("aa"), 1)  # Repeating characters

    def test_boundary_cases(self):
        """Test boundary cases."""
        self.assertEqual(Solution().lengthOfLongestSubstring("abcdefghij"), 10)  # All unique
        self.assertEqual(Solution().lengthOfLongestSubstring("a" * 1000), 1)  # All same characters
        self.assertEqual(Solution().lengthOfLongestSubstring("abc" * 333), 3)  # Repeating pattern

    def test_invalid_input(self):
        """Test invalid input."""
        with self.assertRaises(ValueError):
            Solution().lengthOfLongestSubstring(123)  # Non-string input

if __name__ == "__main__":
    unittest.main()
