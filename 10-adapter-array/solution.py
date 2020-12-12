# Solution to day 10 of AOC 2020, Adapter Array.
# https://adventofcode.com/2020/day/10

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())
string_list = whole_text.split()                    # Split string by any whitespace.
nl = [int(x) for x in string_list]                  # Convert list of strings to list of integers.

if VERBOSE:
    print(nl)

j1, j3 = 0, 1                                       # Counts of number of 1 jolt deltas and 3 jolt deltas.
previous = 0

for a in sorted(nl):
    delta = a - previous
    if delta == 1:
        j1 += 1
    elif delta == 3:
        j3 += 1

    previous = a

if VERBOSE:
    print('j1, j3:', j1, j3)

print('Part 1:', j1 * j3)

# (k: v)
# Where k is the joltage, and v is the number of ways to stack adaptors to get to that joltage.
# Since the charging outlet by your seat has voltage of zero, we can seed the dictionary with,
ways = {0: 1}

for a in sorted(nl):

    # The number of ways to get to current joltage = ways to get to 1 jolt less than this joltage
    #                                                + ways to get to 2 jolts less than this joltage
    #                                                + ways to get to 3 jolts less than this joltage
    #
    # Here is a worked example for "small.txt",
    # 1   4   5   6   7   10   11   12   15   16   19
    # 1   1   1   1   1    4    4    4    8    8    8
    #             +   +              +
    #             1   1              4
    #             =   +              =
    #             2   2              8
    #                 =
    #                 4
    ways[a] = ways.get(a - 1, 0) + ways.get(a - 2, 0) + ways.get(a - 3, 0)

if VERBOSE:
    print('ways:', ways)

print('Part 2:', ways[max(ways)])
