import unittest
import main


class TestMakeReadable(unittest.TestCase):
    def test_one(self):
        """ Should returns the time in a human-readable format (HH:MM:SS) """
        self.assertEqual('00:00:00', main.make_readable(0))
        self.assertEqual('00:00:05', main.make_readable(5))
        self.assertEqual('00:01:00', main.make_readable(60))
        self.assertEqual('23:59:59', main.make_readable(86399))
        self.assertEqual('99:59:59', main.make_readable(359999))
        
if __name__ == '__main__':
    unittest.main()
