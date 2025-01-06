#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on XX XX XX

A module gives a result of adding two numbers.

@author: Tagwa Hashim
"""


def Addition(num1, num2):
  """
  Adds two numbers and returns their sum.

  Args:
    num1: The first number. Can be an integer or a float.
    num2: The second number. Can be an integer or a float.

  Returns:
    The sum of num1 and num2.

  Raises:
    TypeError: If either num1 or num2 is not a number (int or float).

  Examples:
    >>> Addition(3, 5)
    8
    >>> Addition(2.5, 3.7)
    6.2
    >>> Addition("hello", 2.718) 
    Traceback (most recent call last):
            ...
    AssertionError: Both arguments must be numbers (int or float).
  """
  assert (isinstance(num1, (int, float)) and isinstance(num2, (int, float))), "Both arguments must be numbers (int or float)."
     
  return num1 + num2
