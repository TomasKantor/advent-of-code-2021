#!/usr/bin/python3

# advent of code 2021 - Day 9 b

import os
import math


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
                low_points.append((y, x))

    return low_points


# depth first search, find all points of basin
def dfs(array, point, done):
    y = point[0]
    x = point[1]

    if point in done:
        return

    if array[y][x] == 9 or array[y][x] == 10:
        return

    done.add(point)

    dfs(array, (y+1, x), done)
    dfs(array, (y-1, x), done)
    dfs(array, (y, x+1), done)
    dfs(array, (y, x-1), done)


# find basin size
def find_basin_size(array, point):
    done = set()
    dfs(array, point, done)

    return len(done)


# find list of three largist basins
def three_largest_basins(array):
    low_points = find_low_points(array)
    sizes = [find_basin_size(array, p) for p in low_points]
    sizes.sort(reverse=True)

    return sizes[:3]


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    array = load_input(file)

    basins = three_largest_basins(array)

    result = math.prod(basins)

    print(result)
