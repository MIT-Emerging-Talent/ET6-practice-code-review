def minion_game(text):
    """
    Determines the winner of the Minion Game based on the input string.

    The Minion Game is played between two players, Kevin and Stuart, where:
    - Kevin scores points for substrings starting with vowels ('a', 'e', 'i', 'o', 'u').
    - Stuart scores points for substrings starting with consonants.

    The points are awarded based on the number of substrings that start at each index of the string.
    For example, if the string is 'banana', substrings starting at index 0, 1, 2, etc., are considered.

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
    kevin_score = 0
    stuart_score = 0
    vowels = {"a", "e", "i", "o", "u"}
    text = text.lower()
    n = len(text)

    for i in range(n):
        if text[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        return "Kevin", kevin_score
    elif stuart_score > kevin_score:
        return "Stuart", stuart_score
    else:
        return "Draw"
    
