import unittest

from ..word_count_from_file import word_count_txt_file

"""
Counts the number of words in a .txt file.

Parameters:
    file_name (str) - The name of the file

Returns -> The total number of words in the file.

Raises:
    AssertionError: if the  file does not exist
    AssertionError: if the  file is not a .txt file
"""


class TestWordCountFromFile(unittest.TestCase):
    """Test the words counting function"""

    def test_5(self):
        """This method test if the function returns the correct number"""
        actual = word_count_txt_file("solutions/test_5.txt")
        self.assertEqual(actual, 5)

    def test_empty(self):
        """This method test an empty file"""
        actual = word_count_txt_file("solutions/test_empty.txt")
        self.assertEqual(actual, 0)

    def test_multiple_lines(self):
        """This method test when a file has multiple lines"""
        actual = word_count_txt_file("solutions/test_multiple.txt")
        self.assertEqual(actual, 10)

    def test_file_not_exist(self):
        """This method test when a file has multiple lines"""
        with self.assertRaises(AssertionError):
            word_count_txt_file("not_exist.txt")

    def test_not_a_txt_file(self):
        """It should raise an error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            word_count_txt_file("test")
