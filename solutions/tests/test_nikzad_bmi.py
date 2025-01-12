"""
test_nikzad_bmi.py

Unit tests for the BMI calculation function `calculate_bmi` from `nilfersolution`.

This script uses the `unittest` framework to validate the correctness of the
BMI calculation function across different scenarios, including:
- Underweight
- Normal weight
- Overweight
- Obesity
- Invalid inputs

Author: (Nilofar Nikzad)
Date: [Jan 12,2025]
"""

import unittest
from solutions.nilofar_solution import calculate_bmi  # Import the function from the solution file


class TestBMICalculator(unittest.TestCase):
    """
    Unit test class for testing the `calculate_bmi` function.
    """

    def test_underweight(self):
        """
        Test case for the underweight category.
        """
        result = calculate_bmi(45, 1.7)
        self.assertEqual(result, "Underweight (BMI: 15.57)")

    def test_normal_weight(self):
        """
        Test case for the normal weight category.
        """
        result = calculate_bmi(68, 1.75)
        self.assertEqual(result, "Normal weight (BMI: 22.20)")

    def test_overweight(self):
        """
        Test case for the overweight category.
        """
        result = calculate_bmi(80, 1.7)
        self.assertEqual(result, "Overweight (BMI: 27.68)")

    def test_obesity(self):
        """
        Test case for the obesity category.
        """
        result = calculate_bmi(95, 1.6)
        self.assertEqual(result, "Obesity (BMI: 37.11)")

    def test_invalid_input(self):
        """
        Test cases for invalid input scenarios.
        The function should return an appropriate error message
        when height or weight is less than or equal to zero.
        """
        result_negative_weight = calculate_bmi(-45, 1.7)
        self.assertEqual(
            result_negative_weight,
            "Invalid input. Height and weight must be greater than zero.",
        )

        result_zero_height = calculate_bmi(50, 0)
        self.assertEqual(
            result_zero_height,
            "Invalid input. Height and weight must be greater than zero.",
        )


if __name__ == "__main__":
    unittest.main()
