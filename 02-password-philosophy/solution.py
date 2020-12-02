# Solution to day 2 of AOC 2020, Password Philosophy.
# https://adventofcode.com/2020/day/2


f = open('input.txt')
whole_text = (f.read())

string_list = whole_text.split()                    # Split string by any whitespace.

part_1 = 0                                          # Counters of valid password for part 1...
part_2 = 0                                          # ... and part 2 of the quiz.

for offset in range(0, len(string_list), 3):        # Each row of input has been split into 3 elements.
    first_second = string_list[offset].split('-')   # eg. split "1-3"
    first = int(first_second[0])
    second = int(first_second[1])

    letter = string_list[offset + 1][0]             # 1st character of eg. "b:"
    password = string_list[offset + 2]
    occurrences = password.count(letter)

    if first <= occurrences <= second:
        part_1 += 1

    matches = 0
    if password[first - 1] == letter:
        matches += 1
    if password[second - 1] == letter:
        matches += 1
    if matches == 1:
        part_2 += 1

print('Part 1:', part_1)
print('Part 2:', part_2)
