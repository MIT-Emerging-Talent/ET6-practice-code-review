"""
This function takes a sentence and returns the longest word in it.
If multiple words have the same length, the first one is returned.
"""

def find_longest_word(text):
    """
    Finds and returns the longest word in a given sentence.

    Parameters:
        sentence (str): The input sentence as a string.

    Returns:
        str: The longest word in the sentence.
        If there are multiple words with the same length, the first one encountered is returned.
    
    Example:
        find_longest_word("I learned a lot thanks to the Matrix team and this teamwork")
        Output: "teamwork"
    """
    # Split the sentence into a list of words
    words = text.split()

    # Use max() with key=len to find the longest word
    longest_word = max(words, key=len)

    return longest_word

sentence = "I learned a lot of things to the Matrix team and this teamwork" # pylint: disable=invalid-name
print(find_longest_word(sentence))  # Output: "teamwork"
