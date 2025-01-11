"""
Temperature Conversion Module

This module provides functions to convert temperatures between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
    celsius (float): The temperature in Celsius to be converted.

    Returns:
    float: The equivalent temperature in Fahrenheit.

    Example:
    >>> celsius_to_fahrenheit(25)
    77.0
    """
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Example usage:
INPUT_CELSIUS = 25
OUTPUT_FAHRENHEIT = celsius_to_fahrenheit(INPUT_CELSIUS)
print(f"{INPUT_CELSIUS}°C is equal to {OUTPUT_FAHRENHEIT}°F")
