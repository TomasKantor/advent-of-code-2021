#!/usr/bin/python3

# advent of code 2021 - Day 10 b

import os
from statistics import median

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']

opening_to_closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

autocomplete_character_points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


# value of brackets in stack to complete line
def stack_value(stack):

    value = 0

    for c in reversed(stack):
        value *= 5
        c_to_append = opening_to_closing[c]
        value += autocomplete_character_points[c_to_append]

    return value


# value of brackets to add to complete the line
# for correct or corrupted lines return None
def autocomplete_line_value(line):

    stack = []

    for c in line:
        if c == '\n':
            continue
        if c in opening_brackets:
            stack.append(c)
            continue
        if len(stack) == 0:  # corrupted line
            return None

        top = stack.pop()
        if opening_to_closing[top] != c:  # corrupted line
            return None

    if len(stack) == 0:
        return None

    return stack_value(stack)


# file value = median value of line to complete
def file_value(file):

    values = []

    for line in file:
        val = autocomplete_line_value(line)
        if val:
            values.append(val)

    return median(values)


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    value = file_value(file)

    print(value)
