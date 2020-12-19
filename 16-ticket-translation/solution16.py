# Solution to day 16 of AOC 2020, Ticket Translation.
# https://adventofcode.com/2020/day/16

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
f.close()

[rule_text, my_ticket_text, nearby_tickets_text] = whole_text.split('\n\n')

rules = []
for raw_rule in rule_text.split('\n'):
    field, raw_ranges = raw_rule.split(': ')


    raw_range1, _, raw_range2 = raw_ranges.split(' ')




    l1, u1 = raw_range1.split('-')      # First pair of lower and upper range bounds.
    l2, u2 = raw_range2.split('-')      # Second pair of lower and upper range bounds.
    rules.append((field, int(l1), int(u1), int(l2), int(u2)))

if VERBOSE:
    print('rules:', rules)

nearby_tickets = []
for raw_nearby_tickets in nearby_tickets_text.split('\n')[1:]:      # Omit first row, which is boilerplate.
    this_ticket = []
    for data in raw_nearby_tickets.split(','):
        this_ticket.append(int(data))
    nearby_tickets.append(this_ticket)

if VERBOSE:
    print('nearby_tickets:', nearby_tickets)

error_rate = 0

for ticket in nearby_tickets:
    for data in ticket:
        in_range = False
        for field, l1, u1, l2, u2 in rules:
            if l1 <= data <= u1 or l2 <= data <= u2:
                in_range = True
                break
        if not in_range:
            error_rate += data

print('Part 1:', error_rate)
