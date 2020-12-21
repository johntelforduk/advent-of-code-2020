# Solution to day 18 of AOC 2020, Operation Order.
# https://adventofcode.com/2020/day/18

import sys

VERBOSE = ('-v' in sys.argv)


def evaluate_left_to_right(exp: str) -> int:
    """Do left-to-right expression evaluation on the parm flat expression."""

    # A flat expression contains no brackets.
    assert '(' not in exp
    assert ')' not in exp

    terms = exp.split(' ')

    result = int(terms.pop(0))          # First term in the expression is always an operand.

    while len(terms) != 0:
        operator = terms.pop(0)
        operand = int(terms.pop(0))
        assert operator in ['+', '*']

        if operator == '+':
            result += operand
        else:
            result *= operand
    return result


def evaluate_one_operation(exp: str, operator: str) -> str:
    """For the first matching operation in the parm flat expression, replace it - and the 2 operands around it - with
       the results of the operation."""

    # A flat expression contains no brackets.
    assert '(' not in exp
    assert ')' not in exp

    terms = exp.split(' ')

    # Find the first occurrence of required operation in the list of terms.
    operation_pos = terms.index(operator)

    # For an infixed operation, the operands are either side of the operator.
    operand1 = int(terms[operation_pos - 1])
    operand2 = int(terms[operation_pos + 1])

    assert operator in ['+', '*']
    if operator == '+':
        calculation = operand1 + operand2
    else:
        calculation = operand1 * operand2

    # Reconstruct the string for the whole expression, with the one operation found replaced with it's result.
    result = ''
    pos = 0
    for term in terms:
        if operation_pos - 1 <= pos <= operation_pos + 1:
            if operation_pos == pos:
                result += str(calculation) + ' '
        else:
            result += term + ' '
        pos += 1

    return result.strip()                   # Each concatenation also adds a space, so last space needs to be removed.


def inner_brackets(exp: str) -> (int, int):
    """For parm expressions, return the start and end position of the first pair of inner brackets.
       Inner brackets are brackets around a bit of string that contains no other brackets."""

    # Looking for string "(" + some other chars + ")",
    # ... where some other chars doesn't contain any brackets.

    pos, start = 0, 0
    for i in exp:
        if i == "(":
            start = pos
        if i == ')':
            return start, pos
        pos += 1
    return None, None


def inner_brackets_to_value(exp: str, method: str) -> str:
    """For the parm expression, return expression with first inner brackets evaluated."""
    bf, bt = inner_brackets(exp)

    # front + '(' + inner + ')' + end
    front = exp[0:bf]
    inner = exp[bf+1:bt]
    end = exp[bt+1:]

    assert method in ['l_to_r', '+_then_*']
    if method == 'l_to_r':
        return front + str(evaluate_part1(inner)) + end
    else:
        return front + str(evaluate_part2(inner)) + end


def evaluate_part1(exp: str) -> int:
    """For parm expression, evaluate it using the left to right method."""
    # First, evaluate all of the things in brackets.
    while '(' in exp:
        exp = inner_brackets_to_value(exp, 'l_to_r')

    return evaluate_left_to_right(exp)


def evaluate_part2(exp: str) -> int:
    """For parm expression, evaluate it using the addition before multiplication method.."""
    # First, evaluate all of the things in brackets.
    while '(' in exp:
        exp = inner_brackets_to_value(exp, '+_then_*')

    # Then evaluate all the addition operations.
    while '+' in exp:
        exp = evaluate_one_operation(exp, '+')

    # Finally evaluate all the multiplications.
    while '*' in exp:
        exp = evaluate_one_operation(exp, '*')

    return int(exp)


def main():
    filename = sys.argv[1]
    f = open(filename)
    whole_text = f.read()
    f.close()

    total1 = 0
    for exp in whole_text.split('\n'):
        total1 += evaluate_part1(exp)
    print('Part 1:', total1)

    total2 = 0
    for exp in whole_text.split('\n'):
        total2 += evaluate_part2(exp)
    print('Part 2:', total2)


if __name__ == "__main__":
    main()
