def roman_to_int(s: str) -> int:
    """
    Convert a Roman numeral string to an integer.

    Args:
    s (str): The Roman numeral string, containing characters from "I", "V", "X", "L", "C", "D", and "M".

    Returns:
    int: The corresponding integer value of the Roman numeral.

    Raises:
    ValueError: If the input contains invalid Roman numeral characters or sequences.

    Examples:
    >>> roman_to_int("III")
    3
    >>> roman_to_int("IV")
    4
    >>> roman_to_int("IX")
    9
    >>> roman_to_int("LVIII")
    58
    >>> roman_to_int("MCMXCIV")
    1994
    """
    
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    invalid_patterns = [
        "IIII", "VV", "XXXX", "LL", "CCCC", "DD", "MMMM"
    ]

    # Check for invalid characters
    for char in s:
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")

    # Check for invalid sequences
    for pattern in invalid_patterns:
        if pattern in s:
            raise ValueError(f"Invalid Roman numeral sequence: {s}")

    # Initialize total value and previous numeral's value
    total = 0
    prev_value = 0
    
    # Loop through the string from right to left
    for char in reversed(s):
        current_value = roman_values[char]

        # If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        # Update the previous value
        prev_value = current_value

    return total
