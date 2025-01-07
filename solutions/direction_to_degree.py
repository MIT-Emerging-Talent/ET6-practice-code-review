"""
direction_to_degree.py

This module contains a function to convert a cardinal or intercardinal direction
to a corresponding degree, measured clockwise from North (0 degrees).

Author: Obay Salih
Date: Tues 7 Jan 2025
Group: ET6-foundations-group-16

Functions:
- direction_to_degree(direction): Converts a cardinal or intercardinal direction to a degree.
"""


def direction_to_degree(direction: str) -> int:
    """
    Converts a cardinal or intercardinal direction to a degree measured clockwise from North.

    Args:
        direction (str): A cardinal or intercardinal direction (e.g., "N", "NE", "SW", etc.).

    Returns:
        int: The corresponding degree, or 'Invalid direction' if the direction is not recognized.

    Raises:
        ValueError: If the input is not a string.

    Assumptions:
        - The direction must be a string.
        - The direction must be one of the recognized cardinal or intercardinal directions.

    Examples:
        >>> direction_to_degree("N")
        0
        >>> direction_to_degree("NE")
        45
        >>> direction_to_degree("SW")
        225
        >>> direction_to_degree("INVALID")
        'Invalid direction'
    """

    # Defensive check: If the input is not a string, raise a ValueError.
    if not isinstance(direction, str):
        raise ValueError("The direction must be a string.")

    # Define the mapping of directions to degrees
    directions = {
        "N": 0,
        "NNE": 22,
        "NE": 45,
        "ENE": 67,
        "E": 90,
        "ESE": 112,
        "SE": 135,
        "SSE": 157,
        "S": 180,
        "SSW": 202,
        "SW": 225,
        "WSW": 247,
        "W": 270,
        "WNW": 292,
        "NW": 315,
        "NNW": 337,
    }

    # Convert the input direction to uppercase and check if it is valid
    direction = direction.upper()

    # Return the degree for valid directions, or 'Invalid direction' if not found
    return directions.get(direction, "Invalid direction")
