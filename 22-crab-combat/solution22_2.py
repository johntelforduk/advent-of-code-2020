# Solution to part 2 of day 22 of AOC 2020, Crab Combat.
# https://adventofcode.com/2020/day/22

import sys

VERBOSE = ('-v' in sys.argv)


class Deck:

    def __init__(self, player: int, cards: list):
        self.player = player
        self.cards = cards

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
        print('Player', str(self.player) + "'s deck: ", end='')

        first = True
        for card in self.cards:
            if not first:
                print(', ', end='')
            first = False
            print(card, end='')
        print()


class Combat:

    def __init__(self, game: int, p1_cards_list: list, p2_cards_list: list):
        self.p1_deck = Deck(player=1, cards=p1_cards_list)                    # Player 1's deck of cards.
        self.p2_deck = Deck(player=2, cards=p2_cards_list)                    # Player 2's card deck.

        self.previous_rounds = []               # List of decks that each player had in previous rounds.

        self.game = game
        print('=== Game', self.game, '===')
        print()

        self.round = 1
        self.winner = 0                               # 0 indicates no winner yet.

        while self.winner == 0:
            self.winner = self.play_a_round()

    def play_a_round(self) -> int:
        """Play a round of the game.
           If one of the players wins the game in this round, return their player number.
           Otherwise, return 0, to indicate no winner after this round."""
        print('-- Round', self.round, '(Game ' + str(self.game) + ')--')
        self.p1_deck.display()
        self.p2_deck.display()

        # "Before either player deals a card, if there was a previous round in this game that had exactly the same
        # cards in the same order in the same players' decks, the game instantly ends in a win for player 1."
        if (self.p1_deck.cards, self.p2_deck.cards) in self.previous_rounds:
            print('Stalemate, hence Player 1 wins')
            return 1
        self.previous_rounds.append((self.p1_deck.cards.copy(), self.p2_deck.cards.copy()))

        # "... both players draw their top card..."
        p1_card = self.p1_deck.top_card()
        p2_card = self.p2_deck.top_card()

        # "... and the player with the higher-valued card wins the round."
        if p1_card > p2_card:
            print('Player 1 wins round', self.round, 'of game', self.game)

            # "The winner keeps both cards, placing them on the bottom of their own deck so that the winner's card
            # is above the other card."
            self.p1_deck.card_on_bottom(p1_card)
            self.p1_deck.card_on_bottom(p2_card)
        else:
            print('Player 2 wins round', self.round, 'of game', self.game)
            self.p2_deck.card_on_bottom(p2_card)
            self.p2_deck.card_on_bottom(p1_card)
        print()

        self.round += 1

        # "If this causes a player to have all of the cards, they win, and the game ends."
        if len(self.p1_deck.cards) == 0:        # p1 has no cards left, so p2 wins.
            return 2
        elif len(self.p2_deck.cards) == 0:      # p2 has no cards left, so p1 wins.
            return 1
        return 0                                # 0 indicates no winner of the game during this round.

    def calculate_winning_score(self) -> int:
        """Return score of winning deck."""

        # "The bottom card in their deck is worth the value of the card multiplied by 1, the second-from-the-bottom
        # card is worth the value of the card multiplied by 2, and so on."

        if self.winner == 1:
            cards = self.p1_deck.cards
        else:
            cards = self.p2_deck.cards

        score = 0
        multiplier = 1

        for card in cards[::-1]:        # Go through the winners cards backwards.
            score += card * multiplier
            multiplier += 1
        return score


def text_to_cards(text: str) -> list:
    """For parm text file, return a list of integers which are the cards in that text file."""
    cards = []

    # Each card starts on a new line. Ignore the first line, as it is the player number.
    for card in text.split('\n')[1:]:
        cards.append(int(card))
    return cards


def main():
    filename = sys.argv[1]

    f = open(filename)
    whole_text = f.read()
    f.close()

    p1_text, p2_text = whole_text.split('\n\n')  # There is a blank line between the 2 players.

    p1_cards = text_to_cards(p1_text)
    p2_cards = text_to_cards(p2_text)

    game = Combat(game=1, p1_cards_list=p1_cards, p2_cards_list=p2_cards)

    print('== Post-game results ==')
    game.p1_deck.display()
    game.p2_deck.display()

    print('Part 1:', game.calculate_winning_score())


if __name__ == "__main__":
    main()
