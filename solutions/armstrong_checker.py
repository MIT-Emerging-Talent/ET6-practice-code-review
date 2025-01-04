"""Module checks if a number is an Armstrong number."""


def armstrong_checker(number: int) -> str:
    """
    Checks if a given positive integer is an Armstrong number.

    Parameters:
        number (int): The number to check (must be > 0).

    Returns:
        str:
            - "True" if the number is an Armstrong number.
            - "False" if the number is not an Armstrong number.
            - "Invalid input" for invalid inputs.

    Raises:
        AssertionError: If the input is not a positive integer.

    Examples:
        >>> armstrong_checker(153)
        'True'
        >>> armstrong_checker(123)
        'False'
        >>> armstrong_checker(-153)
        'Invalid input'
    """
    if not isinstance(number, int) or number < 0:
        return "Invalid input"

    digits = [int(d) for d in str(number)]
    n = len(digits)
    armstrong_sum = sum(d**n for d in digits)

    return "True" if armstrong_sum == number else "False"
