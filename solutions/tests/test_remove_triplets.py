import unittest

from solutions.remove_triplets import remove_triplets


# Test cases for remove_triplets function
class test_remove_triplets(unittest.TestCase):
    def test_empty_input(self):
        """Test when input is empty"""
        self.assertEqual(remove_triplets(""), "")

    def test_input_without_consecutive(self):
        """Test input without consecutive characters"""
        self.assertEqual(remove_triplets("abc"), "abc")

    def test_input_with_one_consecutive(self):
        """Test input with one consecutive character"""
        self.assertEqual(remove_triplets("helllo"), "hello")
        self.assertEqual(remove_triplets("leeetcode"), "leetcode")

    def test_input_with_two_consecutive(self):
        """Test input with two consecutive characters"""
        self.assertEqual(remove_triplets("aaabaaaa"), "aabaa")

    def test_invalid_input_type(self):
        """Test invalid input type"""
        with self.assertRaises(AssertionError):
            remove_triplets(123)  # Passing an integer instead of a string


if __name__ == "__main__":
    unittest.main()
