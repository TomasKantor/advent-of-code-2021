#!/usr/bin/python3

# advent of code 2021 - Day 14 a

import os
from collections import Counter


# load initial string and insertion rules
def load_input(file):

    rules = {}

    initial_string = file.readline().strip()
    file.readline()  # empty line

    for line in file:
        line = line.strip()
        words = line.split(' -> ')
        rules[words[0]] = words[1]

    return initial_string, rules


# apply insertion rule to every pair in string
def step(string, rules):

    new_string = ''

    for i in range(len(string)-1):
        new_string += string[i]
        pair = string[i:i+2]
        new_string += rules[pair]

    new_string += string[-1]
    return new_string


# make 'steps' steps and return most common - least common counts
def solve(string, rules, steps):

    for i in range(steps):
        string = step(string, rules)

    counts = Counter(string)
    ordered_counts = counts.most_common()

    most = ordered_counts[0][1]
    least = ordered_counts[-1][1]

    return most - least


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    string, rules = load_input(file)
    steps = 10
    res = solve(string, rules, steps)
    print(res)
