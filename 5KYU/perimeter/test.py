import unittest
import main


class TestPerimeter(unittest.TestCase):
    def test_one(self):
        """ Should returns perimeter of squares in a rectangle """
        self.assertEqual(80, main.perimeter(5))
        self.assertEqual(216, main.perimeter(7))
        
if __name__ == '__main__':
    unittest.main()
