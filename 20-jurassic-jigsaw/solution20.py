# Solution to part 1 of day 20 of AOC 2020, Monster Messages.
# https://adventofcode.com/2020/day/20

import sys
from math import sqrt
import pygame


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


class Image:

    def __init__(self, image: dict):

        self.image_size = int(sqrt(len(image)))      # For example, an image of 3 x 3 tiles has size of 3.

        self.monster = [(18, 0),
                        (0, 1), (5, 1), (6, 1), (11, 1), (12, 1), (17, 1), (18, 1), (19, 1),
                        (1, 2), (4, 2), (7, 2), (10, 2), (13, 2), (16, 2)]

        # Define the colors we will use in RGB format.
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.GREY = (50, 50, 50)

        self.hashes = 0             # Number of non-blank pixels in the final image.

        # "The borders of each tile are not part of the actual image; start by removing them."
        self.grid = []
        for tile_y in range(self.image_size):
            for y in range(1, 9):
                row = ''
                for tile_x in range(self.image_size):
                    tile, variant = image[tile_x, tile_y]
                    for x in range(1, 9):
                        pixel = tile.variant_grids[variant][y][x]
                        row += tile.variant_grids[variant][y][x]
                        if pixel == '#':
                            self.hashes += 1
                self.grid.append(row)

        self.zoom_factor = 800 // len(self.grid)
        self.screen_size = [self.zoom_factor * len(self.grid), self.zoom_factor * len(self.grid)]

    def search_for_monster(self) -> list:
        """Search for monsters in the image. Rotate and flip the image in all possible ways.
           Returns a list of coordinates of monsters."""

        monsters = []
        search = 'ORRRRHRRRRHVRRRRHRRRR'

        for translation in search:
            if translation == 'R':
                self.rotate()
            elif translation == 'H':
                self.flip_horizontal()
            elif translation == 'V':
                self.flip_vertical()

            for x in range(len(self.grid) - 20):        # 20 is the width of the monster.
                for y in range(len(self.grid) - 3):     # 3 is height of the monster.
                    found = True
                    for dx, dy in self.monster:
                        if self.grid[y + dy][x + dx] != '#':
                            found = False
                    if found:
                        monsters.append((x, y))
            if len(monsters) != 0:
                return monsters

    def render(self, monsters: list):
        """Render the image to screen."""
        pygame.init()  # Initialize the game engine.

        target_fps = 1

        screen = pygame.display.set_mode(self.screen_size)
        clock = pygame.time.Clock()

        pygame.display.set_caption('Jurassic Jigsaw')           # The window title.

        quiting = False

        while not quiting:
            clock.tick(target_fps)

            screen.fill(self.BLACK)

            for y in range(len(self.grid)):
                for x in range(len(self.grid)):
                    if self.grid[y][x] == '#':
                        pygame.draw.rect(screen, self.GREY, (x * self.zoom_factor, y * self.zoom_factor,
                                         self.zoom_factor, self.zoom_factor))

            for event in pygame.event.get():  # User did something.
                if event.type == pygame.QUIT:  # If user clicked close.
                    quiting = True  # Flag that we are done so we exit this loop, and quit the game

            for x, y in monsters:
                for dx, dy in self.monster:
                    pygame.draw.rect(screen, self.GREEN, ((x + dx) * self.zoom_factor, (y + dy) * self.zoom_factor,
                                                          self.zoom_factor, self.zoom_factor))

            pygame.display.flip()
        pygame.image.save(screen, "screenshot.jpg")
        pygame.quit()

    def rotate(self):
        old = self.grid
        self.grid = []

        for col in range(len(old)):
            new_row = ''
            for row in old[::-1]:  # Go through rows backwards.
                new_row += row[col]
            self.grid.append(new_row)

    def flip_horizontal(self):
        old = self.grid.copy()
        self.grid = []

        for row in old[::-1]:  # Go through the rows backwards.
            self.grid.append(row)

    def flip_vertical(self):
        old = self.grid.copy()
        self.grid = []

        for row in old:
            self.grid.append(row[::-1])  # Reverse the characters in each row.


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
                nt_variant = nt.left_and_top_match(left_pattern=lt_right_edge, top_pattern=tt_bottom_edge)

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

    for tile in whole_text.split('\n\n'):               # Each tile is separated from neighbor by blank line.
        tile_rows = tile.split('\n')
        tile_id = int(tile_rows[0].replace('Tile ', '').replace(':', ''))   # Remove the cruft from tile id row.
        tile_rows.pop(0)                                # Remove first item from rows (it contains the title ID).

        new_tile = Tile(tile_id, tile_rows)
        tiles.append(new_tile)

    width_length = int(sqrt(len(tiles)))                # Dimensions of the image.
    if VERBOSE:
        print('width_height:', width_length)

    image = {}

    # Try every variant of every tile in top-left corner.
    for tl in tiles:                                    # 'tl_' means top-left.
        for tl_variant in range(len(tl.variant_names)):
            image = {(0, 0): (tl, tl_variant)}
            used_tiles = [tl]                           # Tiles already used in this image.

            failure = False
            x, y = 1, 0                                 # Coordinates of next tile to attempt to add to image.

            while not failure and y < width_length:
                nt, nt_variant = find_next_tile(tiles, used_tiles, image, x, y)

                if nt is not None:
                    image[(x, y)] = (nt, nt_variant)
                    used_tiles.append(nt)

                    x += 1
                    if x == width_length:
                        x = 0
                        y += 1
                else:                                   # Failed to find a next tile that fits.
                    failure = True

            if len(image) == width_length ** 2:
                break
        if len(image) == width_length ** 2:
            break

    print_image(image)

    # _ used, because each item in the dict is (tile, variant), and we don't need the variant number for
    # this calculation.
    tl, _ = image[(0, 0)]
    bl, _ = image[(0, width_length - 1)]
    tr, _ = image[(width_length - 1, 0)]
    br, _ = image[(width_length - 1, width_length - 1)]

    print('Part 1', tl.tile_id * bl.tile_id * tr.tile_id * br.tile_id)

    # ----------------

    my_image = Image(image)
    if VERBOSE:
        print(my_image.grid)

    monsters = my_image.search_for_monster()
    if VERBOSE:
        print(monsters)
    my_image.render(monsters)

    print('Part 2:', my_image.hashes - len(monsters) * len(my_image.monster))


if __name__ == "__main__":
    main()
