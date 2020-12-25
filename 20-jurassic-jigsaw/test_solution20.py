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

        self.assertEqual(test_tile.top_match(pattern='##....#.#.'), 0)   # 0 is 'O'
        self.assertEqual(test_tile.top_match(pattern='.#..##.#..'), 4)   # 4 is 'OH'

        # This pattern does not exist in this tile.
        self.assertEqual(test_tile.top_match(pattern='##.##.#.#.'), -1)

        self.assertEqual(test_tile.left_match(pattern='#..#..##..'), 0)   # 0 is 'O'

        self.assertEqual(test_tile.left_and_top_match(left_pattern='#..#..##..', top_pattern='##....#.#.'), 0)


if __name__ == '__main__':
    unittest.main()
