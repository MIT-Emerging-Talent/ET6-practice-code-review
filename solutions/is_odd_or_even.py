def is_odd_or_even(number):
    """
    Check if a number is odd or even.

    Args:
        number (int): The number to check.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.

    Examples:
        >>> is_odd_or_even(4)
        'Even'
        >>> is_odd_or_even(7)
        'Odd'
        >>> is_odd_or_even(0)
        'Even'
        >>> is_odd_or_even(-3)
        'Odd'
        >>> is_odd_or_even(-2)
        'Even'
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Runs the doctests
