import unittest
from solutions.add_int_list import sum_of_squares


class TestSumOfSquares(unittest.TestCase):
    """
    Test cases for the `sum_of_squares` function,
    Each test verifies the correct behavior of the function for various edge
    cases and typical inputs.
    """

    def test_empty_list(self):
        """Test that an empty list returns a sum of 0."""
        self.assertEqual(sum_of_squares([]), 0)

    def test_list_with_no_integers(self):
        """Test that a list with no integers returns a sum of 0."""
        self.assertEqual(sum_of_squares(["a", 3.5, None]), 0)

    def test_list_with_only_integers(self):
        """Test that a list with integers calculates the correct sum of squares."""
        self.assertEqual(sum_of_squares([1, 2, 3]), 14)  # 1^2 + 2^2 + 3^2 = 14

    def test_list_with_negative_integers(self):
        """Test that negative integers are squared correctly."""
        self.assertEqual(
            sum_of_squares([-1, -2, -3]), 14
        )  # (-1)^2 + (-2)^2 + (-3)^2 = 14

    def test_list_with_mixed_elements(self):
        """Test that the function handles a mixed list and excludes non-integers."""
        self.assertEqual(sum_of_squares([1, "b", 2.5, 3]), 10)  # 1^2 + 3^2 = 10


if __name__ == "__main__":
    unittest.main()
