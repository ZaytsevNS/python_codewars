import unittest
import main


class TestGenerateHashtag(unittest.TestCase):
    def test_one(self):
        """ Should return hashtag """
        self.assertEqual('#HelloThereThanksForTryingMyKata', main.generate_hashtag(' Hello there thanks for trying my Kata'))
        self.assertEqual('#HelloWorld', main.generate_hashtag('    Hello     World   '))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, main.generate_hashtag(''))
        
if __name__ == '__main__':
    unittest.main()
