#!/usr/bin/python3

# advent of code 2021 - Day 8 b

import os

# name of segments of every digits
digit_segments = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}


# transform list of digits to number
def digits_to_number(digits):
    number = 0
    for d in digits:
        number *= 10
        number += d
    return number


# decodes segments with help of translation table, returns number
def decode(output_values, translation_table):

    digits = []
    for pattern in output_values:
        length = len(pattern)
        if length == 2:
            digits.append(1)
        elif length == 4:
            digits.append(4)
        elif length == 3:
            digits.append(7)
        elif length == 7:
            digits.append(8)
        elif length == 5:
            if translation_table['e'] in pattern:
                digits.append(2)
            elif translation_table['b'] in pattern:
                digits.append(5)
            else:
                digits.append(3)
        elif length == 6:
            if translation_table['d'] not in pattern:
                digits.append(0)
            elif translation_table['c'] not in pattern:
                digits.append(6)
            else:
                digits.append(9)

    return digits_to_number(digits)


#  update candidates of patterns of unique length
def unique_length_patterns(signal_patterns, candidates):
    for pattern in signal_patterns:
        #  digits with unique length
        for digit in [1, 4, 7]:
            if len(pattern) == len(digit_segments[digit]):
                segments = digit_segments[digit]
                for c in candidates:
                    if c in segments:
                        candidates[c].intersection_update(set(pattern))
                    else:
                        candidates[c].difference_update(set(pattern))


# update candidates of patterns with common length based on common segments
def common_length_patterns(signal_patterns, candidates, length, common_segments):

    patterns = []

    for p in signal_patterns:
        if len(p) == length:
            patterns.append(set(p))

    intersection = patterns[0]
    intersection.intersection_update(patterns[1])
    intersection.intersection_update(patterns[2])

    for c in common_segments:
        candidates[c].intersection_update(intersection)


# removes the candidate from segment with only one candidate
# from candidates of other segments
def update_unambiguous_candidates(candidates):

    for c in candidates:
        if len(candidates[c]) == 1:
            for c_other in candidates:
                if c != c_other:
                    candidates[c_other].difference_update(candidates[c])


# gets all valid candidates for every segment
def get_candidates(signal_patterns):

    candidates = {}
    for c in 'abcdefg':
        candidates[c] = set('abcdefg')

    unique_length_patterns(signal_patterns, candidates)

    # common segments for digits of length 5 (2, 3, 5) are 'adg'
    common_length_patterns(signal_patterns, candidates, 5, 'adg')

    # common segments for digits of length 6 (0, 6, 9) are 'abfg'
    common_length_patterns(signal_patterns, candidates, 6, 'abfg')

    update_unambiguous_candidates(candidates)

    return candidates


# from dict of set to dict of chars
def candidates_to_translation_table(candidates):
    translation_table = {}

    for c in candidates:
        translation_table[c] = next(iter(candidates[c]))

    return translation_table


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:

    total = 0

    for line in file:
        line = line.split('|')
        signal_patterns = line[0].split()
        output_values = line[1].split()

        candidates = get_candidates(signal_patterns)
        translation_table = candidates_to_translation_table(candidates)

        decoded = decode(output_values, translation_table)
        total += decoded

    print(total)
