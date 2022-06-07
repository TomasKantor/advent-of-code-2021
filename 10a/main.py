#!/usr/bin/python3

# advent of code 2021 - Day 10 a

import os

opening_brackets = ['(', '[', '{', '<']
closing_brackets = [')', ']', '}', '>']

opening_to_closing = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

illegal_character_points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}


# error value of line = value of first incorrect bracket
def line_error_value(line):

    stack = []

    for c in line:
        if c == '\n':
            continue
        if c in opening_brackets:
            stack.append(c)
            continue
        if len(stack) == 0:
            return illegal_character_points[c]

        top = stack.pop()
        if opening_to_closing[top] != c:
            return illegal_character_points[c]

    return 0


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    total_syntax_error = 0
    for line in file:
        total_syntax_error += line_error_value(line)

    print(total_syntax_error)
