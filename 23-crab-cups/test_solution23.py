# Unit tests for day 23 of AOC 2020, Crab Cups.

from solution23 import Game
import unittest


class TestFunctions(unittest.TestCase):

    def test_game_class(self):

        g1 = Game('389125467', 10)
        self.assertEqual(g1.current, '3')               # Current is first cup.
        self.assertEqual(g1.pick_up_1_cup(), '8')
        self.assertEqual(g1.cups, list('39125467'))
        g1.update_destination_cup()
        self.assertEqual(g1.destination, '2')

        g2 = Game('389125467', 10)
        g2.current = '7'                                # Force current to be last cup in the list.
        self.assertEqual(g2.current, '7')
        self.assertEqual(g2.pick_up_1_cup(), '3')
        self.assertEqual(g2.cups, list('89125467'))
        g2.update_destination_cup()
        self.assertEqual(g2.destination, '6')

        g3 = Game('389125467', 10)
        g3.current = '2'                                # Force current to be a mid-cup.
        self.assertEqual(g3.current, '2')
        self.assertEqual(g3.pick_up_1_cup(), '5')
        self.assertEqual(g3.cups, list('38912467'))

        g4 = Game('389125467', 10)
        self.assertEqual(g4.current, '3')               # Current is first cup.
        picked_up = g4.pick_up_cups(3)
        self.assertEqual(picked_up, '891')
        self.assertEqual(g4.cups, list('325467'))
        g4.update_destination_cup()
        self.assertEqual(g4.destination, '2')
        g4.insert_cups(inserts=picked_up, insert_after=g4.destination)
        self.assertEqual(g4.cups, list('328915467'))
        g4.select_new_current_cup()
        self.assertEqual(g4.current, '2')

        picked_up = g4.pick_up_cups(3)
        g4.update_destination_cup()
        g4.insert_cups(inserts=picked_up, insert_after=g4.destination)
        self.assertEqual(g4.cups, list('325467891'))
        g4.select_new_current_cup()
        self.assertEqual(g4.current, '5')

        g5 = Game('389125467', 10)
        g5.current = '6'                                # Force current to be the penultimate cup.
        self.assertEqual(g5.current, '6')
        self.assertEqual(g5.pick_up_cups(3), '738')
        self.assertEqual(g5.cups, list('912546'))

        g6 = Game('689125437', 10)
        g6.current = '7'
        self.assertEqual(g6.current, '7')
        picked_up = g6.pick_up_cups(3)
        self.assertEqual(picked_up, '689')
        self.assertEqual(g6.cups, list('125437'))
        g6.update_destination_cup()
        self.assertEqual(g6.destination, '5')
        g6.insert_cups(inserts=picked_up, insert_after=g6.destination)
        self.assertEqual(g6.cups, list('125689437'))
        g6.select_new_current_cup()
        self.assertEqual(g6.current, '1')

        g7 = Game('685219437', 10)
        g7.current = '2'
        self.assertEqual(g7.current, '2')
        picked_up = g7.pick_up_cups(3)
        self.assertEqual(picked_up, '194')
        self.assertEqual(g7.cups, list('685237'))
        g7.update_destination_cup()
        self.assertEqual(g7.destination, '8')
        g7.insert_cups(inserts=picked_up, insert_after=g7.destination)
        self.assertEqual(g7.cups, list('681945237'))
        g7.select_new_current_cup()
        self.assertEqual(g7.current, '3')


if __name__ == '__main__':
    unittest.main()
