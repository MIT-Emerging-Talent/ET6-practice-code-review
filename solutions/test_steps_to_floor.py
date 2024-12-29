import unittest
from steps_to_floor import steps_to_floor

class TestStepsToFloor(unittest.TestCase):
    def test_zero_floor(self):
        self.assertEqual(steps_to_floor(0), 0)

    def test_positive_floor(self):
        self.assertEqual(steps_to_floor(1), 10)
        self.assertEqual(steps_to_floor(5), 50)

    def test_negative_floor(self):
        self.assertEqual(steps_to_floor(-1), 10)
        self.assertEqual(steps_to_floor(-3), 30)

    def test_invalid_input(self):
        with self.assertRaises(AssertionError):
            steps_to_floor("a")  # Non-integer input
        with self.assertRaises(AssertionError):
            steps_to_floor(5.5)  # Float input

if __name__ == "__main__":
    unittest.main()

