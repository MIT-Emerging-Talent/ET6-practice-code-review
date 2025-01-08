import unittest
from solutions.is_palindrome import Solution


class TestIsPalindrome(unittest.TestCase):
    """
    Unit tests for the is_palindrome function in the Solution class.
    """

    def setUp(self):
        """
        Set up the test case environment by initializing a Solution object.
        """
        self.solution = Solution()

    def test_positive_palindrome(self):
        """
        Test that the function returns True for a positive palindrome number.
        """
        self.assertTrue(self.solution.is_palindrome(121))

    def test_negative_number(self):
        """
        Test that the function returns False for a negative number.
        """
        self.assertFalse(self.solution.is_palindrome(-121))

    def test_non_palindrome(self):
        """
        Test that the function returns False for a number that is not a palindrome.
        """
        self.assertFalse(self.solution.is_palindrome(123))

    def test_single_digit(self):
        """
        Test that the function returns True for a single-digit number.
        """
        self.assertTrue(self.solution.is_palindrome(7))


if __name__ == "__main__":
    unittest.main()
