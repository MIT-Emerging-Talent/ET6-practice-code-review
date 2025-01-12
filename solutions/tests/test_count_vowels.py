import unittest

from solutions.count_vowels import count_vowels  # Import the count_vowels function


class TestCountVowels(unittest.TestCase):
    """Test cases for the count_vowels function.

    This class contains unit tests for the count_vowels function to ensure
    that it accurately counts the number of vowels in various input strings.
    """

    def test_count_vowels_normal(self):
        """Test counting vowels in a normal string.

        This test checks that the function correctly counts the vowels in a
        typical string with mixed characters.
        """
        self.assertEqual(count_vowels("Nagham"), 2)

    def test_count_vowels_empty(self):
        """Test counting vowels in an empty string.

        This test verifies that the function returns 0 when the input string
        is empty.
        """
        self.assertEqual(count_vowels(""), 0)

    def test_count_vowels_no_vowels(self):
        """Test counting vowels in a string with no vowels.

        This test checks that the function returns 0 when there are no vowels
        in the input string.
        """
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_count_vowels_case_insensitive(self):
        """Test counting vowels in a case-insensitive manner.

        This test verifies that the function counts both uppercase and lowercase
        vowels correctly.
        """
        self.assertEqual(count_vowels("AbEcIdOfUg"), 5)

    def test_count_vowels_with_spaces(self):
        """Test counting vowels in a string with spaces.

        This test checks that the function correctly counts vowels in a string
        that contains spaces and punctuation.
        """
        self.assertEqual(count_vowels("Hello World!"), 3)


if __name__ == "__main__":
    unittest.main()
