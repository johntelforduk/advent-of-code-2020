# Class for the handheld console computer in AOC day 8: Handheld Halting.

import sys

VERBOSE = ('-v' in sys.argv)


class Computer:

    def __init__(self):

        self.ac = 0                     # "The accumulator starts at 0."
        self.ip = 0                     # Instruction pointer.
        self.terminated = False         # Becomes true when the program is terminated.
        self.lines_of_code = 0          # Number of lines of code in the currently loaded program.

        # Each instruction is a k: v.
        # k = line number.
        # v = (operation, argument).
        # For example, this program,
        #         nop +0
        #         acc +1
        #         jmp +4
        # ... would be represented as,
        #         {0: ('nop', 0), 1: ('acc', 1), 2: ('jmp', 4)}
        self.program = {}

    def load(self, filename:str):
        """Load a program from parameter filename."""
        f = open(filename)
        whole_text = (f.read())
        f.close()

        program = whole_text.split('\n')              # Each line of code is delimited with newline.

        line_number = 0
        for line in program:
            operation, argument = line.split()
            self.program[line_number] = (operation, int(argument))
            line_number += 1

        self.lines_of_code = line_number

    def status(self):
        """Dump computer status to stdout."""
        print('ac:', self.ac, 'ip:', self.ip)

    def inc_ip(self):
        """(Usually after each instruction completed). Advance the instruction pointer to next line of the
        program."""
        # "The program is supposed to terminate by attempting to execute an instruction immediately after the last
        # instruction in the file."
        if self.ip >= (self.lines_of_code - 1):
            self.terminated = True
        else:
            self.ip += 1

    def acc(self, delta: int):
        """acc increases or decreases a single global value called the accumulator by the value given in the
        argument."""
        self.ac += delta

    def jmp(self, delta: int):
        """jmp jumps to a new instruction relative to itself."""
        self.ip += delta
        if self.ip >= (self.lines_of_code - 1):
            self.terminated = True

    def nop(self):
        """nop stands for No OPeration - it does nothing."""
        pass

    def tick(self):
        """Execute one operation in the program."""
        operation, argument = self.program[self.ip]

        if operation == 'acc':
            self.acc(delta=argument)
            self.inc_ip()
        elif operation == 'jmp':
            self.jmp(delta=argument)
        else:
            self.nop()
            self.inc_ip()
