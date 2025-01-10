#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate the volume of a sphere
given its radius.

Module contents:
    - volume_of_the_sphere: Returns the volume of a sphere given its radius.

Created on 2025-01-07
Author: Cyne Jarvis J. Zarceno
"""

import math


def volume_of_the_sphere(radius: float) -> float:
    """
    Calculates the volume of a sphere given its radius.

    Args:
        radius (float): Positive real numbers.

    Returns:
        float: The calculated volume of the sphere, rounded to two decimal places.

    Raises:
        TypeError: If `radius` is not an integer or a float.
        ValueError: If `radius` is zero or negative.

    Examples:
        >>> volume_of_the_sphere(5.0)
        523.6
        >>> volume_of_the_sphere(2.5)
        65.45
        >>> volume_of_the_sphere(1.0)
        4.19
    """
    # Type validation
    if not isinstance(radius, (int, float)):
        raise TypeError("Radius must be a number")

    # Value validation
    if radius <= 0:
        raise ValueError("Radius must have a positive value")

    # Calculate the volume of the sphere using the formula V = (4/3)πr³
    return round((4 / 3) * math.pi * (radius**3), 2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
