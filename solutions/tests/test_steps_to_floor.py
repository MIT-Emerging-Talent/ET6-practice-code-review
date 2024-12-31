import unittest
from ..steps_to_floor import steps_to_floor_core


class TestStepsToFloor(unittest.TestCase):
    def test_zero_floor(self):
        self.assertEqual(steps_to_floor_core(0), 0)

    def test_positive_floor(self):
        self.assertEqual(steps_to_floor_core(1), 10)

    def test_negative_floor(self):
        self.assertEqual(steps_to_floor_core(-3), 30)

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            steps_to_floor_core("a")  # Non-integer input
        with self.assertRaises(AssertionError):
            steps_to_floor_core(5.5)  # Float input


if __name__ == "__main__":
    unittest.main()