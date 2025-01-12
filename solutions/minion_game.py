"""
This module contains a function minion_game which is the implementation of the Minion Game

The Minion Game is played between two players, Kevin and Stuart, where:
    - Kevin scores points for substrings starting with vowels ('a', 'e', 'i', 'o', 'u').
    - Stuart scores points for substrings starting with consonants.

    The points are awarded based on the number of substrings that start at each index of the string.
    For example, if the string is 'banana', substrings starting at index 0, 1, 2, etc., are considered.

Author: Salem Amassi

"""


def minion_game(text : str):
    """
    Determines the winner of the Minion Game based on the input string.

    Args:
        text (str): The input string to play the Minion Game with. The string is converted to lowercase to ensure case-insensitivity.

    Returns:
        tuple or str:
            - If there is a winner, returns a tuple with the winner's name ('Kevin' or 'Stuart') and their score.
            - If it's a draw, returns 'Draw'.

    Example:

    >>> minion_game("banana")
    ('Stuart', 12)

    >>> minion_game("a")
    ('Kevin', 1)

    >>> minion_game("b")
    ('Stuart', 1)

    >>> minion_game("aeiou")
    ('Kevin', 15)

    """
    # check if the input is empty
    if not text:
        raise ValueError("Input must not be empty")

    # check if the input is numeric
    if text.isnumeric():
        raise ValueError("Input must not be empty")

    # define both players' scores
    kevin_score = 0
    stuart_score = 0

    # define vowels to check with
    vowels = {"a", "e", "i", "o", "u"}

    # convert the text to lower case
    text = text.lower()

    # get the length
    text_length = len(text)

    # iterate the input and update scores

    for i in range(text_length):
        if text[i] in vowels:
            kevin_score += (
                text_length - i
            )  # add all other occurrences of character to kevin_score
        else:
            stuart_score += (
                text_length - i
            )  # add all other occurrences of character to stuart_score

    # evaluate the result

    if kevin_score > stuart_score:
        return "Kevin", kevin_score
    elif stuart_score > kevin_score:
        return "Stuart", stuart_score
    else:
        return "Draw"
