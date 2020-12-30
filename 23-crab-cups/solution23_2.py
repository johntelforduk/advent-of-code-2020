# Solution to part 2 (and also part 1, again) of day 23 of AOC 2020, Crab Cups.
# https://adventofcode.com/2020/day/23

class Game:
    def __init__(self):

        # k = cup label.
        # v = (a, c). Where a and c are the labels of the cups anticlockwise and clockwise of this cup respectively.
        # This makes a doubly linked list of cups.
        self.cups = {}

        self.max_label = 0              # Highest cup label in the game.
        self.move_number = 1            # Number of moves in the game so far.
        self.current = 0                # The currently selected cup.
        self.destination = 0

    def cups_from_text(self, text: str):
        """Add cups to the circle based on parm string of digits.
           For example '389' creates a circle of cups 3 -> 8 -> 9 (and 9 points back to 3)."""
        previous_cup = 0
        for this_cup_str in text:
            this_cup = int(this_cup_str)
            self.insert_cup(cup=this_cup, insert_after=previous_cup)
            previous_cup = this_cup

    def insert_many_cups(self, previous_cup: int, highest: int):
        """Add cups to the circle until the parm number is reached."""

        # "Your labeling is still correct for the first few cups; after that, the remaining cups are just numbered in an
        # increasing fashion starting from the number after the highest number in your list and proceeding one by one
        # until one million is reached. (For example, if your labeling were 54321,
        # the cups would be numbered 5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.)
        # In this way, every number from one through one million is used exactly once."
        for this_cup in range(max(self.cups) + 1, highest + 1):
            self.insert_cup(cup=this_cup, insert_after=previous_cup)
            previous_cup = this_cup

    def insert_cup(self, cup: int, insert_after: int):
        """Insert parm cup into the circle. Position to insert the cup is also a parm."""

        # If there are no cups in the circle, then create a new circle with this 1 cup.
        # It's anticlockwise and clockwise pointers will be to itself.
        if len(self.cups) == 0:
            self.cups[cup] = (cup, cup)
            self.current = cup                          # First cup to be inserted is designated as the current cup.

        # For 1 existing cup in circle, we end up with circle of 2 cups, with each cups' anticlockwise and
        # clockwise pointers pointing to the other cup.
        elif len(self.cups) == 1:
            (_, c) = self.cups[insert_after]
            self.cups[cup] = (insert_after, insert_after)
            self.cups[insert_after] = (cup, cup)

        # General case, where cup is being inserted between 2 existing cups.
        else:
            prev_a, prev_c = self.cups[insert_after]    # "prev" is from point of view of new cup.
            _, next_c = self.cups[prev_c]               # "prev_c" gives us the cup to the right.
            self.cups[cup] = (insert_after, prev_c)     # Insert the new cup to the circle.
            self.cups[insert_after] = (prev_a, cup)     # Update cup anticlockwise of the inserted cup.
            self.cups[prev_c] = (cup, next_c)           # Update cup clockwise of the inserted cup.

        self.max_label = max(self.max_label, cup)       # Update the maximum cup number.

    def insert_cups(self, inserts: list, insert_after: int):
        """Insert parm list of cups (in order) after the parm cup."""

        # "The crab places the cups it just picked up so that they are immediately clockwise of the destination cup.
        # They keep the same order as when they were picked up."
        for this_cup in inserts:
            self.insert_cup(cup=this_cup, insert_after=insert_after)
            insert_after = this_cup

    def pick_up_cups(self, num: int) -> list:
        """Remove the parm number of cups clockwise of the current cup.
           Return the cups picked up as list of integers."""

        # "The crab picks up the three cups that are immediately clockwise of the current cup.
        # They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle."
        picked = []
        for i in range(num):
            picked.append(self.pick_up_1_cup())
        return picked

    def pick_up_1_cup(self) -> int:
        """Remove 1 cup clockwise of the current cup. Return the 1 cup picked up."""

        prev_a, pick_up = self.cups[self.current]   # Cup that is anticlockwise from cup to be picked up.
        _, next_cup = self.cups[pick_up]            # next_cup is label of the cup after the one to be picked up.
        _, next_c = self.cups[next_cup]             # Pointers of the cup that is clockwise of one to be picked up.

        self.cups[self.current] = (prev_a, next_cup)
        self.cups[next_cup] = (self.current, next_c)

        del self.cups[pick_up]                      # Remove the picked up cup from the dictionary.

        if pick_up == self.max_label:               # If necessary, adjust the max label attribute.
            self.max_label = max(self.cups)

        return pick_up                              # Return the label of the picked up cup.

    def update_destination_cup(self):
        """Update the destination cup attribute."""

        # "The crab selects a destination cup: the cup with a label equal to the current cup's label minus one.
        # If this would select one of the cups that was just picked up, the crab will keep subtracting one until it
        # finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest
        # value on any cup's label, it wraps around to the highest value on any cup's label instead."

        candidate = self.current
        while True:
            candidate = candidate - 1
            if candidate == 0:
                candidate = self.max_label
            if candidate in self.cups:
                self.destination = candidate
                return

    def select_new_current_cup(self):
        """Update the current cup attribute with new current cup number."""
        # "The crab selects a new current cup: the cup which is immediately clockwise of the current cup."
        (_, c) = self.cups[self.current]
        self.current = c

    def display_cups(self):
        """Print status of cups to stdout."""
        print('cups: (' + str(self.current) + ')', end=' ')

        _, cup = self.cups[self.current]

        while cup != self.current:
            print(cup, end=' ')
            _, cup = self.cups[cup]         # Move on to the cup that is clockwise from this cup.

        print()

    def move(self, verbose: bool):
        """Play 1 move of the game. Parm indicates if information about each move should be sent to stdout."""
        if verbose:
            print('-- move', self.move_number, '--')
            self.display_cups()

        picked_up = self.pick_up_cups(3)
        self.update_destination_cup()

        if verbose:
            print('pick up: ', end='')
            for pick in picked_up:
                print(pick, end=' ')
            print()
            print('destination:', self.destination)
            print()

        self.insert_cups(inserts=picked_up, insert_after=self.destination)
        self.select_new_current_cup()

        self.move_number += 1

    def solution_to_part1(self) -> str:
        """Return the puzzle solution as a string."""

        # "Starting after the cup labeled 1, collect the other cups' labels clockwise into a single string with no
        # extra characters."
        self.current = 1
        eight_cups = self.pick_up_cups(8)       # 9 cups in the circle, so all cups except '1' is 8 cups.

        answer = ''
        for cup in eight_cups:
            answer += str(cup)
        return answer

    def solution_to_part2(self) -> int:
        """Return the solution to part 2."""

        # "Determine which two cups will end up immediately clockwise of cup 1. What do you get if you multiply their
        # labels together?"
        self.current = 1
        [cup1, cup2] = self.pick_up_cups(2)
        return cup1 * cup2


def main():
    labeling = '562893147'

    part1 = Game()
    part1.cups_from_text(labeling)

    for move in range(100):
        part1.move(verbose=True)

    print('-- final --')
    part1.display_cups()

    print('Part 1:', part1.solution_to_part1())

    # ----------

    part2 = Game()
    part2.cups_from_text(labeling)

    part2.insert_many_cups(previous_cup=7, highest=1000000)
    assert len(part2.cups) == 1000000

    for move in range(10000000):
        if move % 1000000 == 0:
            print('move:', move)
        part2.move(verbose=False)

    print('Part 2:', part2.solution_to_part2())


if __name__ == "__main__":
    main()
