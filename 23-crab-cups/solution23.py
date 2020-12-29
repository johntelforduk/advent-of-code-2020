# Solution to day 23 of AOC 2020, Crab Cups.
# https://adventofcode.com/2020/day/23

import sys

VERBOSE = ('-v' in sys.argv)


class Game:
    def __init__(self, cups: str, moves_left: int):

        self.cups = list(cups)
        self.move_number = 1
        self.moves_left = moves_left

        self.current = self.cups[0]
        self.destination = ''


    def pick_up_cups(self, num: int) -> str:
        """Remove the parm number of cups clockwise of the current cup. Return the cups picked up as string."""

        # "The crab picks up the three cups that are immediately clockwise of the current cup.
        # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle."

        picked = ''
        for i in range(num):
            picked += self.pick_up_1_cup()
        return picked

    def pick_up_1_cup(self) -> str:
        """Remove 1 cup clockwise of the current cup. Return the 1 cup picked up."""
        current_position = self.cups.index(self.current)
        if current_position < len(self.cups) - 1:    # Current cup is not on the end of the list.
            return self.cups.pop(current_position + 1)
        return self.cups.pop(0)

    def update_destination_cup(self):
        """Update the destination cup attribute."""

        # "The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
        # If this would select one of the cups that was just picked up, the crab will keep subtracting one until it
        # finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest
        # value on any cup's label, it wraps around to the highest value on any cup's label instead."

        candidate = self.current
        while True:
            candidate = str(int(candidate) - 1)
            if candidate == '0':
                candidate = '9'
            if candidate in self.cups:
                self.destination = candidate
                return

    def insert_cups(self, inserts: str, insert_after: str):
        """Insert parm string of cups (in order) after the parm cup."""

        # "The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
        # They keep the same order as when they were picked up."

        new_list = []
        for cup in self.cups:
            new_list.append(cup)
            if cup == insert_after:
                for each_insert in inserts:
                    new_list.append(each_insert)
        self.cups = new_list

    def select_new_current_cup(self):
        """Update the current cup attribute with new current cup number."""

        # "The crab selects a new current cup: the cup which is immediately clockwise of the current cup."

        current_position = self.cups.index(self.current)
        if current_position < len(self.cups) - 1:           # Current cup is not on the end of the list.
            self.current = self.cups[current_position + 1]
        else:
            self.current = self.cups[0]

    def display_cups(self):
        """Print status of cups to stdout."""
        print('cups: ', end='')
        for cup in self.cups:
            if cup == self.current:
                print('(' + cup + ') ', end='')
            else:
                print(cup, end=' ')
        print()

    def move(self):
        """Play 1 move of the game."""
        if VERBOSE:
            print('-- move', self.move_number, '--')
            self.display_cups()

        picked_up = self.pick_up_cups(3)
        self.update_destination_cup()

        if VERBOSE:
            print('pick up: ',end='')
            for pick in picked_up:
                print(pick, end=' ')
            print()
            print('destination:', self.destination)
            print()

        self.insert_cups(inserts=picked_up, insert_after=self.destination)
        self.select_new_current_cup()

        self.move_number += 1

    def solution(self) -> str:
        """Return the puzzle solution as a string."""

        # "Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no
        # extra characters."

        self.current = '1'
        return self.pick_up_cups(8)         # 9 cups in the circle, so all cups except '1' is 8 cups.


def main():
    labeling = sys.argv[1]
    moves_left = int(sys.argv[2])

    # if VERBOSE:
    #     print('labeling, moves_left:', labeling, moves_left)

    this_game = Game(labeling, moves_left)

    for move in range(moves_left):
        this_game.move()

    if VERBOSE:
        print('-- final --')
        this_game.display_cups()

    print('Part 1:', this_game.solution())


if __name__ == "__main__":
    main()
