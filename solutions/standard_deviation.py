#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the standard deviation for a population dataset.

Module contents:
    - standard_deviation: calculates the population standard deviation for a given dataset.

Created on 30 12 2024
MIT Alpha Project Group
Author: Salih Adam
"""


def standard_deviation(dataset: list[int | float]) -> float:
    """
    Returns the population standard deviation for a given list of numbers.

    Parameters:
    dataset: list[int | float], List of numbers for which the standard deviation is evaluated

    Returns -> float: the standard deviation value for the input list

    Raises:
        AssertionError: if the argument is not a list
        AssertionError: if the argument is an empty list
        AssertionError: if the items in the list are not integers or floats

    >>> standard_deviation([4, 16, 8, 17, 43])
    13.6
    >>> standard_deviation([-8, 0, 37, 13])
    17.04
    >>> standard_deviation([104, 88, 94, 89, 100, 122, 111])
    11.42
    """

    # Ensure correct input

    assert isinstance(dataset, list), "Input must be a list"
    assert len(dataset) > 0, "Input list cannot be empty"
    for item in dataset:
        assert isinstance(item, (int, float)), "List items must be integers or floats"

    # Calculate dataset mean

    mean = sum(dataset) / len(dataset)

    # Calculate variance as (sum(number - mean)^2)/number of data points

    cumulative_squared_diff = 0
    for number in dataset:
        diff_from_mean_squared = (number - mean) ** 2
        cumulative_squared_diff = cumulative_squared_diff + diff_from_mean_squared
    variance = cumulative_squared_diff / len(dataset)

    # Return standard deviation as the square root of variance

    return round(variance**0.5, 2)
