"""
Test Module for Temperature Conversion

This module contains unit tests for the `celsius_to_fahrenheit` function
in the temperature conversion module.
"""

import unittest


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
    celsius (float): The temperature in Celsius to be converted.

    Returns:
    float: The equivalent temperature in Fahrenheit.
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


class TestTemperatureConversion(unittest.TestCase):
    """
    Test class for the `celsius_to_fahrenheit` function.

    This class contains test cases to verify the correctness of the
    temperature conversion function.
    """

    def test_celsius_to_fahrenheit(self):
        """
        Test the `celsius_to_fahrenheit` function with valid inputs.

        This method tests the conversion of various Celsius temperatures
        to Fahrenheit.
        """
        # Test case 1: Freezing point of water
        actual = celsius_to_fahrenheit(0)
        expected = 32
        self.assertAlmostEqual(actual, expected, msg="0°C should equal 32°F")

        # Test case 2: Room temperature
        actual = celsius_to_fahrenheit(25)
        expected = 77
        self.assertAlmostEqual(actual, expected, msg="25°C should equal 77°F")

        # Test case 3: Boiling point of water
        actual = celsius_to_fahrenheit(100)
        expected = 212
        self.assertAlmostEqual(actual, expected, msg="100°C should equal 212°F")

        # Test case 4: Same in Celsius and Fahrenheit
        actual = celsius_to_fahrenheit(-40)
        expected = -40
        self.assertAlmostEqual(actual, expected, msg="-40°C should equal -40°F")

        # Test case 5: Negative temperature
        actual = celsius_to_fahrenheit(-10)
        expected = 14
        self.assertAlmostEqual(actual, expected, msg="-10°C should equal 14°F")

    def test_invalid_input(self):
        """
        Test the `celsius_to_fahrenheit` function with invalid inputs.

        This method tests how the function handles non-numeric and None inputs.
        """
        # Test case 6: Non-numeric input
        with self.assertRaises(
            TypeError, msg="Non-numeric input should raise TypeError"
        ):
            celsius_to_fahrenheit("invalid")

        # Test case 7: None input
        with self.assertRaises(TypeError, msg="None input should raise TypeError"):
            celsius_to_fahrenheit(None)


if __name__ == "__main__":
    unittest.main()
