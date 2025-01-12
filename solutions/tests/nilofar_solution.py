"""
nilfersolution.py

Solution for BMI calculation.

This script defines the `calculate_bmi` function, which calculates the Body Mass Index (BMI)
given weight (in kilograms) and height (in meters). It also categorizes the BMI into one of
the following categories:
- Underweight
- Normal weight
- Overweight
- Obesity

Author: [Your Name]
Date: [Today's Date]
"""


def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) and categorize it.

    Args:
        weight (float): The weight of the person in kilograms.
        height (float): The height of the person in meters.

    Returns:
        str: A message indicating the BMI value and its category.
             Returns an error message for invalid input.

    Examples:
        >>> calculate_bmi(45, 1.7)
        'Underweight (BMI: 15.57)'
        >>> calculate_bmi(68, 1.75)
        'Normal weight (BMI: 22.20)'
        >>> calculate_bmi(-45, 1.7)
        'Invalid input. Height and weight must be greater than zero.'
    """
    # Validate input: weight and height must be positive
    if weight <= 0 or height <= 0:
        return "Invalid input. Height and weight must be greater than zero."

    # Calculate BMI
    bmi = weight / (height**2)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obesity"

    # Format BMI to two decimal places
    return f"{category} (BMI: {bmi:.2f})"


# Example usage (uncomment the following lines to test):
# print(calculate_bmi(45, 1.7))  # Output: 'Underweight (BMI: 15.57)'
# print(calculate_bmi(68, 1.75))  # Output: 'Normal weight (BMI: 22.20)'
# print(calculate_bmi(-45, 1.7))  # Output: 'Invalid input. Height and weight must be greater than zero.'
