def romanToInt(s: str) -> int:
    # Define the values for Roman numerals
    roman_values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    # Define invalid patterns for Roman numerals
    import re

    invalid_patterns = [
        "IIII",
        "VV",
        "XXXX",
        "LL",
        "CCCC",
        "DD",
        "MMMM",  # Invalid repetitions
    ]

    # Input validation: check if all characters in the input are valid Roman numerals
    for char in s:
        if char not in roman_values:
            raise ValueError(f"Invalid Roman numeral character: {char}")

    # Check for invalid patterns
    for pattern in invalid_patterns:
        if pattern in s:
            raise ValueError(f"Invalid Roman numeral sequence: {s}")

    total = 0  # Initialize total value
    prev_value = 0  # Track the value of the previous numeral

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
