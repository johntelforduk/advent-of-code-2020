# Unit tests for day 24 of AOC 2020, Lobby Layout.

from solution24 import text_to_directions
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(text_to_directions('esew'), ['e', 'se', 'w'])
        self.assertEqual(text_to_directions('nwwswee'), ['nw', 'w', 'sw', 'e', 'e'])


if __name__ == '__main__':
    unittest.main()
