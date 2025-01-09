# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A  module for generating a grade based on a numerical score.

Module content:
    - grading_system: Returns the grade corresponding to the provided score.

Created on: 6/1/2025
@author: Razan Ibrahim
Group: Matrix (ET foundations group 16 )
"""


def grading_system(score: int | float) -> str:
    """
    This function must receive a score that can be any value from 0 to 100 and generate a grade.
    The grades are assigned as follows:
    - 'A' for scores between 90 and 100 (inclusive)
    - 'B' for scores between 80 and 89 (inclusive)
    - 'C' for scores between 70 and 79 (inclusive)
    - 'D' for scores between 50 and 69 (inclusive)
    - 'F' for scores below 50

    Parameters:
        score: int or float, greater than or equal to 0 and less than or equal to 100.

    Returns-> str,The grade corresponding to the score,
    which will be one of 'A', 'B', 'C', 'D', or 'F'.

    Raises:
        AssertionError:if the score is not an integer or a float
        AssertionError:if the score is less than 0
        AssertionError: if the score is more than 100

    >>> grading_system(93)
    'A'
    >>> grading_system(29)
    'F'
    >>> grading_system(72)
    'C'
    >>> grading_system(0)
    'F'

    """

    assert isinstance(score, (int, float)), (
        "The score is neither an integer nor a float."
    )
    assert score >= 0, "Score is less than 0"
    assert score <= 100, "Score is greater than 100"

    # assign grades based on score ranges
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
