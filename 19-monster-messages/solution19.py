# Solution to day 19 of AOC 2020, Monster Messages.
# https://adventofcode.com/2020/day/19

import sys
import re                                           # Regular expressions.

VERBOSE = ('-v' in sys.argv)


def rule_to_regex(rules: dict, rule_number: str) -> str:
    """For the parm rule number, return it is a regular expression."""

    rule = rules[rule_number]

    # Base case - single rule which resolves to a literal letter.
    if len(rule) == 1:
        if '"' in rule[0]:
            return rule[0].replace('"', '')         # For example, rule ['"a"'], returns regular expression 'a'.

    # One or more sub-rules.
    result = '('
    first = True
    for each_sub_rule in rule:

        # If there was a preceding sub-rule, delimit this new one with a pipe.
        if first:
            first = False                           # Next time around, this will no longer be the first.
        else:
            result += '|'

        # result += '('                             # Surround the sub-rule with brackets.

        # Each sub-rule is a string of rule numbers delimited with spaces. For example ['1 2 3'].
        for each_rule_num in each_sub_rule.split(' '):
            result += rule_to_regex(rules, rule_number=each_rule_num)

    result += ')'                                   # Close the brackets around this sub-rule.
    return result


def message_match_regexp(message: str, regexp: str) -> bool:
    """Returns true iff the parm message matches the parm regular expression."""

    return re.match('^'                             # The '^' ensures no leading characters.
                    + regexp
                    + '$', message) is not None     # The '$' ensures no trailing characters.


def main():
    filename = sys.argv[1]
    f = open(filename)
    whole_text = f.read()
    f.close()

    rules_raw, messages_raw = whole_text.split('\n\n')
    rules_list = rules_raw.split('\n')
    messages = messages_raw.split('\n')

    if VERBOSE:
        print('rules_list:', rules_list)
        print('messages:', messages)

    # k = rule number (string).
    # v = list of sub rules (strings) for that rule number.
    rules = {}
    for line in rules_list:
        rule_number, rule = line.split(': ')
        rules[rule_number] = rule.split(' | ')

    if VERBOSE:
        print('rules:', rules)

    regex = rule_to_regex(rules, rule_number='0')
    part1 = 0
    for message in messages:
        if message_match_regexp(message, regex):
            part1 += 1
    print('Part 1:', part1)


if __name__ == "__main__":
    main()
