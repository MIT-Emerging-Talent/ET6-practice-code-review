"""This is a code about text operations."""
# text_operations.py


def reverse_text(text):
    """Returns the reversed version of the input text."""
    return text[::-1]


def count_vowels(text):
    """Returns the number of vowels (a, e, i, o, u) in the input text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)


def word_count(text):
    """Returns the number of words in the input text."""
    words = text.split()
    return len(words)


def to_uppercase(text):
    """Converts the input text to uppercase and returns it."""
    return text.upper()


def to_lowercase(text):
    """Converts the input text to lowercase and returns it."""
    return text.lower()


def replace_word(text, old_word, new_word):
    """Replaces all occurrences of old_word with new_word in the input text."""
    return text.replace(old_word, new_word)


def get_first_n_characters(text, n):
    """Returns the first n characters of the input text."""
    return text[:n]


def remove_whitespace(text):
    """Removes all leading and trailing whitespaces from the input text."""
    return text.strip()


def contains_substring(text, substring):
    """Checks if a substring exists within the input text and returns True or False."""
    return substring in text
