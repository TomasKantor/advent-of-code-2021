#!/usr/bin/python3

# advent of code 2021 - Day 3 a


def counts_to_gamma_rate(counts_array, line_count):

    gamma_rate = 0
    for val in counts_array:
        if val > line_count / 2:
            gamma_rate += 1
        gamma_rate <<= 1

    return gamma_rate >> 1


def counts_to_epsilon_rate(counts_array, line_count):

    epsilon_rate = 0
    for val in counts_array:
        if val < line_count / 2:
            epsilon_rate += 1
        epsilon_rate <<= 1

    return epsilon_rate >> 1


with open('input.txt') as file:

    counts_array = None

    line_count = 0

    for line in file:
        line = line.strip()
        line_count += 1

        if not counts_array:
            counts_array = [0]*len(line)

        for i, c in enumerate(line):
            if c != '\n':
                counts_array[i] += int(c)

    gamma_rate = counts_to_gamma_rate(counts_array, line_count)
    epsion_rate = counts_to_epsilon_rate(counts_array, line_count)

    print(gamma_rate*epsion_rate)
