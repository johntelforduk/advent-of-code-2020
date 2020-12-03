# Solution to day 3 of AOC 2020, Toboggan Trajectory.
# https://adventofcode.com/2020/day/3


f = open('input.txt')
whole_text = (f.read())
grid = whole_text.split()                           # Split string by any whitespace.

# Origin is top-left corner of grid (0, 0).
row_num = 0
col_num = 0

trees = 0

for this_row in grid:
    if row_num != 0:                                # First row is skipped.
        if this_row[col_num] == '#':
            trees += 1

    row_num += 1
    col_num = (col_num + 3) % len(this_row)         # Move right 3, and wrap around if end of grid.

print('Trees:', trees)
