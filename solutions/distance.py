#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
distance.py

This module provides a function
 to calculate the distance between
   two points in a 2D point.

   Created on 6 1 2025

@author: omer dafaalla

"""


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Calculate the distance between
      two points in a 2D point.

    Parameters:
    - x1 (float): x-coordinate of the first point.
    - y1 (float): y-coordinate of the first point.
    - x2 (float): x-coordinate of the second point.
    - y2 (float): y-coordinate of the second point.

    Returns:
    - float: The distance between
      the two points rounded to 2 decimal places.

    Raises:
    - AssertionError: If any of
      the inputs are not numeric.

    Examples:
    >>> calculate_distance(0, 0, 3, 4)
    5.0
    >>> calculate_distance(-1, -1, -4, -5)
    5.0
    >>> calculate_distance(2, 3, 2, 3)
    0.0
    """
    # Defensive assertions to check if inputs are valid numbers
    assert isinstance(x1, (int, float)), "x1 must be a number."
    assert isinstance(y1, (int, float)), "y1 must be a number."
    assert isinstance(x2, (int, float)), "x2 must be a number."
    assert isinstance(y2, (int, float)), "y2 must be a number."

    # Calculate the distance
    dx = x2 - x1
    dy = y2 - y1
    distance_squared = dx**2 + dy**2
    distance = distance_squared**0.5
    return round(distance, 2)
