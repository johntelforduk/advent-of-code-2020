# Solution to part 1 of day 17 of AOC 2020, Conway Cubes.
# https://adventofcode.com/2020/day/17

import sys

VERBOSE = ('-v' in sys.argv)


class Pocket:

    def __init__(self, filename: str):
        """Create a new pocket dimension. Initialise the plane z=0 to contents of parm filename."""

        # Each member is a tuple (x, y, z) that represents an active cube in the pocket dimension.
        self.active_cubes = set()

        # The max and min planes (in 3 dimensions) where there are active cubes.
        self.min_x, self.max_x = 0, 0
        self.min_y, self.max_y = 0, 0
        self.min_z, self.max_z = 0, 0

        self.cycles = 0

        # Initialize the pocket dimension using data from file.
        f = open(filename)
        whole_text = f.read()
        f.close()

        x, y = 0, 0
        for row in whole_text.split('\n'):
            for col in row:
                if col == '#':
                    self.activate(x, y, 0)
                x += 1
            x = 0
            y += 1

    def reset(self):
        """Reset the pocket space to empty."""
        self.active_cubes = set()

        # The max and min planes (in 3 dimensions) where there are active cubes.
        self.min_x, self.max_x = 0, 0
        self.min_y, self.max_y = 0, 0
        self.min_z, self.max_z = 0, 0

    def activate(self, x: int, y: int, z: int):
        """Activate the cube at parm coordinates."""
        self.min_x = min(self.min_x, x)
        self.max_x = max(self.max_x, x)
        self.min_y = min(self.min_y, y)
        self.max_y = max(self.max_y, y)
        self.min_z = min(self.min_z, z)
        self.max_z = max(self.max_z, z)
        self.active_cubes.add((x, y, z))

    def print(self):
        """Print out the pocket dimension."""
        print('Cycles:', self.cycles)

        for z in range(self.min_z, self.max_z + 1):
            print('z:', z)

            for y in range(self.min_y, self.max_y + 1):
                for x in range(self.min_x, self.max_x + 1):
                    if (x, y, z) in self.active_cubes:
                        print('#', end='')
                    else:
                        print('.', end='')
                print()
            print()

    def cycle(self):
        """Iterate the pocket dimension through a cycle."""

        # "During a cycle, all cubes simultaneously change their state..."

        prev = self.active_cubes.copy()

        # Search a bit outside the current boundaries of active cubes for possible changes of cube state.
        search_x = range(self.min_x - 3, self.max_x + 3)
        search_y = range(self.min_y - 3, self.max_y + 3)
        search_z = range(self.min_z - 3, self.max_z + 3)

        # Reset the pocket space.
        self.active_cubes = set()
        self.min_x, self.max_x = 0, 0
        self.min_y, self.max_y = 0, 0
        self.min_z, self.max_z = 0, 0

        # Consider space around the current space.
        for x in search_x:
            for y in search_y:
                for z in search_z:
                    neighbors = 0

                    for dx in range(-1, 2):             # Look at the 26 possible positions around it...
                        for dy in range(-1, 2):
                            for dz in range(-1, 2):     # ...

                                # dx, dy, dz = (0, 0, 0) is the active cube we are examining, so ignore this combination
                                # of deltas.
                                if dx != 0 or dy != 0 or dz != 0:
                                    if (x + dx, y + dy, z + dz) in prev:
                                        neighbors += 1

                    # "If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active.
                    # Otherwise, the cube becomes inactive.
                    # If a cube is inactive but exactly 3 of its neighbors are active,
                    # the cube becomes active. Otherwise, the cube remains inactive."

                    if (x, y, z) in prev and 2 <= neighbors <= 3:
                        self.activate(x, y, z)
                    if (x, y, z) not in prev and neighbors == 3:
                        self.activate(x, y, z)
        self.cycles += 1


def main():
    filename = sys.argv[1]
    this_pocket = Pocket(filename)
    this_pocket.print()

    # "Starting with your given initial configuration, simulate six cycles."
    for cycle in range(6):
        this_pocket.cycle()
        this_pocket.print()

    print('Part 1:', len(this_pocket.active_cubes))


if __name__ == "__main__":
    main()
