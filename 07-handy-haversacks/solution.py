# Solution to day 7 of AOC 2020, Handy Haversacks.
# https://adventofcode.com/2020/day/7

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]


def search_for_shiny_gold(root: str) -> int:
    """Search a tree of bags. Return the number of shiny gold bags it contains."""
    if VERBOSE:
        print('root, rule_dict[root]:', root, rule_dict[root])

    if len(rule_dict[root]) == 0:               # If value is empty list...
        return 0                                # ... there are no shiny gold bags in this tree.

    shiny_gold_inside = 0
    for each_inside, num_inside in rule_dict[root]:
        if each_inside == 'shiny gold':
            shiny_gold_inside = num_inside
        else:
            shiny_gold_inside += search_for_shiny_gold(each_inside)
    return shiny_gold_inside


def search_inside(root: str) -> int:
    """Search a tree of bags. Return the total number of bags it contains."""
    if VERBOSE:
        print('root, rule_dict[root]:', root, rule_dict[root])

    if len(rule_dict[root]) == 0:               # If value is empty list...
        return 0                                # ... there are no bags this tree.

    total_inside = 0
    for each_inside, num_inside in rule_dict[root]:
        total_inside += num_inside + num_inside * search_inside(each_inside)

    return total_inside


f = open(filename)
whole_text = (f.read())
f.close()

rules = whole_text.split('\n')                   # Start of each group is indicated by a blank line.
if VERBOSE:
    print('rules:', rules)

# Dictionary contains k: v pairs, one pair per rule.
# k = bag that the rule is about, eg. "light red".
# v = Empty list if bag contains no other bags. Otherwise, contains list of tuples (b, n), where b is bag inside key
# bag, and v is number of those bags.
#
# For example, "light red bags contain 1 bright white bag, 2 muted yellow bags."
# {'light red': [('bright white', 1), ('muted yellow', 2)}
#
# Another example,
# "dotted black bags contain no other bags."
# {'dotted black': []}
rule_dict = {}

for each_rule in rules:
    words = each_rule.split()

    # First 2 words are the name of the bag that the rules is about.
    k = words[0] + ' ' + words[1]

    if VERBOSE:
        print('each_rule, words, k:', each_rule, words, k)

    v = []
    if each_rule[-22:] != 'contain no other bags.':
        four_words = []
        for i in words[4:]:
            four_words.append(i)

            # if VERBOSE:
            #     print('each_rule, i, four_words:', each_rule, i, four_words)

            if len(four_words) == 4:
                v.append((four_words[1] + ' ' + four_words[2], int(four_words[0])))
                four_words = []

    rule_dict[k] = v

if VERBOSE:
    print('rule_dict, len(rule_dict)', rule_dict, len(rule_dict))

shiny_gold = 0
for k in rule_dict:
    if search_for_shiny_gold(k) > 0:
        shiny_gold += 1

print('Part 1:', shiny_gold)

print('Part 2:', search_inside(root='shiny gold'))
