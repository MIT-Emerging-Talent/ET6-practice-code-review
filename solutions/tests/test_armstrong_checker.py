import unittest

from ..armstrong_checker import armstrong_checker


class TestArmstrongChecker(unittest.TestCase):
    """Test cases for the armstrong_checker function."""

    def test_valid_armstrong_numbers(self):
        """Test cases where the number is an Armstrong number."""
        self.assertEqual(armstrong_checker(153), "True")
        self.assertEqual(armstrong_checker(9474), "True")
        self.assertEqual(armstrong_checker(9475), "False")

    def test_non_armstrong_numbers(self):
        """Test cases where the number is not an Armstrong number."""
        self.assertEqual(armstrong_checker(123), "False")
        self.assertEqual(armstrong_checker(100), "False")

    def test_invalid_inputs(self):
        """Test cases for invalid inputs."""
        self.assertEqual(armstrong_checker(-153), "Invalid input")
        self.assertEqual(armstrong_checker("153"), "Invalid input")
        self.assertEqual(armstrong_checker(0.5), "Invalid input")
