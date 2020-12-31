# Solution to day 24 of AOC 2020, Lobby Layout.
# https://adventofcode.com/2020/day/24

import sys
import pygame


VERBOSE = ('-v' in sys.argv)


class Floor:

    def __init__(self):

        # Define the colors we will use in RGB format.
        self.white_tile_colour = (240, 240, 240)
        self.black_tile_colour = (40, 40, 40)
        self.grout_colour = (100, 100, 100)

        self.zoom = 7                                               # Lower zoom, means more tiles rendered.

        pygame.init()                                               # Initialize the game engine.

        self.screen_size = [1100, 800]                              # [width, height]
        self.screen = pygame.display.set_mode(self.screen_size)

        self.black_tiles = set()                                    # Each member is pair (x, y).

    def render(self):
        """Render image of the floor to screen."""

        pygame.display.set_caption('Lobby Layout')                  # The window title.

        self.draw_background()                                      # Cover screen with white tiles.

        for (x, y) in self.black_tiles:
            self.draw_tile(x, y, 'B')

        quiting = False
        while not quiting:
            for event in pygame.event.get():  # User did something.
                if event.type == pygame.QUIT:  # If user clicked close.
                    quiting = True  # Flag that we are done so we exit this loop, and quit the game
            pygame.display.update()

        pygame.image.save(self.screen, "screenshot.jpg")
        pygame.quit()

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

        x, y = 0, 0

        hex_to_cartesian = {'e': (2, 0),
                            'w': (-2, 0),
                            'se': (1, 2),
                            'sw': (-1, 2),
                            'ne': (1, -2),
                            'nw': (-1, -2)}

        for each_step in directions:
            (dx, dy) = hex_to_cartesian[each_step]
            x += dx
            y += dy

        if (x, y) in self.black_tiles:
            self.black_tiles.remove((x, y))
        else:
            self.black_tiles.add((x, y))


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
    f = open(filename)
    whole_text = f.read()
    f.close()

    if VERBOSE:
        print('filename:', filename)

    the_floor = Floor()

    for each_instruction in whole_text.split('\n'):
        directions = text_to_directions(each_instruction)
        the_floor.flip(directions)

    # "After all of the instructions have been followed, how many tiles are left with the black side up?"
    print('Part 1:', len(the_floor.black_tiles))

    the_floor.render()


if __name__ == "__main__":
    main()
