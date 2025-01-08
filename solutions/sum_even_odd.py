"""

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""

def sum_even_odd(d: list) -> dict:
    """function sums the even and odd numbers in list respectively
    
    parameters:
    d: a list containing positive and/or negative integers, including zero
    
    Returns:
    a dict containing the sums of the even and odd numbers respectively

    >>> sum_even_odd([])
    Traceback (most recent call last):
    ...
    AssertionError: Empty list

    >>> sum_even_odd(["goat", "rat"])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sum_even_odd([56, 7, "rat"])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sum_even_odd([[3, 4]])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sum_even_odd([3, 4, [45, 9], 3])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sum_even_odd([2, 4, 0, 8, 10])
    {'sum_of_even': 24, 'sum_of_odd': 0}

    >>> sum_even_odd([2, 4, 0, 8, 10, 47])
    {'sum_of_even': 24, 'sum_of_odd': 47}

    >>> sum_even_odd([2, 4, 0, 8, 10, 47, -1203])
    {'sum_of_even': 24, 'sum_of_odd': -1156}
    """

    # assert d is a list and contains only positive or negative integers
    assert isinstance(d, list)
    if len(d) == 0:
        raise AssertionError("Empty list")
    for i in d:
        if not isinstance(i, int):
            raise AssertionError("item type not int")

    even = 0
    odd = 0
    for item in d:
        if item % 2 == 0:
            even += item
        else:
            odd += item
    return {"sum_of_even": even, "sum_of_odd": odd}
