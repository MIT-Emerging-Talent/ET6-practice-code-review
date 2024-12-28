import unittest
from word_frequency import count_word_frequency

class TestCountWordFrequency(unittest.TestCase):
    def test_basic_case(self):
        text = "Hello world! Hello, world."
        expected = {"hello": 2, "world": 2}
        self.assertEqual(count_word_frequency(text), expected)

    def test_empty_string(self):
        text = ""
        expected = {}
        self.assertEqual(count_word_frequency(text), expected)

    def test_punctuation(self):
        text = "Python, Python. Python!"
        expected = {"python": 3}
        self.assertEqual(count_word_frequency(text), expected)

    def test_mixed_case(self):
        text = "Python python PYTHON"
        expected = {"python": 3}
        self.assertEqual(count_word_frequency(text), expected)

    def test_non_string_input(self):
        with self.assertRaises(ValueError):
            count_word_frequency(12345)

if __name__ == "__main__":
    unittest.main()

