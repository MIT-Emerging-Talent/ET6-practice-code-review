import unittest
from solutions.simple_interest_calculator import (
    calculate_simple_interest,
)  # Adjust the import based on your actual function


class TestSimpleInterestCalculator(unittest.TestCase):
    # Test case for a basic calculation of Simple Interest
    def test_calculate_simple_interest(self):
        principal = 1000  # Example principal amount
        rate_of_interest = 5  # Example rate of interest
        time = 3  # Example time period (in years)

        expected_result = 150  # Expected simple interest
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(
            actual_result, expected_result
        )  # Assert if the calculation is correct

    # Test case for zero principal
    def test_calculate_simple_interest_zero_principal(self):
        principal = 0
        rate_of_interest = 5
        time = 3

        expected_result = 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(
            actual_result, expected_result
        )  # Assert if the result is 0 for zero principal

    # Test case for zero time period
    def test_calculate_simple_interest_zero_time(self):
        principal = 1000
        rate_of_interest = 5
        time = 0

        expected_result = 0  # Simple interest should be 0 if time is 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)

    # Test case for zero rate of interest
    def test_calculate_simple_interest_zero_rate(self):
        principal = 1000
        rate_of_interest = 0
        time = 3

        expected_result = 0  # Simple interest should be 0 if the rate of interest is 0
        actual_result = calculate_simple_interest(principal, rate_of_interest, time)

        self.assertEqual(actual_result, expected_result)


# To run the tests, use this command in the terminal: python -m unittest tests/test_simple_interest_calculator.py
if __name__ == "__main__":
    unittest.main()
