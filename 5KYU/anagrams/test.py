import unittest
import main


class TestAnagrams(unittest.TestCase):
    def test_one(self):
        """ Should return an array of all the anagrams """
        self.assertEqual(['aabb', 'bbaa'], main.anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
        self.assertEqual(['carer', 'racer'], main.anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
        
    def test_two(self):
        """ Should return an empty array """
        self.assertEqual([], main.anagrams('laser', ['lazing', 'lazy',  'lacer']))

if __name__ == '__main__':
    unittest.main()
