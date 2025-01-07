"""
Unit tests for the largest_num function in the Find_largest_number module.

This module contains a set of test cases to ensure the correctness of the
find_largest_number function, which identifies the largest number in a given list.
"""

import unittest
# import sys

# sys.path.append("../")
from solutions.find_largest_number import find_largest_number


class TestLargestNum(unittest.TestCase):
    """
    Unit tests for the find_largest_number function, verifying its correctness
    across positive, negative, mixed, single-element, duplicate, and empty lists.
    """

    def test_positive_numbers(self) -> None:
        """Test case for a list of positive numbers."""
        self.assertEqual(find_largest_number([3, 9, 2, 3, 2]), 9)

    def test_negative_numbers(self) -> None:
        """Test case for a list of negative numbers."""
        self.assertEqual(find_largest_number([-3, -1, -2, -7, -8]), -1)

    def test_mixed_numbers(self) -> None:
        """Test case for a list of mixed positive and negative numbers."""
        self.assertEqual(find_largest_number([4, -9, 3, -8, 5]), 5)

    def test_single_element(self) -> None:
        """Test case for a list with a single element."""
        self.assertEqual(find_largest_number([100]), 100)

    def test_duplicates(self) -> None:
        """Test case for a list with duplicate numbers."""
        self.assertEqual(find_largest_number([1, 1, 1, 1]), 1)

    def test_empty_list(self) -> None:
        """Test case for an empty list (should raise ValueError)."""
        with self.assertRaises(ValueError):
            find_largest_number([])

    def test_non_numeric_input(self) -> None:
        """Test case for non-numeric input (should raise ValueError)."""
        with self.assertRaises(ValueError):
            find_largest_number(["a", "b", "c"])

    def test_large_numbers(self) -> None:
        """Test case for large numbers."""
        self.assertEqual(find_largest_number([1e10, 1e15, 1e11]), 1e15)


if __name__ == "__main__":
    unittest.main()
