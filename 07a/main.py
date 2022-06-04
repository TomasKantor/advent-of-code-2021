#!/usr/bin/python3

# advent of code 2021 - Day 7 a

import os
from statistics import median


def load_input(file):
    # ints divided by ','
    return [int(x) for x in file.readline().split(',')]


def fuel_needed(positions, destination):

    fuel = 0
    for p in positions:
        fuel += abs(p-destination)
    return fuel


# guess optimal destination as median
# iteratively check to the left and righ of this guess
def iterative_guess(positions):
    guess = round(median(crab_positions))
    fuel = fuel_needed(positions, guess)

    while True:

        fuel_right = fuel_needed(positions, guess+1)
        if fuel_right < fuel:
            guess += 1
            fuel = fuel_right
            continue

        fuel_left = fuel_needed(positions, guess-1)
        if fuel_left < fuel:
            guess -= 1
            fuel = fuel_left
            continue

        return (guess, fuel)


input_file_name = os.path.dirname(__file__) + '/input.txt'

with open(input_file_name) as file:

    crab_positions = load_input(file)
    guess, fuel = iterative_guess(crab_positions)
    print(fuel)
