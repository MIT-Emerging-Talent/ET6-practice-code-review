"""

Write a function that takes a list of numbers 
and returns a dictionary with sums of the even and odd numbers in the list.

"""

def sort_and_sum_numbers(d: list) -> list:
    """function sorts numbers into even and odd, and sums them respectively
    
    parameters:
    d: a list containing positive and/or negative integers
    
    Returns:
    a dict containing the sums of the even and odd numbers respectively

    >>> sort_and_sum_numbers([])
    Traceback (most recent call last):
    ...
    AssertionError: Empty list

    >>> sort_and_sum_numbers(["goat", "rat"])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sort_and_sum_numbers([56, 7, "rat"])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sort_and_sum_numbers([[3, 4]])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sort_and_sum_numbers([3, 4, [45, 9], 3])
    Traceback (most recent call last):
    ...
    AssertionError: item type not int

    >>> sort_and_sum_numbers([2, 4, 0, 8, 10])
    {'sum_of_even': 24, 'sum_of_odd': 0}

    >>> sort_and_sum_numbers([2, 4, 0, 8, 10, 47])
    {'sum_of_even': 24, 'sum_of_odd': 47}

    >>> sort_and_sum_numbers([2, 4, 0, 8, 10, 47, -1203])
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
