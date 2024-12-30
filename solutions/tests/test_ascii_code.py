#!/usr/bin/env python3
# --#coding: utf-8 --

"""
DESCRIPTION: Tests for the ASCII code conversion functionality.

This module contains a test suite for the ASCII code conversion functionality.
Tests are written for basic characters, whitespace characters, special characters,
numeric characters.

"""

# Import the unittest module
import unittest

# Import the function to be tested
from solutions.ascii_code import ascii_code


# Define a test suite for the ASCII code conversion functionality:
class TestAsciiCode(unittest.TestCase):
    """Test suite for ASCII code conversion functionality."""

    def test_basic_chars(self):
        """Test conversion of capital and small characters."""
        self.assertEqual(ascii_code("A"), [65])
        self.assertEqual(ascii_code("Z"), [90])
        self.assertEqual(ascii_code("a"), [97])
        self.assertEqual(ascii_code("z"), [122])

    def test_whitespace(self):
        """Test conversion of whitespace characters."""
        self.assertEqual(ascii_code(" "), [32])  # space
        self.assertEqual(ascii_code("\t"), [9])  # tab
        self.assertEqual(ascii_code("\n"), [10])  # newline

    def test_special_chars(self):
        """Test conversion of special characters."""
        self.assertEqual(ascii_code("!"), [33])
        self.assertEqual(ascii_code("@"), [64])
        self.assertEqual(ascii_code("#"), [35])
        self.assertEqual(ascii_code("$"), [36])

    def test_numbers(self):
        """Test conversion of numeric characters."""
        self.assertEqual(ascii_code("0"), [48])
        self.assertEqual(ascii_code("9"), [57])

    def test_word_input(self):
        """Test handling of word inputs."""
        self.assertEqual(ascii_code("Hello"), [72, 101, 108, 108, 111])
        self.assertEqual(ascii_code("ASCII"), [65, 83, 67, 73, 73])
        self.assertEqual(ascii_code("cat "), [99, 97, 116, 32])

    def test_empty_input(self):
        """Test handling of empty string input."""
        self.assertEqual(ascii_code(""), [])
        self.assertEqual(ascii_code(" "), [32])

    def test_number_input(self):
        """Test handling of number input."""
        with self.assertRaises(AssertionError):
            ascii_code(123)

    def test_list_input(self):
        """Test handling of list input."""
        with self.assertRaises(AssertionError):
            ascii_code([1, 2, 3])

    def test_boolean_input(self):
        """Test handling of boolean input."""
        with self.assertRaises(AssertionError):
            ascii_code(True)
