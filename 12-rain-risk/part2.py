# Solution to part 2 of day 12 of AOC 2020, Rain Risk.
# https://adventofcode.com/2020/day/12

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
instructions = whole_text.split()                     # Split string by any whitespace.

if VERBOSE:
    print(instructions)

x, y = 0, 0                                 # Ship starts at origin.

# "The waypoint starts 10 units east and 1 unit north relative to the ship."
wx, wy = 10, -1

for command in instructions:
    action = command[0]
    value = int(command[1:])

    if action == 'N':
        wy -= value
    elif action == 'S':
        wy += value
    elif action == 'E':
        wx += value
    elif action == 'W':
        wx -= value
    elif action == 'L':
        while value > 0:
            wx, wy = wy, -wx
            value -= 90
    elif action == 'R':
        while value > 0:
            wx, wy = -wy, wx
            value -= 90
    else:
        assert action == 'F'
        x += value * wx
        y += value * wy

    if VERBOSE:
        print('command, x, y, wx, wy:', command, x, y, wx, wy)

print('Part 2:', abs(x) + abs(y))
