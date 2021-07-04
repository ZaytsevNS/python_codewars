import unittest
import main


class TestPermutations(unittest.TestCase):
    def test_one(self):
        """ Should return permutations """
        self.assertEqual(['a'], main.permutations('a'))
        self.assertEqual(['ab', 'ba'], main.permutations('ab'))
        self.assertEqual(['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'], main.permutations('aabb'))

if __name__ == '__main__':
    unittest.main()
