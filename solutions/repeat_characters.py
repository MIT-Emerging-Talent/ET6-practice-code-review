"""
Repeat characters

1/4/2025

author by: Dmytro Klymenko

"""


def repeat_characters(word: str) -> str:
    """
    Function repeat all characters in word 2 times and return long word
      Args:
        repeat_characters(str) - desired word

    Returns:
        str: Desired word with doubled characters

    Examples:

    >>>print(repeat_characters("Winter"))
    WWiinntteerr

    >>>print(repeat_characters("peach"))
    ppeeaacchh

    >>>print(repeat_characters("cola"))
    ccoollaa

    """
    assert isinstance(word, str)  # Input must be a string

    long_word = ""

    for char in word:
        long_word += char * 2
    return long_word
