# Solution to day 15 of AOC 2020, Rambunctious Recitation.
# https://adventofcode.com/2020/day/15

import sys

VERBOSE = ('-v' in sys.argv)


def game(spoken: list, rounds: int) -> int:
    """Play the game for parm number of turns, starting with parm list of seed numbers spoken.
       Returns the number spoken in last turn of the game."""

    last = spoken[-1:][0]                       # The last number spoken (last number in spoken list).

    # k, v
    # k = a spoken number.
    # v = list of turns that it was spoken in.
    spoken_dict = {}

    turn = 1

    for number in spoken:
        if number in spoken_dict:
            spoken_dict[number].append(turn)
        else:
            spoken_dict[number] = [turn]
        turn += 1

    this = 0                                    # Word that will be spoken in this turn.

    for turn in range(1 + len(spoken), rounds + 1):
        if len(spoken_dict.get(last)) == 1:     # The last number spoken, has only been spoken 1 time, ie the last time.
            this = 0

        else:                                   # The last number spoken, has been spoken 2 or more times.
            last_time = spoken_dict.get(last)[-1]
            last_time_but_one = spoken_dict.get(last)[-2]
            this = last_time - last_time_but_one

        if this in spoken_dict:
            spoken_dict[this].append(turn)
        else:
            spoken_dict[this] = [turn]

        last = this                             # Get ready for next turn.

        if VERBOSE and turn % 100000 == 0:      # Progress indicator, for large searches.
            print('turn, this:', turn, this)

    return this


def main():
    print('Part 1:', game(spoken=[6, 4, 12, 1, 20, 0, 16], rounds=2020))
    print('Part 2:', game(spoken=[6, 4, 12, 1, 20, 0, 16], rounds=30000000))


if __name__ == "__main__":
    main()
