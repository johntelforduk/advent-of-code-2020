# Unit tests for day 20 of AOC 2020, Jurassic Jigsaw.

from solution20 import Tile
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        test_tile = Tile(tile_id=1877, grid=['##....#.#.',
                                             '....#.....',
                                             '....#..###',
                                             '##.......#',
                                             '...#......',
                                             '..........',
                                             '###..#.###',
                                             '#..##.##..',
                                             '.....#....',
                                             '.#..##.#..'])

        self.assertEqual(test_tile.find_match(edge='T', pattern='##....#.#.'), 0)   # 0 is 'O'
        self.assertEqual(test_tile.find_match(edge='T', pattern='.#..##.#..'), 4)   # 4 is 'OH'

        # This pattern does not exist in this tile.
        self.assertEqual(test_tile.find_match(edge='T', pattern='##.##.#.#.'), -1)

        self.assertEqual(test_tile.find_match(edge='B', pattern='.#..##.#..'), 0)   # 0 is 'O'
        self.assertEqual(test_tile.find_match(edge='B', pattern='...#..##..'), 1)   # 1 is 'OR'

        self.assertEqual(test_tile.find_match(edge='L', pattern='#..#..##..'), 0)   # 0 is 'O'

        self.assertEqual(test_tile.find_match(edge='R', pattern='..##..#...'), 0)   # 0 is 'O'
        self.assertEqual(test_tile.find_match(edge='R', pattern='##....#.#.'), 1)   # 0 is 'OR'
        self.assertEqual(test_tile.find_match(edge='R', pattern='#..#..##..'), 6)   # 8 is 'OHRR'


if __name__ == '__main__':
    unittest.main()
