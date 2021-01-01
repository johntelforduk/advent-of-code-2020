# Solution to day 25 of AOC 2020, Combo Breaker.
# https://adventofcode.com/2020/day/25

import sys


VERBOSE = ('-v' in sys.argv)


def transforms(subject_number: int, target_pk) -> int:
    """For the parm subject number. Transform the subject number several times until it matches the target public key.
       Return the number of iterations needed"""

    # "To transform a subject number, start with the value 1."
    result = 1
    loop = 0

    # "Then, a number of times called the loop size, perform the following steps:
    # Set the value to itself multiplied by the subject number.
    # Set the value to the remainder after dividing the value by 20201227."
    while result != target_pk:
        loop += 1
        result = (result * subject_number) % 20201227

        # if VERBOSE:
        #     print('loop, result:', loop, result)

    return loop


def calc_encryption_key(subject_number: int, loop_size: int) -> int:
    """For a parm subject number (a PK) and loop size, return the encryption key."""

    # "Transforming the subject number of 17807724 (the door's public key) with a loop size of 8 (the card's loop size)
    # produces the encryption key, 14897079."
    result = 1

    for loop in range(loop_size):
        result = (result * subject_number) % 20201227

    return result


def main():
    filename = sys.argv[1]
    f = open(filename)
    whole_text = f.read()
    f.close()

    card_pk_txt, door_pk_txt = whole_text.split('\n')
    card_pk, door_pk = int(card_pk_txt), int(door_pk_txt)

    if VERBOSE:
        print('card_pk, door_pk', card_pk, door_pk)

    card_loop_size = transforms(subject_number=7, target_pk=card_pk)
    door_loop_size = transforms(subject_number=7, target_pk=door_pk)

    if VERBOSE:
        print('card_loop_size, door_loop_size:', card_loop_size, door_loop_size)

    encryption_key = calc_encryption_key(subject_number=card_pk, loop_size=door_loop_size)

    print('Part 1:', encryption_key)


if __name__ == "__main__":
    main()
