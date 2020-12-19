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
    l1, u1 = raw_range1.split('-')                                  # First pair of lower and upper range bounds.
    l2, u2 = raw_range2.split('-')                                  # Second pair of lower and upper range bounds.
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
valid_tickets = []

for ticket in nearby_tickets:
    valid = True
    for data in ticket:
        in_range = False
        for field, l1, u1, l2, u2 in rules:
            if l1 <= data <= u1 or l2 <= data <= u2:
                in_range = True
                break
        if not in_range:
            error_rate += data
            valid = False
    if valid:
        valid_tickets.append(ticket)

if VERBOSE:
    print('valid_tickets:', valid_tickets)

print('Part 1:', error_rate)

# -----------------------------------------------------------------------

# For both of these lists, each item is (field name, position number)
possible = []           # Item in this list means that no data is invalid if this field is at this position.
solution = []           # Item in this list means that this field in this position is definitely part of the solution.

# Initialise the 'possible' list. Items will be removed from it whenever fields are placed in positions.
for field, l1, u1, l2, u2 in rules:
    for position in range(len(rules)):
        valid = True
        for ticket in valid_tickets:
            if VERBOSE:
                print('field, position, ticket:', field, position, ticket)

            if not (l1 <= ticket[position] <= u1 or l2 <= ticket[position] <= u2):
                valid = False
                break
        if valid:
            possible.append((field, position))
            # fields.append(field)

while len(possible) != 0:           # Empty possible list means work is done.

    # Fields is like 'possible', but with position part of tuple removed.
    # For example, possible = [('class', 1), ('row', 0), ('row', 1)], makes fields = ['class', 'row', 'row']
    # This means that counting occurrences of items in 'fields', tells you how often the first item in each tuple
    # in 'possible' occurs.
    fields = []
    for field, _ in possible:
        fields.append(field)

    if VERBOSE:
        print('possible, fields:', possible, fields)

    pos = 0
    for field, _, _, _, _ in rules:
        if fields.count(field) == 1:
            for f, pos in possible:
                if f == field:
                    solution.append((f, pos))
                    break

            possible.remove((f, pos))

            # Remove this position from possible for other fields.
            for f, del_pos in possible:
                if del_pos == pos:
                    possible.remove((f, del_pos))

    if VERBOSE:
        print('solution, possible:', solution, possible)

    # "look for the six fields on your ticket that start with the word departure.
    # What do you get if you multiply those six values together?"
    if VERBOSE:
        print('my_ticket_text', my_ticket_text)

    _, my_fields = my_ticket_text.split('\n')

    my_values = []
    for each_number in my_fields.split(','):
        my_values.append(int(each_number))

    if VERBOSE:
        print('my_values:', my_values)

    part2 = 1
    for field, position in solution:
        if field[0:9] == 'departure':
            if VERBOSE:
                print('field, position:', field, 1 + position)

            part2 *= my_values[position]

    print('Part 2:', part2)
