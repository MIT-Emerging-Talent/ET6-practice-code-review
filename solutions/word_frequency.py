def word_frequency_counter(text):
    """
    Counts the frequency of each word in the given text.

    Args:
        text (str): The input text.

    Returns:
        dict: A dictionary where the keys are words and values are their frequency.

    Examples:
        >>> word_frequency_counter("hello world")
        {'hello': 1, 'world': 1}
        >>> word_frequency_counter("hello hello world")
        {'hello': 2, 'world': 1}
        >>> word_frequency_counter("Python is fun! Python is amazing!")
        {'python': 2, 'is': 2, 'fun!': 1, 'amazing!': 1}
        >>> word_frequency_counter("one fish two fish red fish blue fish")
        {'one': 1, 'fish': 4, 'two': 1, 'red': 1, 'blue': 1}
        >>> word_frequency_counter("It's a beautiful day in the neighborhood.")
        {"it's": 1, 'a': 1, 'beautiful': 1, 'day': 1, 'in': 1, 'the': 1, 'neighborhood.': 1}
    """
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq
