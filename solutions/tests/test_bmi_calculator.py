"""
This module contains a series of unit tests for the BMI Calculator program.
It tests the core functionalities, such as:
- Calculating BMI using both metric and imperial units.
- Handling invalid input for unit types.
- Mocking user input for both valid metric and imperial data.
- Displaying the results correctly.

The tests ensure that the program works as expected in different scenarios.
"""

import unittest
from unittest.mock import patch

from solutions.bmi_calculator import calculate_bmi, display_bmi_result, get_user_input


class TestBMICalculator(unittest.TestCase):
    """
    Unit tests for the BMI Calculator functions. This suite verifies the
    correct functionality of the BMI calculation, user input handling,
    and result display.
    """

    def test_calculate_bmi_metric(self):
        """
        Test the BMI calculation for metric units (kg/m²).
        We will calculate BMI for weight = 70kg and height = 1.75m.
        Expected BMI = 22.86 (rounded to 2 decimal places).
        """
        weight = 70  # kg
        height = 1.75  # meters
        bmi, category = calculate_bmi(weight, height, unit="metric")
        self.assertEqual(
            round(bmi, 2), 22.86, f"Expected BMI: 22.86, but got: {bmi:.2f}"
        )
        self.assertEqual(
            category,
            "Normal weight",
            f"Expected category: 'Normal weight', but got: {category}",
        )

    def test_calculate_bmi_imperial(self):
        """
        Test the BMI calculation for imperial units (lbs/in²).
        We will calculate BMI for weight = 154lbs and height = 68in.
        Expected BMI = 23.43 (rounded to 2 decimal places).
        """
        weight = 154  # lbs
        height = 68  # inches
        bmi, category = calculate_bmi(weight, height, unit="imperial")
        self.assertEqual(
            round(bmi, 2), 23.43, f"Expected BMI: 23.43, but got: {bmi:.2f}"
        )
        self.assertEqual(
            category,
            "Normal weight",
            f"Expected category: 'Normal weight', but got: {category}",
        )

    def test_invalid_unit(self):
        """
        Test the behavior when an invalid unit is passed.
        The function should raise a ValueError.
        """
        with self.assertRaises(ValueError):
            calculate_bmi(70, 1.75, unit="invalid_unit")

    def test_get_user_input_valid_metric(self):
        """
        Test the 'get_user_input' function with valid input for metric system.
        We will mock input for weight = 70kg, height = 1.75m, and unit = 'metric'.
        """
        with patch("builtins.input", side_effect=["metric", "70", "1.75"]):
            weight, height, unit = get_user_input()
            self.assertEqual(weight, 70)
            self.assertEqual(height, 1.75)
            self.assertEqual(unit, "metric")

    def test_get_user_input_valid_imperial(self):
        """
        Test the 'get_user_input' function with valid input for imperial system.
        We will mock input for weight = 154lbs, height = 68in, and unit = 'imperial'.
        """
        with patch("builtins.input", side_effect=["imperial", "154", "68"]):
            weight, height, unit = get_user_input()
            self.assertEqual(weight, 154)
            self.assertEqual(height, 68)
            self.assertEqual(unit, "imperial")

    def test_display_bmi_result(self):
        """
        Test that the 'display_bmi_result' function outputs the correct formatted result.
        This is a simple test to verify that the BMI and category are displayed correctly.
        """
        # Capture the output using unittest.mock
        with patch("builtins.print") as mock_print:
            display_bmi_result(22.86, "Normal weight")
            mock_print.assert_any_call("Well done! You've calculated your BMI.")
            mock_print.assert_any_call("Your BMI is: 22.86")
            mock_print.assert_any_call(
                "Based on your BMI, you fall into the "
                "following category: Normal weight.\n"
            )


if __name__ == "__main__":
    unittest.main()
