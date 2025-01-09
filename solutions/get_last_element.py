"""

Module: get_last_element
    This module provides the implementation of the get_last_element function.
    The function validates input types and returns the last element of a list.

"""


def get_last_element(lst: list) -> object:
    """
    Returns the last element of a given list.


    Pameters:
    lst (list): A list from which the last element is returned. It can contain any type of element, including None or nested lists. If the list is empty, None is returned.

    Returns:
    object: The last element in the list. Returns None if the list is empty.

    Raises:
    TypeError: If the input is not a list.

    Example:
    >>> get_last_element([1, 2, 3, 4])
    4
    >>> get_last_element(['apple', 'banana', 'cherry'])
    'cherry'
    >>> get_last_element([])
    None
    >>> get_last_element('not a list')

    TypeError: Input must be a list
    """
    # Defensive assertion: Ensure input is a list
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")

    return lst[-1] if lst else None
