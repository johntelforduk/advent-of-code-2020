# Solution to part 1 of day 8 of AOC 2020, Handheld Halting.
# https://adventofcode.com/2020/day/8

import sys
from console.computer import Computer

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

comp = Computer()
comp.load(filename)

previous_instructions = []
while True:
    if comp.ip in previous_instructions:
        break
    previous_instructions.append(comp.ip)
    comp.tick()

comp.status()
