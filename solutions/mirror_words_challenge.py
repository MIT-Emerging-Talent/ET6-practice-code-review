import re


def reverse_words(sentence):
    """
    Reverses each word in a given sentence while maintaining the order of the words
    and correctly handling punctuation marks at the end of words.

    Args:
        sentence (str): The sentence to be processed. It can contain words, punctuation,
                         and spaces.

    Returns:
        str: A new string where each word is reversed, but the word order and punctuation
             remain unchanged.

    Example:
        >>> reverse_words("Hello world!")
        'olleH dlrow!'

        >>> reverse_words("Python is fun")
        'nohtyP si nuf'

    Raises:
        TypeError: If the input is not a string.
    """

    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    words = sentence.split()
    reversed_words = []
    for word in words:
        # Match the word and any punctuation at the end
        match = re.match(r"([a-zA-Z]+)([^a-zA-Z]*)", word)
        if match:
            # Reverse the word and keep punctuation at the end without reversing it
            reversed_word = match.group(1)[::-1] + match.group(2)
            reversed_words.append(reversed_word)
        else:
            # If no match is found, just append the word
            reversed_words.append(word)
    return " ".join(reversed_words)
