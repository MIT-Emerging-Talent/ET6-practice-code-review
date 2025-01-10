"""
Unit tests for the `sort_numbers` function in the `sort_numbers.py` module.

The tests cover:
- Sorting numbers in ascending order.
- Handling of empty lists.
- Handling of negative and decimal numbers.
- Validation of input types.
- Verification of no side effects.

Usage:
Run this module using `unittest` to verify the correctness of the function.

Example:
    python -m unittest test_challenge_4.py
"""

import os
import sys
import unittest
from solutions.challenge_4 import sort_numbers

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))


class TestSortNumbers(unittest.TestCase):
    """
    Unit tests for the sort_numbers function.
    """

    def test_sorted_list(self):
        """
        Test sorting a regular list of integers.

        Given:
        - List: [3, 1, 4, 1, 5]

        Expect:
        - Sorted list: [1, 1, 3, 4, 5].
        """
        self.assertEqual(sort_numbers([3, 1, 4, 1, 5]), [1, 1, 3, 4, 5])

    def test_empty_list(self):
        """
        Test sorting an empty list.

        Given:
        - List: []

        Expect:
        - Sorted list: [].
        """
        self.assertEqual(sort_numbers([]), [])

    def test_negative_numbers(self):
        """
        Test sorting a list with negative numbers.

        Given:
        - List: [-3, -1, -4, -1, -5]

        Expect:
        - Sorted list: [-5, -4, -3, -1, -1].
        """
        self.assertEqual(sort_numbers([-3, -1, -4, -1, -5]), [-5, -4, -3, -1, -1])

    def test_decimal_numbers(self):
        """
        Test sorting a list with decimal numbers.

        Given:
        - List: [3.1, 1.2, 4.3, 1.1, 5.5]

        Expect:
        - Sorted list: [1.1, 1.2, 3.1, 4.3, 5.5].
        """
        self.assertEqual(
            sort_numbers([3.1, 1.2, 4.3, 1.1, 5.5]), [1.1, 1.2, 3.1, 4.3, 5.5]
        )

    def test_mixed_numbers(self):
        """
        Test sorting a list with mixed integers and decimals.

        Given:
        - List: [3, 1.2, 4, 1.1, 5]

        Expect:
        - Sorted list: [1.1, 1.2, 3, 4, 5].
        """
        self.assertEqual(sort_numbers([3, 1.2, 4, 1.1, 5]), [1.1, 1.2, 3, 4, 5])

    def test_no_side_effects(self):
        """
        Test that the function does not modify the original list.

        Given:
        - Original list: [3, 1, 4]

        Expect:
        - Original list remains unchanged after sorting.
        """
        numbers = [3, 1, 4]
        sort_numbers(numbers)
        self.assertEqual(numbers, [3, 1, 4])

    def test_invalid_input_type(self):
        """
        Test that a TypeError is raised for non-list inputs.

        Given:
        - Invalid input: "not a list"

        Expect:
        - Raises TypeError.
        """
        with self.assertRaises(TypeError):
            sort_numbers("not a list")

    def test_invalid_element_type(self):
        """
        Test that a TypeError is raised for lists with non-numeric elements.

        Given:
        - Invalid input: [1, 2, "three"]

        Expect:
        - Raises TypeError.
        """
        with self.assertRaises(TypeError):
            sort_numbers([1, 2, "three"])


if __name__ == "__main__":
    unittest.main()
