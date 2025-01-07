import unittest
from ..valid_number import is_number


class TestValidNumber(unittest.TestCase):
    """
    Unit tests for the valid_number function.
    """

    def test_valid_numbers(self):
        """Valid numeric strings."""
        valid_cases = [
            "42",
            "3.14",
            "-3.14",
            "+3.14",
            "1e10",
            "-1E-10",
            "+.5",
            "2.",
            ".2",
            "0",
            "-0",
            "+0",
        ]
        for case in valid_cases:
            with self.subTest(case=case):
                self.assertTrue(valid_number(case))

    def test_invalid_numbers(self):
        """Invalid numeric strings."""
        invalid_cases = [
            "abc",
            "",
            "e",
            "1e",
            "e10",
            ".",
            "-.",
            "1..1",
            "1e1.1",
            "--1",
            "++1",
            "1e10e10",
        ]
        for case in invalid_cases:
            with self.subTest(case=case):
                self.assertFalse(valid_number(case))

    def test_type_errors(self):
        """Non-string inputs should raise a TypeError."""
        invalid_types = [42, None, 3.14, ["1", "2"], {"value": "42"}]
        for case in invalid_types:
            with self.subTest(case=case):
                with self.assertRaises(TypeError):
                    valid_number(case)

    def test_edge_cases(self):
        """Edge cases for valid and invalid numeric strings."""
        edge_cases = {
            " ": False,  # Whitespace only
            "1e-1": True,
            "1234567890": True,
            "0.0000001": True,
            "-1e100": True,
            "+": False,  # Invalid format
        }
        for case, expected in edge_cases.items():
            with self.subTest(case=case):
                self.assertEqual(valid_number(case), expected)


if __name__ == "__main__":
    unittest.main()
