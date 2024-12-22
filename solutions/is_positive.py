"""
A module for checking if a number is positive.


Author: Luyando Chitindi
Date: 12/22/2024


This module contains a function that deals with checking if a number is positive.
The function will take an integer as an input and returns a boolean value indicating
whether the number is greater than zero.

Function:
- is positive(number: int) -> bool


Exceptions:
-Raises TypeError if the input is not an integer.


For Example:
>>> is_positive(5)
True
>>> is_positive(-3)
False
>>> is_positive(0)
False
"""


def is_positive(number: int) -> bool:
    """
  This will check if the number is positive.
  
  
  Arguments:
  number (int): The number to check if it is positive.
  
  
  Returns:
  bool: True if the number is positive, false otherwise.
  
  
  Raises:
  TypeError: If the argument that is provided is not an integer.
  
  
  Example:
  >>> is_positive(10)
  True
  >>> is_positive(-5)
  False
  >>> is_positive(0)
  False
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number > 0
