
"""
    This module contains unit tests for the triangle_printer function in the print_triangle_shape module.
    The unit tests cover various scenarios, including invalid inputs, edge cases, and large inputs.
    
    @Author: Mukuna Kabeya
    @Version: 1.0.0
    @Date: 2024-01-06
"""
import unittest
from ..print_triangle_shape import triangle_printer

class TestPrintTriangleShape(unittest.TestCase):
    """
    Unit tests for the triangle_printer function.

    These tests verify that the function handles invalid inputs gracefully and
    produces the correct output for valid inputs, including edge cases and large inputs.
    """
    def test_invalid_inputs(self):
        """
        Test that the function raises appropriate exceptions for invalid inputs.

        This test falls under the 'Defensive tests' category, as it tests how the function handles 
        invalid inputs, such as non-integer values and integers less than or equal to 1.
        """
        with self.assertRaises(TypeError):
            triangle_printer("abc")
        with self.assertRaises(ValueError):
            triangle_printer(1)

    def test_small_valid_inputs(self):
        """
        Test that the function returns the correct output for small valid inputs.

        This test falls under the 'Standard cases' category, as it checks typical inputs with small 
        numbers like 2 and 3, ensuring the correct triangle is printed for these values.
        """
        self.assertEqual(triangle_printer(3), ["  *", " ***", "*****"])

    def test_edge_and_large_inputs(self):
        """
        Test the function for edge cases and large valid inputs.

        This test covers both 'Edge cases' and 'Standard cases' categories:
        - Edge case: minimum valid input (rows = 2).
        - Standard case: large input (rows = 10) to test how the function handles larger sizes.
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
            "*******************"
        ]
        self.assertEqual(triangle_printer(10), expected_output)

if __name__ == "__main__":
    unittest.main()
