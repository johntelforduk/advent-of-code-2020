# Solution to part 2 of day 8 of AOC 2020, Handheld Halting.
# https://adventofcode.com/2020/day/8

import sys
from computer import Computer

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

for flip, flop in [('jmp', 'nop'), ('nop', 'jmp')]:
    if VERBOSE:
        print(flip, flop)
    change_line = 0

    done = False

    while not done:
        if VERBOSE:
            print('----')
            print(change_line)
        comp = Computer()
        comp.load(filename)

        this_op, this_arg = comp.program[change_line]

        if VERBOSE:
            print(comp.program[change_line])
        if this_op == flip:
            comp.program[change_line] = (flop, this_arg)

        if VERBOSE:
            print(comp.program[change_line])

        previous_instructions = []
        while True:
            if VERBOSE:
                comp.status()
            if comp.ip in previous_instructions or comp.terminated:
                break
            previous_instructions.append(comp.ip)
            comp.tick()

        if comp.terminated:
            comp.status()

        change_line += 1
        if change_line == comp.lines_of_code:
            done = True
