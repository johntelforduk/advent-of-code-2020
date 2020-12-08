# Script to test the Computer class.

from computer import Computer
import unittest


class TestComputer(unittest.TestCase):

    def test_single_opcodes(self):
        comp = Computer()

        self.assertEqual(comp.ip, 0)
        comp.inc_ip()
        self.assertEqual(comp.ip, 1)
        comp.jmp(delta=12)
        self.assertEqual(comp.ip, 13)

        self.assertEqual(comp.ac, 0)
        comp.acc(delta=5)
        self.assertEqual(comp.ac, 5)
        comp.acc(delta=-7)
        self.assertEqual(comp.ac, -2)

    def test_small_program(self):
        comp = Computer()
        comp.load('small.txt')

        # These instructions are visited in this order:
        #
        # nop +0  | 1
        # acc +1  | 2, 8(!)
        # jmp +4  | 3
        # acc +3  | 6
        # jmp -3  | 7
        # acc -99 |
        # acc +1  | 4
        # jmp -4  | 5
        # acc +6  |

        self.assertEqual(comp.lines_of_code, 9)       # This program has 9 lines of code.

        for expected_ip in [0, 1, 2, 6, 7, 3, 4, 1]:
            self.assertEqual(comp.ip, expected_ip)
            comp.tick()


if __name__ == '__main__':
    unittest.main()
