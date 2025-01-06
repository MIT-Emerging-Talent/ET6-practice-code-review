#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the roots of quadratic equations.

Module contents:
- quadratic_roots: returns the roots of a quadratic equation.

Created on 06 Jan 2025
Team Number: 28
Team Name: MIT Alpha
Author: Salih Adam
"""


def quadratic_roots(a: int | float, b: int | float, c: int | float) -> str:
    """
    returns all possible roots of a quadratic equation in the form ax^2 + bx + C = 0.

    Parameters:
    a (int | float): The coefficient of x^2, representing the quadratic term.
    b (int | float): The coefficient of x, representing the linear term.
    c (int | float): The constant term.

    Returns -> str: A string describing the roots of the quadratic equation.

    Raises:
        AssertionError: if the coefficients are not integers or floats.
        AssertionError: if 'a' is zero as the equation must be quadratic.

    >>> quadratic_roots(1, -4, 4)
    'One real root: 2.0'
    >>> quadratic_roots(2, 4, -30)
    'Two real roots: 3.0, -5.0'
    >>> quadratic_roots(5, 0, 20)
    'Two imaginary roots: 2j, -2j'
    >>> quadratic_roots(1, -12, 61)
    'Two complex roots: (6+5j), (6-5j)'
    """

    # Ensure correct input

    assert isinstance(a, (int, float)), "coefficient must be an integer or a float"
    assert a != 0, "Equation must be quadratic"
    assert isinstance(b, (int, float)), "coefficient must be an integer or a float"
    assert isinstance(c, (int, float)), "coefficient must be an integer or a float"

    # Calculating discriminant to determine the type of roots

    discriminant = b**2 - 4 * a * c

    # Calculation when there is only one real root

    if discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"

    # Calculation when there are two real roots

    if discriminant > 0:
        root_1 = round((-b + (discriminant) ** 0.5) / (2 * a), 3)
        root_2 = round((-b - (discriminant) ** 0.5) / (2 * a), 3)
        return f"Two real roots: {root_1}, {root_2}"

    # Calculation when there are two roots with imaginary numbers

    real_part = round(-b / (2 * a), 3)
    imaginary_part = round((-discriminant) ** 0.5 / (2 * a), 3)
    root_1 = complex(real_part, imaginary_part)
    root_2 = complex(real_part, -imaginary_part)

    ## Imaginary roots with no real part

    if b == 0:
        return f"Two imaginary roots: {root_1}, {root_2}"

    ## Complex roots with both real and imaginary parts

    return f"Two complex roots: {root_1}, {root_2}"
