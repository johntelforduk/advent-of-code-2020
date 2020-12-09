# Solution to day 9 of AOC 2020, Encoding Error.
# https://adventofcode.com/2020/day/9

import sys

VERBOSE = ('-v' in sys.argv)


def is_pair_sum(pl: list, target: int) -> bool:
    """Returns True iff target can be made by summing 2 different integers in pl."""
    for i in range(len(pl)):
        for j in range(len(pl)):
            if i != j:
                if pl[i] + pl[j] == target:
                    return True
    return False


filename = sys.argv[1]
preamble = int(sys.argv[2])

if VERBOSE:
    print('filename, preamble:', filename, preamble)

f = open(filename)
whole_text = (f.read())
f.close()
sl = whole_text.split()                    # Split string by any whitespace.
nl = [int(x) for x in sl]                  # Convert list of strings to list of integers.

if VERBOSE:
    print('nl:', nl)

available = []                              # List of integers that are available for pairing.

for this_num in nl:
    if len(available) == preamble:
        if not is_pair_sum(pl=available, target=this_num):
            print('Part 1:', this_num)
            break

    available.append(this_num)

    if len(available) > preamble:
        available.pop(0)                    # Remove the oldest number from the list of available.

    if VERBOSE:
        print('available:', available)
