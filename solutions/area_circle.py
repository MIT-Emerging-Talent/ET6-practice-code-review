"""
Group: ET6-foundations-group-16
Author:Majd Abualsoud
Date: January 11, 2025
This module provides a function to calculate the area of a circle given its radius.
"""

import math


def area_of_circle(radius: float) -> float:
    """
    Calculate the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle. Must be a non-negative number.

    Returns:
        float: The area of the circle.

    Raises:
        ValueError: If the radius is negative.

    Examples:
        >>> area_of_circle(1)
        3.141592653589793
        >>> area_of_circle(0)
        0.0
        >>> area_of_circle(2.5)
        19.634954084936208
    """
    if radius < 0:
        raise ValueError("The radius must be a non-negative number.")

    return math.pi * radius * radius
