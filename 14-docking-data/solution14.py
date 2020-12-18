# Solution to day 14 of AOC 2020, Docking Data.
# https://adventofcode.com/2020/day/14

import sys

VERBOSE = ('-v' in sys.argv)
filename = sys.argv[1]


def dec_to_bin(decimal: str) -> str:
    """Return the parm decimal number as a 36-bit binary string."""
    binary = ''
    dec_int = int(decimal)

    for place in range(35, -1, -1):
        if pow(2, place) <= dec_int:
            binary += '1'
            dec_int -= pow(2, place)
        else:
            binary += '0'

    return binary


def bin_to_dec(binary: str) -> int:
    """Return the parm binary string as a decimal integer."""
    decimal = 0
    place_value = 1
    for bit in binary[::-1]:
        if bit == '1':
            decimal += place_value
        place_value *= 2

    return decimal


def apply_mask(binary: str, mask: str) -> str:
    """Apply the parm mask to the parm binary number.
       A 0 or 1 overwrites the corresponding bit in the value, while an X leaves the bit in the value unchanged."""
    result = ''

    for place in range(36):
        if mask[place] == 'X':
            result += binary[place]
        else:
            result += mask[place]
    return result


def apply_new_mask(binary: str, mask: str) -> str:
    """Apply the parm mask to the parm binary number, according to rules in Part 2.
        If the bitmask bit is 0, the corresponding memory address bit is unchanged.
        If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
        If the bitmask bit is X, the corresponding memory address bit is floating."""
    result = ''

    for place in range(36):
        if mask[place] == '0':
            result += binary[place]
        else:
            result += mask[place]
    return result


def decoder(address: str) -> list:
    """For a parm address (that may contain floating bits), return the list of decoded addresses (floating bits
    expanded out to their options."""
    if 'X' not in address:                      # Base case,
        return [address]                        # Return list with a single address in it.

    # Find the first 'X' in the list.
    first = address.find('X')

    before = address[:first]
    after = address[(first + 1):]

    # Incorporates this list flattener,
    #     flat_list = [item for sublist in t for item in sublist]
    return [item for sublist in [decoder(before + '0' + after),
            decoder(before + '1' + after)] for item in sublist]


def main():
    f = open(filename)
    whole_text = (f.read())
    lines = whole_text.split('\n')                     # Split string by any whitespace.

    # k: v, where k is the memory address, and v is the value stored in it.
    memory = {}
    current_mask = ''

    for line in lines:
        if VERBOSE:
            print('line:', line)

        target, source = line.split(' = ')

        if target == 'mask':
            current_mask = source
            if VERBOSE:
                print('current_mask', current_mask)
        else:
            address = int(target.replace('mem[', '').replace(']', ''))

            memory[address] = apply_mask(binary=dec_to_bin(source), mask=current_mask)

            if VERBOSE:
                print('address, memory[address]:', address, memory[address])

    total = 0
    for address in memory:
        total += bin_to_dec(memory[address])

    print('Part 1:', total)

    # ----------------------------------------------------------------------------------------

    # k: v, where k is the memory address, and v is the value stored in it.
    memory = {}
    current_mask = ''

    for line in lines:
        if VERBOSE:
            print('line:', line)

        target, source = line.split(' = ')

        if target == 'mask':
            current_mask = source
            if VERBOSE:
                print('current_mask', current_mask)

        else:
            address = target.replace('mem[', '').replace(']', '')

            masked_address = apply_new_mask(binary=dec_to_bin(address), mask=current_mask)

            if VERBOSE:
                print('masked_address', masked_address)

            for each_address in decoder(address=masked_address):

                if VERBOSE:
                    print('each_address, source:', each_address, source)

                memory[each_address] = int(source)

    # "What is the sum of all values left in memory after it completes?"
    total = 0

    for address in memory:
        total += memory[address]

    print('Part 2:', total)


if __name__ == "__main__":
    main()
