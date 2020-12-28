# Solution to part 1 of day 22 of AOC 2020, Crab Combat.
# https://adventofcode.com/2020/day/22

import sys

VERBOSE = ('-v' in sys.argv)


class Deck:

    def __init__(self, text: str):

        lines = text.split('\n')   # Each card starts on a new line.

        self.player = lines.pop(0).replace(':', '')     # Strip off trailing colon.

        self.cards = []
        for card in lines:
            self.cards.append(int(card))

    def top_card(self) -> int:
        """Remove the top card from the deck. Return the value of that card."""
        card = self.cards.pop(0)
        print(self.player, 'plays:', card)
        return card

    def card_on_bottom(self, card: int):
        """Put the parm card on the bottom of the deck."""
        self.cards.append(card)

    def display(self):
        """Print out info about the deck to stdout."""
        print(self.player, "'s deck: ", end='')

        first = True
        for card in self.cards:
            if not first:
                print(', ', end='')
            first = False
            print(card, end='')
        print()


class Combat:

    def __init__(self, filename: str):

        f = open(filename)
        whole_text = f.read()
        f.close()

        p1_text, p2_text = whole_text.split('\n\n')     # There is a blank line between the 2 players.

        self.p1_deck = Deck(p1_text)                    # Player 1's card deck.
        self.p2_deck = Deck(p2_text)                    # Player 2's card deck.

        self.round = 1
        self.winner = None                               # Is the game over?

    def play_a_round(self):
        """Play a round of the game."""
        print('-- Round' ,self.round, '--')
        self.p1_deck.display()
        self.p2_deck.display()

        # "... both players draw their top card..."
        p1_card = self.p1_deck.top_card()
        p2_card = self.p2_deck.top_card()

        # "... and the player with the higher-valued card wins the round."
        if p1_card > p2_card:
            print('Player 1 wins the round!')

            # "The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card
            # is above the other card."
            self.p1_deck.card_on_bottom(p1_card)
            self.p1_deck.card_on_bottom(p2_card)
        else:
            print('Player 2 wins the round!')
            self.p2_deck.card_on_bottom(p2_card)
            self.p2_deck.card_on_bottom(p1_card)
        print()

        # "If this causes a player to have all of the cards, they win, and the game ends."
        if len(self.p1_deck.cards) == 0:
            self.winner = self.p2_deck
        elif len(self.p2_deck.cards) == 0:
            self.winner = self.p1_deck

        self.round += 1

    def calculate_winning_score(self) -> int:
        """Return score of winning deck."""

        # "The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom
        # card is worth the value of the card multiplied by 2, and so on."

        score = 0
        multiplier = 1

        for card in self.winner.cards[::-1]:        # Go through the winners cards backwards.
            score += card * multiplier
            multiplier += 1
        return score


def main():
    filename = sys.argv[1]

    game = Combat(filename)

    while game.winner is None:
        game.play_a_round()

    print('== Post-game results ==')
    game.p1_deck.display()
    game.p2_deck.display()

    print('Part 1:', game.calculate_winning_score())


if __name__ == "__main__":
    main()
