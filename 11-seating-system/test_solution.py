# Tests for day 11 of AOC 2020, Seating System.

from solution import *
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):
        # Key,
        #      '#' = Occupied seat.
        #      'L' = Empty seat.
        #      '.' = Floor.

        m = ['#.L',
             '#LL',
             'L.L']

        # Test for positions that are outside of the map.
        self.assertEqual(occupied(m, -1, -1), 0)
        self.assertEqual(occupied(m, 0, -1), 0)
        self.assertEqual(occupied(m, -1, 0), 0)
        self.assertEqual(occupied(m, 3, 1), 0)
        self.assertEqual(occupied(m, 1, 3), 0)

        # Test positions inside the map.
        self.assertEqual(occupied(m, 0, 0), 1)              # Contains '#'
        self.assertEqual(occupied(m, 1, 0), 0)              # Contains '.'
        self.assertEqual(occupied(m, 1, 1), 0)              # Contains 'L'

        self.assertEqual(adjacent(m, 0, 0), 1)
        self.assertEqual(adjacent(m, 1, 1), 2)
        self.assertEqual(adjacent(m, 2, 2), 0)

        self.assertEqual(count_occupied(m), 2)


if __name__ == '__main__':
    unittest.main()
