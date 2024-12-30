import unittest

from ..harmonic_sequence import harmonic_sequence


class TestAsciiCode(unittest.TestCase):
    def test_min_input1(self):
        """Test case when all inputs equal to 1"""
        self.assertEqual(harmonic_sequence(1, 1, 1), [1.0])

    def test_n_equal_0(self):
        """Test case when n is equal to 0"""
        self.assertEqual(harmonic_sequence(1, 1, 0), [])

    def test_a_and_d_equal_0(self):
        """Test case when a and d are equal to 0"""
        self.assertEqual(harmonic_sequence(0, 0, 5), [0, 0, 0, 0, 0])

    def test_n_negative(self):
        """Test case when n is negative"""
        self.assertEqual(harmonic_sequence(1, 1, -1), [])

    def test_a_and_d_equal_1(self):
        """Test a and d are equal 1"""
        self.assertEqual(
            harmonic_sequence(1, 1, 5), [1.0, 0.5, 0.3333333333333333, 0.25, 0.2]
        )

    def test_all_inputs_greater_than_1(self):
        """Test when all inputs are integer and greater than 1"""
        self.assertEqual(harmonic_sequence(2, 2, 3), [0.5, 0.25, 0.16666666666666666])
