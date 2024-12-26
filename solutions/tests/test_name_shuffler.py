import unittest

from solutions.name_shuffler import name_shuffler


class TestNameShuffler(unittest.TestCase):
 
    def test_only_first_name_input(self):
        """Test first  input"""
        self.assertEqual(name_shuffler('Mojtaba'), 'Mojtaba')

    
    def test_fatima_input(self):
        self.assertEqual(name_shuffler('Fatima Malik'), 'Malik Fatima')

    
    def test_long_name_input(self):
        self.assertEqual(name_shuffler(''), '')

    

if __name__ == '__main__':
    unittest.main()