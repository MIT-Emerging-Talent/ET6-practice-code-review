#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for calculating the average of student marks.

Module contents:
    - calculate_average: calculates the average marks for a given student.

Created on: 05/01/2025
@author: Maria Cedeño
"""


def calculate_average(student_marks: dict, query_name: str) -> float:
    """Calculates the average marks for a given student.

    Args:
        student_marks: A dictionary where keys are student name

        query_name: The name of the student for whom to calculate the average.

    Returns:
        The average marks of the student, rounded to 2 decimal places.

    Raises:
        KeyError: If the query_name is not found in the student_marks dictionary.

    Examples:
        >>> student_marks = {'Matt': [52, 56, 60]}
        >>> calculate_average(student_marks, 'Matt')
        56.0

        >>> student_marks = {'Harry': [25, 26.5, 28]}
        >>> calculate_average(student_marks, 'Harry')
        26.5

        >>> student_marks = {'Alice': [90, 85, 92], 'Bob': [78, 82, 75]}
        >>> calculate_average(student_marks, 'Alice')
        89.0

        >>> student_marks = {'David': [65, 70, 68], 'Emily': [88, 91, 85]}
        >>> calculate_average(student_marks, 'Emily')
        88.0
    """

    if query_name not in student_marks:
        raise KeyError(f"Student '{query_name}' not found.")

    average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
    return round(average_marks, 2)
