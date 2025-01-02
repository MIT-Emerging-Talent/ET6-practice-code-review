"""
Creates a sequence where numbers divisible by 4 return 'Foo',
numbers divisible by 6 return 'Bar', numbers divisible by both
return 'FooBar', and other numbers remain unchanged.

Author: Rafaa Ali
Created date: 1.1.2025
"""


def FooBar_code(n: int):
    """This function, `FooBar_code`, creates a sequence that replaces numbers
    based on their divisibility by 4 and 6.

    Parameters:
      n (int):the last number in the list

    Returns:
      List containing the sequence with 'Foo', 'Bar', 'FooBar' or numbers

    assertion:
    n must be integer otherwise error


    example:
    Edge cases:
    >>> FooBar_code(1)
    [1]
    >>> FooBar_code(0)
    []
    >>> FooBar_code(-1)
    []

    Standard cases:
    >>> FooBar_code(8)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo']
    >>> FooBar_code(12)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo', 9, 10, 11, 'FooBar']
    >>> FooBar_code(16)
    [1, 2, 3, 'Foo', 5, 'Bar', 7, 'Foo', 9, 10, 11, 'FooBar',
    13, 14, 15, 'Foo']

    Defensive cases:
    >>> FooBar_code("rafaa")
    AssertionError: N must be integer
    >>> FooBar_code(5.5)
    AssertionError: N must be integer
    >>> FooBar_code([1, 2, 3])
    AssertionError: N must be integer


    """
    assert isinstance(n, int), "N must be integer"
    result = []
    for i in range(1, n + 1):
        if i % 4 == 0 and i % 6 == 0:
            result.append("FooBar")
        elif i % 4 == 0:
            result.append("foo")
        elif i % 6 == 0:
            result.append("Bar")
        else:
            result.append(i)
    return result
