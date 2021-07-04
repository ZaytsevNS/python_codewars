import unittest
import next_bigger as nb


class TestNextBigger(unittest.TestCase):
    def test_one(self):
        """ Should return next bigger """
        self.assertEqual(21, nb.next_bigger(12))
        self.assertEqual(531, nb.next_bigger(513))
        self.assertEqual(2071, nb.next_bigger(2017))

    def test_two(self):
        """ Should return -1 """
        self.assertEqual(-1, nb.next_bigger(9))
        self.assertEqual(-1, nb.next_bigger(111))
        self.assertEqual(-1, nb.next_bigger(531))

if __name__ == '__main__':
    unittest.main()
