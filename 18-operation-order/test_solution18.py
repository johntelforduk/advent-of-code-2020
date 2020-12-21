# Unit tests for day 18 of AOC 2020, Operation Order.

from solution18 import evaluate_left_to_right, inner_brackets, inner_brackets_to_value, evaluate_part1, \
    evaluate_one_operation, evaluate_part2
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        self.assertEqual(evaluate_left_to_right('1 + 2 * 3 + 4 * 5 + 6'), 71)

        self.assertEqual(inner_brackets('1 + (2 * 3) + (4 * (5 + 6))'), (4, 10))
        self.assertEqual(inner_brackets('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), (29, 39))
        self.assertEqual(inner_brackets('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), (1, 11))

        self.assertEqual(inner_brackets_to_value('1 + (2 * 3) + (4 * (5 + 6))', 'l_to_r'), '1 + 6 + (4 * (5 + 6))')

        self.assertEqual(evaluate_part1('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(evaluate_part1('2 * 3 + (4 * 5)'), 26)
        self.assertEqual(evaluate_part1('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
        self.assertEqual(evaluate_part1('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12240)
        self.assertEqual(evaluate_part1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13632)

        self.assertEqual(evaluate_one_operation('1 + 2 * 3 + 4 * 5 + 6', operator='+'), '3 * 3 + 4 * 5 + 6')
        self.assertEqual(evaluate_one_operation('1 + 2 * 3 + 4 * 5 + 6', operator='*'), '1 + 6 + 4 * 5 + 6')

        self.assertEqual(evaluate_part2('1 + 2 * 3 + 4 * 5 + 6'), 231)
        self.assertEqual(evaluate_part2('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(evaluate_part2('2 * 3 + (4 * 5)'), 46)
        self.assertEqual(evaluate_part2('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 1445)
        self.assertEqual(evaluate_part2('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 669060)
        self.assertEqual(evaluate_part2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 23340)


if __name__ == '__main__':
    unittest.main()
