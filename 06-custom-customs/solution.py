# Solution to day 6 of AOC 2020, Custom Customs.
# https://adventofcode.com/2020/day/6

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
f.close()

groups = whole_text.split('\n\n')                   # Start of each group is indicated by a blank line.
if VERBOSE:
    print('groups:', groups)

part1, part2 = 0, 0

for each_group in groups:
    this_count = 0
    question_union = set()                          # Make an empty set.
    question_intersection = set()
    person = set()
    person_num = 1                                  # Number of the person in each group.

    for each_question in each_group:
        if each_question == '\n':                   # Newline indicates a new person.
            if person_num == 1:                     # First person in the group initialises the intersection set.
                question_intersection = person
            else:
                question_intersection = question_intersection.intersection(person)
            person = set()                          # It's a new person, so reset the person set.
            person_num += 1
        else:
            question_union.add(each_question)
            person.add(each_question)

    if person_num == 1:                             # Make sure to add the last person.
        question_intersection = person
    else:
        question_intersection = question_intersection.intersection(person)

    if VERBOSE:
        print('-------------')
        print('each_group:', each_group)
        print('question_intersection:', question_intersection)

    part1 += len(question_union)
    part2 += len(question_intersection)

print('Part 1:', part1)
print('Part 2:', part2)
