# Unit tests for day 15 of AOC 2020, Docking Data.

from solution15 import game
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(game(spoken=[0, 3, 6], rounds=10), 0)
        self.assertEqual(game(spoken=[1, 3, 2], rounds=2020), 1)
        self.assertEqual(game(spoken=[2, 1, 3], rounds=2020), 10)
        self.assertEqual(game(spoken=[1, 2, 3], rounds=2020), 27)
        self.assertEqual(game(spoken=[2, 3, 1], rounds=2020), 78)
        self.assertEqual(game(spoken=[3, 2, 1], rounds=2020), 438)
        self.assertEqual(game(spoken=[3, 2, 1], rounds=2020), 438)
        self.assertEqual(game(spoken=[3, 1, 2], rounds=2020), 1836)


if __name__ == '__main__':
    unittest.main()
