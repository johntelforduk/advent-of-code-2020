# Unit tests for part 1 of day 23 of AOC 2020, Crab Cups.

from solution23_2 import Game
import unittest


class TestFunctions(unittest.TestCase):

    def test_game_class(self):

        g1 = Game()
        self.assertEqual(g1.cups, {})           # Starts with no cups.
        g1.insert_cup(cup=3, insert_after=0)
        self.assertEqual(g1.cups, {3: (3, 3)})
        self.assertEqual(g1.max_label, 3)
        self.assertEqual(g1.current, 3)         # First cup inserted into the circle is designated as the current cup.
        g1.insert_cup(cup=8, insert_after=3)
        self.assertEqual(g1.cups, {3: (8, 8), 8: (3, 3)})
        self.assertEqual(g1.max_label, 8)
        self.assertEqual(g1.current, 3)         # Current cup is changed just by inserting more cups.
        g1.insert_cup(cup=9, insert_after=8)
        self.assertEqual(g1.cups, {3: (9, 8), 8: (3, 9), 9: (8, 3)})
        self.assertEqual(g1.max_label, 9)
        g1.insert_cup(cup=1, insert_after=9)
        self.assertEqual(g1.max_label, 9)

        g2 = Game()
        g2.insert_cups(inserts=[3], insert_after=0)
        g2.insert_cups(inserts=[8, 9], insert_after=3)
        self.assertEqual(g2.cups, {3: (9, 8), 8: (3, 9), 9: (8, 3)})
        self.assertEqual(g1.current, 3)
        self.assertEqual(g2.pick_up_1_cup(), 8)
        self.assertEqual(g2.cups, {3: (9, 9), 9: (3, 3)})
        self.assertEqual(g2.max_label, 9)

        g3 = Game()
        g3.cups_from_text('389')
        self.assertEqual(g3.cups, {3: (9, 8), 8: (3, 9), 9: (8, 3)})
        self.assertEqual(g3.max_label, 9)
        self.assertEqual(g3.current, 3)
        g3.select_new_current_cup()
        self.assertEqual(g3.current, 8)
        g3.select_new_current_cup()
        self.assertEqual(g3.current, 9)
        g3.select_new_current_cup()             # Rotate the current back to start.
        self.assertEqual(g3.current, 3)

        g4 = Game()
        g4.cups_from_text('389125467')
        self.assertEqual(len(g4.cups), 9)
        self.assertEqual(g4.current, 3)
        self.assertEqual(g4.max_label, 9)
        self.assertEqual(g4.pick_up_1_cup(), 8)
        self.assertEqual(g4.pick_up_1_cup(), 9)
        self.assertEqual(g4.pick_up_1_cup(), 1)
        self.assertEqual(g4.max_label, 7)

        g5 = Game()
        g5.cups_from_text('389125467')
        self.assertEqual(len(g5.cups), 9)
        self.assertEqual(g5.pick_up_cups(3), [8, 9, 1])     # Left in the circle '325467'.
        self.assertEqual(len(g5.cups), 6)
        g5.update_destination_cup()
        self.assertEqual(g5.destination, 2)
        g5.select_new_current_cup()
        self.assertEqual(g5.current, 2)
        g5.update_destination_cup()
        self.assertEqual(g5.destination, 7)

        g6 = Game()
        g6.cups_from_text('389125467')
        self.assertEqual(len(g6.cups), 9)
        g6.insert_many_cups(previous_cup=7, highest=20)
        self.assertEqual(len(g6.cups), 20)
        self.assertEqual(max(g6.cups), 20)


if __name__ == '__main__':
    unittest.main()
