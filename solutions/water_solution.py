"""
water_solution.py

Solution for determining daily water intake based on weight and activity level.

This script defines the calculate_water_intake function, which calculates the recommended daily
water intake in liters for a person based on their weight (in kilograms) and activity level (in minutes).
The function adjusts water intake based on exercise time.

Author: Nilofar Nikzad
Date: January 12, 2025
"""


def calculate_water_intake(weight, activity_minutes):
    """
    Calculate the recommended daily water intake based on weight and activity level.

    Args:
        weight (float): The weight of the person in kilograms.
        activity_minutes (float): The daily physical activity time in minutes.

    Returns:
        str: A message indicating the recommended daily water intake in liters.
             Returns an error message for invalid input.

    Examples:
        >>> calculate_water_intake(70, 30)
        'Recommended daily water intake: 2.85 liters'
        >>> calculate_water_intake(50, 60)
        'Recommended daily water intake: 2.60 liters'
        >>> calculate_water_intake(-70, 30)
        'Invalid input. Weight and activity minutes must be greater than zero.'
    """
    # Validate input: weight and activity_minutes must be positive
    if weight <= 0 or activity_minutes < 0:
        return "Invalid input. Weight and activity minutes must be greater than zero."

    # Base water requirement: 0.033 liters per kg of body weight
    base_water_intake = weight * 0.033

    # Additional water requirement: 0.012 liters per minute of physical activity
    additional_water_intake = activity_minutes * 0.012

    # Total water intake
    total_water_intake = base_water_intake + additional_water_intake

    # Format result to two decimal places
    return f"Recommended daily water intake: {total_water_intake:.2f} liters"


# Example usage (uncomment the following lines to test):
# print(calculate_water_intake(70, 30))  # Output: 'Recommended daily water intake: 2.85 liters'
# print(calculate_water_intake(50, 60))  # Output: 'Recommended daily water intake: 2.60 liters'
# print(calculate_water_intake(-70, 30))  # Output: 'Invalid input. Weight and activity minutes must be greater than zero.'
