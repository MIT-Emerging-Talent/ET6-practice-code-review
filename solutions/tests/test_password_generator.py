"""
Test suite for the password_generator function.

Test categories:
    - Standard cases: Tests that check the valid input scenarios for generating passwords.
        - `test_valid_password_length_small`: Verifies a password of length 4.
        - `test_valid_password_length_large`: Verifies a password of length 10.

    - Edge cases: Tests that check the boundaries of the valid input range for password length.
        - `test_password_length_too_small`: Verifies that a password length of 0 or 1 raises an error.
        - `test_valid_password_length_small`: Verifies the lower boundary of valid input (length 4).

    - Defensive cases: Tests that check for invalid inputs that should raise errors.
        - `test_empty_string_input`: Verifies that an empty string raises a `ValueError`.
        - `test_negative_password_length`: Verifies that a negative password length raises a `ValueError`.
        - `test_non_integer_input`: Verifies that non-integer inputs (like string or float) raise a `ValueError`.

@Author: Mukuna Kabeya
@date: 2025-01-05
"""

import unittest
from ..password_generator import password_generator


class TestPasswordGenerator(unittest.TestCase):
    """
    Test suite for the password_generator function.
    Verifies the behavior of the function with various valid and invalid inputs.
    """

    def test_empty_string_input(self):
        """
        Verify that an empty string input raises a ValueError.

        :raises ValueError: when password_generator is called with an empty string.
        """
        with self.assertRaises(ValueError):
            password_generator("")

    def test_password_length_too_small(self):
        """
        Verify that a password length less than 2 raises a ValueError.

        :raises ValueError: when password_generator is called with a length of 0 or 1.
        """
        with self.assertRaises(ValueError):
            password_generator(0)
        with self.assertRaises(ValueError):
            password_generator(1)

    def test_negative_password_length(self):
        """
        Verify that a negative password length raises a ValueError.

        :raises ValueError: when password_generator is called with a negative length.
        """
        with self.assertRaises(ValueError):
            password_generator(-1)

    def test_non_integer_input(self):
        """
        Verify that non-integer inputs raise a ValueError.

        :raises ValueError: when password_generator is called with a string or float.
        """
        with self.assertRaises(ValueError):
            password_generator("hello")
        with self.assertRaises(ValueError):
            password_generator(3.14)

    def test_valid_password_length_small(self):
        """
        Verify that a password of length 4 is generated correctly.

        :assert: the generated password has a length of 4.
        """
        password = password_generator(4)
        self.assertEqual(len(password), 4)

    def test_valid_password_length_large(self):
        """
        Verify that a password of length 10 is generated correctly.

        :assert: the generated password has a length of 10.
        """
        password = password_generator(10)
        self.assertEqual(len(password), 10)


if __name__ == "__main__":
    unittest.main()
