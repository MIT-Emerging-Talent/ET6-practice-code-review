"""
Module returns True if the first and last numbers of the list are the same,
and False if not the same

Created: 01/06/2025
Author: Svitlana Musiienko

"""

from typing import List, Optional

# Imports tools for List- specifies that a parameter is expected to be a list,
# Optional- indicates that the function can return a (bool) or None.


def first_and_last_same(list1: List) -> Optional[bool]:
    """
    Function first_and_last_same check if the first and last numbers of a list are the same.

    Parameters:
    list1 (List): A list of numbers to check

    Returns:
    Optional[bool]:
        -True if the first and last numbers are the same
        -False if the elements are different
        -None if the list is empty ou contains non-numeric elements

    Example:

    >>> first_and_last_same([1,2,3,1])
    True

    >>> first_and_last_same([1,2,3,4])
    False

    >>> first_and_last_same([])
    The list is empty

    >>> first_and_last_same([1, "a", 3, 1])
    The list must contain only numbers

    >>> first_and_last_same([1.5, 2.3, 3.5, 1.5])
    True

    """
    if not list1:
        # checks if the list1 is empty
        print("The list is empty")  # prints a message
        return None  # returns None if the list is empty

    if not all(isinstance(item, (int, float)) for item in list1):
        # validates that the elements in the list are integers or floating-point numbers
        print("The list must contain only numbers")  # prints a message
        return None  # returns None if the list contains any non-numeric elements.

    first_num = list1[0]
    # assigns the first element of the list to the variable first_name
    last_num = list1[-1]
    # assigns the last element of the list to the variable last_name

    return first_num == last_num


# compares the first and last numbers of the list, returns True if they are equal and
# False if they are different.
