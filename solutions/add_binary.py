"""
This module contains a function to add two binary strings.

Constraints:
    - Input strings must consist of '0' and '1' characters only.
    - Input strings must be non-empty.
    - Input strings must not exceed 10^4 characters in length.

Assumptions:
    - Leading zeros in the input do not affect the result.
    - Input strings are well-formed binary strings without embedded whitespace.

Efficiency:
    - The function performs efficiently for binary strings up to 10^4 characters,
      leveraging Python's built-in `int` and `bin` for conversion and calculation.
"""


def add_binary(bin_num1: str, bin_num2: str) -> str:
    """
    Returns the sum of two binary strings as a binary string.

    Args:
        bin_num1 (str): A binary string. Length must be between 1 and 10^4.
        bin_num2 (str): A binary string. Length must be between 1 and 10^4.

    Returns:
        str: The binary string representation of the sum of `bin_num1` and `bin_num2`.
             Leading zeros in the input are ignored in the result.

    Raises:
        ValueError: If either `bin_num1` or `bin_num2` contains non-binary characters,
                    is empty, exceeds the length constraints, or contains whitespace.

    Examples:
        >>> add_binary("11", "1")
        '100'
        >>> add_binary("1010", "1011")
        '10101'
        >>> add_binary("0", "0")
        '0'
        >>> add_binary("00011", "1")
        '100'
        >>> add_binary("102", "1")
        ValueError: Input strings must contain only '0' or '1' characters.
        >>> add_binary("1"*10001, "1")
        ValueError: Input strings must not exceed 10^4 characters.
        >>> add_binary(" 1010 ", "1")
        ValueError: Input strings must not contain whitespace.
    """
    # Defensive assertions
    if not bin_num1 or not bin_num2:
        raise ValueError("Input strings must not be empty.")
    if len(bin_num1) > 10**4 or len(bin_num2) > 10**4:
        raise ValueError("Input strings must not exceed 10^4 characters.")
    if not all(char in "01" for char in bin_num1 + bin_num2):
        raise ValueError("Input strings must contain only '0' or '1' characters.")
    if not bin_num1.strip() == bin_num1 or not bin_num2.strip() == bin_num2:
        raise ValueError("Input strings must not contain whitespace.")

    # Convert binary strings to integers, add them, and convert the result back to binary
    # bin() returns a string starting with '0b'. Slice [2:] to remove '0b'.
    return bin(int(bin_num1, 2) + int(bin_num2, 2))[2:]
