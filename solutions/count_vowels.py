def count_vowels(s):
    """
    Counts the number of vowels in the given string.

    Parameters:
    s (str): The string in which to count vowels.

    Returns:
    int: The number of vowels in the string.

    Example:
    >>> count_vowels("hello")
    2
    >>> count_vowels("Nelsona")
    3
    """
    vowels = "aeiouAEIOU"  # Define vowels (both lowercase and uppercase)
    return sum(
        1 for char in s if char in vowels
    )  # Count vowels using a generator expression
