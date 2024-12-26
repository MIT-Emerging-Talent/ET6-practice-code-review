#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the matrix_2x2_inversion function.

Test categories:
    - Standard test cases: 
    - Edge test cases:
    - Defensive tests:
    

Created on 2024-12-26
Author: Awaab98
"""

import unittest
from solutions.matrix_2x2_inversion import matrix_2x2_inversion


class TestMatrix2x2Inversion(unittest.TestCase):
    """ Tests suite for the matrix_2x2_inversion function. """
  
    def test_matrix_with_integer_elements(self):
        """ It should return the inverse of the input matrix. """
        self.assertEqual(matrix_2x2_inversion([[1, 2], [3, 4]]), [[-2.0, 1.0], [1.5, -0.5]])
