"""
This module contains unit tests for the `calculate_simple_interest` function.

The tests cover:
- Standard simple interest calculations.
- Edge cases where inputs such as principal, rate, or time are zero.
- Validation of correct implementation based on the simple interest formula.

Run this module using `unittest` to verify the function's correctness.
"""

import unittest
from solutions.simple_interest_calculator import (
    calculate_simple_interest,
)  # Adjust the import based on your actual function


class TestSimpleInterestCalculator(unittest.TestCase):
    """Unit tests for the Simple Interest Calculator."""

    def test_calculate_simple_interest(self):
        """
        Test the calculation of simple interest for a standard case.

        Given:
        - Principal: 1000
        - Rate of interest: 5%
        - Time: 3 years

        Expect:
        - The calculated simple interest to be 150.
        """
        principal = 1000
        rate_of_interest = 5
        time = 3

        expected_result = 150
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_principal(self):
        """
        Test simple interest calculation with zero principal.

        Given:
        - Principal: 0
        - Rate of interest: 5%
        - Time: 3 years

        Expect:
        - The calculated simple interest to be 0.
        """
        principal = 0
        rate_of_interest = 5
        time = 3

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_time(self):
        """
        Test simple interest calculation with zero time.

        Given:
        - Principal: 1000
        - Rate of interest: 5%
        - Time: 0 years

        Expect:
        - The calculated simple interest to be 0.
        """
        principal = 1000
        rate_of_interest = 5
        time = 0

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    def test_calculate_simple_interest_zero_rate(self):
        """
        Test simple interest calculation with zero rate of interest.

        Given:
        - Principal: 1000
        - Rate of interest: 0%
        - Time: 3 years

        Expect:
        - The calculated simple interest to be 0.
        """
        principal = 1000
        rate_of_interest = 0
        time = 3

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
