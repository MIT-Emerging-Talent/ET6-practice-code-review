"""Test module for pine_tree_art.

@author: fevziismailsahin
@created: 01/10/2025
"""

import unittest

from ..pine_tree_art import draw_tree


class TestDrawTree(unittest.TestCase):
    """
    Test class to verify the functionality of the draw_tree function.
    """

    maxDiff = None  # To see the full difference in case of failure

    def test_default_tree(self):
        """
        Test case for the default tree with default parameters.
        """
        expected_result = """          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
*********************
          |||
          |||"""

        result = draw_tree()
        self.assertEqual(result, expected_result)

    def test_tree_with_large_height(self):
        """
        Test case for a tree with a large height of 15.
        """
        expected_result = """                *
               ***
              *****
             *******
            *********
           ***********
          *************
         ***************
        *****************
       *******************
      *********************
     ***********************
    *************************
   ***************************
  *****************************
 *******************************
*********************************
                |||
                |||"""

        result = draw_tree(15)
        self.assertEqual(result, expected_result)

    def test_tree_with_narrow_trunk(self):
        """
        Test case for a tree with a narrow trunk width of 1.
        """
        expected_result = """    *
   ***
  *****
 *******
*********
   |
   |"""

        result = draw_tree(5, 1, 2)
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
