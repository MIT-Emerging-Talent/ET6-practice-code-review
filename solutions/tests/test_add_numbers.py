import unittest
from solutions.add_numbers import add_numbers


class TestAddNumbers(unittest.TestCase):
    """class of test cases"""

    def test_add_positive_numbers(self):
        """
        Test adding two positive numbers.

        This test ensures that the function correctly adds two positive integers
        and returns the expected result.
        """
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        """
        Test adding two negative numbers.

        This test checks that the function handles negative numbers correctly
        and returns the correct sum.
        """
        self.assertEqual(add_numbers(-1, -1), -2)

    def test_add_zero(self):
        """
        Test adding two zero values.

        This test confirms that the function returns zero when both inputs
        are zero.
        """
        self.assertEqual(add_numbers(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
