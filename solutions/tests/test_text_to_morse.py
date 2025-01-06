#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

A test for module text_to_morse

Test categories:
  - Standard cases: letters, number, some symbols
  - Edge cases:  sentences, long paragraphes, large numbers
  - Defensive tests: assertions, unknown character

Created on 5 1 2025

@author: Ahmed Hussein
"""

import unittest


from ..text_to_morse import text_to_morse


class TestTextToMorse(unittest.TestCase):
    """Test the text_to_morse function"""

    def test_empty_sapce(self):
        """Test evaluate the Morse code of ' '"""
        self.assertEqual(text_to_morse(" "), "/")

    def test_single_lowercase_letter(self):
        """Test evaluate the Morse code of 'a'"""
        self.assertEqual(text_to_morse("a"), ".-")

    def test_single_uppercase_letter(self):
        """Test evaluate the Morse code of 'A'"""
        self.assertEqual(text_to_morse("A"), ".-")

    def test_one_digit_number(self):
        """Test evaluate the Morse code of '3'"""
        self.assertEqual(text_to_morse("3"), "...--")

    def test_two_digits_number(self):
        """Test evaluate the Morse code of '47'"""
        self.assertEqual(text_to_morse("47"), "....- --...")

    def test_many_digits_number(self):
        """Test evaluate the Morse code of '653367745091'"""
        self.assertEqual(
            text_to_morse("653367745091"),
            "-.... ..... ...-- ...-- -.... --... --... ....- ..... ----- ----. .----",
        )

    def test_simple_word(self):
        """Test evaluate the Morse code of 'Hi'"""
        self.assertEqual(text_to_morse("Hi"), ".... ..")

    def test_two_lowercase_words(self):
        """Test evaluate the Morse code of 'forza milan'"""
        self.assertEqual(
            text_to_morse("forza milan"), "..-. --- .-. --.. .- / -- .. .-.. .- -."
        )

    def test_All_uppercase(self):
        """Test evaluate the Morse code of 'CQD DE MGY'"""
        self.assertEqual(
            text_to_morse("CQD DE MGY"), "-.-. --.- -.. / -.. . / -- --. -.--"
        )

    def test_symbols(self):
        """Test evaluate the Morse code of '/-)'"""
        self.assertEqual(text_to_morse("/-)"), "-..-. -....- -.--.-")

    def test_small_sentence(self):
        """Test evaluate the Morse code of 'In the early days of radio, Morse code was the primary means of communication.'"""
        self.assertEqual(
            text_to_morse(
                "In the early days of radio, Morse code was the primary means of communication."
            ),
            ".. -. / - .... . / . .- .-. .-.. -.-- / -.. .- -.-- ... / --- ..-. / .-. .- -.. .. --- --..-- / -- --- .-. ... . / -.-. --- -.. . / .-- .- ... / - .... . / .--. .-. .. -- .- .-. -.-- / -- . .- -. ... / --- ..-. / -.-. --- -- -- ..- -. .. -.-. .- - .. --- -. .-.-.-",
        )

    def test_long_paragraph(self):
        """Test evaluate the morse code of 'Morse code, invented by Samuel Morse in the 1830s, is a method of encoding text into dots and dashes. It revolutionized communication in the 19th century and was used to send messages like the famous first Morse code transmission -What hath God wrought?-Today, Morse code is still used by ham radio operators, pilots, and enthusiasts who appreciate its simplicity and reliability.'"""
        self.assertEqual(
            text_to_morse(
                "Morse code is like the ancient text messaging of the 19th century. Invented by Samuel Morse in the 1830s, it revolutionized communication by turning letters into dots and dashes. Fun fact The first Morse code message sent was, -What hath God wrought?- which roughly translates to, -Can you hear me now?- Today, Morse code is still used by ham radio enthusiasts, pilots, and spies who refuse to upgrade to emojis."
            ),
            "-- --- .-. ... . / -.-. --- -.. . / .. ... / .-.. .. -.- . / - .... . / .- -. -.-. .. . -. - / - . -..- - / -- . ... ... .- --. .. -. --. / --- ..-. / - .... . / .---- ----. - .... / -.-. . -. - ..- .-. -.-- .-.-.- / .. -. ...- . -. - . -.. / -... -.-- / ... .- -- ..- . .-.. / -- --- .-. ... . / .. -. / - .... . / .---- ---.. ...-- ----- ... --..-- / .. - / .-. . ...- --- .-.. ..- - .. --- -. .. --.. . -.. / -.-. --- -- -- ..- -. .. -.-. .- - .. --- -. / -... -.-- / - ..- .-. -. .. -. --. / .-.. . - - . .-. ... / .. -. - --- / -.. --- - ... / .- -. -.. / -.. .- ... .... . ... .-.-.- / ..-. ..- -. / ..-. .- -.-. - / - .... . / ..-. .. .-. ... - / -- --- .-. ... . / -.-. --- -.. . / -- . ... ... .- --. . / ... . -. - / .-- .- ... --..-- / -....- .-- .... .- - / .... .- - .... / --. --- -.. / .-- .-. --- ..- --. .... - ..--.. -....- / .-- .... .. -.-. .... / .-. --- ..- --. .... .-.. -.-- / - .-. .- -. ... .-.. .- - . ... / - --- --..-- / -....- -.-. .- -. / -.-- --- ..- / .... . .- .-. / -- . / -. --- .-- ..--.. -....- / - --- -.. .- -.-- --..-- / -- --- .-. ... . / -.-. --- -.. . / .. ... / ... - .. .-.. .-.. / ..- ... . -.. / -... -.-- / .... .- -- / .-. .- -.. .. --- / . -. - .... ..- ... .. .- ... - ... --..-- / .--. .. .-.. --- - ... --..-- / .- -. -.. / ... .--. .. . ... / .-- .... --- / .-. . ..-. ..- ... . / - --- / ..- .--. --. .-. .- -.. . / - --- / . -- --- .--- .. ... .-.-.-",
        )

    def test_not_string(self):
        """Test should raise AssertionError for non-string input"""
        with self.assertRaises(AssertionError):
            text_to_morse(123)

    def test_unknown_character(self):
        """Test should raise ValueError for unknown characters"""
        with self.assertRaises(ValueError):
            text_to_morse("π")
