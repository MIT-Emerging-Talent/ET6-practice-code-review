"""
Unit tests for the fizz_buzz function.
"""

import unittest
from solutions.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """Test cases for the fizz_buzz function."""

    def test_standard_case(self):
        """Test standard behavior of FizzBuzz with mixed inputs."""
        result = fizz_buzz([1, 3, 5, 15, 16])
        self.assertEqual(
            result, ["1", "Fizz", "Buzz", "FizzBuzz", "16"], "Failed on standard case."
        )

    def test_all_fizz(self):
        """Test FizzBuzz with all multiples of 3."""
        result = fizz_buzz([3, 6, 9])
        self.assertEqual(
            result, ["Fizz", "Fizz", "Fizz"], "Failed on all multiples of 3."
        )

    def test_all_buzz(self):
        """Test FizzBuzz with all multiples of 5."""
        result = fizz_buzz([5, 10, 20])
        self.assertEqual(
            result, ["Buzz", "Buzz", "Buzz"], "Failed on all multiples of 5."
        )

    def test_all_fizzbuzz(self):
        """Test FizzBuzz with all multiples of both 3 and 5."""
        result = fizz_buzz([15, 30, 45])
        self.assertEqual(
            result,
            ["FizzBuzz", "FizzBuzz", "FizzBuzz"],
            "Failed on all multiples of 3 and 5.",
        )

    def test_no_fizzbuzz(self):
        """Test FizzBuzz with no multiples of 3 or 5."""
        result = fizz_buzz([1, 2, 4, 7])
        self.assertEqual(
            result, ["1", "2", "4", "7"], "Failed on no multiples of 3 or 5."
        )

    def test_empty_list(self):
        """Test FizzBuzz with an empty list."""
        result = fizz_buzz([])
        self.assertEqual(result, [], "Failed on empty list.")

    def test_invalid_input_type(self):
        """Test FizzBuzz with invalid input type."""
        with self.assertRaises(TypeError) as context:
            fizz_buzz("not a list")
        self.assertEqual(str(context.exception), "Input must be a list.")

    def test_invalid_element_type(self):
        """Test FizzBuzz with invalid element types in the list."""
        with self.assertRaises(TypeError) as context:
            fizz_buzz([1, "string", 3.5])
        self.assertEqual(
            str(context.exception), "All elements in the list must be integers."
        )

    def test_negative_integers(self):
        """Test FizzBuzz with negative integers in the list."""
        with self.assertRaises(ValueError) as context:
            fizz_buzz([-1, 3, 5])
        self.assertEqual(
            str(context.exception), "All integers in the list must be non-negative."
        )

    def test_zero(self):
        """Test FizzBuzz with zero as input."""
        result = fizz_buzz([0])
        self.assertEqual(result, ["FizzBuzz"], "Failed on input containing zero.")

    def test_performance_large_list(self):
        """Test FizzBuzz with a large input list for performance."""
        large_input = list(range(1, 1_000_000))  # 1 million numbers
        result = fizz_buzz(large_input)  # Ensure it runs without errors
        self.assertEqual(
            len(result), len(large_input), "Output length mismatch for large input."
        )


if __name__ == "__main__":
    unittest.main()
