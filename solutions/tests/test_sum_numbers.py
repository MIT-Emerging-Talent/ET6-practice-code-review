"""

Team number:28
Team name:MIT Alpha
The author: Maab Mohamedkhair

"""

import unittest

from ..sum_numbers import sum_numbers

class Testsum_numbers(unittest.TestCase):

    """
    This class contains unit tests for (sum_numbers) function.
    The function takes a positive integer and count down until reach one then return the sum
    of all numbers
    """
    
    # Standard test cases
    def test_base_case(self):
      """This test checks if the base case (n=1) works correctly."""
      self.assertEqual(sum_numbers(1), 1)

    
    def test_positive_int(self):
      """This test checks if the function works in the normal case"""
      self.assertEqual(sum_numbers(4),10)
    
    def test_twoDigit_int(self):
      """This test checks the function efficiency with numbers between 10 and 99"""
      self.assertEqual(sum_numbers(25),325)

    #Edg cases
    
    def test_large_number(self):
      """This test checks the function's performance for a large number close to recursion limit."""
      self.assertEqual(sum_numbers(900), 405450)  # This should pass normally.

    
    # Defensive test
    
    def test_zero(self):
      """This test checks if the function raises an Exception for zero input."""
      with self.assertRaises(AssertionError):
            sum_numbers(0)

      
    def test_negative_int(self):
      """this test checks negative number it should raise Exception: Input must be greater than 0"""
      with self.assertRaises(AssertionError):
            sum_numbers(-3)
      
    def test_float(self):
      """this test checks the behavior when (n) is float raise AssertionError"""

      with self.assertRaises(AssertionError):
          sum_numbers(1.4)
      
          
    def test_recursion_error(self):
      """this test checks the functions efficiency with the numbers greater than 1000 will return RecursionError"""
      with self.assertRaises(RecursionError):
            sum_numbers(1000)
            
if __name__ == '__main__':
    unittest.main()

      
