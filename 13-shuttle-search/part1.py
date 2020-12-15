# Solution to part 1 of day 13 of AOC 2020, Shuttle Search.
# https://adventofcode.com/2020/day/13

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
two_lines = whole_text.split('\n')                     # Split string by any whitespace.
earliest = int(two_lines[0])

buses = []
for bus in two_lines[1].split(','):
    if bus != 'x':
        buses.append(int(bus))

if VERBOSE:
    print('earliest, buses', earliest, buses)

bus_wait = []                                       # Each item is (wait, bus).
for bus in buses:
    bus_wait.append((bus - earliest % bus, bus))

if VERBOSE:
    print('bus_wait', bus_wait)

wait, bus = min(bus_wait)
print('Part 1:', wait * bus)
