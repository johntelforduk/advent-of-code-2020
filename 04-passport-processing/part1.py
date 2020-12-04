# Solution to part 1 of day 4 of AOC 2020, Passport Processing.
# https://adventofcode.com/2020/day/4

import sys

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

# Make list of passports. Each passport is a dictionary of passport attributes.
passport_dicts = []
for each_passport in passports_kv:
    pass_dict = {}
    for each_kv in each_passport:
        if VERBOSE:
            print('each_kv:', each_kv)


        k, v = each_kv.split(':')

        if VERBOSE:
            print('k, v:', k, v)

        pass_dict[k] = v
    passport_dicts.append(pass_dict)

if VERBOSE:
    print('passport_dicts', passport_dicts)

valid_passports = 0

required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


for each_passport in passport_dicts:
    key_count = 0
    for check_key in required_keys:
        if check_key in each_passport:
            key_count += 1

    if key_count == 7:
        valid_passports += 1

print('valid_passports', valid_passports)
