import unittest
import main


class TestPig_it(unittest.TestCase):
    def test_one(self):
        """ Should moves the first letter of each word to the end of it, then add 'ay' to the end of the word """
        self.assertEqual('igPay atinlay siay oolcay', main.pig_it('Pig latin is cool'))
        self.assertEqual('hisTay siay ymay tringsay', main.pig_it('This is my string'))
    def test_two(self):
        """ Should moves the first letter of each word to the end of it, then add 'ay' to the end of the word 
        and ignore punctuation marks """
        self.assertEqual('elloHay orldway !', main.pig_it('Hello world !'))
        
if __name__ == '__main__':
    unittest.main()
