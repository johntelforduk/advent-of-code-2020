# Unit tests for day 19 of AOC 2020, Monster Messages.

from solution19 import rule_to_regex, message_match_regexp
import unittest


class TestFunctions(unittest.TestCase):

    def test_functions(self):

        test_regex = rule_to_regex(rules={'0': ['"a"']}, rule_number='0')
        self.assertEqual(test_regex, 'a')
        self.assertTrue(message_match_regexp(message='a', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='b', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='ab', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='ba', regexp=test_regex))

        test_regex = rule_to_regex(rules={'0': ['1 2 3'], '1': ['4 5'], '4': ['"a"'],
                                          '5': ['"b"'], '2': ['"c"'], '3': ['"d"']},
                                   rule_number='0')
        self.assertTrue(message_match_regexp(message='abcd', regexp=test_regex))

        test_regex = rule_to_regex(rules={'0': ['1 2'], '1': ['"a"'], '2': ['1 3', '3 1'], '3': ['"b"']},
                                   rule_number='0')
        self.assertTrue(message_match_regexp(message='aab', regexp=test_regex))
        self.assertTrue(message_match_regexp(message='aba', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='baa', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='abb', regexp=test_regex))

        test_regex = rule_to_regex(rules={'0': ['4 1 5'], '1': ['2 3', '3 2'], '2': ['4 4', '5 5'],
                                          '3': ['4 5', '5 4'], '4': ['"a"'], '5': ['"b"']},
                                   rule_number='0')
        self.assertTrue(message_match_regexp(message='ababbb', regexp=test_regex))
        self.assertTrue(message_match_regexp(message='abbbab', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='bababa', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='aaabbb', regexp=test_regex))
        self.assertFalse(message_match_regexp(message='aaaabbb', regexp=test_regex))


if __name__ == '__main__':
    unittest.main()
