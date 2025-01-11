#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the volume of a cube

Created on 11-Jan-2025
@author: Mahmoud Alnouri
"""


def calculate_cube_volume(side_length: float) -> float:
    """Calculate the volume of a cube given its side length.

    Parameters:
        side_length: float, The length of one side of the cube. Must be a non-negative number.

    Returns -> float, The volume of the cube.

    Raises:
        AssertionError: If the argument is not a float or int.
        ValueError: If the side length is less than 0.

    Examples:
    >>> calculate_cube_volume(1)
    1.0

    >>> calculate_cube_volume(0)
    0.0

    >>> calculate_cube_volume(2.5)
    15.625

    >>> calculate_cube_volume(10)
    1000.0
    """
    # Validate the input type
    assert isinstance(side_length, (int, float)), (
        "Side length must be a number (int or float)."
    )

    # Validate the side length value
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")

    # Formula for the volume of a cube: side_length^3
    return side_length**3


if __name__ == "__main__":
    # Interactive testing
    try:
        side_length_input = float(input("Enter the side length of the cube: "))
        volume = calculate_cube_volume(side_length_input)
        print(
            f"The volume of the cube with side length {side_length_input} is {volume:.2f}"
        )
    except (AssertionError, ValueError) as e:
        print(f"Error: {e}")
