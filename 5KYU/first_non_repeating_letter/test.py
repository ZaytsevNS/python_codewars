import unittest
import main


class TestFirstNonRepeatingLetter(unittest.TestCase):
    def test_one(self):
        """ Should return the first character that is not repeated anywhere in the string """
        self.assertEqual('t', main.first_non_repeating_letter('stress'))
        self.assertEqual('T', main.first_non_repeating_letter('sTreSS'))
    
    def test_two(self):
        """ Should return an empty string """
        self.assertEqual('', main.first_non_repeating_letter('abab'))
        
if __name__ == '__main__':
    unittest.main()
