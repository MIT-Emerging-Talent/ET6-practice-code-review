def count_words(text):
    """
    Counts the number of words in a given string.

    Args:
        text (str): The string to analyze.

    Returns:
        int: The number of words in the string.
    """
    # Split the text by whitespace and count the resulting parts
    words = text.split()
    return len(words)

# Example usage
example_text = "Hello, Nova! How many words are in this sentence?"
word_count = count_words(example_text)
print(f"The text contains {word_count} words.")
