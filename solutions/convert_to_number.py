""" "
Created on 0084/01/2025
@author: Arwa Mohamed

"""


def convert_to_number(input_str):
    """Converts a string to a number (integer or float).

    Parameters:
        input_str (str): The string to convert to a number.

    Returns:
        int: If the string represents an integer.
        float: If the string represents a float.

    Examples:
        >>> convert_to_number("42")
        42

        >>> convert_to_number("3.14")
        3.14

    Raises:
        ValueError: If the input string cannot be converted to a number.
    """
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string.")

    try:
        if "." in input_str:
            return float(input_str)
        return int(input_str)
    except ValueError:
        raise ValueError(f"Cannot convert '{input_str}' to a number.")
