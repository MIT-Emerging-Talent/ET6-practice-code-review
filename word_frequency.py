def count_word_frequency(text):
    """
    Counts the frequency of each word in a given string.

    Args:
        text (str): The input text to analyze.

    Returns:
        dict: A dictionary where keys are words and values are their frequencies.

    Raises:
        ValueError: If the input text is not a string.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Normalize case and split text into words
    words = text.lower().split()

    # Remove punctuation from each word
    cleaned_words = [word.strip('.,!?;:"()') for word in words]

    # Count word frequencies
    word_counts = {}
    for word in cleaned_words:
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts

