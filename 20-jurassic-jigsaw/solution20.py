# Solution to day 20 of AOC 2020, Monster Messages.
# https://adventofcode.com/2020/day/20

import sys
from math import sqrt

VERBOSE = ('-v' in sys.argv)


class Tile:

    def __init__(self, tile_id: int, grid: list):

        self.tile_id = tile_id
        self.original_grid = grid  # The non-variant grid for this tile.

        # List of names of the rotated and flipped variants that the tile has.
        # For example ['O', 'OR', 'ORR', ..., 'OH', 'OHR', ... 'OV', 'OVR', 'OVRR', ... 'OHV', 'OHVR', 'OHVRR', ...]
        # Where,
        # O = Original grid, ie. before variations.
        # R = Rotate right 90 degrees.
        # H = Flip along horizontal axis.
        # V = Flip along horizontal axis.
        self.variant_names = []

        self.current_variant = 'O'              # Name of the current variant. First variant is always 'O' (original).

        self.current_variant_grid = grid.copy()
        self.variant_grids = []                     # List of grids for each variant.


        # List of edges. One item in list for each variant.
        self.top, self.right, self.bottom, self.left = [], [], [], []

        self.snapshot_variant()  # Take snapshot of the original grid.

        # Start calculating the variants of this tile.
        for flips in ['', 'H', 'V', 'HV']:
            self.reset_variant()

            if 'H' in flips:
                self.flip_horizontal()
            if 'V' in flips:
                self.flip_vertical()

            for i in range(3):  # Original grid plus 3 rotations, gives 4 orientations.
                self.rotate_right()

        # Number of selected variant.
        # 0 = 'O', 1 = 'OR', 2 = 'ORR', 3 = 'ORRR', 4 = 'OH', etc.
        self.chosen_variant = 0

    def snapshot_variant(self):
        """For the current variant of the tile. Take a snapshot of it's name and it's edges."""

        left = ''
        right = ''
        for row in self.current_variant_grid:
            left += row[0]
            right += row[9]

        self.variant_names.append(self.current_variant)
        self.variant_grids.append(self.current_variant_grid)
        self.top.append(self.current_variant_grid[0])
        self.bottom.append(self.current_variant_grid[9])
        self.left.append(left)
        self.right.append(right)

    def print_variant(self, variant_number: int):
        """Print one of the variants to screen."""
        print('Tile, Variant:', self.tile_id, self.variant_names[variant_number])
        for row in self.variant_grids[variant_number]:
            print(row)
        print()

    # def print_variant_snaps(self):
    #     """Print to screen the current variant, and also details about the other variants available."""
    #     self.print_current_variant()
    #     print('Current variant:', self.current_variant)
    #     print('Variants:', self.variant_names)
    #     print('Top:', self.top)
    #     print('Bottom:', self.bottom)
    #     print('Left:', self.left)
    #     print('Right:', self.right)

    def reset_variant(self):
        """Reset the current variant to the original grid for this tile."""
        self.current_variant = 'O'
        self.current_variant_grid = self.original_grid.copy()

    def rotate_right(self):
        """Rotate the grid of the current variant 90 degrees clockwise."""
        old = self.current_variant_grid.copy()
        self.current_variant_grid = []

        for col in range(10):
            new_row = ''
            for row in old[::-1]:  # Go through rows backwards.
                new_row += row[col]
            self.current_variant_grid.append(new_row)

        self.current_variant += 'R'
        self.snapshot_variant()

    def flip_horizontal(self):
        """Flip the grid of the variant across its horizontal axis."""
        old = self.current_variant_grid.copy()
        self.current_variant_grid = []

        for row in old[::-1]:  # Go through the rows backwards.
            self.current_variant_grid.append(row)

        self.current_variant += 'H'
        self.snapshot_variant()

    def flip_vertical(self):
        """Flip the grid of the variant across its vertical axis."""
        old = self.current_variant_grid.copy()
        self.current_variant_grid = []

        for row in old:
            self.current_variant_grid.append(row[::-1])  # Reverse the characters in each row.

        self.current_variant += 'V'
        self.snapshot_variant()

    def find_match(self, edge: str, pattern: str) -> int:
        """For the parm edge (eg. 'L'eft, 'R'ight, 'B'ottom, 'T'op), return number of first variant that matches the
           required pattern.
           If no match, -1 is returned."""
        assert edge in ['L', 'R', 'B', 'T']

        for variant_num in range(len(self.variant_names)):
            if (edge == 'T' and pattern == self.top[variant_num]
                    or edge == 'B' and pattern == self.bottom[variant_num]
                    or edge == 'L' and pattern == self.left[variant_num]
                    or edge == 'R' and pattern == self.right[variant_num]):
                return variant_num

        return -1  # No matches found.

    def left_match(self, pattern: str) -> int:
        """Return number of first variant that has left edge that matches the parm pattern.
           If no match, -1 is returned."""
        for variant_num in range(len(self.variant_names)):
            if pattern == self.left[variant_num]:
                return variant_num
        return -1  # No matches found.

    def top_match(self, pattern: str) -> int:
        """Return number of first variant that has top edge that matches the parm pattern.
           If no match, -1 is returned."""
        for variant_num in range(len(self.variant_names)):
            if pattern == self.top[variant_num]:
                return variant_num
        return -1  # No matches found.

    def left_and_top_match(self, left_pattern: str, top_pattern: str) -> int:
        """Return number of first variant that has left and top edges that match the parm patterns.
           If no match, -1 is returned."""
        for variant_num in range(len(self.variant_names)):
            if left_pattern == self.left[variant_num] and top_pattern == self.top[variant_num]:
                return variant_num
        return -1  # No matches found.


def find_next_tile(tiles: [],           # All the tiles that exist.
                   used_tiles: [],      # Tile that have already been placed into the image.
                   image: dict,         # Image that has been made so far.

                   # Position in the image that we want to put the next tile into.
                   x: int, y: int) \
                   -> (Tile, int):      # Tile its variant number of a tile that fits into the (x, y).
    """For the parm image, and list of available tiles. Return an unused tile and its variant number that can fit
       into the image at the parm (x, y) coordinates."""

    left_check_needed = (x != 0)    # Need to check new tile matches tile on its left (if there is a tile on its left)
    top_check_needed = (y != 0)     # Need to check new tile matches tile above (if there is a tile above it).

    for nt in tiles:
        if nt not in used_tiles:                            # Try every tile that hasn't already been used.
            lt_right_edge, tt_bottom_edge = '', ''

            if left_check_needed:
                lt, lt_variant = image[(x - 1, y)]          # lt = tile to the left.
                lt_right_edge = lt.right[lt_variant]
            if top_check_needed:
                tt, tt_variant = image[(x, y - 1)]          # tt = tile to the top.
                tt_bottom_edge = tt.bottom[tt_variant]

            if left_check_needed and top_check_needed:
                nt_variant = nt.left_and_bottom_match(left_pattenr=lt_right_edge, top_pattern=tt_bottom_edge)

            elif left_check_needed:
                # Try to find a left edge in candidate new tile that matches right edge of tile to the left.
                nt_variant = nt.left_match(pattern=lt_right_edge)

            else:
                # Try to find a top edge in candidate new tile that matches bottom edge of tile to the top of it.
                nt_variant = nt.top_match(pattern=tt_bottom_edge)

            if nt_variant != -1:  # Not -1 means a matching edge was found.
                return nt, nt_variant
    return None, None


def print_image(image: dict):
    """Print out the parm image."""
    for (x, y) in image:
        print('POSITION (x, y):', x, y)
        tile, variant_number = image[(x, y)]
        tile.print_variant(variant_number)


def main():
    filename = sys.argv[1]
    f = open(filename)
    whole_text = f.read()
    f.close()

    tiles = []

    for tile in whole_text.split('\n\n'):  # Each tile is separated from neighbor by blank line.
        tile_rows = tile.split('\n')
        tile_id = int(tile_rows[0].replace('Tile ', '').replace(':', ''))  # Remove the cruft from tile id row.
        tile_rows.pop(0)  # Remove first item from rows (it contains the title ID).

        new_tile = Tile(tile_id, tile_rows)
        tiles.append(new_tile)

    width_length = int(sqrt(len(tiles)))            # Dimensions of the image.
    if VERBOSE:
        print('width_height:', width_length)

    image = {}
#    found_tl = False            # Have we found a top-left tile that can seed a whole image?


    # Try every variant of every tile in top-left corner.
    for tl in tiles:                           # 'tl_' means top-left.
        for tl_variant in range(len(tl.variant_names)):
            image = {(0, 0): (tl, tl_variant)}
            used_tiles = [tl]                      # Tiles already used in this image.

            failure = False
            x, y = 1, 0                             # Coordinates of next tile to attempt to add to image.

            nt, nt_variant = find_next_tile(tiles, used_tiles, image, x, y)

            if nt is not None:
                image[(x, y)] = (nt, nt_variant)
                used_tiles.append(nt)
            else:                                   # Failed to find a next tile that fits.
                failure = True

            if len(image) == 2:
                break
        if len(image) == 2:
            break

            # if not found_tl:
            #     # Seed the top-left corner of the image with a tile.
            #     image = {(0, 0): (tl, tl_variant)}
            #     used_tiles = [tl]                      # Tiles already used in this image.
            #
            #     x, y = 1, 0
            #
            #     # For the top-left seed that we are trying, have we found a next tile that fits?
            #     found_nt = False
            #
                # for nt in tiles:
                #     if nt not in used_tiles:
                #         if x != 0:
                #             lt, lt_variant = image[(x - 1, y)]      # tl = tile to the left.
                #             lt_right_edge = lt.right[lt_variant]
                #
                #             # Try to find a left edge in candidate new tile that matches right edge of tile to the left.
                #             nt_variant = nt.find_match(edge='L', pattern=lt_right_edge)
                #             if nt_variant != -1:               # Not -1 means a matching edge was found.
                #
                #                 image[(x, y)] = (nt, nt_variant)
                #                 used_tiles.append(nt)
                #
                #                 found_nt = True
                #                 found_tl = True
                #                 break

    print_image(image)


if __name__ == "__main__":
    main()
