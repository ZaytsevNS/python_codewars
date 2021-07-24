import unittest
import main as valid_ISBN10


class TestValidISBN10(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, valid_ISBN10.valid_ISBN10('1112223339'))
        self.assertEqual(True, valid_ISBN10.valid_ISBN10('048665088X'))
        self.assertEqual(True, valid_ISBN10.valid_ISBN10('1293000000'))
        self.assertEqual(True, valid_ISBN10.valid_ISBN10('1234554321'))       
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, valid_ISBN10.valid_ISBN10('1234512345'))
        self.assertEqual(False, valid_ISBN10.valid_ISBN10('1293'))
        self.assertEqual(False, valid_ISBN10.valid_ISBN10('X123456788'))
        self.assertEqual(False, valid_ISBN10.valid_ISBN10('ABCDEFGHIJ'))
        self.assertEqual(False, valid_ISBN10.valid_ISBN10('XXXXXXXXXX'))
        
if __name__ == '__main__':
    unittest.main()
