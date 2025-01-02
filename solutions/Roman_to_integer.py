def romanToInteger(self, s: str) -> int:
    """
    Convert a Roman numeral string to an integer.
    You can assume the number will be between 1 and 3999.

    Args:
        str (str): The Roman numeral string to convert.

    Returns:
        int: The integer representation of the Roman numeral.

    Exceptions:
        If `str` is not a string or is None, return 0.

    Roman numeral system:
    Roman numerals are made up of the following characters:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.
    Numbers are written from largest to smallest from left to right,
    except when a smaller numeral appears before a larger numeral,
    indicating subtraction (e.g: IV = 4).

    Examples:
        romanToInteger("X") => 10
        romanToInteger("VII") => 7
        romanToInteger("LXXXVII") => 87
    """
