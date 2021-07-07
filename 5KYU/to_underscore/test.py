import unittest
import main


class TestToUnderscore(unittest.TestCase):
    def test_one(self):
        """ Should returns the string in snake_case notation """
        self.assertEqual('test_controller', main.to_underscore('TestController'))
        self.assertEqual('movies_and_books', main.to_underscore('MoviesAndBooks'))
        self.assertEqual('app7_test', main.to_underscore('App7Test'))
        
    def test_two(self):
        """ Should return string """
        self.assertEqual('1', main.to_underscore(1))
        
if __name__ == '__main__':
    unittest.main()
