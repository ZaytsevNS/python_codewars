import unittest
import main as solution


class TestSolution(unittest.TestCase):
    def test_one(self):
        """ Should returns mean square error """
        self.assertEqual(9, solution.solution([1, 2, 3], [4, 5, 6]))
        self.assertEqual(16.5, solution.solution([10, 20, 10, 2], [10, 25, 5, -2]))
        self.assertEqual(1, solution.solution([-1, 0], [0, -1]))
       
if __name__ == '__main__':
    unittest.main()
