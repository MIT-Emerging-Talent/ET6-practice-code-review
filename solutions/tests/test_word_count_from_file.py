"""
Counts the number of words in a .txt file

Parameters:
    file_name (str) - The name of the file

Returns -> The total number of words in the file

Raises: AssertionError


"""

import os
import sys
import unittest

# Add the project root directory to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from solutions.word_count_from_file import word_count_txt_file


class TestWordCountFromFile(unittest.TestCase):
    """Test the words counting function"""

    def test_5(self):
        """This method test if the function returns the correct number"""
        self.assertEqual(word_count_txt_file("solutions/test_5.txt"), 5)

    def test_empty(self):
        """This method test an empty file"""
        self.assertEqual(word_count_txt_file("solutions/test_empty.txt"), 0)

    def test_multiple_lines(self):
        """This method test when a file has multiple lines"""
        self.assertEqual(word_count_txt_file("solutions/test_multiple.txt"), 10)

    def test_file_not_exist(self):
        """This method test when a file has multiple lines"""
        with self.assertRaises(AssertionError):
            word_count_txt_file("not_exist.txt")

    def test_not_a_txt_file(self):
        """It should raise an assertion error if the argument is not an integer"""
        with self.assertRaises(AssertionError):
            word_count_txt_file("test")
