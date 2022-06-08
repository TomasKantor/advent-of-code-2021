#!/usr/bin/python3

# advent of code 2021 - Day 11 a

import os


# load input add None as border
def load_input(file):

    array = []

    for line in file:
        row = [None] + [int(c) for c in line if c != '\n'] + [None]
        array.append(row)

    width = len(array[0])

    return [[None]*width] + array + [[None]*width]


# perform all given flashes and all new flashes
# return total number of flashes
def flash_all(array, flashes):

    flash_count = len(flashes)

    while len(flashes) > 0:
        y0, x0 = flashes.pop()
        for y in (y0-1, y0, y0+1):
            for x in (x0-1, x0, x0+1):

                if array[y][x] is None or array[y][x] == 0:
                    continue
                array[y][x] += 1
                if array[y][x] == 10:
                    array[y][x] = 0
                    flashes.append((y, x))
                    flash_count += 1

    return flash_count


# increment all cells by 1 and return all coordinates that flash
def increment_all(array):
    flashes = []

    for y, row in enumerate(array):
        for x, cell in enumerate(row):
            if cell is None:
                continue
            cell += 1
            array[y][x] = cell

            if cell == 10:
                array[y][x] = 0
                flashes.append((y, x))
    return flashes


# perform 1 step
def step(array):

    flashes = increment_all(array)
    flash_count = flash_all(array, flashes)
    return flash_count


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:
    array = load_input(file)
    count = 0
    number_of_steps = 100
    for _ in range(number_of_steps):
        count += step(array)

    print(count)
