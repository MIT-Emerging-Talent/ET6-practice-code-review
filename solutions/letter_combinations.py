"""Module for generating letter combinations from a telephone keypad.

The mapping follows:
    2 -> a, b, c
    3 -> d, e, f
    4 -> g, h, i
    5 -> j, k, l
    6 -> m, n, o
    7 -> p, q, r, s
    8 -> t, u, v
    9 -> w, x, y, z
"""


def letter_combinations(digits: str) -> list[str]:
    """
    Return all possible letter combinations for the given digits.

    :param digits: str
    :return: list[str]

    :raises AssertionError: If `digits` is not a string.
    :raises AssertionError: If `digits` contains characters outside '2'..'9'.
    :raises AssertionError: If `digits` is longer than 4 characters.

    >>> letter_combinations('23') 
    ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    >>> letter_combinations('2')
    ['a', 'b', 'c']
    >>> letter_combinations('')
    []
    """

    assert isinstance(digits, str), "digits must be a string"
    assert len(digits) <= 4, "digits can have at most 4 characters"
    for digit in digits:
        assert digit in "23456789", "All digits must be in range '2'..'9'"

    if not digits:
        return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result: list[str] = []

    def backtrack(
        combination: str, remaining_digits: str
    ) -> None:  # recursive combinations
        if not remaining_digits:
            result.append(combination)
        else:
            for letter in phone_map[remaining_digits[0]]:
                backtrack(combination + letter, remaining_digits[1:])

    backtrack("", digits)
    return result
