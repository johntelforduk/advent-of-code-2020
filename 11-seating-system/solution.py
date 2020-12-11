# Solution to day 11 of AOC 2020, Seating System.
# https://adventofcode.com/2020/day/11

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]


def dump(m: list):
    """Print the contents of parm list to stdout."""
    for line in m:
        print(line)
    print()


def occupied(m: list, x, y) -> int:
    """Return 1 if the position (x, y) is occupied, or 0 if it is either outside of the map, or unoccupied."""
    if x == -1 or y == -1 or y == len(m):
        return 0
    if x == len(m[y]):
        return 0
    if m[y][x] == '#':
        return 1
    return 0


def adjacent(m: list, x, y) -> int:
    """Return count of number of occupied seats adjacent to a given seat (one of the eight positions immediately up,
    down, left, right, or diagonal from the seat)."""
    adj = 0
    for dx, dy in [(-1, -1), (0, -1), (1, -1),
                   (-1, 0),           (1, 0),
                   (-1, 1),  (0, 1),  (1, 1)]:
        adj += occupied(m, x + dx, y + dy)
    return adj


def see(m: list, x, y) -> int:
    """Return count of how many occupied seats can be seen when looking out from given seat position."""
    seen = 0

    # (dx, dy) is the current direction of gaze.
    for dx, dy in [(-1, -1), (0, -1), (1, -1),
                   (-1, 0),           (1, 0),
                   (-1, 1),  (0, 1),  (1, 1)]:
        check_x, check_y = x, y
        found = 'None'

        while found == 'None':
            # Continue looking in current gaze direction.
            check_x += dx
            check_y += dy

#            print(check_x, check_y)

            # Out of bounds checks.
            if check_x == -1 or check_y == -1 or check_y == len(m):
                found = 'Out'
            elif check_x == len(m[check_y]):
                found = 'Out'

            # Check if found either an occupied or empty seat.
            elif m[check_y][check_x] in ['#', 'L']:
                found = m[check_y][check_x]

        if found == '#':
            seen += 1

    return seen


def p1_tick(m: list) -> list:
    """For parm map, return next iteration of map."""
    nm = []                     # New map, at end of this tick.
    y = 0

    for r in m:                 # Rows.
        x = 0
        nr = ''                 # New row, starts as blank string.
        for c in r:             # Columns.
            # "If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied."
            if c == 'L' and adjacent(m, x, y) == 0:
                nr += '#'

            # "If a seat is occupied (#) and four or more seats adjacent to it are also occupied,
            # the seat becomes empty."
            elif c == '#' and adjacent(m, x, y) >= 4:
                nr += 'L'

            # "Otherwise, the seat's state does not change."
            else:
                nr += c

            x += 1
        nm.append(nr)

        # Start a new row
        y += 1

    return nm


def p2_tick(m: list) -> list:
    """For parm map, return next iteration of map."""
    nm = []                     # New map, at end of this tick.
    y = 0

    for r in m:                 # Rows.
        x = 0
        nr = ''                 # New row, starts as blank string.
        for c in r:             # Columns.
            # "If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied."
            if c == 'L' and see(m, x, y) == 0:
                nr += '#'

            # "... it now takes five or more visible occupied seats for an occupied seat to become empty."
            elif c == '#' and see(m, x, y) >= 5:
                nr += 'L'

            # "Otherwise, the seat's state does not change."
            else:
                nr += c

            x += 1
        nm.append(nr)

        # Start a new row
        y += 1

    return nm



def count_occupied(m: list) -> int:
    """Return how many seats are occupied in parameter map."""
    count = 0
    for r in m:
        for c in r:
            if c == '#':
                count += 1
    return count


def main():
    f = open(filename)
    whole_text = (f.read())
    p1_plan = whole_text.split()                    # Split string by any whitespace.
    p2_plan = p1_plan.copy()

    if VERBOSE:
        print('p1_plan', p1_plan)
        dump(p1_plan)

    prev = []

    while prev != p1_plan:
        prev = p1_plan.copy()
        p1_plan = p1_tick(p1_plan)

        if VERBOSE:
            dump(p1_plan)

    print('Part 1:', count_occupied(p1_plan))

    if VERBOSE:
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        dump(p2_plan)

    prev = []

    while prev != p2_plan:
        prev = p2_plan.copy()
        p2_plan = p2_tick(p2_plan)

        if VERBOSE:
            dump(p2_plan)

    print('Part 2:', count_occupied(p2_plan))


if __name__ == "__main__":
    # execute only if run as a script
    main()
