# Unit tests for day 23 of AOC 2020, Crab Cups.

from solution23_2 import Game
import unittest


class TestFunctions(unittest.TestCase):

    def test_game_class(self):

        g1 = Game('389125467')
        self.assertEqual(g1.current, 3)               # Current is first cup.
        self.assertEqual(g1.pick_up_1_cup(), 8)
        self.assertEqual(g1.cups, [3, 9, 1, 2, 5, 4, 6, 7])
        g1.update_destination_cup()
        self.assertEqual(g1.destination, 2)

        g2 = Game('389125467')
        g2.current = 7                                # Force current to be last cup in the list.
        self.assertEqual(g2.current, 7)
        self.assertEqual(g2.pick_up_1_cup(), 3)
        self.assertEqual(g2.cups, [8, 9, 1, 2, 5, 4, 6, 7])
        g2.update_destination_cup()
        self.assertEqual(g2.destination, 6)

        g3 = Game('389125467')
        g3.current = 2                                # Force current to be a mid-cup.
        self.assertEqual(g3.current, 2)
        self.assertEqual(g3.pick_up_1_cup(), 5)
        self.assertEqual(g3.cups, [3, 8, 9, 1, 2, 4, 6, 7])

        g4 = Game('389125467')
        self.assertEqual(g4.current, 3)               # Current is first cup.
        picked_up = g4.pick_up_cups(3)
        self.assertEqual(picked_up, [8, 9, 1])
        self.assertEqual(g4.cups, [3, 2, 5, 4, 6, 7])
        g4.update_destination_cup()
        self.assertEqual(g4.destination, 2)
        g4.insert_cups(inserts=picked_up, insert_after=g4.destination)
        self.assertEqual(g4.cups, [3, 2, 8, 9, 1, 5, 4, 6, 7])
        g4.select_new_current_cup()
        self.assertEqual(g4.current, 2)

        picked_up = g4.pick_up_cups(3)
        g4.update_destination_cup()
        g4.insert_cups(inserts=picked_up, insert_after=g4.destination)
        self.assertEqual(g4.cups, [3, 2, 5, 4, 6, 7, 8, 9, 1])
        g4.select_new_current_cup()
        self.assertEqual(g4.current, 5)

        g5 = Game('389125467')
        g5.current = 6                                # Force current to be the penultimate cup.
        self.assertEqual(g5.current, 6)
        self.assertEqual(g5.pick_up_cups(3), [7, 3, 8])
        self.assertEqual(g5.cups, [9, 1, 2, 5, 4, 6])

        g6 = Game('689125437')
        g6.current = 7
        self.assertEqual(g6.current, 7)
        picked_up = g6.pick_up_cups(3)
        self.assertEqual(picked_up, [6, 8, 9])
        self.assertEqual(g6.cups, [1, 2, 5, 4, 3, 7])
        g6.update_destination_cup()
        self.assertEqual(g6.destination, 5)
        g6.insert_cups(inserts=picked_up, insert_after=g6.destination)
        self.assertEqual(g6.cups, [1, 2, 5, 6, 8, 9, 4, 3, 7])
        g6.select_new_current_cup()
        self.assertEqual(g6.current, 1)

        g7 = Game('685219437')
        g7.current = 2
        self.assertEqual(g7.current, 2)
        picked_up = g7.pick_up_cups(3)
        self.assertEqual(picked_up, [1, 9, 4])
        self.assertEqual(g7.cups, [6, 8, 5, 2, 3, 7])
        g7.update_destination_cup()
        self.assertEqual(g7.destination, 8)
        g7.insert_cups(inserts=picked_up, insert_after=g7.destination)
        self.assertEqual(g7.cups, [6, 8, 1, 9, 4, 5, 2, 3, 7])
        g7.select_new_current_cup()
        self.assertEqual(g7.current, 3)


if __name__ == '__main__':
    unittest.main()
