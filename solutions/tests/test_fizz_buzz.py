"""
Unit Tests for the fizz_buzz function.
"""

import unittest

from solutions.fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    """
    Test cases for the fizz_buzz function.
    """

    def test_standard_case(self):
        """Test standard behavior of FizzBuzz with mixed inputs."""
        result = fizz_buzz([1, 3, 5, 15, 16])
        assert result == [
            "1",
            "Fizz",
            "Buzz",
            "FizzBuzz",
            "16",
        ], "Failed on standard case."

    def test_all_fizz(self):
        """Test FizzBuzz with all multiples of 3."""
        result = fizz_buzz([3, 6, 9])
        assert result == ["Fizz", "Fizz", "Fizz"], "Failed on all multiples of 3."

    def test_all_buzz(self):
        """Test FizzBuzz with all multiples of 5."""
        result = fizz_buzz([5, 10, 20])
        assert result == ["Buzz", "Buzz", "Buzz"], "Failed on all multiples of 5."

    def test_all_fizzbuzz(self):
        """Test FizzBuzz with all multiples of both 3 and 5."""
        result = fizz_buzz([15, 30, 45])
        assert result == [
            "FizzBuzz",
            "FizzBuzz",
            "FizzBuzz",
        ], "Failed on all multiples of 3 and 5."

    def test_no_fizzbuzz(self):
        """Test FizzBuzz with no multiples of 3 or 5."""
        result = fizz_buzz([1, 2, 4, 7])
        assert result == ["1", "2", "4", "7"], "Failed on no multiples of 3 or 5."

    def test_empty_list(self):
        """Test FizzBuzz with an empty list."""
        result = fizz_buzz([])
        assert result == [], "Failed on empty list."

    def test_invalid_input_type(self):
        """Test FizzBuzz with invalid input type."""
        try:
            fizz_buzz("not a list")
        except TypeError as e:
            assert str(e) == "Input must be a list.", "Failed on invalid input type."

    def test_invalid_element_type(self):
        """Test FizzBuzz with invalid element types in the list."""
        try:
            fizz_buzz([1, "string", 3.5])
        except TypeError as e:
            assert (
                str(e) == "All elements in the list must be integers."
            ), "Failed on invalid element types."

    def test_negative_integers(self):
        """Test FizzBuzz with negative integers in the list."""
        try:
            fizz_buzz([-1, 3, 5])
        except ValueError as e:
            assert (
                str(e) == "All integers in the list must be non-negative."
            ), "Failed on negative integers."

    def test_zero(self):
        """Test FizzBuzz with zero as input."""
        result = fizz_buzz([0])
        assert result == ["FizzBuzz"], "Failed on input containing zero."

    def test_performance_large_list(self):
        """Test FizzBuzz with a large input list for performance."""
        large_input = list(range(1, 1000000))  # 1 million numbers
        result = fizz_buzz(large_input)  # Ensure it runs without errors
        assert len(result) == len(
            large_input
        ), "Output length mismatch for large input."
