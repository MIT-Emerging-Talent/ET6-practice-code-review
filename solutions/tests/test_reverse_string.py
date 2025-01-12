import unittest
from solutions.reverse_string import (
    reverse_string,
)  # Import the reverse_string function


class TestReverseString(unittest.TestCase):
    """Test cases for the reverse_string function.

    This class contains unit tests for the reverse_string function to ensure
    that it correctly reverses strings under various scenarios.
    """

    def test_reverse_normal(self):
        """Test reversing a normal string.

        This test checks that the function correctly reverses a typical string
        with multiple characters.
        """
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty(self):
        """Test reversing an empty string.

        This test verifies that the function returns an empty string when
        the input is empty.
        """
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        """Test reversing a single character string.

        This test checks that the function returns the same character when
        the input is a single character string.
        """
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_palindrome(self):
        """Test reversing a palindrome.

        This test verifies that the function returns the same string when
        the input is a palindrome.
        """
        self.assertEqual(reverse_string("madam"), "madam")

    def test_reverse_spaces(self):
        """Test reversing a string with spaces.

        This test checks that the function correctly reverses a string that
        contains spaces, ensuring that the spaces are also reversed.
        """
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")


if __name__ == "__main__":
    unittest.main()
