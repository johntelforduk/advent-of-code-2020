# Solution to day 5 of AOC 2020, Binary Boarding.
# https://adventofcode.com/2020/day/5

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())

passes = whole_text.split()                      # Split by any whitespace.
seats = []

for each_pass in passes:
    row, col = 0, 0

    for letter in each_pass:

        if letter in ['L', 'R']:
            col = col * 2
        else:
            row = row * 2
        if letter == 'R':
            col = col + 1
        if letter == 'B':
            row = row + 1

    seat_id = row * 8 + col
    if VERBOSE:
        print('each_pass, row, col, seat_id:', each_pass, row, col, seat_id)

    seats.append(seat_id)

print('Part 1:', max(seats))

prev = None
for x in sorted(seats):
    if prev is not None and prev != x - 1:
        print('Part 2:', x - 1)
    prev = x
