# Solution to day 1 of AOC 2020, Report Repair.
# https://adventofcode.com/2020/day/1


f = open('input.txt')
whole_text = (f.read())
string_list = whole_text.split()                    # Split string by any whitespace.
number_list = [int(x) for x in string_list]         # Convert list of strings to list of integers.

for i in range(len(number_list)):

    for j in range(i + 1, len(number_list)):
        x = number_list[i]
        y = number_list[j]

        if x + y == 2020:
            print(x * y)
