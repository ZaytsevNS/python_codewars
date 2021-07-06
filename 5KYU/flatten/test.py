import unittest
import main


class TestFlatten(unittest.TestCase):
    def test_one(self):
        """ Should return flattens arguments into a single array """
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], main.flatten(1, [2, 3], 4, 5, [6, [7]]))
        self.assertEqual(['a', 'b', 2, 3, None, 4, 'c'], main.flatten('a', ['b', 2], 3, None, [[4], ['c']]))
        
if __name__ == '__main__':
    unittest.main()
