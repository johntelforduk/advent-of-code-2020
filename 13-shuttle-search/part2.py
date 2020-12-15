# Solution to part 2 of day 13 of AOC 2020, Shuttle Search.
# https://adventofcode.com/2020/day/13

import sys
from math import gcd
from functools import reduce


def lcm(a: int , b: int) -> int:
    """Returns the least common multiple of the parm pair of numbers."""
    return a*b // gcd(a, b)


def get_lcm_for(your_list: list) -> int:
    """Returns the least common multiple for parm list of numbers."""
    return reduce(lambda x, y: lcm(x, y), your_list)


VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
two_lines = whole_text.split('\n')                      # Split string by any whitespace.


def departure(bus: int, time: int) -> bool:
    """For parm bus ID and time, return True iff the bus departs at that time."""
    if time % bus == 0:
        return True
    return False


buses = []                                              # Each item in the list is (bus, stagger).
stagger = 0                                             # How many minutes after first bus does this one depart.
for bus in two_lines[1].split(','):
    if bus != 'x':
        buses.append((int(bus), stagger))
    stagger += 1

if VERBOSE:
    print('buses', buses)

# Find the three highest bus IDs and remove them from the list of buses.
b1, s1 = max(buses)
buses.remove((b1, s1))
b2, s2 = max(buses)
buses.remove((b2, s2))
b3, s3 = max(buses)
buses.remove((b3, s3))

if VERBOSE:
    print('b1, s1, b2, s2, b3, s3, buses:', b1, s1, b2, s2, b3, s3, buses)


# Find the first time that the 3 biggest bus IDs have their staggers the right distance apart from each other.
candidate_time = 0
while True:
    if (departure(bus=b1, time=candidate_time + s1)
            and departure(bus=b2, time=candidate_time + s2)
            and departure(bus=b3, time=candidate_time + s3)):
        break
    candidate_time += 1

big_lcm = get_lcm_for([b1, b2, b3])

if VERBOSE:
    print('candidate_time, big_lcm:', candidate_time, big_lcm)

# So now we know, the solution time is someone where in the space,
# time = candidate_time + x * big_lcm
# where x is an integer.

solution_found = False

while not solution_found:
    solution_found = True           # Begin optimistically with each candidate time.

    # Test each of the remaining buses in turn.
    for bus, stagger in buses:
        if departure(bus, candidate_time + stagger) is False:
            solution_found = False

    if solution_found:
        break
    else:
        candidate_time += big_lcm             # Try the next possible time in the solution space.

print('Part 2:', candidate_time)
