"""
This module contains unit tests for the `triangle_printer` function from the `print_triangle_shape` module.
The tests check various scenarios, including invalid inputs, edge cases, and larger inputs, ensuring the function behaves as expected.

@Author: Mukuna Kabeya
@Version: 1.0.0
@Date: 2024-01-06
"""

import unittest
from ..print_triangle_shape import triangle_printer


class TestPrintTriangleShape(unittest.TestCase):
    """
    Unit tests for the `triangle_printer` function.

    These tests ensure that the function works correctly for a range of inputs:
    from invalid or edge cases to valid small and large inputs.
    """

    def test_invalid_inputs(self):
        """
        Ensure the function raises the correct exceptions for invalid inputs.

        This test checks how the function handles cases like non-integer values
        and integers that are too small (less than or equal to 1).
        """
        with self.assertRaises(TypeError):
            triangle_printer("abc")
        with self.assertRaises(ValueError):
            triangle_printer(1)

    def test_small_valid_inputs(self):
        """
        Check that the function correctly handles small valid inputs.

        This test ensures the function prints the correct triangle for small numbers like 2 and 3.
        """
        self.assertEqual(triangle_printer(3), ["  *", " ***", "*****"])

    def test_edge_and_large_inputs(self):
        """
        Test the function with edge cases and larger valid inputs.

        This test includes:
        - An edge case with the smallest valid input (2 rows).
        - A larger input (10 rows) to verify the function can handle bigger sizes.
        """

        self.assertEqual(triangle_printer(2), [" *", "***"])
        expected_output = [
            "         *",
            "        ***",
            "       *****",
            "      *******",
            "     *********",
            "    ***********",
            "   *************",
            "  ***************",
            " *****************",
            "*******************",
        ]
        self.assertEqual(triangle_printer(10), expected_output)


if __name__ == "__main__":
    unittest.main()
