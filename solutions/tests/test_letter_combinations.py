import unittest
from solutions.letter_combinations import letter_combinations


class TestLetterCombinations(unittest.TestCase):
    """Tests for the letter_combinations function using unittest."""

    def test1(self):
        """Test '23' returns the expected nine combinations."""
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(sorted(letter_combinations("23")), sorted(expected))

    def test2(self):
        """Test empty string returns an empty list."""
        self.assertEqual(letter_combinations(""), [])

    def test3(self):
        """Test '2' returns ['a', 'b', 'c']."""
        expected = ["a", "b", "c"]
        self.assertEqual(letter_combinations("2"), expected)

    def test4(self):
        """Test that digits outside '2'..'9' raise an AssertionError."""
        with self.assertRaises(AssertionError):
            letter_combinations("1")

    def test5(self):
        """Test that more than four digits raise an AssertionError."""
        with self.assertRaises(AssertionError):
            letter_combinations("23456")

    def test6(self):
        """
        Test '727' returns 48 distinct combinations.
        Therefore, we'll just check the number of combinations to avoid overloading our code"""
        result = letter_combinations("727")
        self.assertEqual(len(result), 48)


if __name__ == "__main__":
    unittest.main()
