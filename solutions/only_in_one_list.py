"""

Write a function that takes in a string and two lists of strings.
It will return true if the item is in _only one_ of the lists.

"""


def only_in_one_list(a: list, b: list, c: str) -> bool:
    """
    function looks for item in both lists. returns true if found in only one

    parameters:
    a: a list containing strings
    b: a list containing strings
    c: a str

    Returns:
    True if item is in only one of the lists

    >>> only_in_one_list([], ["cup"], "spoon")
    Traceback (most recent call last):
    ...
    AssertionError: Empty list

    >>> only_in_one_list([1, 3, 6], ["cup"], "spoon")
    Traceback (most recent call last):
    ...
    AssertionError: item type not str

    >>> only_in_one_list(["spoon", "hat", 6], ["cup"], "spoon")
    Traceback (most recent call last):
    ...
    AssertionError: item type not str

    >>> only_in_one_list(["s", "p", "o", "o", "n"], ["cup"], "spoon")
    False

    >>> only_in_one_list(["s", "p", "o", "o", "n"], ["cup"], "p")
    True

    >>> only_in_one_list(["s", "p", "o", "o", "n"], ["s", "p", "o", "o", "n"], "p")
    False

    >>> only_in_one_list(["s", "p", "o", "o", "n"], ["s", "p", "p", "o", "n"], "p")
    False

    >>> only_in_one_list(["s", "o", "o", "o", "n"], ["s", "p", "p", "p", "n"], "p")
    True

    >>> only_in_one_list(["spoon"], ["cup"], "p")
    False

    >>> only_in_one_list(["spoon"], ["cost"], "p")
    False

    >>> only_in_one_list(["spoon", "pot"], ["cost"], "pot")
    True

    >>> only_in_one_list(["spoon", "pot"], ["cost", "pot"], "pot")
    False
    """

    # assert agr a and b are lists and arg c is str
    assert isinstance(a, list)
    assert isinstance(b, list)
    assert isinstance(c, str)

    # assert list is not empty.
    if len(a) == 0:
        raise AssertionError("Empty list")
    if len(b) == 0:
        raise AssertionError("Empty list")

    # assert list contains only str
    for i in a:
        if not isinstance(i, str):
            raise AssertionError("item type not str")
    for i in b:
        if not isinstance(i, str):
            raise AssertionError("AssertionError: item type not str")

    # applying pythons symmetric difference operation using sets to find items
    # in either lists but not both
    set_a = set(a)
    set_b = set(b)
    not_both = list(set_a.symmetric_difference(set_b))

    if c in not_both:
        return True  # item is in either list but not both
    return False  # item is in both, or does not exist
