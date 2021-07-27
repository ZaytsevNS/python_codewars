import unittest
import main as to_RGB


class TestHexStringToRGB(unittest.TestCase):
    def test_one(self):
        """ Should returns RGB dict """
        self.assertEqual({'r':255, 'g':153, 'b':51}, to_RGB.hex_string_to_RGB("#FF9933"))
        self.assertEqual({'r':190, 'g':173, 'b':237}, to_RGB.hex_string_to_RGB("#beaded"))
        self.assertEqual({'r':0, 'g':0, 'b':0}, to_RGB.hex_string_to_RGB("#000000"))
        self.assertEqual({'r':17, 'g':17, 'b':17}, to_RGB.hex_string_to_RGB("#111111"))
        self.assertEqual({'r':250, 'g':52, 'b':86}, to_RGB.hex_string_to_RGB("#Fa3456"))
        
    def test_one(self):
        """ Should returns empty dict """    
        self.assertEqual({}, to_RGB.hex_string_to_RGB("#FF"))
        self.assertEqual({}, to_RGB.hex_string_to_RGB("1234"))
        
        
if __name__ == '__main__':
    unittest.main()
