"""
Testing Strategy Overview for test_find_duplicates.py:

1. Basic Functionality Tests:
   - Empty list handling
   - No duplicates case
   - Single duplicate
   - Multiple duplicates
   - All items being duplicates

2. Data Type Tests:
   - String duplicates
   - Mixed type handling
   - Nested list handling

3. Order Preservation Tests:
   - First appearance order
   - Case sensitivity
   - Multiple occurrences

4. Defensive Programming Tests:
   - None input
   - Non-list input
   - Set input
   - Tuple input
"""

"""
Test module for find_duplicates function.

This module contains comprehensive unit tests for the find_duplicates function,
covering basic functionality, edge cases, and error conditions.

Created on 2025-01-12
@author: Karina
"""

import unittest
from find_duplicates import find_duplicates


class TestFindDuplicates(unittest.TestCase):
    """Test suite for the find_duplicates function."""

    # Basic functionality tests
    def test_empty_list(self):
        """Test that an empty list returns an empty list."""
        self.assertEqual(find_duplicates([]), [])

    def test_no_duplicates(self):
        """Test that a list with no duplicates returns an empty list."""
        self.assertEqual(find_duplicates([1, 2, 3, 4, 5]), [])

    def test_single_duplicate(self):
        """Test a list with one duplicate element."""
        self.assertEqual(find_duplicates([1, 2, 2, 3]), [2])

    def test_multiple_duplicates(self):
        """Test a list with multiple duplicate elements."""
        self.assertEqual(find_duplicates([1, 2, 2, 3, 3, 3]), [2, 3])

    def test_all_duplicates(self):
        """Test a list where all elements are duplicates."""
        self.assertEqual(find_duplicates([1, 1, 1]), [1])

    # Order preservation tests
    def test_order_preservation(self):
        """Test that duplicates are returned in order of first appearance."""
        self.assertEqual(find_duplicates([3, 1, 2, 1, 3]), [3, 1])

    def test_multiple_occurrences(self):
        """Test handling of elements that appear more than twice."""
        self.assertEqual(find_duplicates([1, 2, 1, 2, 1, 2]), [1, 2])

    # Type handling tests
    def test_string_duplicates(self):
        """Test handling of string duplicates."""
        self.assertEqual(find_duplicates(["a", "b", "a", "c"]), ["a"])

    def test_mixed_types(self):
        """Test list with mixed types."""
        self.assertEqual(find_duplicates([1, "1", 1, "1"]), [1, "1"])

    def test_nested_lists(self):
        """Test handling of nested lists."""
        self.assertEqual(find_duplicates([[1], [2], [1], [3]]), [[1]])

    def test_case_sensitivity(self):
        """Test that string comparison is case-sensitive."""
        self.assertEqual(find_duplicates(["A", "a", "A"]), ["A"])

    # Edge cases and special values
    def test_boolean_values(self):
        """Test handling of boolean values."""
        self.assertEqual(find_duplicates([True, False, True]), [True])

    def test_zero_values(self):
        """Test handling of zero values."""
        self.assertEqual(find_duplicates([0, 1, 0, 2]), [0])

    def test_none_values(self):
        """Test handling of None values."""
        self.assertEqual(find_duplicates([None, 1, None]), [None])

    # Defensive programming tests
    def test_non_list_input(self):
        """Test that non-list input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates("not a list")

    def test_none_input(self):
        """Test that None input raises AssertionError."""
        with self.assertRaises(AssertionError):
            find_duplicates(None)

    def test_nested_empty_lists(self):
        """Test handling of nested empty lists."""
        self.assertEqual(find_duplicates([[], [], [1]]), [[]])


if __name__ == "__main__":
    unittest.main()
