"""This a unit test for calculate_average function"""

import unittest

from ..calculate_average import calculate_average


class TestGetAverage(unittest.TestCase):
    def test_get_average_not_found(self):
        """
        Tests if KeyError is raised when the student is not found in the records.
        """
        student_records = {"Alice": [85, 90, 78], "Bob": [70, 65, 80]}
        with self.assertRaises(KeyError):
            calculate_average(student_records, "Charlie")

    def test_get_average_single_student(self):
        """
        Tests if the average is correctly calculated for a student with a single mark.
        """
        student_records = {"David": [95, 92, 98]}
        self.assertEqual(calculate_average(student_records, "David"), 95.00)

    def test_get_average_empty_records(self):
        """
        Tests if KeyError is raised when the student records dictionary is empty.
        """
        student_records = {}
        with self.assertRaises(KeyError):
            calculate_average(student_records, "David")

    def test_get_average_empty_marks(self):
        """
        Tests if ZeroDivisionError is raised when the student has no marks.
        """
        student_records = {"David": []}
        with self.assertRaises(ZeroDivisionError):
            calculate_average(student_records, "David")

    def test_get_average_one_mark(self):
        """
        Tests if the average is correctly calculated for a student with only one mark.
        """
        student_records = {"Alice": [90]}
        self.assertEqual(calculate_average(student_records, "Alice"), 90.00)

    def test_get_average_negative_marks(self):
        """
        Tests if the average is correctly calculated for a student with negative marks.
        """
        student_records = {"Bob": [-5, 10, -2]}
        self.assertEqual(calculate_average(student_records, "Bob"), 1.00)

    def test_get_average_decimal_marks(self):
        """
        Tests if the average is correctly calculated for a student with decimal marks.
        """
        student_records = {"Charlie": [87.5, 92.25, 89.75]}
        self.assertEqual(calculate_average(student_records, "Charlie"), 89.83)

    def test_get_average_large_number_of_marks(self):
        """
        Tests if the average is correctly calculated for a student with a large number of marks.
        """
        student_records = {"David": [90] * 100}  # 100 marks of 90
        self.assertEqual(calculate_average(student_records, "David"), 90.00)


if __name__ == "__main__":
    unittest.main()
