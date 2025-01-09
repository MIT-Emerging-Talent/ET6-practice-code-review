"""
Year Investment

1/8/2025

created by Dmytro Klymenko

"""


def year_investment(number, percentage: int):
    """
    Function is designed to calculate yearly income with desired
    amout and percentage

    Args:
        number (int): Amount of money to be invested
        percentage (int): Year percantage

    Returns:
      int - Final amount of money after year investment

    Examples:

    >>> year_investment(10000, 5)

    >>> year_investment(100, 2)

    >>> year_investment(278, 3)
    """
    assert isinstance(number, (int, float))
    assert isinstance(percentage, (int, float))
    assert number >= 0
    assert percentage >= 0

    return number * (percentage / 100) + number
