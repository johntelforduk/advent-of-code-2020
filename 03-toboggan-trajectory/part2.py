# Solution to part 2 of day 3 of AOC 2020, Toboggan Trajectory.
# https://adventofcode.com/2020/day/3


f = open('input.txt')
whole_text = (f.read())
grid = whole_text.split()                               # Split string by any whitespace.

tree_product = 1

for delta_x, delta_y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:

    # Origin is top-left corner of grid (0, 0).
    row_num = 0
    col_num = 0

    trees = 0

    for this_row in grid[::delta_y]:                    # Use every 'delta_y'th element in grid.
        if row_num != 0:                                # First row is skipped.
            if this_row[col_num] == '#':
                trees += 1

        row_num += delta_y
        col_num = (col_num + delta_x) % len(this_row)   # Move right delta_x, and wrap around if end of grid.

    tree_product = tree_product * trees

print('Tree Product:', tree_product)
