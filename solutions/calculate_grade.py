#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting numeric scores to letter grades.

Module contents:
    - calculate_grade: converts a numeric score (0-100) to a letter grade (A-F).

Created on 2025-01-08
@author: Karina
"""


def calculate_grade(score: float) -> str:
    """
    Convert a numeric score to a letter grade based on standard grading scale.

    Parameters:
        score: float, the numeric score to convert (must be between 0 and 100)

    Returns:
        str: the corresponding letter grade (A, B, C, D, or F)

    Raises:
        AssertionError: if the input is not a valid numeric score
        ValueError: if the score is not between 0 and 100

    Examples:
        >>> calculate_grade(95)
        'A'
        >>> calculate_grade(83)
        'B'
        >>> calculate_grade(76)
        'C'
        >>> calculate_grade(65)
        'D'
        >>> calculate_grade(50)
        'F'
    """
    # Input validation
    assert isinstance(score, (int, float)), "Score must be a number"
    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100")

    # Grade boundaries
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
