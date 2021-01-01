# Solution to day 24 of AOC 2020, Lobby Layout.
# https://adventofcode.com/2020/day/24

import sys
import pygame
import imageio                          # For making animated GIFs.


VERBOSE = ('-v' in sys.argv)


class Floor:

    def __init__(self, zoom: int):

        # Define the colors we will use in RGB format.
        self.white_tile_colour = (240, 240, 240)
        self.black_tile_colour = (40, 40, 40)
        self.grout_colour = (100, 100, 100)
        self.text_background = (255, 255, 255)
        self.text_colour = (0, 0, 0)

        self.hex_to_cartesian = {'e': (2, 0),
                                 'w': (-2, 0),
                                 'se': (1, 2),
                                 'sw': (-1, 2),
                                 'ne': (1, -2),
                                 'nw': (-1, -2)}

        self.zoom = zoom                                            # Lower zoom, means more tiles in the room.
        self.screen_size = [1100, 800]                              # [width, height]

        pygame.init()                                               # Initialize the game engine.
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.font.init()                      # Start the Pygame text rendering system.
        self.myfont = pygame.font.SysFont('Courier New', 30)
        pygame.display.set_caption('Lobby Layout')                  # The window title.

        self.black_tiles = set()                                    # Each member is pair (x, y).
        self.day = 0

    def art_exhibit(self, days: int) -> bool:
        """Render image of the floor to screen. Then follow art exhibit flipping rules for parm number of days.
           Returns a bool to indicate if the process was quit early."""

        filenames = []

        quiting = False
        while not quiting and self.day < days:
            for event in pygame.event.get():  # User did something.
                if event.type == pygame.QUIT:  # If user clicked close.
                    quiting = True  # Flag that we are done so we exit this loop, and quit the game

            self.draw_background()  # Cover screen with white tiles.

            for (x, y) in self.black_tiles:
                self.draw_tile(x, y, 'B')

            pygame.draw.rect(self.screen, self.text_background, (0, 0, 450, 40))

            caption = 'Day ' + str(self.day) + ': ' + str(len(self.black_tiles)) + ' black tiles'
            text_surface = self.myfont.render(caption, False, self.text_colour)
            self.screen.blit(text_surface, (5, 5))

            pygame.display.flip()

            if self.day in [0, 100]:
                pygame.image.save(self.screen, 'screenshots/day_' + str(self.day) + '.jpg')

            if self.day <= 10:
                screenshot_name = 'screenshots/screen' + format(self.day, '02') + '.png'
                pygame.image.save(self.screen, screenshot_name)
                filenames.append(screenshot_name)

            if self.day == 10:
                images = []
                for filename in filenames:
                    images.append(imageio.imread(filename))
                imageio.mimsave('solution_part2.gif', images, fps=1)

            self.iterate()

        pygame.quit()

        return not quiting

    def draw_background(self):
        """Tile the floor with default white tiles."""
        for y in range(- self.screen_size[1] // self.zoom, self.screen_size[1] // self.zoom):
            for x in range(- self.screen_size[0] // self.zoom, self.screen_size[0] // self.zoom):
                self.draw_tile(x * 2, y * 4, 'W')
                self.draw_tile(1 + x * 2, 2 + y * 4, 'W')

    def draw_tile(self, x, y, colour: str):
        """Draw a tile on the screen."""
        if colour == 'B':
            tile_colour = self.black_tile_colour
        else:
            tile_colour = self.white_tile_colour

        x_screen = self.screen_size[0] // 2 + x * self.zoom * 2
        y_screen = self.screen_size[1] // 2 + y * self.zoom * 1.5

        vertices = ((x_screen, y_screen),
                    (x_screen + 2 * self.zoom, y_screen + 1 * self.zoom),
                    (x_screen + 2 * self.zoom, y_screen + 3 * self.zoom),
                    (x_screen, y_screen + 4 * self.zoom),
                    (x_screen - 2 * self.zoom, y_screen + 3 * self.zoom),
                    (x_screen - 2 * self.zoom, y_screen + 1 * self.zoom),
                    (x_screen, y_screen))

        # Draw the tile.
        pygame.draw.polygon(surface=self.screen, color=tile_colour, points=vertices)

        # Draw a grout border around the tile.
        pygame.draw.polygon(surface=self.screen, color=self.grout_colour, points=vertices, width=1 + self.zoom // 5)

    def flip(self, directions: list):
        """Follows the parm directions to identify a tile. Then flips that tile, from white to black (or vice versa)."""

        x, y = 0, 0         # Start at the origin tile position.

        for each_step in directions:
            (dx, dy) = self.hex_to_cartesian[each_step]
            x += dx
            y += dy

        if (x, y) in self.black_tiles:
            self.black_tiles.remove((x, y))
        else:
            self.black_tiles.add((x, y))

    def iterate(self):
        """Do an iteration of the art exhibit rules."""

        # "The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need
        # to be flipped, then they are all flipped at the same time."
        prev_black_tiles = self.black_tiles.copy()
        self.black_tiles = set()

        # Find a set of tiles that need to be checked. It is is every tile that either a black tile already, or
        # a neighbor of a black tile. That is to say, white tiles that have no black neighbors don't need to be checked.

        check = prev_black_tiles.copy()
        for (x, y) in prev_black_tiles:
            for dx, dy in self.hex_to_cartesian.values():
                check.add((x + dx, y + dy))

        # for range_y in range(- self.screen_size[1] // self.zoom, self.screen_size[1] // self.zoom):
        #     for range_x in range(- self.screen_size[0] // self.zoom, self.screen_size[0] // self.zoom):
        #         self.iteration_rule(prev_black_tiles, range_x * 2, range_y * 4)
        #         self.iteration_rule(prev_black_tiles, 1 + range_x * 2, 2 + range_y * 4)

        for (x, y) in check:
            self.iteration_rule(prev_black_tiles, x, y)

        self.day += 1

    def iteration_rule(self, previous_black_tiles: set, x, y):
        """Apply the iteration rule to parm tile position."""

        adjacent = self.count_adjacent_blacks(previous_black_tiles, x, y)

        # "Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white."
        if (x, y) in previous_black_tiles and not (adjacent == 0 or adjacent > 2):
            self.black_tiles.add((x, y))

        # "Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black."
        if (x, y) not in previous_black_tiles and adjacent == 2:
            self.black_tiles.add((x, y))

    def count_adjacent_blacks(self, previous_black_tiles: set, x, y) -> int:
        """Return the number of black tiles that are adjacent to the parm (x, y) tile."""

        # "Here, tiles immediately adjacent means the six tiles directly touching the tile in question."
        count = 0
        for (dx, dy) in self.hex_to_cartesian.values():
            if (x + dx, y + dy) in previous_black_tiles:
                count += 1
        return count


def text_to_directions(text: str) -> list:
    """Return a list of directions for parm string of codes."""

    # "Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest,
    # and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne.
    # A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile
    # you land on if you start at the reference tile and then move one tile east, one tile southeast,
    # one tile northeast, and one tile east."
    directions = []
    pos = 0

    while pos < len(text):
        if text[pos] in ['e', 'w']:                         # Single character directions.
            directions.append(text[pos])
            pos += 1
        else:                                               # Two character directions.
            directions.append(text[pos:pos + 2])
            pos += 2
    return directions


def main():
    filename = sys.argv[1]
    zoom = int(sys.argv[2])
    f = open(filename)
    whole_text = f.read()
    f.close()

    if VERBOSE:
        print('filename:', filename)

    the_floor = Floor(zoom)

    for each_instruction in whole_text.split('\n'):
        directions = text_to_directions(each_instruction)
        the_floor.flip(directions)

    # "After all of the instructions have been followed, how many tiles are left with the black side up?"
    print('Part 1:', len(the_floor.black_tiles))

    if the_floor.art_exhibit(days=100):
        print('Part 2:', len(the_floor.black_tiles))


if __name__ == "__main__":
    main()
