"""
Temperature Conversion Module

This module provides functions to convert temperatures between Celsius and Fahrenheit.

Assumptions:
- The input temperature in Celsius should be a numeric value (int or float).
- Non-numeric inputs will raise a TypeError.

Edge Cases:
- The function does not handle special cases like absolute zero or extremely high/low values.
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Args:
    celsius (float): The temperature in Celsius to be converted. Must be a numeric value.

    Returns:
    float: The equivalent temperature in Fahrenheit.

    Raises:
    TypeError: If the input `celsius` is not a numeric value (int or float).

    Example:
    >>> celsius_to_fahrenheit(25)
    77.0
    """
    if not isinstance(celsius, (int, float)):
        raise TypeError("Input must be a number.")

    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# Example usage:
INPUT_CELSIUS = 25
OUTPUT_FAHRENHEIT = celsius_to_fahrenheit(INPUT_CELSIUS)
print(f"{INPUT_CELSIUS}°C is equal to {OUTPUT_FAHRENHEIT}°F")
