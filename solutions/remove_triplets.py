def remove_triplets(text: str):
    """
    This function remove triplets from a string. A triplet is a sequence of 3 consecutive characters.

    Args:
        text (str): The input string to process. It can be empty or contain any characters.

    Returns:
        _type_: The processed string where no three consecutive characters are the same.

    Raises:
        AssertionError: If input is not of type string.

    Example:
    >>> remove_triplets("aaabaaaa")
    "aabaa"

    >>> remove_triplets("helllo")
    "hello"

    >>> remove_triplets("leeetcode")
    "leetcode"

    edge case:
    - If input is an empty string, return an empty string.
    - If input has no three consecutive characters, return the input string.
    - If the input contains higher than 3 consecutive characters, the function limits the repetitions to 2 chars
    """
    # Validate input type
    assert isinstance(text, str), "Input must be a string type"

    # Handle empty input
    if text == "":
        return ""

    prev = text[0]
    frequency = 1
    ans = text[0]

    for i in range(1, len(text)):
        if text[i] == prev:
            frequency += 1
        else:
            prev = text[i]
            frequency = 1
        if frequency < 3:
            ans += text[i]

    return ans


print(remove_triplets(""))
