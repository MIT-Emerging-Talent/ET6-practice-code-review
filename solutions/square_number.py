"""
square_number.py
module name: 
square_number 
contains a function to calculate the square of a number.
Module contents:
The function ensures robust error handling and supports
both integers and floats
Created on 2025-01-02
Author: Saeed Ali

"""


def square_number(num):
    """
    Calculate the square of a given number.
    Parameters:
    num (int or float): The number to be squared. Must be a valid numerical input.
    Returns:
    int or float: The square of the input number, matching the input type.
    Raises:
    TypeError: If the input is not an integer or float.
    Examples:
    >>> square_number(5)
    25
    >>> square_number(-3)
    9
    >>> square_number(2.5)
    6.25
    """
    if not isinstance(num, (int, float)):
        raise TypeError("Input must be an integer or a float.")
    return num * num


if __name__ == "__main__":
    import doctest

    doctest.testmod()

print(square_number(4))  # Output: 16
print(square_number(-6))  # Output: 36
print(square_number(1.5))  # Output: 2.25
print(square_number("m"))  # Output: TypeError
