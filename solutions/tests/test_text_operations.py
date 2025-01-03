"""This is a test for the code about text operations."""

# test_text_operations.py
import unittest


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


class TestTextOperations(unittest.TestCase):
    def test_reverse_text(self):
        self.assertEqual(reverse_text("Hello"), "olleH")
        self.assertEqual(reverse_text("Python"), "nohtyP")
        self.assertEqual(reverse_text(""), "")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World!"), 3)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels(""), 0)

    def test_word_count(self):
        self.assertEqual(word_count("Hello World!"), 2)
        self.assertEqual(word_count("This is a test."), 4)
        self.assertEqual(word_count(""), 0)

    def test_to_uppercase(self):
        self.assertEqual(to_uppercase("hello"), "HELLO")
        self.assertEqual(to_uppercase("Python"), "PYTHON")
        self.assertEqual(to_uppercase("123"), "123")

    def test_to_lowercase(self):
        self.assertEqual(to_lowercase("HELLO"), "hello")
        self.assertEqual(to_lowercase("Python"), "python")
        self.assertEqual(to_lowercase("123"), "123")

    def test_replace_word(self):
        self.assertEqual(
            replace_word("Hello World!", "World", "Python"), "Hello Python!"
        )
        self.assertEqual(
            replace_word("This is a test.", "test", "demo"), "This is a demo."
        )
        self.assertEqual(replace_word("Hello Hello", "Hello", "Hi"), "Hi Hi")

    def test_get_first_n_characters(self):
        self.assertEqual(get_first_n_characters("Hello World!", 5), "Hello")
        self.assertEqual(get_first_n_characters("Python", 3), "Pyt")
        self.assertEqual(get_first_n_characters("Test", 10), "Test")

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("  Hello World!  "), "Hello World!")
        self.assertEqual(remove_whitespace("Python"), "Python")
        self.assertEqual(remove_whitespace("    "), "")

    def test_contains_substring(self):
        self.assertTrue(contains_substring("Hello World!", "World"))
        self.assertFalse(contains_substring("Python", "Java"))
        self.assertTrue(contains_substring("This is a test.", "test"))


if __name__ == "__main__":
    unittest.main()
