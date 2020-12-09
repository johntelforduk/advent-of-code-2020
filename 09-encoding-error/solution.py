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


def is_contiguous_sum(pl: list, target: int) -> int:
    """Searches parm list, summing integers starting from first item, and summing items in order trying to equal
    target. If target equals the contiguous sum, then it returns the sum of the max and min items in the sum.
    If contiguous sum fails, the function returns -1."""
    s = 0
    contig = []
    for i in pl:
        s += i
        contig.append(i)
        if s == target:
            return min(contig) + max(contig)
        if s > target:
            return -1
    return -1


filename = sys.argv[1]
preamble = int(sys.argv[2])

if VERBOSE:
    print('filename, preamble:', filename, preamble)

f = open(filename)
whole_text = (f.read())
f.close()
sl = whole_text.split()                     # Split string by any whitespace.
nl = [int(x) for x in sl]                   # Convert list of strings to list of integers.

if VERBOSE:
    print('nl:', nl)


# Part 1.
available = []                              # List of integers that are available for pairing.
p1 = None

for this_num in nl:
    if len(available) == preamble:
        if not is_pair_sum(pl=available, target=this_num):
            p1 = this_num
            print('Part 1:', p1)
            break

    available.append(this_num)

    if len(available) > preamble:
        available.pop(0)                    # Remove the oldest number from the list of available.

    if VERBOSE:
        print('available:', available)

# Part 2.
for start in range(len(nl)):
    if VERBOSE:
        print('start:', start)

    if VERBOSE:
        print('nl[start:], p1:', nl[start:], p1)

    x = is_contiguous_sum(nl[start:], target=p1)

    if x != -1:
        print('Part 2:', x)
        break
