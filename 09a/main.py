#!/usr/bin/python3

# advent of code 2021 - Day 9 a

import os


# load input add 10 as border
def load_input(file):

    array = []

    for line in file:
        row = [10] + [int(c) for c in line if c != '\n'] + [10]
        array.append(row)

    lenght = len(array[0])

    array = [[10]*lenght] + array + [[10]*lenght]

    return array


# def find low points of array
def find_low_points(array):
    low_points = []

    for y, row in enumerate(array):
        for x, val in enumerate(row):
            if val == 10:  # no borders
                continue

            min_val = min(array[y][x+1], array[y][x-1], array[y-1][x], array[y+1][x])

            if val < min_val:
                low_points.append(val)

    return low_points


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    array = load_input(file)
    low_points = find_low_points(array)
    total_risk_level = sum([p + 1 for p in low_points])
    print(total_risk_level)
