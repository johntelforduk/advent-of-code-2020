# Unit tests for day 21 of AOC 2020, Allergen Assessment.

from solution21 import intersect_list
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(intersect_list([{'a', 'b', 'c'}, {'a', 'c'}]), 'None')
        self.assertEqual(intersect_list([{'a', 'b', 'c'}, {'c'}]), 'c')
        self.assertEqual(intersect_list([{'a', 'b', 'c'}, {'c'}, {'c', 'd'}]), 'c')
        self.assertEqual(intersect_list([{'a', 'b', 'c'}, {'c', 'e'}, {'c', 'e'}]), 'c')
        self.assertEqual(intersect_list([{'a', 'b'}, {'c', 'e'}, {'c', 'e'}]), 'None')


if __name__ == '__main__':
    unittest.main()
