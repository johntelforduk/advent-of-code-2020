# Solution to part 1 of day 12 of AOC 2020, Rain Risk.
# https://adventofcode.com/2020/day/12

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]


def positive_bearing(b: int):
    """Converts negative bearing to positive bearing. For example -90 (pointing West), becomes 270."""
    while b < 0:
        b += 360
    return b


f = open(filename)
whole_text = (f.read())
instructions = whole_text.split()                     # Split string by any whitespace.

if VERBOSE:
    print(instructions)

bearing = 90                                # "The ship starts by facing east."
x, y = 0, 0                                 # Ship starts at origin.

for command in instructions:
    action = command[0]
    value = int(command[1:])

    if action == 'N':
        y -= value
    elif action == 'S':
        y += value
    elif action == 'E':
        x += value
    elif action == 'W':
        x -= value
    elif action == 'L':
        bearing -= value
        bearing = positive_bearing(bearing)
    elif action == 'R':
        bearing = (bearing + value) % 360
    else:
        assert action == 'F'
        bearing_moves = {0: (0, -1),
                         90: (1, 0),
                         180: (0, 1),
                         270: (-1, 0)}
        dx, dy = bearing_moves[bearing]
        x = x + value * dx
        y = y + value * dy

    if VERBOSE:
        print('command, action, value:', command, action, value)
        print('x, y, bearing:', x, y, bearing)

print('Part 1:', abs(x) + abs(y))
