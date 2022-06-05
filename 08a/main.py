#!/usr/bin/python3

# advent of code 2021 - Day 8 a

import os

# number of segments is seven-segment display for each digit
segments = {
    0: 6,
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6
}

input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:

    target_lenghts = (segments[1], segments[4], segments[7], segments[8])
    count = 0
    for line in file:
        # part after '|'
        line = line.split('|')[1]

        for w in line.split():
            if len(w) in target_lenghts:
                count += 1

    print(count)
