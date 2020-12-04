# Solution to part 2 of day 4 of AOC 2020, Passport Processing.
# https://adventofcode.com/2020/day/4

import sys
from passport_checker import PassportChecker

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]

f = open(filename)
whole_text = (f.read())

raw_passports = whole_text.split('\n\n')                    # Split by blank line.
if VERBOSE:
    print('raw_passports:', raw_passports)

passports = [x.replace('\n', ' ') for x in raw_passports]   # Standardise remaining newline into spaces.
if VERBOSE:
    print('passports:', passports)

passports_kv = [x.split(' ') for x in passports]
if VERBOSE:
    print('passports_kv:', passports_kv)

valid_passports = 0

pc = PassportChecker()

for each_passport in passports_kv:
    pass_dict = {}
    for each_kv in each_passport:
        if VERBOSE:
            print('each_kv:', each_kv)

        k, v = each_kv.split(':')

        if VERBOSE:
            print('k, v:', k, v)

        pass_dict[k] = v

    if pc.check_passport(pass_dict):
        valid_passports += 1


print('valid_passports:', valid_passports)
