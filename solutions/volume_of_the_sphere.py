#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module provides a function to calculate the volume of a sphere
given its radius.

Module contents:
    - volume_of_the_sphere: returns the volume of a sphere given its radius

Created on 2025-01-07
@author: Cyne Jarvis J. Zarceno
"""

import math


def volume_of_the_sphere(radius: float) -> float:
    """Returns the volume of a sphere given its radius

    Parameter:
        radius (float): Positive real numbers.

    Returns -> float: The volume of the sphere calculated using the formula V = (4/3)πr³

    Raises:
        AssertionError: If radius is not a number
        AssertionError: If radius is not int or float
        ValueError: If radius is zero
        ValueError: If radius is negative

    Examples:
        >>> volume_of_the_sphere(5.0)
        523.5987755982989
        >>> volume_of_the_sphere(2.5)
        65.44984694978736
        >>> volume_of_the_sphere(1.0)
        4.1887902047863905
    """
    # Type validation
    assert isinstance(radius, (int, float)), "Radius must be a number"
    assert type(radius) in (int, float), "Radius must be int or float"

    # Value validation
    assert radius != 0, "Radius cannot be zero"
    assert radius > 0, "Radius must be positive"

    return (4 / 3) * math.pi * (radius**3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
