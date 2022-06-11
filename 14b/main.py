#!/usr/bin/python3

# advent of code 2021 - Day 14 a

import os


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


# increment value in dictionary by count
def add_count(dictionary, key, count):
    dict_count = dictionary.get(key, 0)
    dictionary[key] = dict_count + count


# apply insertion rule to every pair in string
def step(pair_dict, rules):

    new_pair_dict = {}

    for pair, count in pair_dict.items():
        to_insert = rules[pair]
        p1 = pair[0] + to_insert
        p2 = to_insert + pair[1]
        add_count(new_pair_dict, p1, count)
        add_count(new_pair_dict, p2, count)

    return new_pair_dict


# create dictionary of characters and their counts in pair_dictionary
def get_element_counts(pair_dict):

    element_counts = {}

    for pair, count in pair_dict.items():
        for element in pair:
            add_count(element_counts, element, count)
    return element_counts


# make 'steps' steps and return most common - least common counts of chars
def solve(string, rules, steps):

    pair_dict = crete_pair_dict(string)

    for i in range(steps):
        pair_dict = step(pair_dict, rules)

    element_counts = get_element_counts(pair_dict)

    element_counts[string[0]] += 1  # first char is counted only once
    element_counts[string[-1]] += 1  # last char is counted only once

    most_common = max(element_counts, key=element_counts.get)
    least_common = min(element_counts, key=element_counts.get)

    # every char is counted twice
    return (element_counts[most_common] - element_counts[least_common]) // 2


# create dict of every adjacent pair of chars in string and their counts in string
def crete_pair_dict(string):

    pair_dict = {}

    for i in range(len(string)-1):
        pair = string[i:i+2]
        count = pair_dict.get(pair, 0)
        pair_dict[pair] = count + 1

    return pair_dict


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    string, rules = load_input(file)
    steps = 40
    res = solve(string, rules, steps)
    print(res)
