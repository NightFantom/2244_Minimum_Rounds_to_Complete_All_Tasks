from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_solve_1(self):
        array = [2, 2, 3, 3, 2, 4, 4, 4, 4, 4]
        expected = 4
        result = Solution().minimumRounds(array)
        self.assertEqual(expected, result)

    def test_solve_2(self):
        array = [2, 3, 3]
        expected = -1
        result = Solution().minimumRounds(array)
        self.assertEqual(expected, result)

    def test_solve_3(self):
        array = [2]
        expected = -1
        result = Solution().minimumRounds(array)
        self.assertEqual(expected, result)

    def test_solve_4(self):
        array = [2, 2, 2, 2, 2, 2, 2]
        expected = 3
        result = Solution().minimumRounds(array)
        self.assertEqual(expected, result)
