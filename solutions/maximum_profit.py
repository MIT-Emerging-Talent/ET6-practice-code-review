
def max_profit(prices: list[int]) -> int:
    """
    Returns the maximum profit from as many stock transactions as possible.

    Parameters:
        prices (list[int]): A list of integers representing the stock prices on different days.

    Returns:
        int: The maximum profit that can be achieved by making as many transactions as possible.

    Raises:
        AssertionError: If `prices` is not a list of integers.

    Examples:
        >>> max_profit([7, 1, 5, 3, 6, 4])
        7
        >>> max_profit([1, 2, 3, 4, 5])
        4
        >>> max_profit([7, 6, 4, 3, 1])
        0
    """
