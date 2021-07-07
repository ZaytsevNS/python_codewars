import unittest
import main


class TestMoveZeros(unittest.TestCase):
    def test_one(self):
        """ Should moves all of the zeros to the end, preserving the order of the other elements """
        self.assertEqual([1, 1, 2, 1, 3, 0, 0], main.move_zeros([1, 0, 1, 2, 0, 1, 3]))

        
if __name__ == '__main__':
    unittest.main()
