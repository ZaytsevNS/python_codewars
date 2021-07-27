import unittest
import main as alphanumeric


class TestAlphanumeric(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, alphanumeric.alphanumeric('password'))
        self.assertEqual(True, alphanumeric.alphanumeric('password1234'))
        self.assertEqual(True, alphanumeric.alphanumeric('12345'))
        self.assertEqual(True, alphanumeric.alphanumeric('passw0rd1'))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, alphanumeric.alphanumeric(''))
        self.assertEqual(False, alphanumeric.alphanumeric('pass word'))
        self.assertEqual(False, alphanumeric.alphanumeric('12_pass '))
        self.assertEqual(False, alphanumeric.alphanumeric('passw 0rd'))
        self.assertEqual(False, alphanumeric.alphanumeric('pass_word'))
        self.assertEqual(False, alphanumeric.alphanumeric('    '))

if __name__ == '__main__':
    unittest.main()
