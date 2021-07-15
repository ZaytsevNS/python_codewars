import unittest
import main


class TestRGB(unittest.TestCase):
    def test_one(self):
        """ testing zero values """
        self.assertEqual("000000", main.rgb(0, 0, 0))
    def test_two(self):
        """ testing near zero values """
        self.assertEqual("010203", main.rgb(1, 2, 3))
    def test_three(self):
        """ testing max values """
        self.assertEqual("FFFFFF", main.rgb(255, 255, 255))
    def test_four(self):
        """ testing near max values """
        self.assertEqual("FEFDFC", main.rgb(254, 253, 252))
    def test_five(self):
        """ testing out of range values """
        self.assertEqual("00FF7D", main.rgb(-20, 275, 125))
        
if __name__ == '__main__':
    unittest.main()
