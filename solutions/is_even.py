"""
A module for checking if a number is even.


Author: Luyando Ennie Chitindi
Date: 12/22/2024


This module has a function that checks if a number is even.
The function takes an integer as an input and returns a boolean value that 
indicates whether the number is divisible by 2.


Function:
- is_even(number: int) -> bool


Exception:
- Raises TypeError if an input is not an integer.


Example:
>>> is_even(4)
True
>>> is_even(3)
False
>>> is_even(0)
True
"""

def is_even(number: int) -> bool:
    """
    This will check if number is even.
    
    
    Argument:
    number (int): The number to use to check if it is even.
    
    
    Returns:
    bool: Only true if the number is even, false otherwise.
    
    
    Raises:
    TypeError: If the argument provided is not an integer.
    
    
    Example:
    >>> is_even(6)
    True
    >>> is_even(7)
    False
    >>> is_even(0)
    True
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    return number % 2 == 0
